from moviepy import editor as moviepy
import numpy as np 
import os
from datetime import datetime

from legalTechFlask import LegalTechFlask

"""
Exported: CapitalCamelCase
Unexported: lowerCamelCase
"""
packageDir = os.path.realpath(LegalTechFlask.root_path)
VideoDir = os.path.join( os.path.dirname(packageDir), "videos")


class Video():

    def __init__(self, videoOrig):
        self.VideoOrigName = videoOrig
        self.VideoDir = VideoDir
        self.VideoModName = self.getVideoModName()
        self.WatermarkPath = os.path.join(LegalTechFlask.root_path, "watermark.png")

    def getVideoModName(self):
        namePart, extPart = os.path.splitext( os.path.basename(self.VideoOrigName) )
        date = datetime.utcnow().strftime("%y%m%d")
        modName = namePart + "_" + date + "mod" + extPart

        return modName

    def overlayText(self, color, text, start, dur):
        text = (moviepy.TextClip(text, font="Adobe-Gothic-Std", fontsize=150, color=color)
            .set_position(("right", "top"))
            .margin(right=50, top=50, opacity=0)
            .set_duration(dur)
            .set_start(start)
            .crossfadein(0.5)
            .crossfadeout(0.5)
        )

        return text

    def overlayWatermark(self, dur, watermarkPath):
        watermark = (moviepy.ImageClip(watermarkPath)
            .set_position(("left", "bottom"))
            .margin(left=25, bottom=25, opacity=0)
            .set_duration(dur)
        )

        return watermark

    def Overlay(self):
        videoOrig = moviepy.VideoFileClip(self.VideoOrigName)
        videoOrigLen = videoOrig.duration

        codeAmts = 3 # how many video codes to create
        codeDur = 30 # unit: [s]
        codeColors = ["red", "green", "blue", "yellow", "purple", "orange"]
        np.random.shuffle(codeColors)
        codeColors = codeColors[0:codeAmts]
        codeNums = np.random.randint(0, 10000, codeAmts)
        codeNums = [str(n).zfill(4) for n in codeNums] # adds leading zeros for numbers less than 4 digits
        codeZip = list(zip(codeColors, codeNums))
        
        for indx, pair in enumerate(codeZip):

            if indx == 0:
                startTime = 15 # unit: [s]
            elif indx == 1:
                startTime = np.floor(videoOrigLen / 2).astype(int) - 15
            elif indx == 2:
                startTime = np.floor(videoOrigLen - 45).astype(int)

        videoText = self.overlayText(pair[0], pair[1], startTime, codeDur)
        videoWatermark = self.overlayWatermark(videoOrigLen, self.WatermarkPath)

        videoOverlayComp = moviepy.CompositeVideoClip([videoOrig, videoText, videoWatermark])
        
        return videoOverlayComp

    def Save(self, compClip):

        compClip.write_videofile( os.path.join(self.VideoDir, self.VideoModName) )

        pass


