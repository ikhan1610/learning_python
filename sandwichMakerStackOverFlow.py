'''From Stackoverflow'''
import pyinputplus as pyip

customerOrder = []
costPerSandwich = 0
totalCost = 0.00
breadType = ['wheat', 'white', 'sourdough']
proteinType = ['chicken', 'turkey', 'ham', 'tofu']
cheeseType = ['cheddar', 'swiss', 'mozzarella']
condiments = ['mayo', 'mustard', 'lettuce','tomato']
#extras = []
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
while True:
    bread = pyip.inputMenu(breadType,prompt="What kind of bread do you care for ? \n",numbered= True)
    customerOrder.append(bread)
    protein = pyip.inputMenu(proteinType,prompt="What kind of protien keeps you healthy ? \n",numbered=True)
    customerOrder.append(protein)
    cheeseChoice = pyip.inputYesNo("Do you need cheese ? \n")
    if cheeseChoice == "yes":
        cheese = pyip.inputMenu(cheeseType,prompt="What kind of cheese satifies your appetite ? \n",numbered=True)
        customerOrder.append(cheese)
    else:
        cheeseChoice = ''
    for i in range(4):
        extra = pyip.inputYesNo(f'Do you care for {condiments[i]} ? \n')
        if extra == "yes":
            customerOrder.append(condiments[i])
        else:
            pass

    totalNumberOfSandwiches = pyip.inputInt("How many sandwiches to go ? \n")

    for item in customerOrder:
        costPerSandwich += price[item]

    totalCost = costPerSandwich * totalNumberOfSandwiches

    anythingElse = pyip.inputYesNo('Would you care for anything else ? \n')
    if anythingElse == "no":
        print(f'That would be ${totalCost:.2f}, Thank You')
        break
    else:
        continue

