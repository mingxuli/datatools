# encode="utf8"
from osgeo import ogr
import sys,glob
import os,string,codecs,unicodedata    

def shp2shp(shapefile,outputfile):
    driver=ogr.GetDriverByName('ESRI Shapefile')
    dataSource=driver.Open(shapefile,0)    
    lookup='utf8'
    if dataSource is None:
        print 'Could not open '+shapefile
        sys.exit(1)
    layer=dataSource.GetLayer()
    feature=layer.GetNextFeature()
    field_count=feature.GetFieldCount()
            
    geom=feature.GetGeometryRef()
    geoType=geom.ExportToWkt()
    geoType=string.split(geoType,'((')
    geoType=geoType[0]
    geoType=string.strip(geoType)
    
    count=0


    dataSource.Destroy()

if __name__=='__main__':
    inpath='D://Globe Maps//Bhutan//'
    outpath='D://test//'
    filelist=glob.glob(inpath+'*.shp')
    for shapefile in filelist:
        print shapefile
    print 'end'
