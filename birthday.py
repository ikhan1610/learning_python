# Write your code here :-)
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    name = input("Enter name: (blank to quit) ")
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print("I don't have birthday information of " + name)
        newBDay = input("Please enter birthday ")
        birthdays[name] = newBDay
        print("Birthday database updated")

