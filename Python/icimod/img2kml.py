##covert img to google earth
from osgeo import gdal,ogr

workspace=''
filename=r'D:\Python\world.200410.3x21600x10800.JPG'
database=gdal.Open(filename)
print database.RasterCount,database.GetGeoTransform()

print '====end===='
