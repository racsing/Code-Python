# Day 3 : Treasure Map

# Instructions
# You are going to write a program which will mark a spot with an X.
# our job is to write a program that allows you to mark a square on the map using a two-digit system. 
# The first digit is the vertical column number and 
# The second digit is the horizontal row number.

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? [Col][Row] ")
# 🚨 Don't change the code above 👆
col = int(position[0])
row = int(position[1])
map[row-1][col-1] = "X "

#Write your code below this row 👇






#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")