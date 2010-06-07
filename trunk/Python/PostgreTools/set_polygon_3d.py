#encoding=utf8
#! /usr/bin/python
#get z value and convert a polygon to polygon 3d 
try:
    from osgeo import ogr,gdal
except:
    import ogr,gdal
from osgeo.gdalconst import *
from numpy import *
from psycopg2 import connect

if __name__ == "__main__":
    srtm_file='G:\\Nepal\\DEM\\SRTM_Nepal.img'
    gdem_file='G:\\Nepal\\DEM\\ASTGTM_Nepal.tif'
    ## connect to postgres/postgis
    conn=connect("host=localhost dbname=GGLIS user=postgres password=postgres")
    curs=conn.cursor()
    sql_str="select gid,astext(geom_2d) from \"Nepal_Glacial_Lake_2009_3d\";"
    curs.execute(sql_str)
    records=curs.fetchall()
    #Open DEM
    gdal.AllRegister()
    ##dataset=gdal.Open(srtm_file,GA_ReadOnly)
    dataset=gdal.Open(gdem_file,GA_ReadOnly)
    if dataset is None:
        print 'Can not open '+ srtm_file
        sys.exit(1) #
    cols=dataset.RasterXSize
    rows=dataset.RasterYSize
    bands=dataset.RasterCount
    geotransform = dataset.GetGeoTransform()
    x0=geotransform[0] #x起点
    y0=geotransform[3] #y起点
    ps_x=geotransform[1]
    ps_y=geotransform[5]
    band=dataset.GetRasterBand(1)
    
    for gid,text_WKT in records:
        text_WKT=text_WKT.replace('),(',' '+str(gid)+').(')
        text_WKT=text_WKT.replace(',',' '+str(gid)+',')
        text_WKT=text_WKT.replace('))',' '+str(gid)+'))')
        text_WKT=text_WKT.replace(').(','),(')
        

        

##        x_offset=(x - x0)/ps_x
##        y_offset=(y - y0)/ps_y
##        value=band.ReadAsArray(int(x_offset),int(y_offset),1,1)
##        elevation=value[0,0]
        str_update="update \"Nepal_Glacial_Lake_2009_3d\" set geom_3d=st_force_3dz(ST_GeomFromText('"+text_WKT+"')) where gid="+str(gid)+";"
        print gid
        curs.execute(str_update)
    conn.commit() 
    curs.close()
    conn.close()

    print "--end--";
