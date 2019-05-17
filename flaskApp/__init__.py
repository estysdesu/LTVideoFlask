from flask import Flask
import os

# init the flask app
FlaskApp = Flask(__name__, instance_relative_config=True)

# config
FlaskApp.config.from_object("config")
if os.path.exists("instance"):
    FlaskApp.config.from_pyfile("config.py")

# import modules
from .. import videoProcessing
