from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False
csrf = CSRFProtect(app)
app.config.from_object(Config)
toolbar = DebugToolbarExtension(app)

db = SQLAlchemy(app)

migrate = Migrate(app, db)


# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


from app.models import *
from app import views