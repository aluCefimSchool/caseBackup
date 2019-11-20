##
# INITIALISATION FLASK
##
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

#IMPORT CONFIGURATION FLASK
app.config.from_object(Config)

db = SQLAlchemy(app)

login = LoginManager(app)

#PROTECT ROUTE AGAINST ANONYMOUS USERS / @login_required
login.login_view = 'login'

from app import routes, models
