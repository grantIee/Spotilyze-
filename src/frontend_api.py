'''
    frontend_api.py
    Grant Lee & Jaemok Yoon

    Code that returns the user's information to the frontend. 
'''
from flask import Flask, request
import json
from db2 import db, User, Data

db_filename = "data.db"
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' %db_filename
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)

CLIENT_SIDE_URL = "http://127.0.0.1"
PORT = 8080

@app.route('/')


# Get the list of users in db
@app.route('/api/users')
def get_users():
    users = User.query.all()
    res = {'success': True, 'data': [user.serialize() for user in users]}
    return json.dumps(res), 200


#Get a specific user's data
@app.route('/api/<int:spotify_id>/data/')
def get_userdata(id):
    data = User.query.filter_by(spotify_id=id).first()
    if data is not None:
        data = [data.serialize() for data in user.data]
        return json.dumps({"data": data}), 200
    else:
        return json.dumps({"error": "Post not found..."}), 404    

#Get a specific user's profile
@app.route('/api/<int:spotify_id>/data/user_profile/')
def get_user_profile(spotify_id):
    user = User.query.filter_by(spotify_id=spotify_id).first()
    if user is not None:
        user_data = [data.serialize() for data in user.user_data]
        profile = user_data[0]['user_profile']
        return json.dumps({'user_profile': profile}), 200
    else:
        return json.dumps({"error": "Post not found..."}), 404    

#Get a specific user's playlists
@app.route('/api/<int:spotify_id>/data/user_playlists/')
def get_user_playlists(spotify_id):
    user = User.query.filter_by(spotify_id=spotify_id).first()
    if user is not None:
        user_data = [data.serialize() for data in user.user_data]
        playlists = user_data[0]['user_playlists']
        return json.dumps({"playlist": playlists}), 200
    else:
        return json.dumps({"error": "Post not found..."}), 404    


#Get a specific user's favorite artists
@app.route('/api/<int:spotify_id>/data/top_artists_long/')
def get_user_top_artsts_long(spotify_id):
    user = User.query.filter_by(spotify_id=spotify_id).first()
    if user is not None:
        user_data = [data.serialize() for data in user.user_data]
        artists = user_data[0]['user_top_artists_long']
        return json.dumps({"favorite artists": artists}), 200
    else:
        return json.dumps({"error": "Post not found..."}), 404  

#Get a specific user's favorite artists
@app.route('/api/<int:spotify_id>/data/top_artists_mid/')
def get_user_top_artists_mid(spotify_id):
    user = User.query.filter_by(spotify_id=spotify_id).first()
    if user is not None:
        user_data = [data.serialize() for data in user.user_data]
        artists = user_data[0]['user_top_artists_mid']
        return json.dumps({"favorite artists": artists}), 200
    else:
        return json.dumps({"error": "Post not found..."}), 404    

#Get a specific user's favorite artists
@app.route('/api/<int:spotify_id>/data/top_artists_short/')
def get_user_top_artist_short(spotify_id):
    user = User.query.filter_by(spotify_id=spotify_id).first()
    if user is not None:
        user_data = [data.serialize() for data in user.user_data]
        artists = user_data[0]['user_top_artists_short']
        return json.dumps({"favorite artists": artists}), 200
    else:
        return json.dumps({"error": "Post not found..."}), 404    


#Get a specific user's favorite tracks
@app.route('/api/<int:spotify_id>/data/top_tracks_long/')
def get_user_top_tracks_long(spotify_id):
    user = User.query.filter_by(spotify_id=spotify_id).first()
    if user is not None:
        user_data = [data.serialize() for data in user.user_data]
        tracks = user_data[0]['user_top_tracks_long']
        return json.dumps({"favorite tracks": tracks}), 200
    else:
        return json.dumps({"error": "Post not found..."}), 404    

#Get a specific user's favorite tracks
@app.route('/api/<int:spotify_id>/data/top_tracks_mid/')
def get_user_top_tracks_mid(spotify_id):
    user = User.query.filter_by(spotify_id=spotify_id).first()
    if user is not None:
        user_data = [data.serialize() for data in user.user_data]
        tracks = user_data[0]['user_top_tracks_mid']
        return json.dumps({"favorite tracks": tracks}), 200
    else:
        return json.dumps({"error": "Post not found..."}), 404    

#Get a specific user's favorite tracks
@app.route('/api/<int:spotify_id>/data/top_tracks_short/')
def get_user_top_tracks_short(spotify_id):
    user = User.query.filter_by(spotify_id=spotify_id).first()
    if user is not None:
        user_data = [data.serialize() for data in user.user_data]
        tracks = user_data[0]['user_top_tracks_short']
        return json.dumps({"favorite tracks": tracks}), 200
    else:
        return json.dumps({"error": "Post not found..."}), 404    


if __name__ == "__main__":
    app.run(debug=True,port=PORT)