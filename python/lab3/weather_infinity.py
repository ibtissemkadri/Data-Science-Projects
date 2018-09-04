import requests
import sys
import time
import signal

if len(sys.argv)==1:
	print("you have to inter the city name")
	sys.exit(0)
else:
	city=sys.argv[1]

api_key="bc3dbc9f88d3d484ee1865b765665f1b"

class Weather:
    def __init__(self, key):
        self.key=key
    def get_city_weather(self, city):
        r=requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+self.key)
        return r.json()
    def show_data(self, json_object):
        print("The temperature is" , json_object["main"]["temp"])
        print("The humidity is", json_object["main"]["humidity"])
        print("The weather description is", json_object["weather"][0]["description"])

weather_today=Weather(api_key)
obj=weather_today.get_city_weather(city)
        
while True:
    try:
        weather_today.show_data(obj)
        time.sleep(60)
    except keyboardInterept:
        sys.exit(0)
