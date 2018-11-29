'''

    db.py
    Grant Lee & Richard Yoon

    Database structure for Spotilyze API
'''

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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
    


