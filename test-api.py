import requests
import keys

url = "https://the-cocktail-db3.p.rapidapi.com/"


response = requests.get(url, headers=keys.headers)

data = response.json()

# for item in data:
    # print(item["title"])
for id in data:
    print(id["id"])


