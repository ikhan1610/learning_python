'''
Filling in the Gaps

Write a program that finds all files with a given prefix, 
such as spam001.txt, spam002.txt, and so on, in a single 
folder and locates any gaps in the numbering (such as if 
there is a spam001.txt and spam003.txt but no spam002.txt). 
Have the program rename all the later files to close this gap.

'''

import os,re
def fillGapsInFileNames(folder,filePrefix):
    #todo: Write a pattern and identify files with given prefix
    filePrefixRegex = re.compile(filePrefix + '.txt')

    # todo: Walk through the folder and find out files with the given prefix
    for folderName,subFolderNames,fileNames in os.walk(folder):
        fileNamesArray = []
        for fileName in fileNames:
            if filePrefixRegex in fileName:
                fileNamesArray.append(fileName)





#  
