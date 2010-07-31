#encoding=utf8
#! /usr/bin/python
from psycopg2 import connect
import string


if __name__ == "__main__":
    
    Dry_2000_id=[]
    Dry_2000_area=[]
    New_id=[]
    New_area=[]
    New_type=[]
    same_2000_id=[]
    same_2000_area=[]    
    same_2010_id=[]
    same_2010_area=[]
    same_2010_type=[]
    merge_2000_id=[]
    merge_2000_area=[]
    merge_2010_id=[]
    merge_2010_area=[]
    merge_2020_type=[]
    split_2000_id=[]
    split_2000_area=[]
    split_2010_id=[]
    split_2010_area=[]
    split_2010_type=[]
    
    ##########################################
    print 'Start Runing>>>>>>>>>>>>>>>>>>>>>>>'
#    gl_2000='test_old'
#    gl_2010='test_new'
    gl_2000="\"Nepal_Glacial_Lake_2001_Revised_v2\""
    gl_2010="\"Nepal_Glacial_Lake_2009_final\""
    conn=connect("host=localhost dbname=GGLIS user=postgres password=postgres")
    curs=conn.cursor()

    sql_str="select gid,\"Gl_Area\" from "+gl_2000+"  order by gid;"
    curs.execute(sql_str)
    records=curs.fetchall()

    for gid_2000,area_2000 in records:        
        #check overlaps
        sql_overlaps="select gid,\"Gl_Class\",\"Gl_Area\" from "+gl_2010+\
                        " where st_overlaps(the_geom,(select the_geom from "+gl_2000+\
                        " where gid="+str(gid_2000)+"));"
        curs.execute(sql_overlaps)
        rows_overlaps=curs.fetchall()
        if len(rows_overlaps)>0:
            #一个冰湖分裂为多个冰湖
            if len(rows_overlaps)>1: #与超过1个以上的多边形重叠            
                split_2000_id.append(gid_2000)
                split_2000_area.append(area_2000)
                for gid_2010 , type, area_2010 in rows_overlaps:                                        
                    split_2010_id.append(gid_2010)
                    split_2010_area.append(area_2010) 
                # 检查是否还包含多边形
                sql_within="select gid,\"Gl_Class\",\"Gl_Area\" from "+gl_2010+\
                           " where st_within(the_geom,(select the_geom from "+gl_2000+\
                           " where gid="+str(gid_2000)+"));"
                curs.execute(sql_within)
                rows_within=curs.fetchall()
                if len(rows_within)>0:
                    for gid_2010, type, area_2010 in rows_within:
                        split_2010_id.append(gid_2010)
                        split_2010_area.append(area_2010)
                           
            if len(rows_overlaps)==1: #只与一个多边形重叠
                gid_2010=rows_overlaps[0][0]
                type_2010=rows_overlaps[0][1]
                area_2010=rows_overlaps[0][2]    
                # 检查是否还包含多边形
                sql_within2="select gid,\"Gl_Class\",\"Gl_Area\" from "+gl_2010+\
                           " where st_within(the_geom,(select the_geom from "+gl_2000+\
                           " where gid="+str(gid_2000)+"));"
                curs.execute(sql_within2)
                rows_within2=curs.fetchall()
                if len(rows_within2)>0: #如果还包含其他的多边形，也属于分裂                    
                    split_2000_id.append(gid_2000)
                    split_2000_area.append(area_2000)
                    split_2010_id.append(gid_2010)
                    split_2010_area.append(area_2010)                    
                    for gid_other,type_other,area_other in rows_within2:
                        split_2010_id.append(gid_other)
                        split_2010_area.append(area_other)
                else:#如果没有包含多边形
                    #检查与该多边形重叠的多边形是否还包含其他的多边形，如果是，则该冰湖与其他冰湖融合为一个大的冰湖                    
                    sql_contains="select gid,\"Gl_Area\" from "+gl_2000+\
                                        " where st_within(the_geom,(select the_geom from "+gl_2010+\
                                        " where gid="+str(gid_2010) +"));"
                    curs.execute(sql_contains)
                    rows_contains=curs.fetchall()
                    if len(rows_contains)>0:
                        pass
