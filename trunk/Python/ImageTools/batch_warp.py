##batch_imagewarp
import os,os.path
import string
import glob
from osgeo import gdal,osr

workspace='F:\\Himalaya_Lakes\\images\\Landsat_B543\\'
outpath='F:\\Himalaya_Lakes\\images\\Landsat_Geo\\'
filelist=glob.glob(workspace+'*.tif')
for filename in filelist:
    basename=os.path.basename(filename)
    print basename
    outfile=outpath+basename
    ds=gdal.Open(filename)
    wkt=ds.GetProjection()
    
    srs=osr.SpatialReference()
    srs.ImportFromWkt(wkt)
    proj4=srs.ExportToProj4()
##    t_srs=osr.SpatialReference()
##    t_srs.ImportFromEPSG(4326)
    
    
    cmd_str='gdalwarp -s_srs "'+proj4+'" -t_srs EPSG:4326 -tr 0.0002 0.0002 '+filename+' '+outfile
    os.system(cmd_str)
print '------------end---------------'
