from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, ImageClip
import numpy as np 
import os

"""
Exported: CapitalCamelCase
Unexported: lowerCamelCase
"""

class Video():

    def __init__(self, videoOrig):
        self.VideoOrig = videoOrig

        self.VideoDir = self.getVideoDir()
        self.VideoMod = self.getVideoModName()
        self.WatermarkPath = r"videoProcessing/watermark.png" # need to make not set
        self.Colors = ["red", "green", "blue", "yellow", "purple", "orange"]
        self.FlashCodeDur = 10 # desc: color/number code duration for video; unit: [s]
        self.Flashes = 4 # desc: number of video code flashes in each video

    def getVideoDir(self):
        usrHome = os.path.expanduser("~")
        videoDir = usrHome + "/" + "legalTechVideos/tmp"
        return videoDir

    def getVideoModName(self):
        namePart, extPart = os.path.splitext(self.VideoOrig)
        modName = namePart + "_mod" + extPart
        return modName

    def getWatermarkPath(self):
        # self.__module__
        # self.__package__
        # os.path.dirname(existGDBPath)
        pass

    def Overlay(self):
        """
        Desc:
            Create video overlay composite clip
        Args:

        Returns:

        """






# numCodeDuration = 5  # seconds


# def segmentDivider(length, overlap, cutSize):
#     from numpy import linspace, array

#     ar = linspace(0, length, (int(length/cutSize)+1))

#     x = 0

#     ar2 = [[0, int(ar[1])]]

#     x = 1

#     while x <= (len(ar)-2):
#         ar2.append([int(ar[x]-overlap), int(ar[x+1])])
#         x = x+1

#     print(ar)
#     print(ar2)

#     return ar2


# filePath = r"courtchanges20183.mp4"
# videoOrig = VideoFileClip(filePath)

# videoLength = videoOrig.duration

# colors = ["red", "green", "blue", "yellow", "purple", "orange"]
# shuffle(colors)

# ar = segmentDivider(videoLength, 3, 40)

# for q in range(len(ar)):
#     print(q)
#     videoText = (TextClip(str(randint(1000, 10000)), font="Adobe-Gothic-Std", fontsize=150, color=colors[q])
#                  .set_position(("right", "top"))
#                  # (optional) logo-border padding
#                  .margin(right=50, top=50, opacity=0)
#                  .set_duration(numCodeDuration)
#                  .set_start(randint(ar[q][0], (ar[q][1]-numCodeDuration)))
#                  .crossfadein(0.5)
#                  .crossfadeout(0.5)
#                  )

#     watermark = (ImageClip(r"watermark.png")
#                  .set_position(("left", "bottom"))
#                  .margin(left=25, bottom=25, opacity=0)
#                  .set_duration(videoOrig.duration)
#                  )

#     videoOverlay = CompositeVideoClip([videoOrig, videoText, watermark])
#     videoOverlay.subclip(ar[q][0], ar[q][1]).write_videofile(
#         "videoOverlay"+str(q)+".mp4")