#                        merge_2010_id.append(gid_2010)
#                        merge_2010_area.append(area_2010)
#                        for gid_2000, area_2000 in rows_contains:
#                            merge_2000_id.append(gid_2000)
#                            merge_2000_area.append(area_2000)                    
                    else:
                        #检查与该多边形重叠的多边形是否还和多个多边形重叠，如果是，则多个湖泊融合为一个大冰湖
                        sql_overlaps2="select gid,\"Gl_Area\" from "+gl_2000+\
                                            " where st_overlaps(the_geom,(select the_geom from "+gl_2010+\
                                            " where gid="+str(gid_2010) +"));"
                        curs.execute(sql_overlaps2)
                        rows_overlaps2=curs.fetchall()
                        if len(rows_overlaps2)>1:
                            pass # merge                             
                        else:
                            same_2000_id.append(gid_2000)
                            same_2000_area.append(area_2000)
                            same_2010_id.append(gid_2010)
                            same_2010_area.append(area_2010)
                
        #如果不跟其他多边形重叠
        if len(rows_overlaps)==0:         
            # check within检查包含关系
            sql_within3="select gid,\"Gl_Class\",\"Gl_Area\" from "+gl_2010+\
                           " where st_within(the_geom,(select the_geom from "+gl_2000+\
                           " where gid="+str(gid_2000)+"));"
            curs.execute(sql_within3)
            rows_within3=curs.fetchall()
            
            if len(rows_within3)>0:                
                if len(rows_within3)==1:                   
                    same_2000_id.append(gid_2000)
                    same_2000_area.append(area_2000)
                    for gid_2010,type, area_2010 in rows_within3:
                        same_2010_id.append(gid_2010)
                        same_2010_area.append(area_2010)
                    
                else:                        
                    split_2000_id.append(gid_2000)
                    split_2000_area.append(area_2000)
                    for gid_2010,type, area_2010 in rows_within3:
                        split_2010_id.append(gid_2010)
                        split_2010_area.append(area_2010) 
            
            else:
               
                #检查被包含
                sql_contains="select gid,\"Gl_Class\",\"Gl_Area\" from "+gl_2010+\
                           " where st_contains(the_geom,(select the_geom from "+gl_2000+\
                           " where gid="+str(gid_2000)+"));"
                curs.execute(sql_contains)
                rows_contains=curs.fetchall()    
                if  len(rows_contains)>0:                    
                                          
                    if len(rows_contains)==1:
                        gid_2010=rows_contains[0][0]
                        area_2010=rows_contains[0][2]                        
                        sql_within4="select gid,\"Gl_Class\",\"Gl_Area\" from "+gl_2000+\
                                   " where st_within(the_geom,(select the_geom from "+gl_2010+\
                                   " where gid="+str(gid_2010)+"));"
                        curs.execute(sql_within4)
                        rows_within4=curs.fetchall() 
                        if len(rows_within4)==1:
                            sql_overlaps4="select gid,\"Gl_Class\",\"Gl_Area\" from "+gl_2000+\
                                   " where st_overlaps(the_geom,(select the_geom from "+gl_2010+\
                                   " where gid="+str(gid_2010)+"));"
                            curs.execute(sql_overlaps4)
                            rows_overlaps4=curs.fetchall() 
                            if len(rows_overlaps4)==0:
                                print 'gid', gid_2000
                                same_2000_id.append(gid_2000)
                                same_2000_area.append(area_2000)                        
                                same_2010_id.append(gid_2010)
                                same_2010_area.append(area_2010)
                else:                    
                    Dry_2000_id.append(gid_2000)
                    Dry_2000_area.append(area_2000)                

    conn.commit()
    
    same_old_count=str(len(same_2000_id))
    same_old_area=str(sum(same_2000_area))
    same_new_count=str(len(same_2010_id))
    same_new_area=str(sum(same_2010_area))
    
    split_old_count=str(len(split_2000_id))
    split_old_area=str(sum(split_2000_area))
    split_new_count=str(len(split_2010_id))
    split_new_area=str(sum(split_2010_area))    

    Dry_lake_count=str(len(Dry_2000_area))
    Dry_lake_area=str(sum(Dry_2000_area))
    
    
   ######################################################################### 
        
    Dry_2000_id=[]
    Dry_2000_area=[]
    New_id=[]
    New_area=[]
    New_type=[]
    same_2000_id=[]
    same_2000_area=[]    
    same_2010_id=[]
    same_2010_area=[]
    same_2010_type=[]
    merge_2000_id=[]
    merge_2000_area=[]
    merge_2010_id=[]
    merge_2010_area=[]
    merge_2020_type=[]
    split_2000_id=[]
    split_2000_area=[]
    split_2010_id=[]
    split_2010_area=[]
    split_2010_type=[]
    
    ##########################################
