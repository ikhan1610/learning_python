# Write your code here :-)
# Write your code here :-)
import random

numberOfStreaks = 0
hundredRandomList = []
streak = 0

for experimentNumber in range(10000):

    # Code that creates a list of 100 'heads' or 'tails' values.
    for i in range(100):
        if random.randint(0,1) == 1:
            hundredRandomList.append('H')
        else:
            hundredRandomList.append('T')

    # Code that checks if there is a streak of 6 heads or tails in a row.
        if i == 0:
            continue
        elif hundredRandomList[i] == hundredRandomList[i-1]:
            streak += 1
        else:
            streak = 0
        if streak == 6:
            numberOfStreaks += 1

    hundredRandomList = []

print('Chance of streak: %s%%' % (numberOfStreaks / 100))


