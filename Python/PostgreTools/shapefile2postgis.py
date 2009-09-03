# encode="utf8"
from osgeo import ogr
import sys
import os,string,codecs,unicodedata
from psycopg2 import connect
    
shapefile='D://glims_query_25016//glims_query_25016.shp'
driver=ogr.GetDriverByName('ESRI Shapefile')
dataSource=driver.Open(shapefile,0)
conn=connect("host=localhost dbname=glof user=postgres password=glacier")
curs=conn.cursor()
table_name='glims_glaicer'
create_sql='CREATE TABLE '+table_name+'(gid integer NOT NULL PRIMARY KEY,'
lookup='utf8'
if dataSource is None:
    print 'Could not open '+shapefile
    sys.exit(1)
layer=dataSource.GetLayer()
feature=layer.GetNextFeature()
field_count=feature.GetFieldCount()
for i in range(field_count):
    fieldDefn=feature.GetFieldDefnRef(i)
    if fieldDefn.GetType()==0:
        FieldType='integer'
    if fieldDefn.GetType()==1:
        FieldType='integer'
    if fieldDefn.GetType()==2:
        FieldType='double precision'
    if fieldDefn.GetType()==3:
        FieldType='double precision'
    if fieldDefn.GetType()==4:
        FieldType='varchar'
    if fieldDefn.GetType()==5:
        FieldType='varchar'
    if fieldDefn.GetType()==6:
        FieldType='varchar'
    create_sql=create_sql+fieldDefn.GetName()+' '+FieldType+',\n'
    
geom=feature.GetGeometryRef()
geoType=geom.ExportToWkt()
geoType=string.split(geoType,'((')
geoType=geoType[0]
geoType=string.strip(geoType)
create_sql=create_sql+"""
  the_geom geometry,
  CONSTRAINT enforce_dims_the_geom CHECK (ndims(the_geom) = 2),
  CONSTRAINT enforce_geotype_the_geom CHECK (geometrytype(the_geom) = '"""+geoType+"""'::text OR the_geom IS NULL),
  CONSTRAINT enforce_srid_the_geom CHECK (srid(the_geom) = 4326)
);"""
curs.execute(create_sql)
conn.commit()
count=0
while feature:
    insert_sql='insert into '+table_name+' values('+str(count)+','
    for i in range(field_count):
        value=feature.GetField(i)
        fieldDefn=feature.GetFieldDefnRef(i)
        if fieldDefn.GetType()==4:
            insert_sql=insert_sql+"'"+str(value)+"',"
        else:
            insert_sql=insert_sql+str(value)+','
    geom=feature.GetGeometryRef()
    geom.SetCoordinateDimension(2)
    insert_sql=insert_sql+"GeomFromText('"+geom.ExportToWkt()+"',4326));"
    insert_sql=string.replace(insert_sql,'None','NULL')
    insert_sql=string.replace(insert_sql,"'NULL'",'NULL')
    insert_sql=codecs.lookup('utf8')[3](insert_sql)
    insert_sql=unicode(insert_sql)
    curs.execute(insert_sql)
    conn.commit()
    feature.Destroy()
    feature=layer.GetNextFeature()
    count=count+1

dataSource.Destroy()
curs.close()
print 'end'
