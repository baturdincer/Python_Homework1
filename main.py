from moviepy.editor import VideoFileClip

videopath="rickrolled.mp4"
videoclip=VideoFileClip(videopath)

gifpath="rickrolledhaha.gif"
videoclip.write_gif(gifpath)