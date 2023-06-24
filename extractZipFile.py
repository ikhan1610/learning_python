#import os
import peruseFolders
from zipfile import ZipFile as zf
zipFileObj = zf('C:\\Users\\admin\\Desktop\\Learn_Python\\Automate_the_Boring_Stuff_2e_onlinematerials\\automate_online-materials\\example.zip')

print(zipFileObj.namelist())
print("")

newFolderPath = 'C:\\Users\\admin\\Desktop\\Learn_Python\\delicious2'

zipFileObj.extractall(newFolderPath)
peruseFolders.peruseFolder(newFolderPath)



'''for folderName,subFolders,fileNames in os.walk('C:\\Users\\admin\\Desktop\\Learn_Python\\delicious2'):
    print('The current folder is ' + folderName)
    for subFolder in subFolders:
        print('SUBFOLDER OF '+ folderName + ': '+subFolder)
    for fileName in fileNames:
        print('FILE INSIDE '+ folderName+ ': ' +fileName)
    print("")'''


zipFileObj.close()
