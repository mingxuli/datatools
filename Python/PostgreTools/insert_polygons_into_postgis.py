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

##---------------------start script----------------------
##only for polygon

def insert_polygon(host,dbname,user,password,kmlfile,table_name,srid='4326'):
    print 'Program for import kml to postgres is  running>>>>>>>>>>>>>>>>'
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

    dom=minidom.parse(kmlfile)
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
                ## if length of rows eq 0,then the lake in the kml is different from the data in postgis,maybe new one or modify lake.
                if len(rows)==0:
                    sql_str="select gid,flag from "+table_name+" where st_overlaps(the_geom,GeomFromText('"+wkt+"',"+srid+"));"            
                    curs.execute(sql_str)
                    Rows=curs.fetchall()                
                    if len(Rows)>0:                    
                        sql_str="insert into "+table_name+"(gid,the_geom,create_time,flag) values("+str(max_gid+1)+','+"GeomFromText('"+wkt+"',"+srid+"""),
    '"""+str(datetime.today())+"','overlap');"
                        curs.execute(sql_str)
                        max_gid=max_gid+1
                        count_overlap=count_overlap+1
                        for gid,flag in rows:
                            sql_str="update "+table_name+" set flag='overlap',modify_time='"+str(datetime.today())+"' where gid="+str(gid)+";"
                            curs.execute(sql_str)
                            gid_list.remove(gid)
                    else:                    
                        sql_str="insert into "+table_name+"(gid,the_geom,create_time,flag) values("+str(max_gid+1)+','+"GeomFromText('"+wkt+"',"+srid+"""),
    '"""+str(datetime.today())+"','new');"
                        curs.execute(sql_str)
                        max_gid=max_gid+1
                        count_new=count_new+1
                else:
                    if len(rows)==1:
                        for gid,flag in rows:
                            gid_list.remove(gid)
                        count_existed=count_existed+1
                    else:
                        for gid,flag in rows:
                            sql_str="update "+table_name+" set flag='duplicate',modify_time='"+str(datetime.today())+"' where gid="+str(gid)+";"
                            curs.execute(sql_str)
                            gid_list.remove(gid)
    count_tobedel=len(gid_list)
    if count_tobedel>0:
        for gid in gid_list:    
            sql_str="update "+table_name+" set flag='TobeDel',modify_time='"+str(datetime.today())+"' where gid="+str(gid)+";"
            curs.execute(sql_str)
        

    conn.commit() 
    curs.close()
    conn.close()
    print '  ',count_existed,' same as kml'
    print '  ',count_new,' add to database'
    print '  ',count_overlap,' overlap with kml'
    print '  ',count_tobedel,' need to del'
    message="  kml file has imported to postgre database"
    return message


if __name__=='__main__':
    ## variale for connect postgre
    host='localhost'
    dbname='GGLIS'
    user='postgres'
    password='postgres'    
    table_name='HKH_Glacial_Lakes_final'
    gid='gid'
    ##define the geosystem code,default value is 4326 (=WGS84)
    srid='4326'
    kml_file=''
    


print "---end---"





















