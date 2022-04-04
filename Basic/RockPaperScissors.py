# Day 3 : Rock Paper Scissors

# Instructions
# Make a rock, paper, scissors game.

from random import randint
import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

yourchoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
list = [rock, paper, scissors]
length_list = len(list)
mychoice = random.randint(0, length_list -1)

# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.

if yourchoice >=3 or yourchoice < 0 :
    print("Invalid Number, You lose!")
else :
  print(list[yourchoice])
  print("Computer chose")
  print(list[mychoice])
  if ((yourchoice==0 and mychoice==2) or (yourchoice==1 and mychoice==0) or (yourchoice==2 and mychoice==1)) :
    print("YOU WIN !")
  elif  yourchoice == mychoice :
    print("DRAW !")
  else :
    print("YOU LOSE !")

