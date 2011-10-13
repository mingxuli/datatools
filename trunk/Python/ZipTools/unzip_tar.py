##extract tar file
import string
import tarfile
import glob

filelist=glob.glob("D:\\Python\\GLOF\\landsat\\*.tar.gz")
for filename in filelist:
    tar = tarfile.open(filename, 'r:gz')
    for member in tar.getmembers():
        outpath=string.replace(filename,".tar.gz","")
        print outpath
        tar.extract(member, outpath)
print "end"
