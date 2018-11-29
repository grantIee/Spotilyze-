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
        return json.dumps({"data": datas}), 200
    else:
        return json.dumps({"error": "Post not found..."}), 404    

#Get a specific user's playlists
@app.route('/api/post/<int: id>/data/user_playlists/')
def get_userdata(id):
    data = User.query.filter_by(id=id).first()
    if data is not None:
        datas = [data.serialize() for data in user.datas]
        playlists = datas[0]['']
        return json.dumps({"data": datas}), 200
    else:
        return json.dumps({"error": "Post not found..."}), 404    


#Get a specific user's favorite artists
@app.route('/api/post/<int: id>/data/user_favorite_artists/')
def get_userdata(id):
    data = User.query.filter_by(id=id).first()
    if data is not None:
        datas = [data.serialize() for data in user.datas]
        return json.dumps({"data": datas}), 200
    else:
        return json.dumps({"error": "Post not found..."}), 404    

#Get a specific user's favorite tracks
@app.route('/api/post/<int: id>/data/user_favorite_tracks/')
def get_userdata(id):
    data = User.query.filter_by(id=id).first()
    if data is not None:
        datas = [data.serialize() for data in user.datas]
        return json.dumps({"data": datas}), 200
    else:
        return json.dumps({"error": "Post not found..."}), 404    


