from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FloatField, TextAreaField, IntegerField, SelectField, SubmitField,DateField, TimeField
from wtforms.validators import InputRequired, DataRequired, NumberRange
from flask_wtf.file import FileField, FileAllowed, FileRequired

# Add any form classes for Flask-WTF here

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = StringField('Password', validators=[InputRequired()])
    firstname = StringField('Firstname', validators=[InputRequired()])
    lastname = StringField('Lastname', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    biography = TextAreaField('Biography', validators=[InputRequired()])
    profile_photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])

class NewPostForm(FlaskForm):
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    caption = TextAreaField('Caption', validators=[InputRequired()])

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

