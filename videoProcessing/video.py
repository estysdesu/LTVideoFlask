from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, ImageClip

filePath = r"courtchanges20183.mp4"
videoOrig = VideoFileClip(filePath)

videoText = (TextClip("5432", fontsize=150, color="white", stroke_width=100)
             .set_position(("right", "top"))
             # (optional) logo-border padding
             .margin(right=50, top=50, opacity=0)
             .set_duration(videoOrig.duration)
             )

# videoText2 = (TextClip("LegalTechnicality.com", fontsize=100, color="white", stroke_width=500)
#        .set_pos(("left", "bottom"))
#        .margin(left=50, bottom=50, opacity=50)
#        .set_duration(videoOrig.duration)
#        )

watermark = (ImageClip("watermark.png")
             .set_position(("left", "bottom"))
             .margin(left=50, bottom=50, opacity=0)
             .set_duration(videoOrig.duration)
             )

videoOverlay = CompositeVideoClip([videoOrig, videoText, watermark])
videoOverlay.subclip(0, 5).write_videofile("videoOverlay.mp4")
