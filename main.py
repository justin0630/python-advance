import requests, json
import matplotlib.pyplot as plt
from tkinter import *




def get_data():
    base_url = "https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"
    response = requests.get(base_url)
    info = response.json()
    a_list = []
    b_list = []
    c_list = []
    show = ''
    for i in info["retVal"]:

        if info["retVal"][i]["sarea"] == input_city.get():
            print("地點=" + info["retVal"][i]["sna"])
            print("總車輛=" + info["retVal"][i]["tot"])
            print("剩餘車輛=" + info["retVal"][i]["sbi"])
            a_list.append(info["retVal"][i]["sna"])
            b_list.append(int(info["retVal"][i]["tot"]))
            c_list.append(int(info["retVal"][i]["sbi"]))
            show += ("地點=" + info["retVal"][i]["sna"]) + (
                "總車輛=" + info["retVal"][i]["tot"]) + (
                    "剩餘車輛=" + info["retVal"][i]["sbi"] + "\n")
    print(a_list)
    print(b_list)
    print(c_list)
    plt.plot(a_list, b_list, "r-^", label="總共車輛")
    plt.plot(a_list, c_list, "g-o", label="剩餘車輛")
    plt.legend(loc="best")
    put_day1.config(text=show)

    plt.show()


def clean_screen():
    put_day1.config(text='')


win = Tk()
win.title("hi")

btn1 = Button(win, text="please entry city", command=get_data)
btn1.pack()
btn2 = Button(win, text="clean screen", command=clean_screen)
btn2.pack()
input_city = Entry(win)
input_city.pack()

put_day1 = Label(win, text="", fg="#588795", bg="#00FFFF")
put_day1.pack()
win.mainloop()
