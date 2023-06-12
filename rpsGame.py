#:Let's build a game:-)
import random, sys

print('ROCK, PAPER, SCISSORS')

win = 0
losses = 0
ties = 0

while True:
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    plyMove = input()
    if plyMove == 'q':
        sys.exit()
    elif plyMove == 'r':
        print('ROCK versus...')
    elif plyMove == 'p':
        print('PAPER versus...')
    elif plyMove == 's':
        print('SCISSORS versus...')
    else:
        print('Make a valid move')
        continue

    compMoveNum = random.randint(1,3)
    if compMoveNum == 1:
        compMoveLttr = 'r'
        print('ROCK')
        if plyMove == compMoveLttr:
            print('It is a tie!')
            ties += 1
            print('%s Wins %s Losses %s Ties'%(win,losses,ties))
        elif plyMove == 'p':
            print('Haya win!')
            win += 1
            print('%s Wins %s Losses %s Ties'%(win,losses,ties))
        else:
            print('Computer wins!')
            losses += 1
            print('%s Wins %s Losses %s Ties'%(win,losses,ties))
    elif compMoveNum == 2:
        compMoveLttr = 'p'
        print('PAPER')
        if plyMove == compMoveLttr:
            print('It is a tie!')
            ties += 1
            print('%s Wins %s Losses %s Ties'%(win,losses,ties))
        elif plyMove == 's':
            print('Haya win!')
            win += 1
            print('%s Wins %s Losses %s Ties'%(win,losses,ties))
        else:
            print('Computer win!')
            losses += 1
            print('%s Wins %s Losses %s Ties'%(win,losses,ties))
    else:
        compMoveLttr = 's'
        print('SCISSORS')
        if plyMove == compMoveLttr:
            print('It is a tie!')
            ties += 1
            print('%s Wins %s Losses %s Ties'%(win,losses,ties))
        elif plyMove == 'r':
            print('Haya win!')
            win += 1
            print('%s Wins %s Losses %s Ties'%(win,losses,ties))
        else:
            print('Computer win!')
            losses += 1
            print('%s Wins %s Losses %s Ties'%(win,losses,ties))





