from tkinter import *


def move_canvas(event):
    key = event.keysym
    print(key)
    if key == "Right":
        canvas.move(circle, 10, 0)
    elif key == "Left":
        canvas.move(circle, -10, 0)
    elif key == "Up":
        canvas.move(circle, 0, -10)
    elif key == "Down":
        canvas.move(circle, 0, 10)


windows = Tk()
windows.title("Hi")
canvas = Canvas(windows, width=400, height=600)
canvas.pack()
img = PhotoImage(file='20210822/螢幕擷取畫面 2021-08-22 102448.png')
my_img = canvas.create_image(300, 300, image=img)
windows.iconbitmap("20210822/A0EDB242-611B-4EBC-A275-67AEFB4C6A10.ico  ")
circle = canvas.create_oval(100, 100, 300, 300, fill="red")
rect = canvas.create_rectangle(220, 400, 340, 430, fill="blue")
msg = canvas.create_text(300,
                         100,
                         text="Ninja",
                         fill="black",
                         font=('Ariel', 30))
canvas.bind_all('<Key>', move_canvas)
windows.mainloop()
