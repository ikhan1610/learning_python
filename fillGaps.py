'''
Filling in the Gaps

Write a program that finds all files with a given prefix, 
such as spam001.txt, spam002.txt, and so on, in a single 
folder and locates any gaps in the numbering (such as if 
there is a spam001.txt and spam003.txt but no spam002.txt). 
Have the program rename all the later files to close this gap.

'''

import os,re
def fillGapsInFileNames(folder,filePrefix,extension):
    #todo: Write a pattern and identify files with given prefix
    fileNames =  os.listdir(folder)
    filePrefixRegex = re.compile(rf'^{re.escape(filePrefix)}(\d+)(\.\w+)$')
    print(f'All files in the folder: {fileNames}')
    matchingFileNames = [file for file in fileNames if filePrefixRegex.search(file) ]
    numRegex = re.compile(r'(\d+)')
    matchingFileNames = sorted(matchingFileNames, key= lambda x: numRegex.search(x).group())
    for index,file in enumerate(matchingFileNames):
        numberInTheFileName = int(numRegex.search(file).group())
        expectedNumber = index + 1
        newFileName = filePrefix + '00' + str(expectedNumber) + extension
        if expectedNumber != numberInTheFileName:
            newPath = os.path.join(folder,newFileName)
            oldPath = os.path.join(folder,file)
            os.rename(oldPath,newPath)
            print(f'Renamed "{file}" to "{newFileName}"') 

if __name__ == '__main__':
    fillGapsInFileNames('testFolder','spam','.txt')

