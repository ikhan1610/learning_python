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
        matchingPatterns = 0
        joinedFilesNames = ''.join(fileNames)
        while counter < totalNumberOfFiles:
            filePrefixRegex = re.compile(filePrefix + '00' + str(counter) + extension)
            #print(f'file prefix regex: {filePrefixRegex}')
            matchingObject = filePrefixRegex.findall(joinedFilesNames)
            if matchingObject:
                print(f'Pattern matching file: {matchingObject[0]}')
                matchingPatterns += 1
            counter += 1
    

   
if __name__ == '__main__':
    fillGapsInFileNames('testFolder','spam','.txt')

