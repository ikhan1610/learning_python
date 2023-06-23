# Write your code here :-)
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def totalBought(guests,item):
    numBrought = 0

    for k,v in guests.items():
        numBrought += v.get(item,0)
    return numBrought

print('Number if things being broguht:')
print("- Apples                  " + str(totalBought(allGuests,'apples')))
print("- Sandwiches              " + str(totalBought(allGuests,'ham sandwiches')))
print("- Papper Plates           " + str(totalBought(allGuests,'Papper Plates')))
print("- Cups                    " + str(totalBought(allGuests,'cups')))
print("- Applie Pies             " + str(totalBought(allGuests,'apple pies')))
