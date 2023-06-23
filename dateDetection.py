# Date Detection and validate the date
# Date format should be DD/MM/YYYY
# Day Range 01 to 31
# Month Range 01 to 12
# Year Range 1000 to 2999

import re

#Get day, month and year from a user date
def dateRegex(date):
    dateRegexPattern = re.compile(r'(\d{1,2})\/(\d{1,2})\/(\d{4})')
    matchingObject = dateRegexPattern.search(date)
    day = matchingObject.groups()[0]
    month = matchingObject.groups()[1]
    year = matchingObject.groups()[2]
    #print(day+'-'+month+'-'+year)
    return (day,month,year)



#Check the validity of the date
def checkValidityOfDate(dayMonthYear):
    properDate = dayMonthYear[0]+'/'+dayMonthYear[1]+'/'+dayMonthYear[2]
    if len(dayMonthYear[0]) !=2 or len(dayMonthYear[1]) != 2 or len(dayMonthYear[2]) != 4:
        print("Please enter the date in DD/MM/YYYY format.")
    elif dayMonthYear[1] in ['04','06','09','11']:
        if int(dayMonthYear[0]) <= 30:
            print(f'{properDate} is a valid date.')
        else:
            print(f'{properDate} is an invalid date.')
    elif dayMonthYear[1] == '02':
        if (int(dayMonthYear[2]) % 4 == 0 and int(dayMonthYear[2]) % 100 != 0) or int(dayMonthYear[2]) % 400 == 0:
            if int(dayMonthYear[0]) > 29:
                print(f'{properDate} is an invalid date')
            else:
                print(f'{properDate} is a valid date and a leap year.')
        else:
            print(f'{properDate} is an invalid date.')
    else:
        if int(dayMonthYear[0]) <= 31:
            print(f'{properDate} is a valid date.')
        else:
            print(f'{properDate} is an invalid date.')


userDate = input("Please enter a date in DD/MM/YYYY format: ")
dayMonthYear = dateRegex(userDate)
checkValidityOfDate(dayMonthYear)
