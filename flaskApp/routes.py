from flask import render_template
from . import FlaskApp

# app routes
@FlaskApp.route("/index/")
@FlaskApp.route("/")
def index():
    return render_template("index.html")

