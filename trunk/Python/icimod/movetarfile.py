##move tar.gz file
import os

import glob

workspace=u'F:\\Himalaya_Lakes\\Data\\Landsat'
outpath=u'F:\\Himalaya_Lakes\\Data\\tar\\'
i=1
for root,dirs,filenames in os.walk(workspace):
    path=root+u'\\'
    filelist=glob.glob(path+u'*.tar.gz')
    for filename in filelist:
        #print filename
        (fpath,fname)=os.path.split(filename)
        out_filename=outpath+fname
        #print out_filename
        if os.path.isfile(out_filename):
            out_filename=out_filename+u'('+str(i)+u')'
            i=i+1
            print out_filename
        os.rename(filename,out_filename)
print 'end'


