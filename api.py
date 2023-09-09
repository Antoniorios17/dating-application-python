import json
import requests
import keys
url = "https://the-cocktail-db3.p.rapidapi.com/"
response = requests.get(url, headers=keys.headers)
data = response.json()

print(data)