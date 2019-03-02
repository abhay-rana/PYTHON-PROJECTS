#final project of whether

from requests import *

def by_city_name():
    city=input("enter city name")
    url="https://api.openweathermap.org/data/2.5/weather?q={}" \
        "&appid=787e8ad7306dbb237292e32c431116d0&units=metric".format(city)
    res=get(url)
    data=res.json()
    show_data(data)

def by_geo_location():
    res = get("https://ipinfo.io/")
    data = res.json()
    latit, longit = data["loc"].split(",")
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latit}&lon={longit}&appid=787e8ad7306dbb237292e32c431116d0&units=metric"
    res = get(url)
    data = res.json()
    show_data(data)

def show_data(data):
    temp = data["main"]["temp"]
    wind_speed = data["wind"]["speed"]
    latitude = data["coord"]["lat"]
    longitude = data["coord"]["lon"]
    description = data["weather"][0]["description"]
    print()
    print()
    print(f"temp is : {temp} degree celsius")
    print(f"wind speed is : {wind_speed} m\s")
    print(f"latitude is : {latitude}")
    print(f"longitude is : {longitude}")
    print(f"description is : {description}")

def main():
    print("1. Get Data By City")
    print("2. Get Data By Geographical Location")
    choice=input("enter your choice\n")
    if choice=="1":
        by_city_name()
    elif choice=="2":
        by_geo_location()
    else:
        print("you dont have enter the right choice")

if __name__== "__main__":
    main()

