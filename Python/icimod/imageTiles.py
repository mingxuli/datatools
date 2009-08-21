##test
import glob
import os,os.path
outdir='F:\\website\\data_dir\\Lansat\\'
inputdir='D:\\working\\Geo\\'
filelist=glob.glob(inputdir+'*.tif')
for filename in filelist:
    basename=os.path.basename(filename)
    cmd_str='gdal2tiles.py -config -title "'+basename
    cmd_str=cmd_str+'" '+filename+' '+outdir
    print cmd_str

    os.system(cmd_str)
print 'end'
##  -publishurl http://192.168.0.127:8080/data_dir/landsat/
