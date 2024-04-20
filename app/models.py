from datetime import datetime, timezone
from . import db
from werkzeug.security import generate_password_hash
from sqlalchemy.orm import relationship

# Add any model classes for Flask-SQLAlchemy here
class User(db.Model):
    __tablename__='Users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(200))
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    email = db.Column(db.String(200))
    location = db.Column(db.String(400))
    biography = db.Column(db.String(800))
    profile_photo = db.Column(db.String(100))
    joined_on = db.Column(db.DateTime, default=datetime.now)
    # Relationship with posts made by the user
    posts = relationship('Posts', backref='author', lazy='dynamic')

    # Relationship with followers
    followers = relationship('Follows', foreign_keys='Follows.user_id', backref='followed_user', lazy='dynamic')

    # Relationship with followed users
    followed = relationship('Follows', foreign_keys='Follows.follower_id', backref='follower', lazy='dynamic')


    def count_posts(self):
        return self.posts.count()

    # Method to count the number of followers for the user
    def count_followers(self):
        return self.followers.count()

    # Method to count the number of users the user follows
    def count_followed_users(self):
        return self.followed.count()


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)


    def __repr__(self):
        return '<User %r>' % (self.username)
    
    def __init__(self,username, password, firstname, lastname, email, location, biography, profile_photo,joined_on):
        self.username = username
        self.password = generate_password_hash(password, method='pbkdf2:sha256')
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.location = location
        self.biography = biography
        self.profile_photo = profile_photo
        self.joined_on = joined_on
        
class Posts(db.Model):
    __tablename__='Posts'
    id = db.Column(db.Integer, primary_key = True)
    caption = db.Column(db.String(400))
    photo = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
    created_on = db.Column(db.DateTime, default=datetime.now)
    # Relationship with likes on the post
    likes = relationship('Likes', backref='post', lazy='dynamic')

    def get_id(self):
        return str(self.id)
    
    # Method to count the number of likes for the post
    def count_likes(self):
        return self.likes.count()

    def __repr__(self):
        return '<Post %r>' % (self.caption)
    
    def __init__(self, caption, photo, user_id, created_on):
        self.caption = caption
        self.photo = photo
        self.user_id = user_id
        self.created_on = created_on

class Likes(db.Model):
    __tablename__='Likes'
    id = db.Column(db.Integer, primary_key = True)
    post_id = db.Column(db.Integer, db.ForeignKey('Posts.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))

    def get_id(self):
        return str(self.id)
    
    def __repr__(self):
        return '<Like %r>' %(self.id)

class Follows(db.Model):
    __tablename__='Follows'
    id = db.Column(db.Integer, primary_key = True)
    follower_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
    
    

