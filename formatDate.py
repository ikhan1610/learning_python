#Standardize date dd-mm-yyyy format

#todo: create a standard date regex
#todo: substitute entered date with

import re

dateRegexStandard = re.compile(r'\d{2}[\-]\d{2}[\-]\d{4}') #dd-mm-yyyy

#dateRegex = re.compile(r'(\d{4}\/\d\/\d{2})|(\d{2}\-\d{2}-\d{4})|(\d\/\d{2}\/\d{4})')

dateRegex = re.compile(r'''
                (\d{1,4})
                (\-|\/|\.)
                (\d{1,2})
                (\-|\/|\.)
                (\d{1,4})
''',re.VERBOSE)



def convertDateFormat(textDate):
    dd = ''
    mm = ''
    yyyy = ''
    newDate = []
    groups = dateRegex.findall(textDate)
    for i in range(len(groups)):
        for j in range(len(groups[i])):
            if groups[i][j] in ['/','-','.']:
                continue
            if int(groups[i][j]) <= 12:
                if len(groups[i][j]) < 2:
                    mm = '0'+ groups[i][j]
                elif len(groups[i][j]) == 2:
                    mm = groups[i][j]
            elif int(groups[i][j]) <= 31:
                if len(groups[i][j]) < 2:
                    dd = '0'+ groups[i][j]
                elif len(groups[i][j]) == 2:
                    dd = groups[i][j]
            else:
                yyyy = groups[i][j]
        tempDate = dd + '-' + mm + '-' + yyyy
        print(tempDate)
        if dateRegexStandard.search(tempDate):
            newDate.append(tempDate)
        else:
            newDate.append("Invalid Date")
    return newDate

textDate = '3/12/2019, 03-13-2019, 2015/3/25, abcd, 02/03/2020'
standardDateFormat = convertDateFormat(textDate)
''''for date in standardDateFormat:
    print(date)'''
