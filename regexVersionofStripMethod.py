'''Write a function that takes a string and does the same thing as
the strip() string method. If no other arguments are passed other than
the string to strip, then whitespace characters will be removed from the
beginning and end of the string. Otherwise, the characters specified in
the second argument to the function will be removed from the string.

>>> spam = '    Hello, World    '
>>> spam.strip()
'Hello, World'
>>> spam.lstrip()
'Hello, World    '
>>> spam.rstrip()
'    Hello, World'


>>> spam = 'SpamSpamBaconSpamEggsSpamSpam'
>>> spam.strip('ampS')
'BaconSpamEggs'
'''

'''import re #my logic

def regexStripMethod(word, char = ''):
    stripRegexPattern = re.compile(r'\w')
    wordTuple = stripRegexPattern.findall(word)
    print(wordTuple)
    lengthofWordTuple = len(wordTuple)
    finalWord = ''
    i = 0
    if char == ' ':
        wordTuple[0] = ''
        wordTuple[lengthofWordTuple-1] = ''
        for c in wordTuple:
            finalWord += c
        print(f'Stripped string is \"{finalWord}\"')
    else:
        for c in wordTuple:
            if c == char:
                wordTuple[i] = ''
            i += 1
        for c in wordTuple:
            finalWord += c
        print(f'Stripped final string is \"{finalWord}\"')

userString = input('Enter a string: ')
charToBeRemoved = input('Enter character to be stripped: ')
if charToBeRemoved == ' ' or charToBeRemoved == None:
    regexStripMethod(userString)
else:
    regexStripMethod(userString,charToBeRemoved)'''


# logic that I'm trying from StackOverFlow

import re

def stripMethodWithRegex(string, ch = ' '):
    if ch == ' ':
        print(string)

        leftStripPattern = re.compile(r'^\s+')
        rightStripPattern = re.compile(r'\s+$')
        #newString = leftStripPattern.findall(string)
        newString = leftStripPattern.sub('',string)
        newString = rightStripPattern.sub('',newString)
        print(newString)
    else:
        print(string)
        leftStripPattern = re.compile(r'^[{ch}]+'.format(ch=ch))
        rightStripPattern = re.compile(r'[{ch}]+$'.format(ch=ch))
        #newString = rightStripPattern.findall(string)
        newString = leftStripPattern.sub('',string)
        newString = rightStripPattern.sub('',newString)
        print(newString)



string = '     Hello, World!!     ' #expected result is 'Hello,World!!'
string1 = 'SpamSpamBaconSpamEggsSpamSpam'
stripMethodWithRegex(string)
stripMethodWithRegex(string1,'ampS')