#    gl_2010='test_old'
#    gl_2000='test_new'

    gl_2010="\"Nepal_Glacial_Lake_2001_Revised_v2\""
    gl_2000="\"Nepal_Glacial_Lake_2009_final\""

    sql_str="select gid,\"Gl_Area\" from "+gl_2000+"  order by gid;"
    curs.execute(sql_str)
    records=curs.fetchall()

    for gid_2000,area_2000 in records:        
        #check overlaps
        sql_overlaps="select gid,\"Gl_Class\",\"Gl_Area\" from "+gl_2010+\
                        " where st_overlaps(the_geom,(select the_geom from "+gl_2000+\
                        " where gid="+str(gid_2000)+"));"
        curs.execute(sql_overlaps)
        rows_overlaps=curs.fetchall()
        if len(rows_overlaps)>0:
            #一个冰湖分裂为多个冰湖
            if len(rows_overlaps)>1: #与超过1个以上的多边形重叠            
                split_2000_id.append(gid_2000)
                split_2000_area.append(area_2000)
                for gid_2010 , type, area_2010 in rows_overlaps:                                        
                    split_2010_id.append(gid_2010)
                    split_2010_area.append(area_2010) 
                # 检查是否还包含多边形
                sql_within="select gid,\"Gl_Class\",\"Gl_Area\" from "+gl_2010+\
                           " where st_within(the_geom,(select the_geom from "+gl_2000+\
                           " where gid="+str(gid_2000)+"));"
                curs.execute(sql_within)
                rows_within=curs.fetchall()
                if len(rows_within)>0:
                    for gid_2010, type, area_2010 in rows_within:
                        split_2010_id.append(gid_2010)
                        split_2010_area.append(area_2010)
                           
            if len(rows_overlaps)==1: #只与一个多边形重叠
                gid_2010=rows_overlaps[0][0]
                type_2010=rows_overlaps[0][1]
                area_2010=rows_overlaps[0][2]    
                # 检查是否还包含多边形
                sql_within2="select gid,\"Gl_Class\",\"Gl_Area\" from "+gl_2010+\
                           " where st_within(the_geom,(select the_geom from "+gl_2000+\
                           " where gid="+str(gid_2000)+"));"
                curs.execute(sql_within2)
                rows_within2=curs.fetchall()
                if len(rows_within2)>0: #如果还包含其他的多边形，也属于分裂                    
                    split_2000_id.append(gid_2000)
                    split_2000_area.append(area_2000)
                    split_2010_id.append(gid_2010)
                    split_2010_area.append(area_2010)                    
                    for gid_other,type_other,area_other in rows_within2:
                        split_2010_id.append(gid_other)
                        split_2010_area.append(area_other)
                else:#如果没有包含多边形
                    #检查与该多边形重叠的多边形是否还包含其他的多边形，如果是，则该冰湖与其他冰湖融合为一个大的冰湖                    
                    sql_contains="select gid,\"Gl_Area\" from "+gl_2000+\
                                        " where st_within(the_geom,(select the_geom from "+gl_2010+\
                                        " where gid="+str(gid_2010) +"));"
                    curs.execute(sql_contains)
                    rows_contains=curs.fetchall()
                    if len(rows_contains)>0:
                        pass
