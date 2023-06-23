#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile, os

def backupToZip(folder):
    # Back up the entire contents of "folder" into a ZIP file.
    folder = os.path.abspath(folder) # make sure folder is absolute
    # Figure out the filename this code should use based on
    # what files already exist.
    number = 1
    while True:
        zipFileName = os.path.basename(folder)+'_'+str(number)+'.zip'
        if not os.path.exists(zipFileName):
            break
        number += 1

    # Create the ZIP file.
    print(f'Creating {zipFileName}')
    backUpZip = zipfile.ZipFile(zipFileName,'w')

    # Walk the entire folder tree and compress the files in each folder.
    for folderName,subFolderNames,fileNames in os.walk('delicious2'):
        print(f'Adding files in {folderName}')
        #Add current folder to the ZIP file
        backUpZip.write(folderName)
        # Add all the files in this folder to the ZIP file.
        for fileName in fileNames:
            newBase = os.path.basename(folder)+'_'
            if fileName.startswith(newBase) and fileName.endswith('.zip'):
                print('before continue')
                continue # don't back up the backup ZIP files
            backUpZip.write(os.path.join(folderName,fileName))
    backUpZip.close()


    print('Done.')

backupToZip('C:\\Users\\admin\\Desktop\\Learn_Python\\delicious2')
