import requests
import keys
from random import randint as r

def get_menu():
    url = "https://the-cocktail-db3.p.rapidapi.com/"
    response = requests.get(url, headers=keys.headers)
    data = response.json()
    counter = 0
    drinks = {}
    while counter < 5:
        counter +=1
        drinks[str(counter)]=(data[r(1,132)]["title"])
    def show_menu():
        for key, values in drinks.items():
            print(key,values)
    return show_menu()
get_menu()

# print(data)