#encoding=utf8
#! /usr/bin/python
from psycopg2 import connect
import string
       
    
if __name__ == "__main__":
    conn=connect("host=localhost dbname=GGLIS user=postgres password=postgres")
    curs=conn.cursor()
    sql_str="delete from \"Nepal_Glacial_Lake_Change_2001_to_2009\""
    curs.execute(sql_str)
    conn.commit()
    sql_str="select gid,\"Gl_Code\" from \"Nepal_Glacial_Lake_2001_Revised_v2\" order by gid;"
    curs.execute(sql_str)
    records=curs.fetchall()
    gid=1
    for gid_01,Code_01 in records:
        sql_overlaps="select gid,\"Gl_Code\" from \"Nepal_Glacial_Lake_2009_final\""\
                      +" where st_overlaps(the_geom,(select the_geom from \"Nepal_Glacial_Lake_2001_Revised_v2\" where gid="+str(gid_01)+"));"
        curs.execute(sql_overlaps)
        rows=curs.fetchall()
        if len(rows)>0:
            for gid_09,Code_09 in rows:
                sql_insert="INSERT INTO \"Nepal_Glacial_Lake_Change_2001_to_2009\""\
                            +"(gid_2001,code_01,area_01,class_01,new_class_01,gid_2009,code_09,area_09,class_09,remarks)"\
                            +" select a.gid,a.\"Gl_Code\",a.\"Gl_Area\",a.\"Gl_Class\",new_class,"\
                            +"b.gid,b.\"Gl_Code\",b.\"Gl_Area\",b.\"Gl_Class\",'overlaps_"+str(len(rows))+"'"\
                            +"from \"Nepal_Glacial_Lake_2001_Revised_v2\" a,\"Nepal_Glacial_Lake_2009_final\" b "\
                            +"where a.gid="+str(gid_01)+" and b.gid="+str(gid_09)+";"
                curs.execute(sql_insert)
        else:
            ## check within
            sql_within="select gid,\"Gl_Code\" from \"Nepal_Glacial_Lake_2009_final\""\
                        +" where st_within(the_geom,(select the_geom from \"Nepal_Glacial_Lake_2001_Revised_v2\" where gid="+str(gid_01)+"));"
            curs.execute(sql_within)
            rows_2=curs.fetchall()
            
            if len(rows_2)>0:
                for gid_09,Code_09 in rows_2:
                    sql_insert_1="INSERT INTO \"Nepal_Glacial_Lake_Change_2001_to_2009\""\
                                +"(gid_2001,code_01,area_01,class_01,new_class_01,gid_2009,code_09,area_09,class_09,remarks)"\
                                +" select a.gid,a.\"Gl_Code\",a.\"Gl_Area\",a.\"Gl_Class\",a.new_class,"\
                                +"b.gid,b.\"Gl_Code\",b.\"Gl_Area\",b.\"Gl_Class\",'Split_"+str(len(rows_2))+"'"\
                                +" from \"Nepal_Glacial_Lake_2001_Revised_v2\" a,\"Nepal_Glacial_Lake_2009_final\" b "\
                                +"where a.gid="+str(gid_01)+" and b.gid="+str(gid_09)+";"
                    curs.execute(sql_insert_1)
            else:
                ## check contains
                sql_contains="select gid,\"Gl_Code\" from \"Nepal_Glacial_Lake_2009_final\""\
                            +" where st_contains(the_geom,(select the_geom from \"Nepal_Glacial_Lake_2001_Revised_v2\" where gid="+str(gid_01)+"));"
                curs.execute(sql_contains)
                rows_3=curs.fetchall()
                
                if len(rows_3)>0:
                    for gid_09,Code_09 in rows_3:
                        sql_insert_2="INSERT INTO \"Nepal_Glacial_Lake_Change_2001_to_2009\""\
                                    +"(gid_2001,code_01,area_01,class_01,new_class_01,gid_2009,code_09,area_09,class_09,remarks)"\
                                    +" select a.gid,a.\"Gl_Code\",a.\"Gl_Area\",a.\"Gl_Class\",a.new_class,"\
                                    +"b.gid,b.\"Gl_Code\",b.\"Gl_Area\",b.\"Gl_Class\",'Merge_"+str(len(rows_3))+"'"\
                                    +" from \"Nepal_Glacial_Lake_2001_Revised_v2\" a,\"Nepal_Glacial_Lake_2009_final\" b "\
                                    +"where a.gid="+str(gid_01)+" and b.gid="+str(gid_09)+";"
                        curs.execute(sql_insert_2)
                else:
                    sql_insert_3="INSERT INTO \"Nepal_Glacial_Lake_Change_2001_to_2009\"(gid_2001,code_01,area_01,class_01,new_class_01,remarks)"\
                              +" select gid,\"Gl_Code\",\"Gl_Area\",\"Gl_Class\",new_class,'Dry' "\
                            +" from \"Nepal_Glacial_Lake_2001_Revised_v2\" "\
                            +"where gid="+str(gid_01)+";"
                    curs.execute(sql_insert_3)

    conn.commit()
    gid_list=''
    sql_str="SELECT gid_2009,count(gid_2009) FROM \"Nepal_Glacial_Lake_Change_2001_to_2009\" where gid_2009 is not null group by gid_2009 order by gid_2009;"
    curs.execute(sql_str)    
    records_new=curs.fetchall()
    for gid_2009,count in records_new:
        gid_list=gid_list+','+str(gid_2009)
    gid_list='('+gid_list+')'
    gid_list=gid_list.replace('(,','(')
    sql_insert_4="insert into \"Nepal_Glacial_Lake_Change_2001_to_2009\"(gid_2009,code_09,area_09,class_09,remarks)"\
            +" select gid,\"Gl_Code\",\"Gl_Area\",\"Gl_Class\",'new_lake'"\
            +" from \"Nepal_Glacial_Lake_2009_final\""\
            +" where gid not in "+gid_list+";"
    curs.execute(sql_insert_4)
    sql_update="update \"Nepal_Glacial_Lake_Change_2001_to_2009\" set remarks='Supra_Lake' where class_09='IS' or new_class_01='S';"
    curs.execute(sql_update)
    sql_update_1="update \"Nepal_Glacial_Lake_Change_2001_to_2009\" set change=remarks;"
    curs.execute(sql_update_1)
    ## mark split
    gid_list=''
    sql_select="select gid_2001,count(gid_2001) from \"Nepal_Glacial_Lake_Change_2001_to_2009\" group by gid_2001 having count(gid_2001)>1;"
    curs.execute(sql_select)
    rows_5=curs.fetchall()
    for gid,count in rows_5:
        gid_list=gid_list+','+str(gid)
    gid_list='('+gid_list+')'
    gid_list=gid_list.replace('(,','(')
    sql_update_2="update \"Nepal_Glacial_Lake_Change_2001_to_2009\" set change='Split' where gid_2001 in "+gid_list+';'
    curs.execute(sql_update_2)
    ##mark merge lake
    gid_list=''
    sql_select="select gid_2009,count(gid_2009) from \"Nepal_Glacial_Lake_Change_2001_to_2009\" group by gid_2009 having count(gid_2009)>1;"
    curs.execute(sql_select)
    rows_6=curs.fetchall()
    for gid,count in rows_6:
        gid_list=gid_list+','+str(gid)
    gid_list='('+gid_list+')'
    gid_list=gid_list.replace('(,','(')
    sql_update_3="update \"Nepal_Glacial_Lake_Change_2001_to_2009\" set change='Merge' where gid_2009 in "+gid_list+';'
    curs.execute(sql_update_3)
    sql_update_4="update \"Nepal_Glacial_Lake_Change_2001_to_2009\" set change='Same Lake' where change='Split_1' or change='overlaps_1' or change='Merge_1';"
    curs.execute(sql_update_4)
    conn.commit()
    curs.close()
    conn.close()
    print '---end---'
