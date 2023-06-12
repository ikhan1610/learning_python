'''
    Write Your Own Multiplication Quiz
    To see how much PyInputPlus is doing for you, try re-creating the
    multiplication quiz project on your own without importing it.
    This program will prompt the user with 10 multiplication questions,
    ranging from 0 × 0 to 9 × 9. You’ll need to implement the following features:

    If the user enters the correct answer, the program displays “Correct!” for
    1 second and moves on to the next question.
    The user gets three tries to enter the correct answer before the program
    moves on to the next question.
    Eight seconds after first displaying the question, the question is marked
    as incorrect even if the user enters the correct answer after the 8-second limit.
    Compare your code to the code using PyInputPlus in “Project: Multiplication Quiz” on page 196.

'''

import pyinputplus as pyip
import random,time
count = 0
while count < 10:
    firstNumber = random.randint(0,9)
    secondNumber = random.randint(0,9)

    correctProduct = firstNumber * secondNumber
    try:
        product = pyip.inputInt(f'Q. #{count+1} Product of {firstNumber} and {secondNumber} is ? \n', timeout = 8)
        if correctProduct == product:
            print("Correct!")
            time.sleep(1)
        else:
            print("Incorrect")
    except pyip.TimeoutException:
        print("Incorrect")
    count += 1

