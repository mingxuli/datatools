#encoding=utf8
# To change this template, choose Tools | Templates
# and open the template in the editor.
import Image,os,sys
from osgeo import gdal
from osgeo.gdalconst import *
from numpy import *
from psycopg2 import connect

if __name__=="__main__":
    dem_file='D:\\Workspace\\DEM\\SRTM_Nepal.img'
    outpath="D:\\Workspace\\DEM\\out_dem\\"
    conn=connect("host=localhost dbname=GGLIS user=postgres password=postgres")
    curs=conn.cursor()
    sql_str="select gid,st_xmax(st_box2d(the_geom)),st_xmin(st_box2d(the_geom)),st_ymax(st_box2d(the_geom)),st_ymin(st_box2d(the_geom))"\
             " from \"Nepal_Glacial_Lake_2009_final\" where \"Gl_Area\">0.1;"
    curs.execute(sql_str)
    rows=curs.fetchall()
    
    for gid,max_x,min_x,max_y,min_y in rows:
        outfile=outpath+str(gid)+".tif"
        cmd_str="gdal_translate -of GTiff -projwin "+str(min_x)+" "+ str(max_y)+" "\
             +str(max_x)+" "+str(min_y)+" "+dem_file+" "+outfile
        os.popen(cmd_str)
    curs.close()
    conn.close()
    print 'end'
