#SandwichMaker

import pyinputplus as pyip


cheese = None

bread = pyip.inputMenu( ['wheat', 'white', 'sourdough'], prompt="Please enter bread type:")
print("You have selected: " + bread)

protein = pyip.inputMenu( ['chicken','turkey','ham', 'tofu'], prompt="Please enter protein:")
print("You have selected: " + protein)

hasCheese = pyip.inputYesNo(prompt="Would you like cheese?")
print("You have selected "+ hasCheese)

if hasCheese == 'yes':
    cheese = pyip.inputMenu(['cheddar', 'swiss','mozzarella'],prompt="What cheese would you like?")
    print("You have selected "+ cheese)

hasMayo = pyip.inputYesNo(prompt="Would you like mayo?")
print("You have selected "+ hasMayo)

hasMustard = pyip.inputYesNo(prompt="Would you like Mustard?")
print("You have selected "+ hasMustard)

hasLettuce = pyip.inputYesNo(prompt="Would you like lettuce?")
print("You have selected "+ hasLettuce)

hasTomato = pyip.inputYesNo(prompt="Would you like Tomato?")
print("You have selected "+ hasTomato)

numberOfSandwiches = pyip.inputInt("how many sandwiches?")

sandwichTotal = 1 + 1
if hasCheese:
    sandwichTotal += 1
if hasMayo:
    sandwichTotal += 1
if hasLettuce:
    sandwichTotal += 1
if hasTomato:
    sandwichTotal += 1

total = numberOfSandwiches * sandwichTotal
print(total)
