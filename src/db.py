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
            'userid': self.id,
            'spotifyid': self.spotify_id
        }

class Data(db.Model):
    __tablename__ = 'datas'
    id = db.Column(db.Integer, primary_key=True)
    """
    userprof = db.Column(db.String, nullable=True)
    userplay = db.Column(db.String, nullable=True)
    userfavartist = db.Column(db.String, nullable=True)
    userfavtrack = db.Column(db.String, nullable=True)
    """
    userid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    #spotifyid = db.Column(db.String, db.ForeignKey('user.spotify_id'), nullable=False)
    playlists = db.relationship('Playlist', cascade='delete')
    profiles = db.relationship('Profile', cascade='delete')
    artists = db.relationship('Artist', cascade='delete')
    tracks = db.relationship('Track', cascade='delete')

    

    def __init__(self, **kwargs):
        """
        self.userprof = kwargs.get('user_profile', '')
        self.userplay = kwargs.get('user_playlists', '')
        self.userfavartist = kwargs.get('user_favorite_artists', '')
        self.userfavtrack = kwargs.get('user_favorite_tracks', '')
        """
        self.userid = kwargs.get('userid', '')
    

    def serialize(self):
        return {
            """
            'user profile': self.userprof,
            'user playlists': self.userplay,
            'user favorite artists': self.userfavartist,
            'user favorite tracks': self.userfavtrack
            """
            'userdataid': self.id,
            'userid': self.userid,
            #'spotifyid': self.spotifyid
        }

class Playlist(db.Model):
    __tablename__ = 'playlists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    images = db.Column(db.String, nullable=True)
    dataid = db.Column(db.Integer, db.ForeignKey('datas.id'), nullable=False)

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.images = kwargs.get('images', '')
        self.dataid = kwargs.get('dataid')


    def serialize(self):
        return {
            'playlist id': self.id,
            'user playlists': self.userplay,
            'playlist image': self.images[0],
            'data id': self.dataid
        }
    
class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    #userprof = db.Column(db.String, nullable=True)
    display_name = db.Column(db.String, nullable=True)
    images = db.Column(db.String, nullable=True)
    dataid = db.Column(db.Integer, db.ForeignKey('datas.id'), nullable=False)

    def __init__(self, **kwargs):
        self.userprof = kwargs.get('user_profile', '')
        self.display_name = kwargs.get('user_name', '')
        self.images = kwargs.get('user_images', '')
        self.dataid = kwargs.get('dataid')

    def serialize(self):
        return {
            'user id': self.id,
            'user name': self.display_name,
            'user image': self.images[0],
            'data id': self.dataid
        }

class Artist(db.Model):
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    images = db.Column(db.String, nullable=True)
    genres = db.Column(db.String, nullable=True)
    dataid = db.Column(db.Integer, db.ForeignKey('datas.id'), nullable=False)

    def __init__(self, **kwargs):
        self.name = kwargs.get('artist name', '')
        self.images = kwargs.get('artist images', '')
        self.genres = kwargs.get('artist genres', '')
        self.dataid = kwargs.get('dataid')

    def serialize(self):
        return {
            'artist id': self.id,
            'artist name': self.name,
            'artist image': self.images[0],
            'artist genre': self.genres[0],
            'data id': self.dataid
        }

class Track(db.Model):
    __tablename__ = 'tracks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    url = db.Column(db.String, nullable=True)
    dataid = db.Column(db.Integer, db.ForeignKey('datas.id'), nullable=False)

    def __init__(self, **kwargs):
        self.name = kwargs.get('track name', '')
        self.url = kwargs.get('track url', '')
        self.dataid = kwargs.get('dataid')
        

    def serialize(self):
        return {
            'track id': self.id,
            'track name': self.name,
            'track url': self.url,
            'data id': self.dataid
        }



