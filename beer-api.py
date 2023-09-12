import requests
import json
import random
from random import randint

url = "https://api.punkapi.com/v2/beers"
r = requests.get(url)
data = json.loads(r.text)
# print(json.dumps(data[0], indent = 4))
# print(data)
# for drink in data:
#     print(drink['name'])
# print(data[0]['food_pairing'][randint(0, len([data[0]['food_pairing']])+1)])


def get_menu():
    url = "https://api.punkapi.com/v2/beers"
    r = requests.get(url)
    data = json.loads(r.text)
    counter = 0
    drinks = {}
    print("Please select your drink of choice\n")
    while counter < 5:
        counter +=1
        food_selection = random.choice(data[randint(0,len(data))]["food_pairing"])
        drinks[str(counter)]= food_selection
        
    def show_menu():
        for key, values in drinks.items():
            print(key,values)
    return show_menu()

get_menu()



