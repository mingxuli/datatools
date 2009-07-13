#coding=utf8
#assign data by location
from psycopg2 import connect

global host,dbname,user,password,table_assign_to,table_assign_from,field_assign_to,field_assign_from
def assign_data():
    conn=connect("host="+host+" dbname="+dbname+" user="+user+" password="+password)
    curs=conn.cursor()
    sql_str="select gid,astext(the_geom) from "+table_assign_to+' order by gid;'
    curs.execute(sql_str)
    rows=curs.fetchall()
    for gid,geom_A in rows:
        print gid
        sql_str="select gid,"+field_assign_from+" from "+table_assign_from+" where st_Within(the_geom,GeomFromText('"+geom_A+"',4326));"
        curs.execute(sql_str)
        rows=curs.fetchall()
        if len(rows)==1:
            field=[field for new_gid,field in rows][0]
            print gid,field
            sql_str="update "+table_assign_to+" set "+field_assign_to+"='"+field+"' where gid="+str(gid)+";"
            curs.execute(sql_str)
    conn.commit()    
    return 'message'
    curs.close()
    conn.close()

if __name__=='__main__':
    host='localhost'
    dbname='glof'
    user='postgres'
    password='glacier'
    table_assign_to='ge_image_footprint'
    field_assign_to='requ_date'
    table_assign_from='ge_image_footprint_label'
    field_assign_from='requ_date'
    result=assign_data()
    
    print '----end-----'
