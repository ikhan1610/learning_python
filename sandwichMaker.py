'''Sandwich Maker
Write a program that asks users for their sandwich preferences.
The program should use PyInputPlus to ensure that they enter valid input, such as:

Using inputMenu() for a bread type: wheat, white, or sourdough.
Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
Using inputYesNo() to ask if they want cheese.
If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.
Come up with prices for each of these options, and have your program display a
total cost after the user enters their selection.'''

import pyinputplus as pyip
def sandwichMaker():
    price = {
        'wheat': 1.00,
        'white': 1.50,
        'sourdough': 2.00,
        'chicken': 2.00,
        'turkey': 2.50,
        'ham': 2.00,
        'tofu': 3.00,
        'cheddar': 1.00,
        'Swiss': 1.50,
        'mozzarella': 2.00,
        'mayo': 0.50,
        'mustard': 0.50,
        'lettuce': 0.50,
        'tomato': 0.50,
    }
    condiments = []
    counter = 0
    priceForSanwich = 0
    totalPrice = 0
    cheeseType = ''
    breadType = ''
    proteinType = ''
    breadType = pyip.inputMenu(['wheat', 'white', 'sourdough'],numbered=True)
    proteinType = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'],numbered=True)
    wantCheese = pyip.inputYesNo('Do you want cheese ? ')
    if wantCheese == 'yes':
        cheeseType = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'],numbered=True)
    else:
        cheeseType = ''
    while counter < 4:
        wantExtras = pyip.inputYesNo('Do you want mayo, mustard, lettuce, or tomato ? ')
        if wantExtras == 'yes':
            condiments.append(pyip.inputChoice(['mayo', 'mustard', 'lettuce','tomato'],limit=4))
            counter += 1
        else:
            break
    totalSandwiches = pyip.inputInt('How many sandwiches ? ',min=1)
    if breadType == 'wheat':
        priceForSanwich += price[breadType]
    elif breadType == 'white':
        priceForSanwich += price[breadType]
    elif breadType == 'sourdough':
        priceForSanwich += price[breadType]
    if proteinType == 'chicken':
        priceForSanwich += price[proteinType]
    elif proteinType == 'turkey':
        priceForSanwich += price[proteinType]
    elif proteinType == 'ham':
        priceForSanwich += price[proteinType]
    elif proteinType == 'tofu':
        priceForSanwich += price[proteinType]
    if cheeseType == 'cheddar':
        priceForSanwich += price[cheeseType]
    elif cheeseType == 'swiss':
        priceForSanwich += price[cheeseType]
    elif cheeseType == 'mozzarella':
        priceForSanwich += price[cheeseType]
    for condiment in condiments:
        priceForSanwich += price[condiment]
    totalPrice = priceForSanwich * totalSandwiches
    if totalSandwiches > 1:
        print(f'Your sandwiches cost ${totalPrice:.2f}')
    else:
        print(f'Your sandwich cost ${totalPrice:.2f}')
response = pyip.inputYesNo("Do you want sandwich ?")
if response == "yes":
    sandwichMaker()
else:
    print("Alright, you can have something else.")




