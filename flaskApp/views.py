from flask import render_template, send_from_directory, redirect, url_for, request
from werkzeug import secure_filename
import os

from . import legalTechFlask
import videoProcessing

# get home dir and assign tmp folder; create if not exists
usrHome = os.path.expanduser("~")
fileDir = usrHome + "/" + "legalTechVideos/tmp/"
if not os.path.exists(fileDir):
    os.makedirs(fileDir)

filename = None

# app routes
@legalTechFlask.route("/index/")
@legalTechFlask.route("/")
def index():
    return render_template("index.html")

@legalTechFlask.route("/upload/", methods=["POST"])
def upload_file():
    if request.method == "POST" and "ltVideo" in request.files:
        global filename
        filename = request.files["ltVideo"].filename

        f = request.files["ltVideo"]
        f.save(fileDir + secure_filename(f.filename))

    # retrieve upload and call video processing
    # add progress bar?
    # when finished, redirect to download
        return redirect(url_for("return_file"))

@legalTechFlask.route("/download/")
def return_file():
    if filename is None:
        # flash("Please upload a file.")
        pass
    return send_from_directory(fileDir, filename, as_attachment=True)

