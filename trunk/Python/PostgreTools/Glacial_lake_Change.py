#encoding=utf8
#! /usr/bin/python
from psycopg2 import connect
import string


if __name__ == "__main__":
    
    
    print 'Start Runing>>>>>>>>>>>>>>>>>>>>>>>'
    gl_old="\"Nepal_2000_v2\""
    gl_new="\"Nepal_2005_final\""
    conn=connect("host=localhost dbname=GGLIS user=postgres password=postgres")
    curs=conn.cursor()

    sql_str="select gid,gl_area from "+gl_old+"  order by gid;"
    curs.execute(sql_str)
    records=curs.fetchall()

    for gid_old,area in records:        
        #check overlaps
        sql_overlaps="select gl_id,gl_area from "+gl_new+\
                        " where st_overlaps(the_geom,(select the_geom from "+gl_old+\
                        " where gid="+str(gid_old)+"));"
        curs.execute(sql_overlaps)
        rows_overlaps=curs.fetchall()
        if len(rows_overlaps)==1:
            for gid_new,area_new in rows_overlaps:
                sql_update="update "+gl_old+" set gl_id="+str(gid_new)+" where gid="+str(gid_old)+";"
                curs.execute(sql_update)
    sql_str="select gid,gl_area from "+gl_old+" where gl_id is null order by gid;"
    curs.execute(sql_str)
    records1=curs.fetchall()
    
    for gid_old1,area in records1:        
        #check contains
        sql_contains="select gl_id,gl_area from "+gl_new+\
                        " where st_contains(the_geom,(select centroid(the_geom) from "+gl_old+\
                        " where gid="+str(gid_old1)+"));"
        curs.execute(sql_contains)
        rows_contains=curs.fetchall()
        if len(rows_contains)>0:
            for gid_new1,area_new in rows_contains:
                sql_update1="update "+gl_old+" set gl_id="+str(gid_new1)+" where gid="+str(gid_old1)+";"
                curs.execute(sql_update1) 

            
    conn.commit()
