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
from db2 import db, User, Data
import time
import datetime

db_filename = "data.db"
app = Flask(__name__)

#  Client Key (Be sure to leave these out)
CLIENT_ID = 'a9c19b55cef14742aba314f3d27ae7d5'
CLIENT_SECRET = '46a536eb74a14a3b94b70650d02a2db4'

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
USER_ID = 10

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
    user_profile_response = requests.get(user_profile_api_endpoint, headers=authorization_header)
    user_profile_data = json.loads(user_profile_response.text)

    # Info needed beforehand
    datetime_current = datetime.datetime.now()
    spotify_id = user_profile_data.get('id')
    user = User.query.filter_by(spotify_id = spotify_id).first()

    # Check that user is already in the system or not
    if user is not None:
        # Check that the last time it was refreshed was within 1 week
        last_refreshed_date = user.date_last_refreshed
        if datetime_current - last_refreshed_date < datetime.timedelta(days=7):
            return json.dumps({'success': False, 'error': 'user has been refreshed within the past week'}), 429
    else:
        # If not in the db, make a new entry
        user_entry = User (
            spotify_id = spotify_id,
            date_last_refreshed = datetime_current
        )
        db.session.add(user_entry)
        db.session.commit()

    # User should now be defined either way
    user = User.query.filter_by(spotify_id = spotify_id).first()

    # Retrieve Playlist Data
    user_playlists_api_endpoint = "{}/playlists".format(user_profile_data["href"])
    user_playlists_response = requests.get(user_playlists_api_endpoint, headers=authorization_header)
    user_playlists_data = json.loads(user_playlists_response.text)

    # Retrieve Favorite Tracks: Short_Term
    favorite_tracks_short_api_endpoint = "{}/me/top/{}?time_range=short_term".format(SPOTIFY_API_URL, "tracks")
    favorite_tracks_short_response = requests.get(favorite_tracks_short_api_endpoint, headers=authorization_header)
    favorite_tracks_short_data = json.loads(favorite_tracks_short_response.text)
    
    # Retrieve Favorite Tracks: Medium_Term
    favorite_tracks_mid_api_endpoint = "{}/me/top/{}?time_range=medium_term".format(SPOTIFY_API_URL, "tracks")
    favorite_tracks_mid_response = requests.get(favorite_tracks_mid_api_endpoint, headers=authorization_header)
    favorite_tracks_mid_data = json.loads(favorite_tracks_mid_response.text)

    # Retrieve Favorite Tracks: Long_Term
    favorite_tracks_long_api_endpoint = "{}/me/top/{}?time_range=long_term".format(SPOTIFY_API_URL, "tracks")
    favorite_tracks_long_response = requests.get(favorite_tracks_long_api_endpoint, headers=authorization_header)
    favorite_tracks_long_data = json.loads(favorite_tracks_long_response.text)

    # Retrieve Favorite Artists: Short_Term
    favorite_artists_short_api_endpoint = "{}/me/top/{}?time_range=short_term".format(SPOTIFY_API_URL, "artists")
    favorite_artists_short_response = requests.get(favorite_tracks_short_api_endpoint, headers=authorization_header)
    favorite_artists_short_data = json.loads(favorite_tracks_short_response.text)
    
    # Retrieve Favorite Artists: Medium_Term
    favorite_artists_mid_api_endpoint = "{}/me/top/{}?time_range=medium_term".format(SPOTIFY_API_URL, "artists")
    favorite_artists_mid_response = requests.get(favorite_tracks_mid_api_endpoint, headers=authorization_header)
    favorite_artists_mid_data = json.loads(favorite_tracks_mid_response.text)

    # Retrieve Favorite Artists: Long_Term
    favorite_artists_long_api_endpoint = "{}/me/top/{}?time_range=long_term".format(SPOTIFY_API_URL, "artists")
    favorite_artists_long_response = requests.get(favorite_tracks_long_api_endpoint, headers=authorization_header)
    favorite_artists_long_data = json.loads(favorite_tracks_long_response.text)

    user_data_entry = Data (
        user_top_artists_short = str(favorite_artists_short_data),
        user_top_artists_mid = str(favorite_artists_mid_data),
        user_top_artists_long = str(favorite_artists_long_data),
        user_top_tracks_short = str(favorite_tracks_short_data),
        user_top_tracks_mid = str(favorite_tracks_mid_data),
        user_top_tracks_long = str(favorite_tracks_long_data),
        user_profile = str(user_profile_data),
        user_playlists = str(user_playlists_data)
    )

    user.user_data.clear()
    user.user_data.append(user_data_entry)
    db.session.add(user_data_entry)

    final_json = json.dumps({'user_profile_data': user_profile_data,
                             'user_playlists_data': user_playlists_data,
                             'favorite_artists_short': favorite_artists_short_data, 
                             'favorite_artists_mid': favorite_artists_mid_data,
                             'favorite_artists_long': favorite_artists_long_data, 
                             'favorite_tracks_short': favorite_tracks_short_data,  
                             'favorite_tracks_mid': favorite_tracks_mid_data,
                             'favorite_tracks_long': favorite_tracks_long_data})

    # Commit all adds to db
    db.session.commit()

    return json.dumps({'success': True, 'data': final_json}), 201

    

if __name__ == "__main__":
    app.run(debug=True,port=PORT)
