import requests

CITY = "Krakow"
API_KEY = "7d0c48134ae346811fa50cf99109251f"  # wpisz swój klucz API

my_url = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(my_url)
data = response.json()

for item in data["list"]:
    print(item["dt_txt"], item["main"]["temp"], sep=' | ')