##        if len(rows_overlaps)>0:
##            #一个冰湖分裂为多个冰湖
##            if len(rows_overlaps)>1: #与超过1个以上的多边形重叠            
##                split_2000_id.append(gid_2000)
##                split_2000_area.append(area_2000)
##                for gid_2010 , type, area_2010 in rows_overlaps:                                        
##                    split_2010_id.append(gid_2010)
##                    split_2010_area.append(area_2010) 
##                # 检查是否还包含多边形
##                sql_within="select gid,\"Gl_Class\",\"Gl_Area\" from "+gl_2010+\
##                           " where st_within(the_geom,(select the_geom from "+gl_2000+\
##                           " where gid="+str(gid_2000)+"));"
##                curs.execute(sql_within)
##                rows_within=curs.fetchall()
##                if len(rows_within)>0:
##                    for gid_2010, type, area_2010 in rows_within:
##                        split_2010_id.append(gid_2010)
##                        split_2010_area.append(area_2010)
##                           
##            if len(rows_overlaps)==1: #只与一个多边形重叠
##                gid_2010=rows_overlaps[0][0]
##                type_2010=rows_overlaps[0][1]
##                area_2010=rows_overlaps[0][2]    
##                # 检查是否还包含多边形
##                sql_within2="select gid,\"Gl_Class\",\"Gl_Area\" from "+gl_2010+\
##                           " where st_within(the_geom,(select the_geom from "+gl_2000+\
##                           " where gid="+str(gid_2000)+"));"
##                curs.execute(sql_within2)
##                rows_within2=curs.fetchall()
##                if len(rows_within2)>0: #如果还包含其他的多边形，也属于分裂                    
##                    split_2000_id.append(gid_2000)
##                    split_2000_area.append(area_2000)
##                    split_2010_id.append(gid_2010)
##                    split_2010_area.append(area_2010)                    
##                    for gid_other,type_other,area_other in rows_within2:
##                        split_2010_id.append(gid_other)
##                        split_2010_area.append(area_other)
##                else:#如果没有包含多边形
##                    #检查与该多边形重叠的多边形是否还包含其他的多边形，如果是，则该冰湖与其他冰湖融合为一个大的冰湖                    
##                    sql_contains="select gid,\"Gl_Area\" from "+gl_2000+\
##                                        " where st_within(the_geom,(select the_geom from "+gl_2010+\
##                                        " where gid="+str(gid_2010) +"));"
##                    curs.execute(sql_contains)
##                    rows_contains=curs.fetchall()
##                    if len(rows_contains)>0:
##                        pass
###                        merge_2010_id.append(gid_2010)
###                        merge_2010_area.append(area_2010)
###                        for gid_2000, area_2000 in rows_contains:
###                            merge_2000_id.append(gid_2000)
###                            merge_2000_area.append(area_2000)                    
##                    else:
##                        #检查与该多边形重叠的多边形是否还和多个多边形重叠，如果是，则多个湖泊融合为一个大冰湖
##                        sql_overlaps2="select gid,\"Gl_Area\" from "+gl_2000+\
##                                            " where st_overlaps(the_geom,(select the_geom from "+gl_2010+\
##                                            " where gid="+str(gid_2010) +"));"
##                        curs.execute(sql_overlaps2)
##                        rows_overlaps2=curs.fetchall()
##                        if len(rows_overlaps2)>1:
##                            pass # merge                             
##                        else:
##                            same_2000_id.append(gid_2000)
##                            same_2000_area.append(area_2000)
##                            same_2010_id.append(gid_2010)
##                            same_2010_area.append(area_2010)
##                
##        #如果不跟其他多边形重叠
##        if len(rows_overlaps)==0:         
##            # check within检查包含关系
##            sql_within3="select gid,\"Gl_Class\",\"Gl_Area\" from "+gl_2010+\
##                           " where st_within(the_geom,(select the_geom from "+gl_2000+\
##                           " where gid="+str(gid_2000)+"));"
##            curs.execute(sql_within3)
##            rows_within3=curs.fetchall()
##            
##            if len(rows_within3)>0:                
##                if len(rows_within3)==1:                   
##                    same_2000_id.append(gid_2000)
##                    same_2000_area.append(area_2000)
##                    for gid_2010,type, area_2010 in rows_within3:
##                        same_2010_id.append(gid_2010)
##                        same_2010_area.append(area_2010)
##                    
##                else:                        
##                    split_2000_id.append(gid_2000)
##                    split_2000_area.append(area_2000)
##                    for gid_2010,type, area_2010 in rows_within3:
##                        split_2010_id.append(gid_2010)
##                        split_2010_area.append(area_2010) 
##            
##            else:
##               
##                #检查被包含
##                sql_contains="select gid,\"Gl_Class\",\"Gl_Area\" from "+gl_2010+\
##                           " where st_contains(the_geom,(select the_geom from "+gl_2000+\
##                           " where gid="+str(gid_2000)+"));"
##                curs.execute(sql_contains)
##                rows_contains=curs.fetchall()    
##                if  len(rows_contains)>0:                    
##                                          
##                    if len(rows_contains)==1:
##                        gid_2010=rows_contains[0][0]
##                        area_2010=rows_contains[0][2]                        
##                        sql_within4="select gid,\"Gl_Class\",\"Gl_Area\" from "+gl_2000+\
##                                   " where st_within(the_geom,(select the_geom from "+gl_2010+\
##                                   " where gid="+str(gid_2010)+"));"
##                        curs.execute(sql_within4)
##                        rows_within4=curs.fetchall() 
##                        if len(rows_within4)==1:
##                            sql_overlaps4="select gid,\"Gl_Class\",\"Gl_Area\" from "+gl_2000+\
##                                   " where st_overlaps(the_geom,(select the_geom from "+gl_2010+\
##                                   " where gid="+str(gid_2010)+"));"
##                            curs.execute(sql_overlaps4)
##                            rows_overlaps4=curs.fetchall() 
##                            if len(rows_overlaps4)==0:
##                                print 'gid', gid_2000
##                                same_2000_id.append(gid_2000)
##                                same_2000_area.append(area_2000)                        
##                                same_2010_id.append(gid_2010)
##                                same_2010_area.append(area_2010)
##                else:                    
##                    Dry_2000_id.append(gid_2000)
##                    Dry_2000_area.append(area_2000)                

    conn.commit()
    
 
    
   ######################################################################### 
        


print '---end---'
