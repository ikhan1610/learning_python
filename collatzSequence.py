# Collatz Sequence Generator :-)
import sys

def collatz(number): #Sequence generator function
    if number % 2 == 0:
        return number // 2
    else:
        return 3*number + 1

print("Enter a number to generate Collatz Sequence: ",end = '')
try:
    myNum = int(input())
    seqRec = collatz(myNum)
    print(seqRec)
    while seqRec != 1:
        seqRec = collatz(seqRec)
        print(seqRec)

except ValueError:
    print('Please enter an interger value')
