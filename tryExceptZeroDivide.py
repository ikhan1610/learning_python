# Write your code here :-)
def spam(divideby):
    try:
        return 42 / divideby
    except:
        print('Error: Division with Zero is invalid')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
