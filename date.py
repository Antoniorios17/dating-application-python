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
def get_api():
    url = "https://the-cocktail-db3.p.rapidapi.com/"
    response = requests.get(url, headers=keys.headers)
    data = response.json()
    return data
def get_menu():
    url = "https://the-cocktail-db3.p.rapidapi.com/"
    response = requests.get(url, headers=keys.headers)
    data = response.json()
    counter = 0
    drinks = {}
    print("Please select your drink of choice\n")
    while counter < 5:
        counter +=1
        drinks[str(counter)]=(data[r(1,132)]["title"])
    def show_menu():
        for key, values in drinks.items():
            print(key,values)
    return show_menu()
get_menu()

# randomize prices of all the drinks



# reduce budget by drink price


# function to track wellness of date


