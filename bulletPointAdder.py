#! python3
#  bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip

text = pyperclip.paste()


# Split the list of LISTS of LISTS
listOfLists = text.split('\n') #loop through all indexes in the "listOfLists" list
for i  in range(len(listOfLists)):
    listOfLists[i] = "* "+listOfLists[i] #add star to each string in "listOfLists" list
text = ('\n').join(listOfLists)
print("Your List with * is ready")
pyperclip.copy(text)


