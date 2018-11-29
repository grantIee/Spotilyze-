'''

    db.py
    Grant Lee & Richard Yoon

    Database structure for Spotilyze API
'''
"""
class Track(db.Model):
    __tablename__ = 'track'
    id = db.Column(db.Integer, primary_key = True)
    
    


class User(db.Model):
    __tablename__ = 'user'


class Album(db.Model):
    __tablename__ = 'album'


class Playlist(db.Model):
    __tablename__ = 'playlist'


class Artist(db.Model):
    __tablename__ = 'artist'
    
"""

from flask_sqlalchemy import SQLAlchemy 
db = SQLAlchemy()
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    spotify_id = db.Column(db.String, nullable=False)
    datas = db.relationship('Data', cascade='delete')
    def __init__(self, **kwargs):
        self.spotify_id = kwargs.get('spotify_id', '')
        #self.items = kwargs.get('items', '')

    def serialize(self):
        return {
            'userid': self.id;
        }

class Data(db.Model):
    __tablename__ = 'datas'
    id = db.Column(db.Integer, primary_key=True)
    userprof = db.Column(db.String, nullable=True)
    userplay = db.Column(db.String, nullable=True)
    userfavartist = db.Column(db.String, nullable=True)
    userfavtrack = db.Column(db.String, nullable=True)
    postid = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

    def __init__(self, **kwargs):
        self.userprof = kwargs.get('user_profile', '')
        self.userplay = kwargs.get('user_playlists', '')
        self.userfavartist = kwargs.get('user_favorite_artists', '')
        self.userfavtrack = kwargs.get('user_favorite_tracks', '')
        self.postid = kwargs.get('postid')

    def serialize(self):
        return {
            'user profile': self.userprof,
            'user playlists': self.userplay,
            'user favorite artists': self.userfavartist,
            'user favorite tracks': self.userfavtrack
        }

