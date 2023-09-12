import json
import requests
from random import randint
import random


# welcome statement
print("Welcome to the date simulator\n")
# name of customer
name = input("What is your name: ").capitalize()
# name of date
date_name = input("What is your date's name: ").capitalize()
print("")
print(f"****** Welcome {name} and {date_name}! *******\n")

# amount of food in stomach rated to 10
belly_meter = 0

# set budget
budget = int(input("Please insert your budget: \n"))

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
    print("")
    selection = input("Please select an item from the menu: ")
    price = randint(15,25)
    print(f'You selected {menu[selection]} and the price for both is ${price}')
    global budget
    budget = budget - price*2
    print(f"Your budget is now ${budget}")  
    global belly_meter
    belly_meter = belly_meter + 2

reduce_budget()


# function to track wellness of date

while True:
    choice = input("Would you like to order more? (yes/no) ").strip().lower()
    if choice[0] == "y":
        get_menu()
        reduce_budget()
    elif choice[0] == 'n':
        print(f"Thank you for coming {name} and {date_name}")
        if belly_meter > 10:
            print(f"{date_name} had too much food")
            print(f'Sorry {name}, you are not getting a second date')
        elif belly_meter > 2 and belly_meter < 6:
            print(f'{date_name} had a great time and is satisfied')
            print(f'{name} you are getting a second date with {date_name}')

