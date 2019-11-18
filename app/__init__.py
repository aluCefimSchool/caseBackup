##
# Initialisation Flask
##
from flask import Flask
from config import Config

#Predefined variable to configure Flask
app = Flask(__name__)
app.config.from_object(Config)

from app import routes
