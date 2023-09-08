import json
import requests
import keys #importing the api keys from another local file

print("Welcome to the date simulator")
name = input("what is your name")
date_name = input("What is your date's name")

url = "https://the-cocktail-db3.p.rapidapi.com/"


response = requests.get(url, headers=keys.headers)

data = response.json()

print(data)

# welcome statement
# print("Welcome to the date simulator")

# name of customer
name = input("what is your name")

# name of date

date_name = input("What is your date's name")

# set budget

# show the menu
  # show selection of random 5 drinks
  # randomize prices of all the drinks
  # reduce budget by drink price


# function to track wellness of date

# 