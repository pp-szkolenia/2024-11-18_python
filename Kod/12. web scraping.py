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
