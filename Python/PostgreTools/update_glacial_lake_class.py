#encoding=utf8
#convert kml to esri generate formate

###############################################################################
# GPSyncTools
# Author:Wulizong
# Date:11/6/2009
# Description:Using this tools to Sync glacial lakes data between Google Earth and Postgis.
# For the glacial lake only polygon is usfull in the kml file.
# the polygon name store the glacial lake id and description tag used for glacial lake's attirbute
# History:

###############################################################################

import os,string,codecs,unicodedata
from datetime import *
from psycopg2 import connect
from osgeo import ogr
from xml.dom import minidom
from types import *

def export_gl_centroid(basin_code,kml_file):    
    #kml_file=outpath+'gl_'+basin_code+'_p_other.kml'   
       
    conn=connect("host=localhost dbname=GGLIS user=postgres password=postgres")
    curs=conn.cursor()

    sql_str="select a.gid,askml(centroid(a.the_geom)) from \"HKH_Glacial_Lakes_final\" a, \"HKH_Basin_Pfaf_v3_poly\" b "\
            "where st_within(centroid(a.the_geom),b.the_geom) and b.lv3_code='"+basin_code+"' and a.\"Gl_Class\" is null order by a.gid;"
    
    curs.execute(sql_str)
    rows=curs.fetchall()
    ##
    impl=minidom.getDOMImplementation()
    dom=impl.createDocument(None,'kml',None)
    root=dom.documentElement
    ns='http://earth.google.com/kml/2.1'
    Document_node=dom.createElement('Document')
    root.appendChild(Document_node)
    Doc_name=dom.createElement('name')
    Document_node.appendChild(Doc_name)
    ##add style
    Style_node=dom.createElement('Style')
    Document_node.appendChild(Style_node)
    Style_node.setAttribute('id','Default_PolyStyle')
    
    LineStyle=dom.createElement('LineStyle')
    Style_node.appendChild(LineStyle)
    color_node=dom.createElement('color')
    LineStyle.appendChild(color_node)
    Text=dom.createTextNode('ff0000ff')
    color_node.appendChild(Text)
    width_node=dom.createElement('width')
    LineStyle.appendChild(width_node)
    Text=dom.createTextNode('1')
    width_node.appendChild(Text)

    PolyStyle=dom.createElement('PolyStyle')
    Style_node.appendChild(PolyStyle)
    color_node=dom.createElement('color')
    PolyStyle.appendChild(color_node)
    Text=dom.createTextNode('ff0000ff')
    color_node.appendChild(Text)
    fill_node=dom.createElement('fill')
    PolyStyle.appendChild(fill_node)
    Text=dom.createTextNode('0')
    fill_node.appendChild(Text)
    outline_node=dom.createElement('outline')
    PolyStyle.appendChild(outline_node)
    Text=dom.createTextNode('1')
    outline_node.appendChild(Text)   


    for i in range(len(rows)):
        gid=rows[i][0]
        kml=rows[i][1]
        Placemark_node=dom.createElement('Placemark')
        Document_node.appendChild(Placemark_node)
        
        name_node=dom.createElement('name')
        Placemark_node.appendChild(name_node)
        Text=dom.createTextNode(str(gid))
        name_node.appendChild(Text)  
        
        kml_dom=minidom.parseString(kml)
        kml_node=kml_dom.documentElement
        Placemark_node.appendChild(kml_node)
                  
    
    f=open(kml_file,'w')
    writer=codecs.lookup('utf8')[3](f)
    dom.writexml(writer,encoding='utf8')
    writer.close()
    curs.close()
    conn.close()
    print '---There are still '+str(len(rows))+' need to add classification and glacial lake centroid without '+gl_type+ ' exported!----'

