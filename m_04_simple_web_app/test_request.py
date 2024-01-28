import requests

# response = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11')
# exchange_rate = response.json()
# print(exchange_rate)
#

# response = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=33&lon=66&appid=')
# weather = response.json()
# print(weather)

url = "https://api.privatbank.ua/p24api/exchange_rates?date=01.12.2014"

response = requests.get(url)
exchange = response.json()
print("11111111111   ", exchange)

url2 = "https://api.privatbank.ua/p24api/exchange_rates?json&date=01.12.2014"
response2 = requests.get(url2)
exchange2 = response2.json()
print("2222222222    ", exchange2)
