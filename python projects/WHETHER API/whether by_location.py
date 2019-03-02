# URL="https://api.openweathermap.org/data/2.5/weather?q=CITY&appid={API KEY}"
# API KEY=787e8ad7306dbb237292e32c431116d0
# Temperature is available in Fahrenheit, Celsius and Kelvin units.
# For temperature in Fahrenheit use units=imperial
# For temperature in Celsius use units=metric
# Temperature in Kelvin is used by default, no need to use units parameter in API call

import requests
from pprint import pprint
city=input("enter city name")
url="https://api.openweathermap.org/data/2.5/weather?q={}" \
    "&appid=787e8ad7306dbb237292e32c431116d0&units=metric".format(city)
res=requests.get(url) #get the data on python script
data=res.json()  #convert the data to json ==dictionary
pprint(data)   #pprint gives us good theme of json data
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

## for writing the values in a txt files
# with open("file1.txt","w") as wf:
#     wf.write(f"temp is : {temp} degree celsius\n")
#     wf.write(f"wind speed is : {wind_speed} m\s\n")
#     wf.write(f"latitude is : {latitude}\n")
#     wf.write(f"longitude is : {longitude}\n")
#     wf.write(f"description is : {description}\n")
