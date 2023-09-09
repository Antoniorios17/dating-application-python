import json
import requests
import keys #importing the api keys from another local file

url = "https://the-cocktail-db3.p.rapidapi.com/"


response = requests.get(url, headers=keys.headers)

data = response.json()

# print(data)


# welcome statement
print("Welcome to the date simulator")
# name of customer
name = input("what is your name: ")
# name of date
date_name = input("What is your date's name")


# set budget

# show the menu
  
  # randomize prices of all the drinks
  # reduce budget by drink price
# show selection of random 5 drinks
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

# randomize prices of all the drinks



# reduce budget by drink price


# function to track wellness of date


