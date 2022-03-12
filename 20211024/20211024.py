import requests

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
if "fields" in info.keys():
    for i in range(int(limit)):
        data = info["records"][i]["County"]
        if data == "臺北市":
            print("City=" + info["records"][i]["County"])
            print("County=" + info["records"][i]["SiteName"])
            print("AQI=" + info["records"][i]["AQI"])
            print("PM2.5=" + info["records"][i]["PM2.5"])
            print("Status=" + info["records"][i]["Status"] + "\n")
