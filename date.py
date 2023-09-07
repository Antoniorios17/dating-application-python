import json
import requests
import headers

print("Welcome to the date simulator")
name = input("what is your name")
date_name = input("What is your date's name")

import requests

url = "https://the-cocktail-db3.p.rapidapi.com/"


response = requests.get(url, headers=headers.headers)

data = response.json()

print(data)