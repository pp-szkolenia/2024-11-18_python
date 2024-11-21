import requests


url = "http://localhost:8000"
response = requests.get(url)
# print(type(response), response.status_code, response.ok)

print(response.json())


import requests


API_KEY = "bef18344d09a9963fda9d0c8402ace0e"  # wpisz swój klucz API
DATE = "2019-05-12"
CURRENCIES_LIST = "EUR,PLN"

# my_url = f"http://api.currencylayer.com/historical?access_key={API_KEY}&date={DATE}&currencies={CURRENCIES_LIST}"

url = "http://api.currencylayer.com/historical"
params = {"access_key": API_KEY, "date": DATE, "currencies": CURRENCIES_LIST}
response = requests.get(url, params=params)
data = response.json()
# print(response.url)
print(data)


CITY = "Krakow"
API_KEY = "7d0c48134ae346811fa50cf99109251f"  # wpisz swój klucz API

my_url = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(my_url)
data = response.json()

for item in data["list"]:
    print(item["dt_txt"], item["main"]["temp"], sep=' | ')


# -------------
from pprint import pprint
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

pprint(
    [item.text for item in soup.find_all("a", "tag")]
)
