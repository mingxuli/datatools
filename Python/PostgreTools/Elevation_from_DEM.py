#encoding=utf8
#read glacial lake centorid from postgis and get the elevation from dem data(srtm or aster gdem), at last store/updating these value into database. 
#需要用到的模块包括:
#GDAL,ChartDirect和numpy
try:
    from osgeo import ogr,gdal    
except:
    import ogr,gdal
from osgeo.gdalconst import *
from numpy import *
from psycopg2 import connect

if __name__=='__main__':
    host='localhost'
    dbname='GGLIS'
    user='postgres'
    password='postgres'
    table_name="\"Nepal_Glacial_Lake_2009_final\""
    srtm_file='G:\\Nepal\\DEM\\SRTM_Nepal.img'
    gdem_file='G:\\Nepal\\DEM\\ASTGTM_Nepal.tif'
    ## connect to postgres/postgis
    conn=connect("host="+host+" dbname="+dbname+" user="+user+" password="+password)
    curs=conn.cursor()
    sql_str="select gid,st_x(centroid(the_geom)),st_y(centroid(the_geom)) from" +table_name +";"
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
    for gid,x,y in records:
        x_offset=(x - x0)/ps_x
        y_offset=(y - y0)/ps_y
        value=band.ReadAsArray(int(x_offset),int(y_offset),1,1)
        elevation=value[0,0]
        str_update="update "+table_name+" set ele_gdem="+str(elevation)+" where gid="+str(gid)+";"
        curs.execute(str_update)
    conn.commit() 
    curs.close()
    conn.close()
    print 'end'
