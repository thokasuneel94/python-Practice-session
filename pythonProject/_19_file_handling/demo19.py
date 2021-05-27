# zipping and unzipping files:

# to perform unzip operation:

# f=ZipFile("files.zip","r",ZIP_STORED)      # ZIP_STORED constant represents unzipfile
# names=f.namelist()
from zipfile import *
f=ZipFile("files.zip","r",ZIP_STORED)
names=f.namelist()     # zipfile contains files. we can get all filenames present in zipfile by using namelist() method
for name in names:
    print("file name:",name)
    print("the content of this file:")
    f1=open(name,"r")
    print(f1.read())
    print()
