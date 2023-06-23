# Write your code here :-)
import random

numberOfStreaks = 0
hundredRandomList = []
numH = 0
numT = 0

for experimentNumber in range(10000):

    # Code that creates a list of 100 'heads' or 'tails' values.
    for i in range(100):
        if random.randint(0, 1) == 1:
            hundredRandomList.append("H")
        else:
            hundredRandomList.append("T")
    # print(hundredRandomList)
    # Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(len(hundredRandomList)):
        if hundredRandomList[i] == "H":
            numT = 0
            numH += 1
            if numH == 6:
                numberOfStreaks += 1
            # print('numH = ', numH)
        else:
            numH = 0
            numT += 1
            if numT == 6:
                numberOfStreaks += 1
            # print('numT = ', numT)
    hundredRandomList = []
print("Chance of streak: %s%%" % (numberOfStreaks / 100))
