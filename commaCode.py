# Convert a list into a single string with 'and' before the last string
'''def convertToString (customList):
    lengthOfTheList = len(customList)
    if lengthOfTheList == 0:
        print("The List is Empty")
    elif lengthOfTheList == 1:
        print("There's only a single item in the list: ",customList[0])
    else:
        print('{} and {}'.format(','.join(customList[:-1]),customList[-1]))
listOfStrings = [listItems for listItems in input('Enter your list values: ').split()]
convertToString(listOfStrings)'''

def commaCode(userList):
    newString = ''
    if len(userList) == 0:
        return("The list is empty")
    elif len(userList) == 1:
        newString += userList[0]
        return(newString)
    elif len(userList) == 2:
        return(userList[0] + ' and ' + userList[-1])
    else:
        for i in range(len(userList)-1):
            newString += userList[i] + ', '
        newString += 'and ' + userList[-1]
        return newString

spam1 = []
newString1 = commaCode(spam1)
print(newString1)
spam2 = ['dog']
newString2 = commaCode(spam2)
print(newString2)
spam3 = ['dog','cat']
newString3 = commaCode(spam3)
print(newString3)
spam4 = ['dog','cat','pig']
newString4 = commaCode(spam4)
print(newString4)
spam5 = ['foo','bar','bacon','cheese']
newString5 = commaCode(spam5)
print(newString5)







