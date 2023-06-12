# Check palindrome or not
def isPalindrome(text):
    text = str.lower(text)
    reverse_text = text[::-1]
    if reverse_text == text:
       return True
    else:
        return False

print("Please enter a text: ",sep=' ',end='')
custom_text = input()
if isPalindrome(custom_text):
    print(f'{custom_text} is a palindrome.')
else:
    print(f'{custom_text} is not a palindrome.')

