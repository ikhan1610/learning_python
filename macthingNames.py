# Create a Name Regex and match
import re

def matchNames(names):
    nameRegex = re.compile(r'[A-Z]\w+\sWatanabe') #Regex pattern
    #nameRegex = re.compile(r'[A-Z][a-z]*\sWatanabe') #Regex pattern
    print('\n')
    print("---------------")
    print("Matching Names:")
    print("---------------")
    for name in names:
        matchingNames = nameRegex.search(name)
        if matchingNames:
            print(matchingNames.group())

testNames = ['Haruto Watanabe','Alice Watanabe','RoboCop Watanabe',
            'haruto Watanabe','Mr. Watanabe','Watanabe','Haruto watanabe']
print("---------------")
print("Original List of Names:")
print("---------------")
for name in testNames:
        print(name)

matchNames(testNames)
