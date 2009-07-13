##thumbnail
import glob
import string
import os

workspace='F:\\Himalaya_Lakes\\images\\Landsat_B543\\bad\\'
filelist=glob.glob(workspace+'*.tif')
for filename in filelist:
    outfile=filename[0:-4]+'.png'
    cmd="C:\\gdalwin32-1.6\\bin\\gdal_translate -of PNG -outsize 10% 10% "+filename +' '+outfile
    os.system(cmd)

print '====end========'
