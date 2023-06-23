# Write your code here :-)
def check(nameDict):
    nameCount = {}

    for name in nameDict.keys():
        print(len(name))
        nameCount.setdefault(name,0)
        nameCount[name] +=1
    return nameCount

nameDict = {'Khan': 1983, 'Aichu': 1986, 'Haya': 2013,'Khan':1983}

print(check(nameDict))
