'''Selective Copy
Write a program that walks through a folder tree and searches
for files with a certain file extension (such as .pdf or .jpg).
Copy these files from whatever location they are in to a new folder.'''

import os, shutil
srcFolder = "C:\\Users\\admin\\Desktop\\Learn_Python\\folderA"

desFolder = "C:\\Users\\admin\\Desktop\\Learn_Python\\folderB"
for folderName,subFolderNames,fileNames in os.walk('folderA'):
    print(f'Copying files in the folder {folderName}')
    for fileName in fileNames:
        if fileName.endswith('.pdf') or fileName.endswith('.jpg') or fileName.endswith('.jpeg') or fileName.endswith('.csv') or fileName.endswith('.png'):
            shutil.copy((os.path.join(folderName,fileName)),desFolder)

print('Copied all files')
