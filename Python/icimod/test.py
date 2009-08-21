## test
import glob
import string
from osgeo import ogr
import os
filename='D:\\GPS_test\\Garmin_6460.txt'
shapefile='D:\\GPS_test\\testfile.shp'
f=open(filename)
data=f.readlines()
f.close()


driver=ogr.GetDriverByName('ESRI Shapefile')
## if shapefile already there, delete it.
if os.access(shapefile,os.F_OK):
    driver.DeleteDataSource(shapefile)
shp=driver.CreateDataSource(shapefile)
layer=shp.CreateLayer('GPS_Servey_Point',None,ogr.wkbPoint)

field=ogr.FieldDefn('ID',ogr.OFTInteger)
field.SetWidth(8)
layer.CreateField(field)

field=ogr.FieldDefn('date_time',ogr.OFTString)
field.SetWidth(10)
layer.CreateField(field)

feature=ogr.Feature(layer.GetLayerDefn())
gid=0
for rec in data:
    gid=gid+1
    rec=string.split(rec,'	')
    if rec[0]=='Waypoint':
        xy=rec[4]
        date_time=rec[2]
        xy=string.replace(xy,'N','')
        xy=string.replace(xy,'E','')
        xy=string.split(xy)
        longitude=float(xy[0])+float(xy[1])/60
        latitude=float(xy[2])+float(xy[3])/60
        feature.SetField(0,gid)
        feature.SetField(1,date_time)
        wkt='POINT('+str(longitude)+' '+str(latitude)+')'
        point=ogr.CreateGeometryFromWkt(wkt)                
        feature.SetGeometry(point)
        layer.CreateFeature(feature)


shp.Destroy()
print '---end-----'
