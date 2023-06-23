# guess the number game :-)
import random, sys

print('I am thinking of a number between 1 and 20.')
count = 0
myNumber = random.randint(1,20)
while True:
    print('Take a guess.')
    gNumber = int(input())
    count += 1
    if gNumber < myNumber :
        print('Your guess is too low.')
        continue
    elif gNumber > myNumber:
        print('Your guess is too high.')
        continue
    else:
        print('Good job! You guessed my number in '+ str(count) +' guesses!')
        break


