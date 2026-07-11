import requests
city=input("entre city:")
url=f"https://wttr.in/{city}?format=j1"
response=requests.get(url)
data=response.json()
temp=data["current_condition"][0]["temp_C"]
print("temperature",temp,"C")
humidity=data["current_condition"][0]["humidity"]
condition=data["current_condition"][0]["weatherDesc"][0]["value"]
windspeed=data["current_condition"][0]["windspeedKmph"]
print("Humidity:",humidity,"%")
print("weather:",condition)
print("wind speed:",windspeed,"km/h")
print("\n -------hourly forecast-------")
hourly=data["weather"][0]["hourly"]
for hour in hourly:
    print(
        f"time:{hour['time']} |"
        f"temp:{hour['tempC']}C |"
        f"humidity:{hour['humidity']}% |"
        f"weather:{hour['weatherDesc'][0]['value']} |"
    )

