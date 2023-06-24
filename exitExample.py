# exit command :-)
import sys
while True:
    print('Enter exit to exit')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You have typed '+response+'.')