def update_by_class(kml_file,gl_type):
    conn=connect("host=localhost dbname=GGLIS user=postgres password=postgres")
    curs=conn.cursor()

    dom=minidom.parse(kml_file)
    root=dom.documentElement
    Placemark_List=root.getElementsByTagName('Placemark')
    print len(Placemark_List),' Placemarks in kmlfile'
    update_count=0

    if Placemark_List.length==0:
        print 'no data in this kml file!' 
    else:
        for Placemark in Placemark_List:
            name_mark=Placemark.getElementsByTagName('name')
            name=name_mark[0].firstChild.data            
            Point_mark=Placemark.getElementsByTagName('Point')
            coordinates=Point_mark[0].getElementsByTagName('coordinates')
            if coordinates.length>0:
                coor=coordinates[0].firstChild.data
                point_wkt = ogr.Geometry(ogr.wkbPoint)                
                coor=string.split(coor,',')                
                point_wkt.AddPoint(float(coor[0]),float(coor[1]))                    
                point_wkt.SetCoordinateDimension(2)
                wkt=point_wkt.ExportToWkt()
                point_wkt.Destroy()
                ## compare lake with exist data in postgis
                sql_str="select gid,\"Gl_Class\" from "+table_name+" where st_within(GeomFromText('"+wkt+"',4326),the_geom);"            
                curs.execute(sql_str)
                rows=curs.fetchall()
                ## if length of rows eq 0,means this polygon in kml file not exist in postgis database.
                if len(rows)==0:
                    print 'Point placemark with name '+name+' not existed in database!'
                if len(rows)==1:
                    for gid,gl_class in rows:
                        if type(gl_class) is NoneType:
                            update_str="update "+table_name+" set \"Gl_Class\"='"+gl_type+"' where gid="+str(gid)+";"
                            curs.execute(update_str)
                            update_count=update_count+1
                        else:
                            print str(gid)+' already have a class! new_class:'+gl_type+' old_class:'+gl_class
                  
    conn.commit() 
    curs.close()
    conn.close()

def update_by_name(kml_file):
    conn=connect("host=localhost dbname=GGLIS user=postgres password=postgres")
    curs=conn.cursor()

    dom=minidom.parse(kml_file)
    root=dom.documentElement
    Placemark_List=root.getElementsByTagName('Placemark')
    print len(Placemark_List),' Placemarks in kmlfile'
    update_count=0
    name_list=[]
    if Placemark_List.length==0:
        print 'no data in this kml file!' 
    else:
        for Placemark in Placemark_List:
            name_mark=Placemark.getElementsByTagName('name')
            name=name_mark[0].firstChild.data
            name_list.append(name)
            Point_mark=Placemark.getElementsByTagName('Point')
            coordinates=Point_mark[0].getElementsByTagName('coordinates')
            if coordinates.length>0:
                coor=coordinates[0].firstChild.data
                point_wkt = ogr.Geometry(ogr.wkbPoint)                
                coor=string.split(coor,',')                
                point_wkt.AddPoint(float(coor[0]),float(coor[1]))                    
                point_wkt.SetCoordinateDimension(2)
                wkt=point_wkt.ExportToWkt()
                point_wkt.Destroy()
                ## compare lake with exist data in postgis
                sql_str="select gid,\"Gl_Class\" from "+table_name+" where st_within(GeomFromText('"+wkt+"',4326),the_geom);"            
                curs.execute(sql_str)
                rows=curs.fetchall()
                ## if length of rows eq 0,means this polygon in kml file not exist in postgis database.
                gl_type=name
                
                    
                if len(rows)==0:
                    print 'Point placemark with name '+name+' not existed in database!'
                if len(rows)==1:
                    for gid,gl_class in rows:
                        if type(gl_class) is NoneType:
                            update_str="update "+table_name+" set \"Gl_Class\"='"+gl_type+"' where gid="+str(gid)+";"
                            curs.execute(update_str)
                            update_count=update_count+1
                        else:
                            update_str="update "+table_name+" set \"Gl_Class\"='"+gl_type+"' where gid="+str(gid)+";"
                            curs.execute(update_str)
                            update_count=update_count+1
                            print str(gid)+' already have a class! new_class:'+gl_type+' old_class:'+gl_class
                  
    conn.commit() 
    curs.close()
    conn.close()
    print set(name_list)
    print str(update_count)+' records have updated!'
    
if __name__=='__main__':
       
    table_name="\"HKH_Glacial_Lakes_final\""
    kml_file='C:\\gl_class\\ud_point_new.kml'
    out_kml_file='C:\\gl_class\\ud_point_new_other.kml'
    gl_type='E(c)'
    basin_code='Ir91'
    outpath='C:\\gl_class\\'    
    
    update_by_name(kml_file)
    export_gl_centroid(basin_code,out_kml_file)
    
    print "---end---"





















