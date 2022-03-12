from tkinter import *

a = 0


def hi_fun():
    print("Hi singular")
    display.config(text="Hi Singular", fg="green", bg="orange")
    a = True


win = Tk()
win.title("hi")
btn1 = Button(win, text="Show screen", command=hi_fun)
btn1.pack()
display = Label(win, text="hi", fg="#588795", bg="#00FFFF")
display.pack()
win.mainloop()
