import requests, json
from tkinter import *


def get_data():
    api_key = "2f7671995fd280c1b8c10843d66b3f93"
    base_url = "https://api.openweathermap.org/data/2.5/onecall?"
    exclude = "minutely,hourly"
    units = "metric"
    lang = "zh_tw"
    lat = input_lat.get()
    lon = input_lon.get()
    send_url = base_url
    send_url += "lat=" + lat
    send_url += "&lon=" + lon
    send_url += "&exclude=" + exclude
    send_url += "&appid=" + api_key
    send_url += "&units=" + units
    send_url += "&lang=" + lang
    response = requests.get(send_url)
    info = json.loads(response.text)
    print(info)
    days = [
        put_day1.config, put_day2.config, put_day3.config, put_day4.config,
        put_day5.config, put_day6.config, put_day7.config
    ]

    try:
        if info["lat"] != "":
            for i in range(7):
                temps = info["daily"][i]["temp"]["day"]
                print("Day%d Temp=%s C" % (i, temps))
                days[i](text="Day%d Temp=%s C" % (i, temps))
    except:
        print(" Request Fail ")


win = Tk()
win.title("hi")
btn1 = Button(win, text="讀取七天，天氣預報", command=get_data)
btn1.pack()

put_day1 = Label(win, text="", fg="#588795", bg="#00FFFF")
put_day2 = Label(win, text="", fg="#588795", bg="#00FFFF")
put_day3 = Label(win, text="", fg="#588795", bg="#00FFFF")
put_day4 = Label(win, text="", fg="#588795", bg="#00FFFF")
put_day5 = Label(win, text="", fg="#588795", bg="#00FFFF")
put_day6 = Label(win, text="", fg="#588795", bg="#00FFFF")
put_day7 = Label(win, text="", fg="#588795", bg="#00FFFF")
input_lat = Entry(win)
input_lat.pack()
input_lon = Entry(win)
input_lon.pack()

put_day1.pack()
put_day2.pack()
put_day3.pack()
put_day4.pack()
put_day5.pack()
put_day6.pack()
put_day7.pack()
win.mainloop()
