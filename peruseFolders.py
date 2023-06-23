# Write your code here :-)
import os

def peruseFolder(path = 'C:\\Users\\admin\\Desktop\\Learn_Python\\delicious'):
    for folderName,subFolders,fileNames in os.walk(path):
        print('The current folder is ' + folderName)
        for subFolder in subFolders:
            print('SUBFOLDER OF '+ folderName + ': '+subFolder)
        for fileName in fileNames:
            print('FILE INSIDE '+ folderName+ ': ' +fileName)
        print("")


#peruseFolder()
