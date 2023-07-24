'''
    Debugging Coin Toss
    The following program is meant to be a simple coin toss guessing game.
    The player gets two guesses (it’s an easy game). However, the program has several bugs in it.
    Run through the program a few times to find the bugs that keep the program from working correctly.
'''
import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    assert guess in ('heads','tails'), "No valid value was entered, exiting the program !!"
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if guess == 'heads':
    guess = 1
else:
    guess = 0
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    assert guess in ('heads','tails'), "No valid value was entered, exiting the program !!"
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
