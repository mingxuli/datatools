#gps 2 shapefile
import os.path
import glob
import string
from osgeo import ogr
import os
from xml.dom.minidom import parse

workspace='D:\\GPS_test\\'
shapefile='D:\\GPS_test\\gps_servey.shp'
driver=ogr.GetDriverByName('ESRI Shapefile')
## if shapefile already there, delete it.
if os.access(shapefile,os.F_OK):
    driver.DeleteDataSource(shapefile)
shp=driver.CreateDataSource(shapefile)
layer=shp.CreateLayer('GPS_Servey_Point',None,ogr.wkbPoint)

field=ogr.FieldDefn('ID',ogr.OFTInteger)
field.SetWidth(8)
layer.CreateField(field)

field=ogr.FieldDefn('Longitude',ogr.OFTReal)
field.SetWidth(15)
field.SetPrecision(11)
layer.CreateField(field)

field=ogr.FieldDefn('Latitude',ogr.OFTReal)
field.SetWidth(15)
field.SetPrecision(11)
layer.CreateField(field)

field=ogr.FieldDefn('Elevation',ogr.OFTReal)
field.SetWidth(10)
field.SetPrecision(4)
layer.CreateField(field)

field=ogr.FieldDefn('Time',ogr.OFTString)
field.SetWidth(25)
layer.CreateField(field)

field=ogr.FieldDefn('Active',ogr.OFTString)
field.SetWidth(25)
layer.CreateField(field)

field=ogr.FieldDefn('Type',ogr.OFTString)
field.SetWidth(15)
layer.CreateField(field)

feature=ogr.Feature(layer.GetLayerDefn())


filelist=glob.glob(workspace+'*.gpx')
gid=0
for gpxfile in filelist:
    print gpxfile 

    dom=parse(gpxfile)
    data=f.readlines()
    f.close()

    Active=''
    for rec in data:
        rec=string.split(rec,'	')
        if len(rec)>0:
            if rec[0]=='Track':
                Active=rec[1]    
            if rec[0]=='Trackpoint':
                gid=gid+1
                
                xy=rec[1]
                xy=string.replace(xy,'N','')
                xy=string.replace(xy,'n','')
                xy=string.replace(xy,'S','-')
                xy=string.replace(xy,'s','-')
                xy=string.replace(xy,'E','')
                xy=string.replace(xy,'e','')
                xy=string.replace(xy,'W','-')
                xy=string.replace(xy,'w','-')
                xy=string.split(xy)
                
                latitude=float(xy[0])+float(xy[1])/60
                longitude=float(xy[2])+float(xy[3])/60                
                elevation=string.replace(rec[3],'ft','')
                date_time=rec[2]                
                               
                feature.SetField(0,gid)
                feature.SetField(1,longitude)
                feature.SetField(2,latitude)
                feature.SetField(3,elevation)
                feature.SetField(4,date_time)
                feature.SetField(5,Active)
                feature.SetField(6,'Trackpoint')
                wkt='POINT('+str(longitude)+' '+str(latitude)+')'                
                point=ogr.CreateGeometryFromWkt(wkt)
                
                feature.SetGeometry(point)
                layer.CreateFeature(feature)
            
            if rec[0]=='Waypoint':                
                gid=gid+1
                Active=''
                xy=rec[4]
                xy=string.replace(xy,'N','')
                xy=string.replace(xy,'n','')
                xy=string.replace(xy,'S','-')
                xy=string.replace(xy,'s','-')
                xy=string.replace(xy,'E','')
                xy=string.replace(xy,'e','')
                xy=string.replace(xy,'W','-')
                xy=string.replace(xy,'w','-')                
                xy=string.split(xy)
                
                latitude=float(xy[0])+float(xy[1])/60
                longitude=float(xy[2])+float(xy[3])/60
                
                elevation=string.replace(rec[5],'ft','')
                date_time=rec[2]           
                               
                feature.SetField(0,gid)
                feature.SetField(1,longitude)
                feature.SetField(2,latitude)
                feature.SetField(3,elevation)
                feature.SetField(4,date_time)
                feature.SetField(5,Active)
                feature.SetField(6,'Waypoint')
                wkt='POINT('+str(longitude)+' '+str(latitude)+')'                
                point=ogr.CreateGeometryFromWkt(wkt)
                
                feature.SetGeometry(point)
                layer.CreateFeature(feature)


feature.Destroy()
shp.Destroy()
print '----end-----'
