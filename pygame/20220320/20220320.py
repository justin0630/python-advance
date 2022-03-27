from pytube import YouTube
from moviepy.editor import VideoFileClip
import sys
import os

os.chdir(sys.path[0])
url = "https://www.youtube.com/watch?v=ugk2e_5WZ8E"  #請輸入YT網址
yt = YouTube(url)
print("We are downloading video...")
video = yt.streams
result = video.filter(progressive=False, subtype="mp4", res="360p")
print(result[0])
fname = "music.mp4"
result[0].download(filename=fname)
print("Download finished...")
if os.path.isfile(fname):
    clip = VideoFileClip(fname)
else:
    exit()
new_file = "music"
new_path = new_file + ".mp3"
i = 0
while os.path.isfile(new_path):
    i += 1
    new_path = new_file + str(i) + ".mp3"
clip.audio.write_audiofile(new_path)
print("Convert mp3 Success")