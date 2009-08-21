## test2
import os
from osgeo import ogr
shapefile='D:\\GPS_test\\testfile.shp'

driver=ogr.GetDriverByName('ESRI Shapefile')
## if shapefile already there, delete it.
if os.access(shapefile,os.F_OK):
    driver.DeleteDataSource(shapefile)
shp=driver.CreateDataSource(shapefile)
layer=shp.CreateLayer('GPS_Servey_Point',None,ogr.wkbPoint)

field=ogr.FieldDefn('ID',ogr.OFTInteger)
field.SetWidth(8)
layer.CreateField(field)

field=ogr.FieldDefn('name',ogr.OFTString)
field.SetWidth(10)
layer.CreateField(field)

feature=ogr.Feature(layer.GetLayerDefn())
feature.SetField(0,23)
feature.SetField(1,'ssssss')

wkt='POINT(86 34)'
point=ogr.CreateGeometryFromWkt(wkt)                
feature.SetGeometry(point)
layer.CreateFeature(feature)
shp.Destroy()
print '---end---'


