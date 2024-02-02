import requests


# response = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=33&lon=66&appid=')
# weather = response.json()
# print(weather)

url = "https://api.privatbank.ua/p24api/exchange_rates?date=29.01.2024"

response = requests.get(url)
exchange = response.json()
print("11111111111   ", exchange)

url2 = "https://api.privatbank.ua/p24api/exchange_rates?json&date=29.01.2024"
response2 = requests.get(url2)
exchange2 = response2.json()
print("2222222222    ", exchange2)

