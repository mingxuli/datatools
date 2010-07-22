## replace raster value
import sys,types
from osgeo import gdal
from osgeo.gdalconst import *
import numpy


gdal.AllRegister()
filename='C:\srtm\hkh_srtm.img'
ds=gdal.Open(filename,GA_ReadOnly)
if ds is None:
    print 'Could not open '+ filename
    sys.exit(1)
cols = ds.GetRasterXSize
rows = ds.GetRasterYSize
geotransform = ds.GetGeoTransform()

band = ds.GetRasterBand(1)
for i in range(cols):
    for j in range(rows):
        data= band.ReadAsArray(i,j,1,1)

print '====end==========='
