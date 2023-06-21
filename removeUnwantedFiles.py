'''Deleting Unneeded Files

It’s not uncommon for a few unneeded but humongous files or
folders to take up the bulk of the space on your hard drive.
If you’re trying to free up room on your computer, you’ll get
the most bang for your buck by deleting the most massive of
the unwanted files. But first you have to find them.

Write a program that walks through a folder tree and searches
for exceptionally large files or folders—say, ones that have a
file size of more than 100MB. (Remember that to get a file’s size,
you can use os.path.getsize() from the os module.)
Print these files with their absolute path to the screen.'''

import os

def removeFoldersFiles(sourceFolder,folderFileSize=100000):
    for folderName,subFolderNames,fileNames in os.walk(sourceFolder):
        print(f'inside {os.path.abspath(folderName)}')
        for fileName in fileNames:
            filePath = os.path.join(folderName,fileName)
            fileSize = os.path.getsize(filePath)
            if fileSize > folderFileSize:
                #print(f'Unwanted File: {os.path.abspath(filePath)}')
                print(f'File size of the \"{filePath}\" file : {os.path.getsize(filePath)}')


folder = input('Enter folder name to be cleaned up: ')
removeFoldersFiles(folder)
