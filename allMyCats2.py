# Write your code here :-)
catNames = []
while True:
    print('Enter the name of cat '+str(len(catNames)+1)+'(Or nothing to stop.):')
    name = input()
    if name == '':
        break
    else:
        catNames = catNames + [name] #list concatenation
print('Name of the cats are:')
for name in catNames:
    print(' '+name)
