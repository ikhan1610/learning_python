# Write your code here :-)
def eggs(params):
    print('params id: ',id(params))
    params.append('hello')

spam = [1,2,3]
print('spam id: ',id(spam))
eggs(spam)
print(spam)

