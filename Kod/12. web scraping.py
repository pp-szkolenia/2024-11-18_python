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

soup.find_all("a", class_="tag")


soup.find_all("a")[3].attrs

soup.find_all("div", {'itemtype': 'http://schema.org/CreativeWork'})

soup.find_all("div", {'class': 'quote'})


# ---

url = "https://example.org"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')



soup.find("div")                               # znajdź pierwszy znacznik 'div' jaki napotkasz
soup.find_all("a")                             # znajdź wszystkie znaczniki 'a'
soup.find_all("a", "class_name")               # znajdź wszystkie znaczniki 'a' z klasą class_name
soup.find_all("p")[3].text                     # spośród wszystkich znaczników 'p' weź ten o indeksie 3 i wyciągnij jego zawartość
soup.find("span").attrs["class"]               # znajdź pierwszy znacznik 'span' i wyciągnij nazwę jego klasy
soup.find("h1").find("a")                      # znajdź znacznik "a" wewnątrz znacznika "h1"
soup.find("div", {"attr_name": "attr_value"})  # znajdź znacznik "div" z konkretną wartością danego atrybutu
