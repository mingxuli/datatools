#encoding=utf8

####################################################################################################
# GPSyncTools
# Author:Wulizong
# Date:11/6/2009
# Description:Using this tools to Sync glacial lakes data between Google Earth and Postgis.
# For the glacial lake only polygon is usfull in the kml file.
# the polygon name store the glacial lake id and description tag used for glacial lake's attirbute
# History:

####################################################################################################

import os,string,codecs,unicodedata
from datetime import *
from psycopg2 import connect
from osgeo import ogr
from xml.dom import minidom


def insert_polygon(host,dbname,user,password,kml_file,table_name,srid='4326'):
    print 'Start Running>>>>>>>>>>>>>>>>'
    conn=connect("host="+host+" dbname="+dbname+" user="+user+" password="+password)
    curs=conn.cursor()
    sql_str="select gid from "+table_name+';'
    curs.execute(sql_str)
    rows=curs.fetchall()
    print 'Found ',len(rows),' geometrys in database:'
    if len(rows)>0:
        gid_list=[s[0] for s in rows]
        max_gid=max(gid_list)
    else:
        max_gid=0
        gid_list=[]
    max_gid_old=max_gid
    print max_gid_old
    dom=minidom.parse(kml_file)
    root=dom.documentElement
    Placemark_List=root.getElementsByTagName('Placemark')
    print len(Placemark_List),' Placemarks in kmlfile'
    count_existed=0
    count_new=0
    count_overlap=0
    count_tobedel=0
    if Placemark_List.length==0:
        print 'no data in this kml file!' 
    else:
        for Placemark in Placemark_List:
            name_list=Placemark.getElementsByTagName('name')
            desc_list=Placemark.getElementsByTagName('description')
            Polygon_list=Placemark.getElementsByTagName('Polygon')
            if Polygon_list.length>0:
                Polygon=Polygon_list[0]
                outerBoundary=Polygon_list[0].getElementsByTagName('outerBoundaryIs')
                innerBoundary=Polygon_list[0].getElementsByTagName('innerBoundaryIs')
                polygon = ogr.Geometry(ogr.wkbPolygon)
                if outerBoundary.length>0:
                    coordinates=outerBoundary[0].getElementsByTagName('coordinates')
                    if coordinates.length>0:
                        coors=coordinates[0].firstChild.data
                        coors=string.split(coors)
                        outring = ogr.Geometry(ogr.wkbLinearRing)
                        for coor in coors:
                            coor=string.split(coor,',')                        
                            outring.AddPoint(float(coor[0]),float(coor[1]))                    
                        polygon.AddGeometry(outring)                    
                        outring.Destroy()
                if innerBoundary.length>0:
                    coordinates=innerBoundary[0].getElementsByTagName('coordinates')
                    if coordinates.length>0:
                        coors=coordinates[0].firstChild.data
                        coors=string.split(coors) 
                        inring.AddGeometry(ring)
                        for coor in coors:
                            coor=string.split(coor,',')
                            inring.AddPoint(float(coor[0]),float(coor[1]))
                        polygon.AddGeometry(inring)                    
                        inring.Destroy()
                polygon.SetCoordinateDimension(2)
                wkt=polygon.ExportToWkt()
                polygon.Destroy()
                ## compare lake with exist data in postgis
                sql_str="select gid,the_geom from "+table_name+" where st_equals(the_geom,GeomFromText('"+wkt+"',4326));"            
                curs.execute(sql_str)
                rows=curs.fetchall()
                ## if length of rows eq 0,means this polygon in kml file not exist in postgis database.
                if len(rows)==0:
                    sql_insert="insert into "+table_name+"(gid,the_geom) values("+str(max_gid+1)+','+"GeomFromText('"+wkt+"',"+srid+"));"

                    curs.execute(sql_insert)
                    max_gid=max_gid+1
    print max_gid-max_gid_old, 'have added into database'
    conn.commit() 
    curs.close()
    conn.close()
    

    print "---end---"

if __name__=='__main__':
    ## variale for connect postgre
    host='localhost'
    dbname="GGLIS"
    user='postgres'
    password='postgres'
    table_name="\"HKH_Glacial_Lakes_final\""
    gid='gid'
    ##define the geosystem code,default value is 4326 (=WGS84)
    srid='4326'
    kml_file='C:\\gl_class\\gl_br61_new.kml'
    insert_polygon(host,dbname,user,password,kml_file,table_name)

