#                        merge_2010_id.append(gid_2010)
#                        merge_2010_area.append(area_2010)
#                        for gid_2000, area_2000 in rows_contains:
#                            merge_2000_id.append(gid_2000)
#                            merge_2000_area.append(area_2000)                    
                    else:
                        #检查与该多边形重叠的多边形是否还和多个多边形重叠，如果是，则多个湖泊融合为一个大冰湖
                        sql_overlaps2="select gid,\"Gl_Area\" from "+gl_2000+\
                                            " where st_overlaps(the_geom,(select the_geom from "+gl_2010+\
                                            " where gid="+str(gid_2010) +"));"
                        curs.execute(sql_overlaps2)
                        rows_overlaps2=curs.fetchall()
                        if len(rows_overlaps2)>1:
                            pass # merge                             
                        else:
                            same_2000_id.append(gid_2000)
                            same_2000_area.append(area_2000)
                            same_2010_id.append(gid_2010)
                            same_2010_area.append(area_2010)
                
        #如果不跟其他多边形重叠
        if len(rows_overlaps)==0:         
            # check within检查包含关系
            sql_within3="select gid,\"Gl_Class\",\"Gl_Area\" from "+gl_2010+\
                           " where st_within(the_geom,(select the_geom from "+gl_2000+\
                           " where gid="+str(gid_2000)+"));"
            curs.execute(sql_within3)
            rows_within3=curs.fetchall()
            
            if len(rows_within3)>0:                
                if len(rows_within3)==1:                   
                    same_2000_id.append(gid_2000)
                    same_2000_area.append(area_2000)
                    for gid_2010,type, area_2010 in rows_within3:
                        same_2010_id.append(gid_2010)
                        same_2010_area.append(area_2010)
                    
                else:                        
                    split_2000_id.append(gid_2000)
                    split_2000_area.append(area_2000)
                    for gid_2010,type, area_2010 in rows_within3:
                        split_2010_id.append(gid_2010)
                        split_2010_area.append(area_2010) 
            
            else:
               
                #检查被包含
                sql_contains="select gid,\"Gl_Class\",\"Gl_Area\" from "+gl_2010+\
                           " where st_contains(the_geom,(select the_geom from "+gl_2000+\
                           " where gid="+str(gid_2000)+"));"
                curs.execute(sql_contains)
                rows_contains=curs.fetchall()    
                if  len(rows_contains)>0:                    
                                          
                    if len(rows_contains)==1:
                        gid_2010=rows_contains[0][0]
                        area_2010=rows_contains[0][2]                        
                        sql_within4="select gid,\"Gl_Class\",\"Gl_Area\" from "+gl_2000+\
                                   " where st_within(the_geom,(select the_geom from "+gl_2010+\
                                   " where gid="+str(gid_2010)+"));"
                        curs.execute(sql_within4)
                        rows_within4=curs.fetchall() 
                        if len(rows_within4)==1:
                            sql_overlaps4="select gid,\"Gl_Class\",\"Gl_Area\" from "+gl_2000+\
                                   " where st_overlaps(the_geom,(select the_geom from "+gl_2010+\
                                   " where gid="+str(gid_2010)+"));"
                            curs.execute(sql_overlaps4)
                            rows_overlaps4=curs.fetchall() 
                            if len(rows_overlaps4)==0:
                                print 'gid', gid_2000
                                same_2000_id.append(gid_2000)
                                same_2000_area.append(area_2000)                        
                                same_2010_id.append(gid_2010)
                                same_2010_area.append(area_2010)
                else:                    
                    Dry_2000_id.append(gid_2000)
                    Dry_2000_area.append(area_2000)                

    conn.commit()
    
    
    same_old_count1=str(len(same_2000_id))
    same_old_area1=str(sum(same_2000_area))
    same_new_count1=str(len(same_2010_id))
    same_new_area1=str(sum(same_2010_area))
    
    merge_new_count=str(len(split_2000_id))
    merge_new_area=str(sum(split_2000_area))
    merge_old_count=str(len(split_2010_id))
    merge_old_area=str(sum(split_2010_area))    

    new_lake_count=str(len(Dry_2000_area))
    new_lake_area=str(sum(Dry_2000_area))
    
    
    print '|--type--|--old count--|--old area--|--new count--|--new area--|'
    print '|--same--|--'+same_old_count+'--|--'+same_old_area+'--|--'+same_new_count+'--|--'+same_new_area+'--|'
    print '|--same--|--'+same_old_count1+'--|--'+same_old_area1+'--|--'+same_new_count1+'--|--'+same_new_area1+'--|'

    print '|--split--|--'+split_old_count+'--|--'+split_old_area+'--|--'+split_new_count+'--|--'+split_new_area+'--|'
    print '|--merge--|--'+merge_old_count+'--|--'+merge_old_area+'--|--'+merge_new_count+'--|--'+merge_new_area+'--|'
    print '|--dry --|--'+Dry_lake_count+'--|--'+Dry_lake_area+'--|'
    print '|--New --|--'+new_lake_count+'--|--'+new_lake_area+'--|'

print '---end---'
