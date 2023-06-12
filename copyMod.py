# Write your code here :-)
import copy

spam = [1,2,3]
print('spam id: ',id(spam))

cheese = copy.copy(spam)
print('cheese id: ',id(spam))

if id(spam) == id(cheese):
    print('Both spam and cheese IDs are same')
else:
    print('Different IDs')
#cheese.append(42)
cheese[1] = 42

print('spam = ',spam)
print('cheese = ',cheese)
