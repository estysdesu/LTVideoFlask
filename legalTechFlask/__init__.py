from flask import Flask
from flask_dotenv import DotEnv
import os

# init the flask app
LegalTechFlask = Flask(__name__, instance_relative_config=True)

# imports
from legalTechFlask import views
