'''Let’s create a program that poses 10 multiplication problems to the user,
where the valid input is the problem’s correct answer.'''

import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(1,numberOfQuestions+1):
    # Pick two random numbers:
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    prompt = f'#{questionNumber}: {num1} x {num2} = '
    try:
        #Right answers are handled by allowRegexes.
        #Wrong answers are handled by blockRegexes, with a custom message.
        pyip.inputStr(prompt,allowRegexes = ['^%s$'%(num1 * num2)],
                             blockRegexes = [('.*','Incorrect')],
                             timeout = 8, limit =3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of Tries')
    else:
        # This block runs if no exceptions were raised in the try block.
        print('Correct!')
        correctAnswers += 1
    time.sleep(1)
print(f'Score: {correctAnswers} out of {numberOfQuestions}')


