import requests
from pprint import pprint
from bs4 import BeautifulSoup


url = "https://quotes.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

pprint(
    [item.text for item in soup.find_all("a", "tag")]
)
