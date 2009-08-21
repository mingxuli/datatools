#unzip landsat image
import os
import glob
import sys
import tarfile
import string
workspace=u"F:\\Himalaya_Lakes\\Data\\tar\\"
filelist=glob.glob(workspace+u'*.tar.gz')
out_path=u"F:\\Himalaya_Lakes\\Data\\unziped\\"
for filename in filelist:    
    tar=tarfile.open(filename,'r:gz')
    (filepath,fname)=os.path.split(filename)
    outpath=out_path+string.replace(fname,'.tar.gz','')
    print outpath
    for member in tar.getmembers():
        tar.extract(member,outpath)

print '-----end--------'
    
