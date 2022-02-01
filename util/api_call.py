import requests
import json

# open weather map

api_key = "d2d3e4f69596b98f5f12532bfc485c0a"
lat = "48.208176"
lon = "16.373819"
url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
response = requests.get(url)
data = response.json()
print(data)