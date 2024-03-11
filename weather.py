import requests
import json
import win32com.client as wincom
city = input("enter the name of the city\n")
url =f"https://api.weatherapi.com/v1/current.json?key=c83ab6d59f4243c5bdb161140241103&q={city}"

r=requests.get(url)
# print(r.text)

data = json.loads(r.text)
print(data["current"]["temp_f"])
speak = wincom.Dispatch("SAPI.SpVoice")
speak.Speak(f"The temperature of {city} is {data['current']['temp_f']} fahrenheit")