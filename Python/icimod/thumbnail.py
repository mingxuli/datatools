##thumbnail
import gdal,ogr,osr
import glob
from psycopg2 import connect
import string
import os.path
from osgeo.gdalconst import *
workspace='F:\\Himalaya_Lakes\\images\\Landsat_B543\\'
filelist=glob.glob(workspace+'*.tif')

conn=connect("dbname=glof user=postgres password=glacier")
curs=conn.cursor()
sql_str="delete from landsat_footprint;"
curs.execute(sql_str)
gid=0
for filename in filelist:
    driver=gdal.GetDriverByName('GTiff')
    driver.Register()
    basename=os.path.basename(filename)
    outfile=filename[0:-4]+'_geo.TIF'
    ds=gdal.Open(filename)
    
    proj=ds.GetProjection()
    UTM=osr.SpatialReference()
    UTM.ImportFromWkt(proj)
    Geo=osr.SpatialReference()
    Geo.ImportFromEPSG(4326)
    out_wkt=Geo.ExportToWkt()
    in_wkt=proj

    GeoTran=ds.GetGeoTransform()
    xsize=ds.RasterXSize
    ysize=ds.RasterYSize
    min_x=GeoTran[0]
    max_x=min_x+xsize*GeoTran[1]
    max_y=GeoTran[3]
    min_y=max_y+ysize*GeoTran[5]   

    ct=osr.CoordinateTransformation(UTM,Geo)
    p1=ct.TransformPoint(min_x,min_y)
    p2=ct.TransformPoint(max_x,min_y)
    p3=ct.TransformPoint(max_x,max_y)
    p4=ct.TransformPoint(min_x,max_y)
    
    wkt=[]
    wkt.append(str(p1[0])+' '+str(p1[1]))
    wkt.append(str(p2[0])+' '+str(p2[1]))
    wkt.append(str(p3[0])+' '+str(p3[1]))
    wkt.append(str(p4[0])+' '+str(p4[1]))
    wkt.append(str(p1[0])+' '+str(p1[1]))
    wkt=string.join(wkt,',')
    wkt="GeomFromText('POLYGON(("+wkt+"))',4326)"
    sql_str="insert into landsat_footprint(gid,the_geom) values("+str(gid)+','+wkt+");"
    gid=gid+1
    ##curs.execute(sql_str)
    
    
    ##project
    gdal.ReprojectImage(ds,outfile,src_wkt=in_wkt,dst_wkt=out_wkt,dst_driver=driver,eResampleAlg=GRA_Bilinear)
    ds=None
##conn.commit()
curs.close()
conn.close()
print '====end========'
