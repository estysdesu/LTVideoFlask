from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

filePath = r"courtchanges20183.mp4"
videoOrig = VideoFileClip(filePath)

videoText = (TextClip("5432", fontsize=150, color="white", stroke_width=100)
        .set_position(("right", "top"))
        .margin(right=50, top=50, opacity=0) # (optional) logo-border padding
        .set_duration(videoOrig.duration)
        )

videoText2 = (TextClip("LegalTechnicality.com", fontsize=100, color="white", stroke_width=500)
        .set_pos(("left", "bottom"))
        .margin(left=50, bottom=50, opacity=50)
        .set_duration(videoOrig.duration)
        )

videoOverlay = CompositeVideoClip([videoOrig, videoText, videoText2])
videoOverlay.subclip(0, 60).write_videofile("videoOverlay.mp4")
