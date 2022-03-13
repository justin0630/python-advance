from tkinter import *

a = 0


def hi_fun():
    print("Hi singular")
    display.config(text="Hi Singular", fg="green", bg="orange")


def bye_fun():

    display.config(text="Hi Singular", fg="white", bg="white")


win = Tk()
win.title("hi")
btn1 = Button(win, text="Show screen", command=hi_fun)
btn1.pack()
btn2 = Button(win, text="Clear screen", command=bye_fun)
btn2.pack()

display = Label(win, text="hi", fg="#588795", bg="#00FFFF")
display.pack()
win.mainloop()
