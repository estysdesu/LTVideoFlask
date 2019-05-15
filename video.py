import moviepy.editor as mp

filePath = r"courtchanges20183.mp4"
videoOrig = mp.VideoFileClip(filePath)

videoText = (mp.TextClip("5432", fontsize=150, color="white", stroke_width=50)
        .set_position(("right", "top"))
        .margin(right=50, top=50, opacity=0) # (optional) logo-border padding
        .set_duration(videoOrig.duration)
        )
videoOverlay = mp.CompositeVideoClip([videoOrig, videoText])
videoOverlay.subclip(300, 350).write_videofile("videoOverlay.mp4")
