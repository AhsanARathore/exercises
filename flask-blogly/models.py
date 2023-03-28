from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)

"""Models for Blogly."""

default_image ="https://t4.ftcdn.net/jpg/01/36/08/69/360_F_136086944_knpNCEhMDywOOD3Ggu0ufUC2L2D8BVFm.jpg"


class User(db.Model):
    """Site user."""
    
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False, default=default_image)

    posts = db.relationship("Post", backref="user")


    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    

class Post(db.Model):
    """user Posts"""

    __tabelname__ = "posts"

    id = db.Column (db.Integer, primary_key=True, autoincrement=True)
    title = db.Column (db.Text, nullable=False)
    content = db.Column (db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'), nullable=False)