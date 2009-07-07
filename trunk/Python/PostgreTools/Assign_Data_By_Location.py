#coding=utf8
#assign data by location
from psycopg2 import connect

global host,dbname,user,password,table_assign_to,table_assign_from,field_assign_to,field_assign_from
def assign_data():
    conn=connect("host="+host+" dbname="+dbname+" user="+user+" password="+password)
    curs=conn.cursor()
    sql_str="select gid,"+field_assign_to+",the_geom from "+table_assign_to+';'
    curs.execute(sql_str)
    rows=curs.fetchall()
    for gid,field_to,geom_A in rows:
        sql_str="select gid,"+field_assign_from+",the_geom from "+table_assign_from+" where st_Within("");"
        
    return 'message'
    

if __name__=='__main__':
    host='localhost'
    dbname='glof'
    user='postgres'
    password='glacier'
    table_assign_to='ge_image_footprint'
    field_assign_to='requ_date'
    table_assign_from='ge_image_footprint_label'
    field_assign_from=''
    result=assign_data()
    
    print '----end-----'
