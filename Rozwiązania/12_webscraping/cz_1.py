import requests

API_KEY = "7d0c48134ae346811fa50cf99109251f"

cities = ["Warszawa", "Kraków", "Poznań", "Wrocław"]

coordinates = {}
for city in cities:
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    lat = data[0]["lat"]
    lon = data[0]["lon"]
    coordinates[city] = [lat, lon]

print(coordinates)
