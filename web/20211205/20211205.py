from pytube import YouTube
from moviepy.editor import *
import os
from tkinter import *


def cut_video():
    video_path = "web-crawler/adv-12/雪兒.mp4"
    if os.path.isfile(video_path):
        clip = VideoFileClip(video_path)
        clip = clip.subclip(int(url_info.get()), int(name_info.get()))
        i = 0
        base_path = "web-crawler/adv-12/"
        new_file = title_info.get()
        new_path = base_path + new_file + str(i) + ".mp4"
        while os.path.isfile(new_path):
            i += 1
            new_path = base_path + new_file + str(i) + ".mp4"
        clip.write_videofile(new_path)

        if (state.get()):
            print("checkval = True")
            clip.write_gif(base_path + new_file + str(i) + ".gif")
    else:
        exit()


windows = Tk()
windows.title("My Gif")
url = Label(windows, text="請輸入影片開始時間", font=('Arial', 12))
url.grid(row=0, column=0)
url_info = Entry(windows)
url_info.grid(row=0, column=1)

name = Label(windows, text="請輸入影片結束時間", font=('Arial', 12))
name.grid(row=1, column=0)
name_info = Entry(windows)
name_info.grid(row=1, column=1)

title = Label(windows, text="請輸入影片名字", font=('Arial', 12))
title.grid(row=2, column=0)
title_info = Entry(windows)
title_info.grid(row=2, column=1)

state = BooleanVar()
state.set(True)
chk = Checkbutton(windows, text="gif", var=state)
chk.grid(row=3, column=0)

btn = Button(windows, text='開始切割', command=cut_video)
btn.grid(row=3, columnspan=2)

movie_name = Label(windows, text="切割完畢")
movie_name.grid(row=4, columnspan=4)

windows.geometry("300x150")
windows.mainloop()
