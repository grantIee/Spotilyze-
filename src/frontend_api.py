from flask import FLask, request
import json
from db import db, User, Data

db_filename = "data.db"
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' %db_filename
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

@app.route('/')

#Get a specific user's data
@app.route('/api/post/<int: id>/datas/')
def get_userdata(id):
    data = User.query.filter_by(id=id).first()
    if data is not None:
        datas = [data.serialize() for data in user.datas]
        return json.dumps({"data": datas}), 200
    else:
        return json.dumps({"error": "Post not found..."}), 404    


#Get a specific user's profile
@app.route('/api/post/<int: id>/data/user_profile/')
def get_userdata(id):
    data = User.query.filter_by(id=id).first()
    if data is not None:
        datas = [data.serialize() for data in user.datas]
        profile = datas[0]['user profile']
        return json.dumps({"profile": profile}), 200
    else:
        return json.dumps({"error": "Post not found..."}), 404    

#Get a specific user's playlists
@app.route('/api/post/<int: id>/data/user_playlists/')
def get_userdata(id):
    data = User.query.filter_by(id=id).first()
    if data is not None:
        datas = [data.serialize() for data in user.datas]
        playlists = datas[0]['user playlists']
        return json.dumps({"playlist": playlists}), 200
    else:
        return json.dumps({"error": "Post not found..."}), 404    


#Get a specific user's favorite artists
@app.route('/api/post/<int: id>/data/user_favorite_artists/')
def get_userdata(id):
    data = User.query.filter_by(id=id).first()
    if data is not None:
        datas = [data.serialize() for data in user.datas]
        artists = datas[0]['user favorite artists']
        return json.dumps({"favorite artists": artists}), 200
    else:
        return json.dumps({"error": "Post not found..."}), 404    

#Get a specific user's favorite tracks
@app.route('/api/post/<int: id>/data/user_favorite_tracks/')
def get_userdata(id):
    data = User.query.filter_by(id=id).first()
    if data is not None:
        datas = [data.serialize() for data in user.datas]
        tracks = datas[0]['user favorite tracks']
        return json.dumps({"favorite tracks": tracks}), 200
    else:
        return json.dumps({"error": "Post not found..."}), 404    


