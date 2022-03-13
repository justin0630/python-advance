import os
from pytube import YouTube
from moviepy.editor import VideoFileClip

video_path = "web-crawler/adv-12/小雪人.mp4"
if os.path.isfile(video_path):
    clip = VideoFileClip(video_path)
else:
    exit()
base_path = "web-crawler/adv-12/"
new_file = "雪人"
new_path = base_path + new_file + ".mp3"

i = 0
while os.path.isfile(new_path):
    i += 1
    new_path = base_path + new_file + str(i) + ".mp3"

clip.audio.write_audiofile(new_path)
print("Convert mp3 Success")