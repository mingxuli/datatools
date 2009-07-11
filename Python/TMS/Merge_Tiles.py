#conding=utf8
##merge tiles image

import os
import glob

workspace="D:\\Python\\data\\new1\\"
outpath=""
result=os.walk(workspace)
count=0
for dir,subdir,basename in result:    
    if len(basename)>0:
        for filename in basename:
            fullname=dir+os.sep+filename
            fo

            count=count+1
            print fullname
print count
    
