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
<<<<<<< HEAD
@app.route('/api/user/<int:spotify_id>/datas/')
=======
@app.route('/api/<int:spotify_id>/data/')
>>>>>>> 6c840d647f9357cc809837f8c6442081b446aa87
def get_userdata(id):
    data = User.query.filter_by(spotify_id=id).first()
    if data is not None:
        data = [data.serialize() for data in user.data]
        return json.dumps({"data": data}), 200
    else:
        return json.dumps({"error": "Post not found..."}), 404    

"""
#Get a specific user's profile
<<<<<<< HEAD
@app.route('/api/user/<int:spotify_id>/datas/profiles/')
def get_user_profile(id):
    data = Data.query.filter_by(id=id).first()
    if data is not None:
        datas = [data.serialize() for data in 
        profile = datas[0]['user profile']
        return json.dumps({"profile": profile}), 200
=======
@app.route('/api/<int:spotify_id>/data/user_profile/')
def get_user_profile(spotify_id):
    user = User.query.filter_by(spotify_id=spotify_id).first()
    if user is not None:
        user_data = [data.serialize() for data in user.user_data]
        profile = user_data[0]['user_profile']
        return json.dumps({'user_profile': profile}), 200
>>>>>>> 6c840d647f9357cc809837f8c6442081b446aa87
    else:
        return json.dumps({"error": "Post not found..."}), 404    

#Get a specific user's playlists
<<<<<<< HEAD
@app.route('/api/post/<int:spotify_id>/datas/<int: id>/user_playlists/')
=======
@app.route('/api/<int:spotify_id>/data/user_playlists/')
>>>>>>> 6c840d647f9357cc809837f8c6442081b446aa87
def get_user_playlists(id):
    data = User.query.filter_by(spotify_id=id).first()
    if data is not None:
        data = [data.serialize() for data in user.data]
        playlists = data[0]['user playlists']
        return json.dumps({"playlist": playlists}), 200
    else:
        return json.dumps({"error": "Post not found..."}), 404    


#Get a specific user's favorite artists
@app.route('/api/<int:spotify_id>/data/user_favorite_artists/')
def get_user_favorite_artists(id):
    data = User.query.filter_by(spotify_id=id).first()
    if data is not None:
        data = [data.serialize() for data in user.data]
        artists = data[0]['user favorite artists']
        return json.dumps({"favorite artists": artists}), 200
    else:
        return json.dumps({"error": "Post not found..."}), 404    

#Get a specific user's favorite tracks
@app.route('/api/<int:spotify_id>/data/user_favorite_tracks/')
def get_user_favorite_tracks(id):
    data = User.query.filter_by(spotify_id=id).first()
    if data is not None:
        data = [data.serialize() for data in user.data]
        tracks = data[0]['user favorite tracks']
        return json.dumps({"favorite tracks": tracks}), 200
    else:
        return json.dumps({"error": "Post not found..."}), 404    
"""
if __name__ == "__main__":
    app.run(debug=True,port=PORT)