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
    for _,_,fileNames in os.walk(folder):
        print(f'All files in the folder: {fileNames}')
        totalNumberOfFiles = len(fileNames)
        counter = 1 
        while counter < totalNumberOfFiles:
            for fileName in fileNames:
                filePrefixRegex = re.compile(filePrefix + '00' + str(numOfFilesWithPrefix) +extension)
                print(f'file prefix regex: {filePrefixRegex}')
                matchingObject = filePrefixRegex.search(fileName)
                if matchingObject:
                    print(f'Pattern matching file: {matchingObject}')
                numOfFilesWithPrefix += 1
    print(f'Total number of files matching pattern: {numOfFilesWithPrefix}')
    #countFileWithPrefix = files.len()
            
    #filePrefixRegex = re.compile(filePrefix + '.txt')

    # todo: Walk through the folder and find out files with the given prefix
    '''for folderName,subFolderNames,fileNames in os.walk(folder):
        fileNamesArray = []
        for fileName in fileNames:
            if filePrefixRegex in fileName:
                print(filename)
                #fileNamesArray.append(fileName)
    for file in fileNamesArray:
        print(file)'''

#folder = input("Enter name of the folder: ")
#pattern = input("Enter the prefix: ")
if __name__ == '__main__':
    fillGapsInFileNames('testFolder','spam','.txt')

