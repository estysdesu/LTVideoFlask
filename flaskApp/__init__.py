from flask import Flask
from flask_dotenv import DotEnv
import os

# init the flask app
legalTechFlask = Flask(__name__, instance_relative_config=True)

# config
env = DotEnv(legalTechFlask)

# imports
from . import views

if __name__ == "__main__":
    legalTechFlask.run()