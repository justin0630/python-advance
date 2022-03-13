from tkinter import *
from random import *


def hi_fun():
    print("hello singular")
    display.config(text="Hi Singular", fg="green", bg="orange")


win = Tk()
win.title("hi")
btn = Button(win, text="Click me", command=hi_fun)
btn.pack()
display = Label(win, text="hi", fg="#588795", bg="#00FFFF")
display.pack()
win.mainloop()
