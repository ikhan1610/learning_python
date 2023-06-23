'''
Create a Mad Libs program that reads in text files and lets the user
add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB
appears in the text file. For example, a text file may look like this:

The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.

The program would find these occurrences and prompt the user to replace them.

Enter an adjective:
silly
Enter a noun:
chandelier
Enter a verb:
screamed
Enter a noun:
pickup truck

The following text file would then be created:

The silly panda walked to the chandelier and then screamed. A nearby pickup
truck was unaffected by these events.
'''

import re

madLibsFile = open("madLibs.txt","r")
contentMadLibsFile = madLibsFile.read()
libRegex = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB',re.I)
placeHolders = libRegex.findall(contentMadLibsFile)
for placeHolder in placeHolders:
    word = input(f'Please enter {placeHolder}: ')
    contentMadLibsFile = re.sub(placeHolder,word,contentMadLibsFile,count=1)


madLibsAnsFile = open("madLibsAns.txt","w")
madLibsAnsFile.write(contentMadLibsFile)
madLibsAnsFile.close()
madLibsFile.close()




