'''Let’s use PyInputPlus to create a simple program that does the following:

Ask the user if they’d like to know how to keep an idiot busy for hours.
If the user answers no, quit.
If the user answers yes, go to Step 1.'''

import pyinputplus as pyip



while True:
    prompt = "Want to keep an idiot busy for hours \n"
    response = pyip.inputYesNo(prompt)
    if response == 'no':
        break

print('Thank you. Have a nice day.')

