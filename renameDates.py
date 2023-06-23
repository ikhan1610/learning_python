 #! python3
 # renameDates.py - Renames filenames with American MM-DD-YYYY date format
 # to European DD-MM-YYYY.

import shutil,os,re

# Create a regex that matches files with the American date format.

datePattern = re.compile(r"""^(.*?)
    ((0|1)?\d)-
    ((1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$
    """,re.VERBOSE)

# Loop over the files in the working directory.
for amerFileName in os.listdir('.'):
    mo = datePattern.search(amerFileName)

    # Skip files without a date.

    if mo == None:
        continue

    # Get the different parts of the filename.

    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Form the European-style filename.
    euroFileName = beforePart+dayPart+'-'+monthPart+'-'+yearPart+afterPart

    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFileName = os.path.join(absWorkingDir,amerFileName)
    euroFileName = os.path.join(absWorkingDir,euroFileName)

    # Rename the files.
    #print(f'Renaming "{amerFileName}" to "{euroFileName}"...')
    shutil.move(amerFileName, euroFileName)   # uncomment after testing

#print(os.path.abspath('.'))


