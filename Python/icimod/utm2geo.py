##covert project from utm 2 wgs84
import gdal,osr
from gdalconst import *
import glob,string,os.path

workspace='F:\\Himalaya_Lakes\\images\\Landsat_B543\\'
outpath='F:\\Himalaya_Lakes\\images\\Landsat_Geo\\'
filelist=glob.glob(workspace+'*.tif')
for filename in filelist:    
    basename=os.path.basename(filename)
    outfile=outpath+basename[0:-4]+'_geo.TIF'
    print basename
    driver=gdal.GetDriverByName('GTiff')
    driver.Register()    
    ds=gdal.Open(filename)    
    in_wkt=ds.GetProjection()
    print in_wkt
    Geo=osr.SpatialReference()
    Geo.ImportFromEPSG(4326)
    out_wkt=Geo.ExportToWkt()
    
    gdal.CreateAndReprojectImage(ds,outfile,src_wkt=in_wkt,dst_wkt=out_wkt,dst_driver=driver,eResampleAlg=GRA_Bilinear)
    ds=None

print '====end========'
