'''
    db2.py
    Grant Lee & Jaemok Yoon

    Database structure for Spotilyze API
'''
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    spotify_id = db.Column(db.String, nullable=False)
    date_last_refreshed = db.Column(db.DateTime, nullable=False)
    user_data = db.relationship('Data', cascade='delete')
    

    def __init__(self, **kwargs):
        self.spotify_id = kwargs.get('spotify_id', '')
        self.date_last_refreshed = kwargs.get('date_last_refreshed', '')

    def serialize(self):
        return {
            'user_id': self.id,
            'spotify_id': self.spotify_id,
            'date_last_refreshed': str(self.date_last_refreshed),
        }

class Data(db.Model):
    __tablename__ = 'data'

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user_top_tracks_short = db.Column(db.String, nullable=False)
    user_top_tracks_mid = db.Column(db.String, nullable=False)
    user_top_tracks_long = db.Column(db.String, nullable=False)
    user_top_artists_short = db.Column(db.String, nullable=False)
    user_top_artists_mid = db.Column(db.String, nullable=False)
    user_top_artists_long = db.Column(db.String, nullable=False)
    user_profile = db.Column(db.String, nullable=False)
    user_playlists = db.Column(db.String, nullable=False)

    def __init__(self, **kwargs):
        self.user_top_artists_short = kwargs.get('user_top_artists_short', '')
        self.user_top_artists_mid = kwargs.get('user_top_artists_mid', '')
        self.user_top_artists_long = kwargs.get('user_top_artists_long', '')
        self.user_top_tracks_short = kwargs.get('user_top_tracks_short', '')
        self.user_top_tracks_mid = kwargs.get('user_top_tracks_mid', '')
        self.user_top_tracks_long = kwargs.get('user_top_tracks_long', '')
        self.user_profile = kwargs.get('user_profile', '')
        self.user_playlists = kwargs.get('user_playlists', '')
    
    def serialize(self):
        return {
            'user_top_artists_short' : self.user_top_artists_short,
            'user_top_artists_mid' : self.user_top_artists_mid,
            'user_top_artists_long' : self.user_top_artists_long,
            'user_top_tracks_short' : self.user_top_tracks_short,
            'user_top_tracks_mid' : self.user_top_tracks_mid,
            'user_top_tracks_long' : self.user_top_tracks_long,
            'user_profile' : self.user_profile,
            'user_playlists': self.user_playlists
        }

    