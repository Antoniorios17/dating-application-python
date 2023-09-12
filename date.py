import json
import requests
import keys #importing the api keys from another local file
from random import randint as r
import api

# welcome statement
print("Welcome to the date simulator\n")
# name of customer
# name = input("what is your name: ")
# name of date
# date_name = input("What is your date's name: ")


# set budget
budget = input("Please insert your budget: ")
# show the menu
  
  # randomize prices of all the drinks
  # reduce budget by drink price
# show selection of random 5 drinks

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

# randomize prices of all the drinks
def price_per_drink(price):
    price = r(10,15)
    return price



# reduce budget by drink price


# function to track wellness of date


