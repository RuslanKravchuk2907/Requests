import requests
from API import API_TOKEN

params = {"q" : "Лондон", "appid" : API_TOKEN}

response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)

print(response.status_code)
# print(response.headers)
# print(response.text)