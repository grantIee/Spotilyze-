from flask import Flask, request
import json
from db import db, User, Data

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
@app.route('/api/user/<int:spotify_id>/datas/')
def get_userdata(id):
    data = User.query.filter_by(id=id).first()
    if data is not None:
        datas = [data.serialize() for data in user.datas]
        return json.dumps({"data": datas}), 200
    else:
        return json.dumps({"error": "Post not found..."}), 404    

"""
#Get a specific user's profile
@app.route('/api/user/<int:spotify_id>/datas/profiles/')
def get_user_profile(id):
    data = Data.query.filter_by(id=id).first()
    if data is not None:
        datas = [data.serialize() for data in 
        profile = datas[0]['user profile']
        return json.dumps({"profile": profile}), 200
    else:
        return json.dumps({"error": "Post not found..."}), 404    

#Get a specific user's playlists
@app.route('/api/post/<int:spotify_id>/datas/<int: id>/user_playlists/')
def get_user_playlists(id):
    data = User.query.filter_by(id=id).first()
    if data is not None:
        datas = [data.serialize() for data in user.datas]
        playlists = datas[0]['user playlists']
        return json.dumps({"playlist": playlists}), 200
    else:
        return json.dumps({"error": "Post not found..."}), 404    


#Get a specific user's favorite artists
@app.route('/api/post/<int:spotify_id>/data/user_favorite_artists/')
def get_user_favorite_artists(id):
    data = User.query.filter_by(id=id).first()
    if data is not None:
        datas = [data.serialize() for data in user.datas]
        artists = datas[0]['user favorite artists']
        return json.dumps({"favorite artists": artists}), 200
    else:
        return json.dumps({"error": "Post not found..."}), 404    

#Get a specific user's favorite tracks
@app.route('/api/post/<int:spotify_id>/data/user_favorite_tracks/')
def get_user_favorite_tracks(id):
    data = User.query.filter_by(id=id).first()
    if data is not None:
        datas = [data.serialize() for data in user.datas]
        tracks = datas[0]['user favorite tracks']
        return json.dumps({"favorite tracks": tracks}), 200
    else:
        return json.dumps({"error": "Post not found..."}), 404    
"""
if __name__ == "__main__":
    app.run(debug=True,port=PORT)