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

if __name__=='__main__':
    print 'Running>>>>>>>>>>>>>>>>'
    table_name="\"Nepal_Glacial_Lake_wu_v2\""
    conn=connect("host=localhost dbname=GGLIS user=postgres password=postgres")
    curs=conn.cursor()
    sql_str="select gid,astext(the_geom) from "+table_name+' order by gid;'
    curs.execute(sql_str)
    records=curs.fetchall()
    gid_list=[]
    for gid,wkt in records:
        wkt=wkt.replace("POLYGON((","'POLYGON((")
        wkt=wkt.replace("))","),4326)")
        sql_str="select gid,st_numpoints(the_geom) from "+table_name+" where st_overlaps(the_geom,(select the_geom from \"Nepal_Glacial_Lake_wu_v2\" where gid="+str(gid)+"));"
        curs.execute(sql_str)
        rows=curs.fetchall()
        ## if length of rows eq 0,then the lake in the kml is different from the data in postgis,maybe new one or modify lake.
        if len(rows)>0:
            gid_list.append(gid)
    print gid_list
##            for new_gid,num_2 in rows:
##                print new_gid,num
            
        

    conn.commit() 
    curs.close()
    conn.close()
    print "---end---"





















