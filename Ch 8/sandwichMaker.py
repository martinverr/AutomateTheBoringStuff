"""
Write a program that asks users for their sandwich preferences.
The program should use PyInputPlus to ensure that they enter
valid input, such as:

Using inputMenu() for a bread type: wheat, white, or sourdough.
Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
Using inputYesNo() to ask if they want cheese.
If so, using inputMenu() to ask for a cheese type: cheddar, Swiss,
    or mozzarella.
Using inputYesNo() to ask if they want mayo, mustard, lettuce, or
    tomato.
Using inputInt() to ask how many sandwiches they want. Make sure this
    number is 1 or more.
Come up with prices for each of these options, and have your program
display a total cost after the user enters their selection.
"""

import pyinputplus as pyip

#Menu chosen(sandwich) and menu prices(prices)
sandwich={"bread":"wheat", "protein":"Chicken", "cheese":False, "numOfSandwitches":1}
prices = [  {"Wheat": 1, "White":1.25, "Sourdough":1.5},
            {"Chicken": 0.5, "Turkey": 1, "Ham": 0.75, "Tofu": 0.5},
            {True:1, False:0}]

#Take order
print("TYPE OF BREAD:")
sandwich["bread"] = pyip.inputMenu(['Wheat', 'White', 'Sourdough'], numbered=True)
print()

print("TYPE OF PROTEIN:")
sandwich["protein"]=pyip.inputMenu(['Chicken', 'Turkey', 'Ham', 'Tofu'], numbered=True)

sandwich["cheese"]=bool(pyip.inputYesNo("\nAdd cheese?[yes/no]"))

sandwich["numOfSandwitches"]=pyip.inputInt("\nHow many sandwiches would you like?", min=1)

print(sandwich)

#Calculate price
cost=0
counter=0
for ingredientType in sandwich:
    cost+=prices[counter][sandwich[ingredientType]]
    counter += 1
    if counter == 3: break
cost *= sandwich["numOfSandwitches"]
print(f"Total price:{cost}$")
