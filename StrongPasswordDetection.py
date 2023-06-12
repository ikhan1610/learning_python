'''
Write a function that uses regular expressions to make sure the password
string it is passed is strong. A strong password is defined as one that is
at least eight characters long, contains both uppercase and lowercase characters,
and has at least one digit. You may need to test the string against multiple regex
patterns to validate its strength.
'''
import re
def validateStengthOfPassword(password):
    passwordPattern1 = re.compile(r'[a-z]+')
    passwordPattern2 = re.compile(r'[A-Z]+')
    passwordPattern3 = re.compile(r'[0-9]+')
    if len(password) < 8 :
        print("Password entered is too short. Atleast 8 charactes.")
    else:
        if not passwordPattern1.search(password):
            print('Password should have atleast a lowercase character.')
        elif not passwordPattern2.search(password):
            print('Password should have atleast an uppercase character.')
        elif not passwordPattern3.search(password):
            print('Password should have atleast a digit.')
        else:
            print(f'Your password \"{password}\" is strong.')


userPassword = input('Enter your password: ')
validateStengthOfPassword(userPassword)
