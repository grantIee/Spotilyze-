from flask_sqlalchemy import SQLAlchemy 
db = SQLAlchemy()
class User(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    datas = db.relationship('Data', cascade='delete')

    def __init__(self, **kwargs):
        self.items = kwargs.get('items', '')

    def serialize(self):
        return {
            'username': self.items
        }

class Data(db.Model):
    __tablename__ = 'datas'
    id = db.Column(db.Integer, primary_key=True)
    items = db.Column(db.String, nullable=False)
    postid = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

    def __init__(self, **kwargs):
        self.items = kwargs.get('items', '')
        self.postid = kwargs.get('postid')

    def serialize(self):
        return {
            'playlists': self.items
        }



        # top songs/
