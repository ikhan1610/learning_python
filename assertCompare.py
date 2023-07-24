'''Write an assert statement that triggers an AssertionError 
if the variables eggs and bacon contain strings that are the 
same as each other, even if their cases are different 
(that is, 'hello' and 'hello' are considered the same, and 
'goodbye' and 'GOODbye' are also considered the same).
'''
eggs = input("Enter first text: ")
bacon = input("Enter secong text: ")
assert eggs.lower() != bacon.lower(), "Both 'egss' and 'bacon' have same text value"

