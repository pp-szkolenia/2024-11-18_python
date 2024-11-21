import requests

API_KEY = "7d0c48134ae346811fa50cf99109251f"

cities = ["Warszawa", "Kraków", "Poznań", "Wrocław"]

def get_coordinates(city):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data[0]["lat"], data[0]["lon"]


def get_air_pollution(lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data["list"][0]["components"]["pm10"]


for city in cities:
    lat, lon = get_coordinates(city)
    pm10 = get_air_pollution(lat, lon)
    print(f"{city}: Współrzędne: {lat}, {lon}, PM10: {pm10} ug/m3")
