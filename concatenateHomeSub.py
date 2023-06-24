# Write your code here :-)
import shutil, os
from pathlib import Path

src = Path(r"C:\Users\admin\Desktop\FolderA")
dest = Path(r"C:\Users\admin\Desktop\FolderA_backup")
shutil.copytree(src,dest)




