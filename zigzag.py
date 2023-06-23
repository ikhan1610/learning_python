# Write your code here :-)
import sys, time
indent = 0
indentIncrease = True

try:
    while True:
        print(' '*indent,end='')
        print('********')
        time.sleep(.1)

        if indentIncrease:
            #Increase number of spaces
            indent += 1
            if indent == 20:
                #Change direction
                indentIncrease = False
        else:
            #Decrease number of spaces
            indent -= 1
            #Change direction
            if indent == 0:
                indentIncrease = True

except KeyboardInterrupt:
    sys.exit()
