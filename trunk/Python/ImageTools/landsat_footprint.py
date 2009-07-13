##thumbnail
from osgeo import gdal,ogr,osr
import glob
from psycopg2 import connect
import string
import os.path
from osgeo.gdalconst import *
workspace='H:\Himalaya_lake\data\Landsat_unziped\\'
dir_list=glob.glob(workspace+'*')

conn=connect("dbname=glof user=postgres password=glacier")
curs=conn.cursor()
sql_str="delete from landsat_footprint;"
curs.execute(sql_str)
conn.commit()
gid=0
for folder in dir_list:    
    linkage=r"'file:///"+string.replace(str(folder),'\\',"/")+"/'"    
    
    filelist=glob.glob(folder+'\\*.*')
    file_list=[]
    filesize=0.0
    for filename in filelist:        
        file_list.append(os.path.basename(filename))    
        filesize=filesize+os.path.getsize(filename)
    file_list="'"+string.join(file_list,',')+"'"
    filesize=str(filesize/1024.0/1024.0)
    
    filelist=glob.glob(folder+'\\*MTL.txt')
    if len(filelist)==1:
        filename=filelist[0]        
        f=open(filename)
        text=f.readlines()
        f.close()
        meta=text[0:-1]
        meta=string.join(meta)
        meta=string.replace(meta,'"','')
        meta="'"+string.replace(meta,"'",'')+"'"
        filename="'"+string.replace(os.path.basename(filename),'_MTL.txt','')+"'"
        for rec in text:
            rec=str(rec)
            index=string.find(rec,'ACQUISITION_DATE')
            if index>-1:
                rec=string.split(rec,'=')
                Acqu_date="'"+rec[1]+"'"                    
                continue
            index=string.find(rec,'WRS_PATH')
            if index>-1:
                rec=string.split(rec,'=')
                Path=str(rec[1])
                Path=string.replace(Path,'\n','')
                Path=string.replace(Path,' ','')
                continue
            index=string.find(rec,'STARTING_ROW')
            if index>-1:
                rec=string.split(rec,'=')
                Row=str(rec[1])
                Row=string.replace(Row,'\n','')
                Row=string.replace(Row,' ','')
                continue
            
            index=string.find(rec,'PRODUCT_UL_CORNER_LAT')
            if index>-1:
                rec=string.split(rec,'=')
                UL_y=float(rec[1])                    
                continue
            
            index=string.find(rec,'PRODUCT_UL_CORNER_LON')
            if index>-1:
                rec=string.split(rec,'=')
                UL_x=float(rec[1])                    
                continue
                    
            index=string.find(rec,'PRODUCT_UR_CORNER_LAT')
            if index>-1:
                rec=string.split(rec,'=')
                UR_y=float(rec[1])
                continue
            index=string.find(rec,'PRODUCT_UR_CORNER_LON')
            if index>-1:
                rec=string.split(rec,'=')
                UR_x=float(rec[1])
                continue

            index=string.find(rec,'PRODUCT_LL_CORNER_LAT')
            if index>-1:
                rec=string.split(rec,'=')
                LL_y=float(rec[1])
                continue
            index=string.find(rec,'PRODUCT_LL_CORNER_LON')
            if index>-1:
                rec=string.split(rec,'=')
                LL_x=float(rec[1])
                continue

            index=string.find(rec,'PRODUCT_LR_CORNER_LAT')
            if index>-1:
                rec=string.split(rec,'=')
                LR_y=float(rec[1])
                continue
            index=string.find(rec,'PRODUCT_LR_CORNER_LON')
            if index>-1:
                rec=string.split(rec,'=')
                LR_x=float(rec[1])
                continue
            
            if rec=='END':
                break
        
        Path_Row="'"+Path+'-'+Row+"'"
        wkt=[]
        wkt.append(str(UL_x)+' '+str(UL_y))
        wkt.append(str(UR_x)+' '+str(UR_y))
        wkt.append(str(LR_x)+' '+str(LR_y))
        wkt.append(str(LL_x)+' '+str(LL_y))
        wkt.append(str(UL_x)+' '+str(UL_y))
        wkt=string.join(wkt,',')
            
        wkt="GeomFromText('POLYGON(("+wkt+"))',4326)"            
        sql_str="""insert into landsat_footprint(gid,filename,linkage,filelist,acqu_date,path_row,filesize,meta,the_geom) values(
"""+str(gid)+','+filename+','+linkage+','+file_list+','+Acqu_date+','+Path_Row+','+filesize+','+meta+','+wkt+");"
        gid=gid+1
        curs.execute(sql_str)

conn.commit()
curs.close()
conn.close()

print '====end========'
