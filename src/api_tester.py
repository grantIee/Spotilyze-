'''
    api.py
    Grant Lee & Richard Yoon

    Code that retrieves information on authenticated Spotify User
'''

from flask import Flask, request, redirect
import requests
import base64
import urllib
from urllib.parse import quote
import json
from db import db, User, Data, Playlist, Track, Artist, Profile

db_filename = "data.db"
app = Flask(__name__)

#  Client Key (Be sure to leave these out)
CLIENT_ID = 'a9c19b55cef14742aba314f3d27ae7d5'
CLIENT_SECRET = '8e540d477c1e4e52b5c41d8383b14d6d'

# Spotify URLS (Request url materials)
SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_BASE_URL = "https://api.spotify.com"
SPOTIFY_API_URL = "https://api.spotify.com/v1"

# Server-side Parameters
CLIENT_SIDE_URL = "http://127.0.0.1"
PORT = 8080
REDIRECT_URI = "{}:{}/callback/q".format(CLIENT_SIDE_URL, PORT)
SCOPE = "user-follow-read user-top-read user-read-private playlist-read-collaborative"
SHOW_DIALOG_bool = True
SHOW_DIALOG_str = str(SHOW_DIALOG_bool).lower()

#SQLALC database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' %db_filename
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
with app.app_context():
  db.create_all()

# Get authenticated 
@app.route("/")
def index():
    response_type = "response_type=code"
    redirect_uri = "redirect_uri=" + REDIRECT_URI
    scope = "scope=" + SCOPE
    client_id = "client_id=" + CLIENT_ID
    final_url = SPOTIFY_AUTH_URL + "/?{0}&{1}&{2}&{3}".format(response_type, redirect_uri, scope, client_id)

    return redirect(final_url)


@app.route("/callback/q")
def callback():

    auth_token = request.args['code']

    # Need payload that contains the authorization_code from the authentication part of the USER
    code_payload = {
        "grant_type": "authorization_code",
        "code": str(auth_token),
        "redirect_uri": REDIRECT_URI
    }

    # Client Info Construction

    # This constructs the information that authenticates the Client
    client_info = CLIENT_ID + ':' + CLIENT_SECRET
    client_info_bytes = client_info.encode('utf-8')
    client_info_string = base64.b64encode(client_info_bytes).decode('utf-8')
    authorization_value = 'Basic ' + client_info_string

    headers = {"Authorization": authorization_value}
    post_request = requests.post(SPOTIFY_TOKEN_URL, data=code_payload, headers=headers)

    # Sift for the required information
    response_data = json.loads(post_request.text)
    access_token = response_data["access_token"]
    refresh_token = response_data["refresh_token"]
    token_type = response_data["token_type"]
    expires_in = response_data["expires_in"]

    # Authorization_header that uses all parts
    authorization_header = {"Authorization":"Bearer {}".format(access_token)}
    
    # Retrieve User Profile
    user_profile_api_endpoint = "{}/me".format(SPOTIFY_API_URL)
    profile_response = requests.get(user_profile_api_endpoint, headers=authorization_header)
    profile_data = json.loads(profile_response.text)
    spotify_id = profile_data.get('id')
    user = User.query.filter_by(spotify_id = spotify_id).first()
    if user is not None:
        # Check that the last time it was refreshed was within 1 week
        return 
        # If not in the db, make a new entry
    else:
        user_entry = User(
            spotify_id = spotify_id
        )
        db.session.add(user_entry)

    # Retrieve Playlist Data
    playlist_api_endpoint = "{}/playlists".format(profile_data["href"])
    playlists_response = requests.get(playlist_api_endpoint, headers=authorization_header)
    playlist_data = json.loads(playlists_response.text)
    pdata = Playlist(
        name = playlist_data.get('items')[0].get('name'),
        images = playlist_data.get('items')[0].get('images'),
        dataid = user.id
    )
    user.datas.playlists.append(pdata)
    db.session.add(pdata)
    db.session.commit()

    # Retrieve Favorite Tracks
    favorite_tracks_api_endpoint = "{}/me/top/{}?time_range=medium_term".format(SPOTIFY_API_URL, "tracks")
    favorite_tracks_response = requests.get(favorite_tracks_api_endpoint, headers=authorization_header)
    favorite_tracks_data = json.loads(favorite_tracks_response.text)
    favtrackdata = Track(
        name = favorite_tracks_data.get('items')[0].get('name'),
        url = favorite_tracks_data.get('items')[0].get('url'),
        dataid = user.id
    )
    user.datas.tracks.append(favtrackdata)
    db.session.add(favtrackdata)
    db.session.commit()

    # Retrieve Favorite Artists
    favorite_artists_api_endpoint = "{}/me/top/{}?time_range=medium_term".format(SPOTIFY_API_URL, "artists")
    favorite_artists_response = requests.get(favorite_artists_api_endpoint, headers=authorization_header)
    favorite_artists_data = json.loads(favorite_artists_response.text)

    # Compile Final User Data
    final_user_data = json.dumps({'user_profile': profile_data, 'playlist_data': playlist_data, 'favorite_artists_data': favorite_artists_data, 'favorite_tracks_data': favorite_tracks_data})

    db.session.commit()
    return final_user_data

if __name__ == "__main__":
    app.run(debug=True,port=PORT)
