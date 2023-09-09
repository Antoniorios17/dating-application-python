import requests
import keys
from random import randint as r
url = "https://the-cocktail-db3.p.rapidapi.com/"


response = requests.get(url, headers=keys.headers)

data = response.json()

# for item in data:
    # print(item["title"])

# get the ids 
# for id in data:
    # print(id["id"])

# print(len(data))

# print(r(0,9))
def get_menu():
    counter = 0
    drinks = {}
    while counter < 5:
        counter +=1
        drinks[str(counter)]=(data[r(1,132)]["title"])
    def print_menu():
        for key, values in drinks.items():
            print("1", key,values)
    return print_menu()
print(get_menu())

# print(data)