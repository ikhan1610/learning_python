# Write your code here :-)
myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name: ',end='')
petName = input()
if petName in myPets:
    print(petName + ' is my pet.')
else:
    print('I do not have a pet called '+petName+'.')
