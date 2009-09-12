# encoding="utf8"
# wulizong@lzb.ac.cn
# 2009.9.11
import sys,glob,os,string 
from osgeo import ogr

def shp2shp(shapefile,outfile):
    driver=ogr.GetDriverByName('ESRI Shapefile')
    dataSource=driver.Open(shapefile,0)    
    lookup='utf8'
    if dataSource is None:
        print 'Could not open '+shapefile
        sys.exit(1)
    layer=dataSource.GetLayer()
    #几何对象数目
    Feature_count=layer.GetFeatureCount()
    Feature=layer.GetFeature(0)
    FeatureDef=Feature.GetDefnRef()
    #几何类型,错误就在此处
    GeomType=FeatureDef.GetGeomType()    
    #真实的几何类型
    Geom=Feature.GetGeometryRef()
    geoType=Geom.ExportToWkt()
    True_GeomType=string.split(geoType,'(')
    True_GeomType=True_GeomType[0]
    True_GeomType=string.strip(True_GeomType)
    #字段数
    Field_count=FeatureDef.GetFieldCount()    
    #地图投影信息
    mapinfo=layer.GetSpatialRef()    
    if GeomType<0:        
        if os.access(outfile,os.F_OK):
            driver.DeleteDataSource(str(outfile))
        New_ds=driver.CreateDataSource(outfile)
        if True_GeomType=='POINT':
            New_Layer=New_ds.CreateLayer('',mapinfo,geom_type=ogr.wkbPoint)
        if True_GeomType=='LINESTRING':
            New_Layer=New_ds.CreateLayer('',mapinfo,geom_type=ogr.wkbLineString)
        if True_GeomType=='POLYGON': 
            New_Layer=New_ds.CreateLayer('',mapinfo,geom_type=ogr.wkbPolygon)
        # 拷贝原有的字段定义
        for i in range(Field_count):
            New_FieldDefn=FeatureDef.GetFieldDefn(i)
            New_Layer.CreateField(New_FieldDefn)
            
        for i in range(Feature_count):
            Feature=layer.GetFeature(i)
            FeatureDef=Feature.GetDefnRef()
            Geom=Feature.GetGeometryRef()
            wkt=Geom.ExportToWkt()
            
            New_Feature=ogr.Feature(New_Layer.GetLayerDefn())             
            New_Geom = ogr.CreateGeometryFromWkt(wkt)            
            New_Feature.SetGeometry(New_Geom)
            
            for j in range(Field_count):
                New_Feature.SetField(j,Feature.GetField(j))
                
            New_Layer.CreateFeature(New_Feature)        
        New_ds.Destroy()
    else:         
        if os.access(outfile,os.F_OK):
            driver.DeleteDataSource(str(outfile))
        New_ds=driver.CreateDataSource(outfile)
        if GeomType == 1:            
            New_Layer=New_ds.CreateLayer('',mapinfo,geom_type=ogr.wkbPoint)
        if GeomType == 2:
            New_Layer=New_ds.CreateLayer('',mapinfo,geom_type=ogr.wkbLineString)
        if GeomType == 3: 
            New_Layer=New_ds.CreateLayer('',mapinfo,geom_type=ogr.wkbPolygon)
        # 拷贝原有的字段定义
        for i in range(Field_count):
            New_FieldDefn=FeatureDef.GetFieldDefn(i)
            New_Layer.CreateField(New_FieldDefn)
            
        for i in range(Feature_count):
            Feature=layer.GetFeature(i)
            FeatureDef=Feature.GetDefnRef()
            Geom=Feature.GetGeometryRef()
            wkt=Geom.ExportToWkt()
            
            New_Feature=ogr.Feature(New_Layer.GetLayerDefn())             
            New_Geom = ogr.CreateGeometryFromWkt(wkt)            
            New_Feature.SetGeometry(New_Geom)
            
            for j in range(Field_count):
                New_Feature.SetField(j,Feature.GetField(j))
                
            New_Layer.CreateFeature(New_Feature)        
        New_ds.Destroy()
    dataSource.Destroy()
    print shapefile+' OK!'

if __name__=='__main__':
    inpath='D://Globe Maps//Bahrain//'
    outpath='D://Globe Maps//New_Result//Bahrain//'
    filelist=glob.glob(inpath+'*.shp')
    for shapefile in filelist:        
        outfile=outpath+os.path.basename(shapefile)
        shp2shp(shapefile,outfile)
    print '==end=='
