# Day 3 : Banker Roulette - Who will pay the bill?

import random
from posixpath import split


str = input("Enter a string containing a list of names separated by ',': \n")
list = str.split(", ")

# Option 1
# inbuilt function 'choice' exists in random module
# randname = random.choice(list) 
# print(f"{randname} is going to buy the meal.")

# Option 2
length_list = len(list)
rand_choice = random.randint(0, length_list -1)
print(f"{list[rand_choice]} is going to buy the meal.")

