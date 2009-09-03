#encoding=utf8
#convert kml to esri generate formate

##Author:wulizong
##E-mail:wulizong@lzb.ac.cn
##Description:
## 1.How to use
## 2.Main Funtcion:
##   1)can export kml folder structure in shapefile' attribute table,2 field was defined in attribute,name,document and folder.
##      the name field save the placemark name node
##      the document field save the document name node
##      the folder field save the folder name node.because there maybe more than on folder node in one kml file, so the first level names folder0,the second is folder1 and then on.

## 3.
##History:
## v0.3 July 7,2009 support Kmz file.
## v0.3 Jun 12,2009 support batch working mode.
## v0.2 Jun 10,2009 support Non-english language, for example Chinese.user need to define the look varyiable.
## v0.1 Mar 5,2009 just support kml file,can store folder structure in shapefile's attribute

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
    ns=root.nsmap[None]##.values()[0]
##    print root.nsmap[None]
##    print root.nsmap
##    print ns
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
        Layer=shp.CreateLayer('Polygon',None,ogr.wkbPolygon)    
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
            
            Geom = ogr.Geometry(ogr.wkbPolygon)
            out_ring = ogr.Geometry(ogr.wkbLinearRing)
            coors_node=node.xpath('./ns:outerBoundaryIs/ns:LinearRing/ns:coordinates',namespaces={"ns":ns})            
            coors=coors_node[0].text
            coors=string.replace(coors,'\n','')            
            coors=string.split(coors,' ')
            for coor in coors:            
                coor=string.split(coor,',')
                if len(coor)>1:
                    out_ring.AddPoint(float(coor[0]),float(coor[1]))            
            Geom.AddGeometry(out_ring)
            
            coors_node=node.xpath('./ns:innerBoundaryIs/ns:LinearRing/ns:coordinates',namespaces={"ns":ns})
            if len(coors_node)>0:
                for coor_node in coors_node:
                    inner_ring = ogr.Geometry(ogr.wkbLinearRing)
                    coors=coor_node.text
                    coors=string.replace(coors,'\n','')            
                    coors=string.split(coors,' ')
                    for coor in coors:            
                        coor=string.split(coor,',')
                        if len(coor)>1:
                            out_ring.AddPoint(float(coor[0]),float(coor[1]))
                    Geom.AddGeometry(inner_ring)
            feature.SetGeometryDirectly(Geom)
            Layer.CreateFeature(feature)
        shp.Destroy()
        print "completed kml file conversion @",datetime.today()     
            
            
    message=kmlfile+" finish"
    return message

if __name__=="__main__":
    ##defined the input and output file    
    outpath='F:\\KML\\'
    ##define the encoding for chinese character
    look=codecs.lookup('gbk')
    
    ##for single file
    kmlfile=u'F:\\KML\\hkh_glacier_lake_21_Aug.kml'
    result=kml2shp(kmlfile,outpath)
    print result
    ##for batch model
##    workspace=u'C:\\TDDOWNLOAD\\kml\\地名\\kml\\'
##    filelist=glob(workspace+'*.kml')
##    for kmlfile in filelist:
##        print kmlfile+' is exporting...'
##        result=kml2shp(kmlfile,outpath)
##        print result

print '---end-----'
