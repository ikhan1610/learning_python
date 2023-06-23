# Write your code here :-)

from zipfile import ZipFile as zf
zipFileObj = zf('C:\\Users\\admin\\Desktop\\Learn_Python\\Automate_the_Boring_Stuff_2e_onlinematerials\\automate_online-materials\\example.zip')

print(zipFileObj.namelist())

spaminfo = zipFileObj.getinfo('spam.txt')

print(f'Original file size is {spaminfo.file_size}')
print(f'Compressed file size is {spaminfo.compress_size}')

print(f'Original file size is {round(spaminfo.file_size/spaminfo.compress_size,2)}x times bigger than compressed file size')

zipFileObj.close()
