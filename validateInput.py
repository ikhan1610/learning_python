# Validate the values entered by the users
while True:
    age = input('Please enter your age: ')
    if age.isdecimal():
        break
    else:
        print('Please enter your age in decimal.')

while True:
    password = input('Please enter the password (letters & numbers): ' )
    if password.isalnum():
        break
    else:
        print('Passwords can only have letters and numbers.')

