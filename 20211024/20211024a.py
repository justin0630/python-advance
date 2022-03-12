import requests
import matplotlib.pyplot as plt

base_url = "https://data.epa.gov.tw/api/v1/"
api_num = "aqx_p_432?"
offset = "0"
limit = "50"
api_key = "9be7b239-557b-4c10-9775-78cadfc555e9"
send_url = base_url
send_url += api_num
send_url += "offset=" + offset
send_url += "&limit=" + limit
send_url += "&api_key=" + api_key
response = requests.get(send_url)
info = response.json()
a_list = []
b_list = []
c_list = []
if "fields" in info.keys():
    for i in range(int(limit)):
        data = info["records"][i]["County"]
        if data == "新北市":
            print("City=" + info["records"][i]["County"])
            a_list.append(info["records"][i]["SiteName"])
            print("County=" + info["records"][i]["SiteName"])
            print("AQI=" + info["records"][i]["AQI"])
            b_list.append(info["records"][i]["AQI"])
            print("PM2.5=" + info["records"][i]["PM2.5"])
            c_list.append(info["records"][i]["PM2.5"])
            print("Status=" + info["records"][i]["Status"] + "\n")
print(a_list)
print(b_list)
plt.plot(a_list, b_list, "r-^", label="AQI")
plt.plot(a_list, c_list, "g-o", label="PM2.5")
plt.legend(loc="best")
plt.show()
