"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app
from app import models, forms, db, login_manager
from flask_login import login_user, logout_user, current_user, login_required
from flask import render_template, request, redirect, url_for, flash, session, abort, jsonify, send_file, current_app, send_from_directory, g
from werkzeug.utils import secure_filename
from app.models import Posts, User, Likes
from app.forms import NewPostForm, RegisterForm, LoginForm
from datetime import datetime, timedelta
from werkzeug.security import check_password_hash
from functools import wraps
import jwt
# from flask_wtf.csrf import generate_csrf

import os


###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = db.session.execute(db.select(User).filter_by(username=username)).scalar()

        if user and check_password_hash(user.password, password):
            login_user(user)

            return jsonify({
            "message": "Login Successfully ",
            "username": username,
        })
        else:
            return jsonify({"errors": form_errors(form)}), 400  



# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
@login_manager.user_loader
def load_user(id):
    return db.session.execute(db.select(User).filter_by(id=id)).scalar()


# @app.route('/api/v1/csrf-token', methods=['GET'])
# def get_csrf():
#     return jsonify({'csrf_token': generate_csrf()})
# Endpoint for adding posts

@app.route('/api/v1/register', methods = ['POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        location = form.location.data
        biography = form.biography.data
        profile_photo = form.profile_photo.data
        filename = secure_filename(profile_photo.filename)
        profile_photo.save(os.path.join(current_app.root_path, 'uploads', filename))

        user = User(username=username, password=password, firstname=firstname, lastname=lastname, email=email, location=location, biography=biography, profile_photo=filename)
        db.session.add(user)
        db.session.commit()

        return jsonify({
            "message": "User Successfully added",
            "profile_photo": filename,
            "username": username
        })
    else:
        return jsonify({"errors": form_errors(form)}), 400



@app.route('/api/v1/users/<int:user_id>/posts', methods=['POST'])
def add_post(user_id):
    form = NewPostForm()
    # user = User.query.get_or_404(user_id)
    if form.validate_on_submit():
        photo = form.photo.data
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(current_app.root_path, 'uploads', filename))
        caption = form.caption.data
        user_id = user_id
        
        post = Posts(photo=filename, caption=caption, user_id=user_id)
        db.session.add(post)
        db.session.commit()

        return jsonify({
            "message": "Post Successfully added",
            "photo": filename,
            "caption": caption
        })
    else:
        return jsonify({"errors": form_errors(form)}), 400


@app.route('/api/v1/posts', methods=['GET'])
def get_posts():
    posts = Posts.query.all()
    posts_list = []
    for post in posts:
        likes_count = Likes.query.filter_by(post_id=post.id).count()
        posts_list.append({
            'id': post.id,
            'caption': post.caption,
            'created_on': post.created_on,
            'photo': f"/api/v1/photos/{post.photo}",
            'user': {
                'id': post.user.id,
                'username': post.user.username,
                'profile_photo': f"/api/v1/photos/{post.user.profile_photo}"
            },
            'like': {
                'count': likes_count
            }
        })
    return jsonify({'posts': posts_list})

@app.route('/users/<int:id>', methods=['GET'])
def user(id):
    user = db.session.execute(db.select(User).filter_by(id=id)).scalar()

    return jsonify({"id": user.id,
            "username": user.username,
            "firstname": user.firstname,
            "lastname": user.lastname,
            "location": user.location,
            "biography": user.biography,
            "joined_on": user.joined_on,
            "profile_photo": f"/api/v1/photos/{user.profile_photo}"
            })

@app.route('/api/v1/photos/<filename>', methods=['GET'])
def get_photo(filename):
    return send_from_directory(os.path.join(app.root_path, 'uploads'), filename)

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


# Create a JWT @requires_auth decorator
# This decorator can be used to denote that a specific route should check
# for a valid JWT token before displaying the contents of that route.
def requires_auth(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    auth = request.headers.get('Authorization', None) # or request.cookies.get('token', None)

    if not auth:
      return jsonify({'code': 'authorization_header_missing', 'description': 'Authorization header is expected'}), 401

    parts = auth.split()

    if parts[0].lower() != 'bearer':
      return jsonify({'code': 'invalid_header', 'description': 'Authorization header must start with Bearer'}), 401
    elif len(parts) == 1:
      return jsonify({'code': 'invalid_header', 'description': 'Token not found'}), 401
    elif len(parts) > 2:
      return jsonify({'code': 'invalid_header', 'description': 'Authorization header must be Bearer + \s + token'}), 401

    token = parts[1]
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])

    except jwt.ExpiredSignatureError:
        return jsonify({'code': 'token_expired', 'description': 'token is expired'}), 401
    except jwt.DecodeError:
        return jsonify({'code': 'token_invalid_signature', 'description': 'Token signature is invalid'}), 401

    g.current_user = user = payload
    return f(*args, **kwargs)

  return decorated

@app.route("/api/v1/generate-token")
def generate_token():
    timestamp = datetime.utcnow()
    payload = {
        "sub": 1,
        "iat": timestamp,
        "exp": timestamp + timedelta(minutes=3)
    }

    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')

    return jsonify(token=token)


@app.route('/api/v1/posts/<int:post_id>/like', methods=['POST'])
def like_post(post_id):
    # Extract user_id from the request, assuming it's sent in the JSON body
    data = request.json
    user_id = data.get('user_id')

    if not user_id:
        return jsonify({'errors': 'User ID is required'}), 400

    post = Posts.query.get(post_id)
    if not post:
        return jsonify({'errors': 'Post not found'}), 404

    # Check if the user has already liked the post
    if Likes.query.filter_by(post_id=post.id, user_id=user_id).first():
        return jsonify({'message': 'You have already liked this post'}), 400

    # Add like for the post by the user
    like = Likes(post_id=post.id, user_id=user_id)
    db.session.add(like)
    db.session.commit()

    return jsonify({'message': 'Post liked successfully'}), 200