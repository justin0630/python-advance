import requests
from tkinter import *


def get_weather():
    api_key = "2f7671995fd280c1b8c10843d66b3f93"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = city_info.get()
    units = "metric"
    lang = "zh_tw"

    send_url = base_url
    send_url += "appid=" + api_key
    send_url += "&q=" + city_name
    send_url += "&units=" + units
    send_url += "&lang=" + lang

    # print("%s\n" % send_url)
    response = requests.get(send_url)
    info = response.json()

    if "main" in info.keys():
        temp_info = info["main"]["temp"]
        weather_info = info["weather"][0]["description"]
        print("City = " + city_name)
        put_city.config(text="City = " + city_name)
        print("Temperature = " + str(temp_info))
        put_temp.config(text="Temperature = " + str(temp_info))
        print("Description = " + str(weather_info))
        put_disc.config(text="Description = " + str(weather_info))
    else:
        print(" City Not Found ")


windows = Tk()
windows.title("My Weather")

put_city = Label(windows, text="city:")
put_city.pack()

put_temp = Label(windows, text="temp:")
put_temp.pack()

put_disc = Label(windows, text="disc:")
put_disc.pack()

city_info = Entry(windows)
city_info.pack()

btn = Button(windows, text='get weather', command=get_weather)
btn.pack()

windows.mainloop()
