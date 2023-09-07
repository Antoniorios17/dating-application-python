import json
import requests
import keys

print("Welcome to the date simulator")
name = input("what is your name")
date_name = input("What is your date's name")

import requests

url = "https://the-cocktail-db3.p.rapidapi.com/"


response = requests.get(url, headers=keys.headers)

data = response.json()

print(data)

# show the menu