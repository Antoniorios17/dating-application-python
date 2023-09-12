import json
import requests
from random import randint
import random


# # welcome statement
# print("Welcome to the date simulator\n")
# # name of customer
# name = input("What is your name: ").capitalize()
# # name of date
# date_name = input("What is your date's name: ").capitalize()
# print("")
# print(f"****** Welcome {name} and {date_name}! *******\n")


# set budget
budget = int(input("Please insert your budget: "))

# show the menu

def get_menu():
    url = "https://api.punkapi.com/v2/beers"
    r = requests.get(url)
    data = json.loads(r.text)
    counter = 0
    global menu
    menu = {}
    while counter < 6:
        counter +=1
        food_selection = random.choice(data[randint(0,len(data)-1)]["food_pairing"])
        menu[str(counter)]= food_selection
        
    def show_menu():
        for key, values in menu.items():
            print(key,values)
    return show_menu()

get_menu()

# randomize prices of all the menu
def reduce_budget():
    selection = input("Please select an item from the menu\n")
    price = randint(10,15)
    print(f'You selected {menu[selection]} and the price is ${price}')
    global budget
    budget = budget - price
    print(f"Your budget is now ${budget}")  

reduce_budget()


# function to track wellness of date

while True:
    
