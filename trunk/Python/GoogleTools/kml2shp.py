#encoding=utf8
#convert kml to esri generate formate

import os,os.path
from datetime import *
import string
from types import *
from lxml import etree
import unicodedata
import codecs
from osgeo import ogr
from glob import glob

def kml2shp(kmlfile,outpath,look=codecs.lookup('gbk')):
    print 'Start @',datetime.today()
    basename=os.path.basename(kmlfile)
    basename=string.replace(basename,'.kml','')
    basename=string.replace(basename,'.kmz','')
    basename=string.replace(basename,'.','-')
    driver=ogr.GetDriverByName('ESRI Shapefile')
    
    tree=etree.parse(kmlfile)
    root=tree.getroot()
    ns=root.nsmap[None]
    Document_Node=tree.xpath("//ns:Document/ns:name",namespaces={"ns":ns})
    Document_name=Document_Node[0].text
    Document_name=string.lower(Document_name)
    Document_name=string.replace(Document_name,'.kml','')
    Document_name=string.replace(Document_name,'.kmz','')
    Document_name=(look.encode(Document_name))[0]

    Geo_Node=tree.xpath("//ns:Point",namespaces={"ns":ns})
    if len(Geo_Node)>0:
        Depth=max([len(node.xpath("ancestor::ns:Folder",namespaces={"ns":ns})) for node in Geo_Node])
        shapefile=outpath+basename+u'_Point.shp'
        shapefile=str(shapefile)
        if os.access(shapefile,os.F_OK):
            driver.DeleteDataSource(shapefile)
        shp=driver.CreateDataSource(shapefile)
        Layer=shp.CreateLayer('Point',None,ogr.wkbPoint)    
        field = ogr.FieldDefn('Name', ogr.OFTString)
        field.SetWidth(250)
        Layer.CreateField(field)
        field = ogr.FieldDefn('Document', ogr.OFTString)
        field.SetWidth(250)
        Layer.CreateField(field)
        for i in range(Depth):
            field = ogr.FieldDefn('Folder_'+str(i), ogr.OFTString)
            field.SetWidth(250)
            Layer.CreateField(field)
        for node in Geo_Node:
            feature = ogr.Feature(Layer.GetLayerDefn())
            PlacemarkName_node=node.xpath("../ns:name",namespaces={"ns":ns})
            if len(PlacemarkName_node)>0:
                Placemark_Name=PlacemarkName_node[0].text
                Placemark_Name=(look.encode(Placemark_Name))[0] 
            else:
                Placemark_Name='None'
            feature.SetField(0,Placemark_Name)
            feature.SetField(1,Document_name)
            Folder_node=node.xpath("ancestor::ns:Folder",namespaces={"ns":ns})
            for i in range(len(Folder_node)):
                name=Folder_node[i].xpath("./ns:name",namespaces={"ns":ns})
                if len(name)>0:
                    Folder_name=name[0].text
                    Folder_name=(look.encode(Folder_name))[0]
                else:
                    Folder_name="None"
                feature.SetField(i+2,Folder_name)
            coor_node=node.xpath('./ns:coordinates',namespaces={"ns":ns})            
            coors=coor_node[0].text
            Geom = ogr.Geometry(ogr.wkbPoint)
            coors=string.split(coors,' ')
            for coor in coors:            
                coor=string.split(coor,',')
                Geom.AddPoint(float(coor[0]),float(coor[1]))        
            feature.SetGeometryDirectly(Geom)
            Layer.CreateFeature(feature)
        shp.Destroy()
        
        print 'completed point geometry conversion@',datetime.today()
        
    Geo_Node=tree.xpath("//ns:LineString",namespaces={"ns":ns})
    if len(Geo_Node)>0:
        Depth=max([len(node.xpath("ancestor::ns:Folder",namespaces={"ns":ns})) for node in Geo_Node])      
        
        shapefile=outpath+basename+u'_Line.shp'
        shapefile=str(shapefile)
        if os.access(shapefile,os.F_OK):
            driver.DeleteDataSource(shapefile)
        shp=driver.CreateDataSource(shapefile)
        Layer=shp.CreateLayer('Line',None,ogr.wkbLineString)    
        field = ogr.FieldDefn('Name', ogr.OFTString)
        field.SetWidth(250)
        Layer.CreateField(field)
        field = ogr.FieldDefn('Document', ogr.OFTString)
        field.SetWidth(250)
        Layer.CreateField(field)
        for i in range(Depth):
            field = ogr.FieldDefn('Folder_'+str(i), ogr.OFTString)
            field.SetWidth(250)
            Layer.CreateField(field)
        for node in Geo_Node:
            feature = ogr.Feature(Layer.GetLayerDefn())
            PlacemarkName_node=node.xpath("../ns:name",namespaces={"ns":ns})
            if len(PlacemarkName_node)>0:
                Placemark_Name=PlacemarkName_node[0].text
                Placemark_Name=(look.encode(Placemark_Name))[0] 
            else:
                Placemark_Name='None'
            feature.SetField(0,Placemark_Name)
            feature.SetField(1,Document_name)
            Folder_node=node.xpath("ancestor::ns:Folder",namespaces={"ns":ns})
            for i in range(len(Folder_node)):
                name=Folder_node[i].xpath("./ns:name",namespaces={"ns":ns})
                if len(name)>0:
                    Folder_name=name[0].text
                    Folder_name=(look.encode(Folder_name))[0]
                else:
                    Folder_name="None"
                feature.SetField(i+2,Folder_name)
            coor_node=node.xpath('./ns:coordinates',namespaces={"ns":ns})            
            coors=coor_node[0].text
            Geom = ogr.Geometry(ogr.wkbLineString)
            coors=string.split(coors,' ')
            for coor in coors:            
                coor=string.split(coor,',')
                if len(coor)>1:
                    Geom.AddPoint(float(coor[0]),float(coor[1]))        
            feature.SetGeometryDirectly(Geom)
            Layer.CreateFeature(feature)
        shp.Destroy()        
        print 'completed Line geometry conversion@',datetime.today()
        
    Geo_Node=tree.xpath("//ns:Polygon",namespaces={"ns":ns})
    if len(Geo_Node)>0:
        Depth=max([len(node.xpath("ancestor::ns:Folder",namespaces={"ns":ns})) for node in Geo_Node])      
        
        shapefile=outpath+basename+u'_Polgyon.shp'
        shapefile=str(shapefile)
        if os.access(shapefile,os.F_OK):
            driver.DeleteDataSource(shapefile)
        shp=driver.CreateDataSource(shapefile)
        Layer=shp.CreateLayer('Polygon',None,ogr.wkbPoint)    
        field = ogr.FieldDefn('Name', ogr.OFTString)
        field.SetWidth(250)
        Layer.CreateField(field)
        field = ogr.FieldDefn('Document', ogr.OFTString)
        field.SetWidth(250)
        Layer.CreateField(field)
        for i in range(Depth):
            field = ogr.FieldDefn('Folder_'+str(i), ogr.OFTString)
            field.SetWidth(250)
            Layer.CreateField(field)
        for node in Geo_Node:
            feature = ogr.Feature(Layer.GetLayerDefn())
            PlacemarkName_node=node.xpath("../ns:name",namespaces={"ns":ns})
            if len(PlacemarkName_node)>0:
                Placemark_Name=PlacemarkName_node[0].text
                Placemark_Name=(look.encode(Placemark_Name))[0] 
            else:
                Placemark_Name='None'
            feature.SetField(0,Placemark_Name)
            feature.SetField(1,Document_name)
            Folder_node=node.xpath("ancestor::ns:Folder",namespaces={"ns":ns})
            for i in range(len(Folder_node)):
                name=Folder_node[i].xpath("./ns:name",namespaces={"ns":ns})
                if len(name)>0:
                    Folder_name=name[0].text
                    Folder_name=(look.encode(Folder_name))[0]
                else:
                    Folder_name="None"
                feature.SetField(i+2,Folder_name)
            coors_node=node.xpath('./ns:coordinates',namespaces={"ns":ns})
            Geom = ogr.Geometry(ogr.wkbPolygon)
            for coor_node in coors_node:
                coors=coor_node.text                
                ring = ogr.Geometry(ogr.wkbLinearRing)
                coors=string.split(coors,' ')
                for coor in coors:            
                    coor=string.split(coor,',')
                    ring.AddPoint(float(coor[0]),float(coor[1]))
                Geom.AddGeometry(ring)
            feature.SetGeometryDirectly(Geom)
            Layer.CreateFeature(feature)
        shp.Destroy()
        print "completed kml file conversion @",datetime.today()     
            
            
    message=kmlfile+" finish"
    return message

if __name__=="__main__":
    ##defined the input and output file    
    outpath='d:\\'
    ##define the encoding for chinese character
    look=codecs.lookup('gbk')
    
    ##for single file
    kmlfile=u'D:\\test.kml'
    result=kml2shp(kmlfile,outpath)
    print result
    ##for batch model
##    workspace=u'D:\\kml\\'
##    filelist=glob(workspace+'*.kml')
##    for kmlfile in filelist:
##        print kmlfile+' is exporting...'
##        result=kml2shp(kmlfile,outpath)
##        print result

print '---end-----'
