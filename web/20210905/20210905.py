import datetime
from tkinter import *

b = datetime.date.today()
a = datetime.datetime.now().time()


def get_date():
    time = b
    display.config(text=str(time), fg='red')


def get_time():
    time = a
    display.config(text=str(time), fg='green')


def display_entry():
    a = float(input_data.get()) / 2.54
    display.config(text=str(a), fg='green')


windows = Tk()
windows.title("My first GUI")
display = Label(windows, text="")
display.pack()
btn1 = Button(windows, text='獲得今天日期', command=get_date)
btn1.pack()
btn2 = Button(windows, text='獲得現在時間', command=get_time)
btn2.pack()
input_data = Entry(windows)
input_data.pack()
btn3 = Button(windows, text='轉成英吋', command=display_entry)
btn3.pack()
windows.mainloop()
