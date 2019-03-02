#GETTING WHETHER BY GEOGRAPHICAL COORDINATES
#LONGITUDE AND LATITUDE
# it automatically detect my location and give me the temperature
#url="https://api.openweathermap.org/data/2.5/" \
#    "weather?lat=28.65&lon=77.22&appid=787e8ad7306dbb237292e32c431116d0&units=metric"
# API KEY=787e8ad7306dbb237292e32c431116d0

from requests import *
from pprint import pprint
res=get("https://ipinfo.io/")
data=res.json()
latit,longit=data["loc"].split(",")
url=f"https://api.openweathermap.org/data/2.5/weather?lat={latit}&lon={longit}&appid=787e8ad7306dbb237292e32c431116d0&units=metric"
res=get(url)
data=res.json()
pprint(data)
temp=data["main"]["temp"]
wind_speed=data["wind"]["speed"]
latitude=data["coord"]["lat"]
longitude=data["coord"]["lon"]
description=data["weather"][0]["description"]
print()
print()
print(f"temp is : {temp} degree celsius")
print(f"wind speed is : {wind_speed} m\s")
print(f"latitude is : {latitude}")
print(f"longitude is : {longitude}")
print(f"description is : {description}")
