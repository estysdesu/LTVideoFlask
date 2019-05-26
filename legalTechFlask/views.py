from flask import render_template, send_from_directory, redirect, url_for, request
from werkzeug import secure_filename
import os

from legalTechFlask import LegalTechFlask
from legalTechFlask.video import VideoDir, Video

# app routes
@LegalTechFlask.before_first_request
def startup():
    if not os.path.exists(VideoDir):
        os.makedirs(VideoDir)


@LegalTechFlask.route("/index/")
@LegalTechFlask.route("/")
def index():
    return render_template("index.html")

@LegalTechFlask.route("/upload/", methods=["POST"])
def upload_file():

    if request.method == "POST" and "ltVideo" in request.files:
        v = request.files["ltVideo"]
        vPath = os.path.join(VideoDir, secure_filename(v.filename))
        v.save(vPath)

        return redirect(url_for("processing_file", vName = v.filename))
    else:
        pass


@LegalTechFlask.route("/process/<vName>")
def processing_file(vName):

    vPath = os.path.join(VideoDir, vName)
    video = Video(vPath)
    compClip = video.Overlay()
    video.Save(compClip)
    
    # retrieve upload and call video processing
    # add progress bar?
    # when finished, redirect to download
    # handle erros with try except
    return redirect(url_for("return_file", newVName=video.VideoModName))

@LegalTechFlask.route("/download/<newVName>")
def return_file(newVName):

    return send_from_directory(VideoDir, newVName, as_attachment=True)

