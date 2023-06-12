'''Regex Search
Write a program that opens all .txt files in a folder and searches for any line that
matches a user-supplied regular expression. The results should be printed to the screen.'''

import re

with open('championsLeague.txt','r') as file:
    content = file.read()

randText = input("Enter a word you wish to search = ")

inputPattern = re.compile(randText)

outputPattern = re.search(inputPattern,content)

if outputPattern:
    print('Match Found..')
    print(outputPattern.group())
else:
    print('Pattern not found')

file.close()



