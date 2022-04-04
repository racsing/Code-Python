# Day 1 : Tip Calculator

# Instructions
# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Example Input
# Welcome to the tip calculator!
# What was the total bill? $124.56
# How much tip would you like to give? 12
# How many people to split the bill? 7

# Example Output
# Each person should pay: $19.93
#=================================================================================================

#Solution

#1 Create a greeting for your program.
print("Welcome to the tip calculator..")

#2 Ask the user for the bill.
bill = float(input("What was the total bill ? $"))

#3 Ask the user for the tip percentage
tip = int(input("What percentage tip would you like to give ? ->"))

#4 How many people to split the bill?
people = int(input("How many people to split the bill ? ->"))

#5 Calculate the bill
amount = bill + (bill * (tip / 100))
pay = amount / people
print(f"Each person should pay ${round(pay,2)}")
