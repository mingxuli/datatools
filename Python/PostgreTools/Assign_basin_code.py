#coding=utf8
#assign data by location
from psycopg2 import connect

if __name__=='__main__':
    host='localhost'
    dbname='GGLIS'
    user='postgres'
    password='postgres'
    table_assign_to='\"HKH_Glacial_Lakes_final\"'
    field_assign_to='\"Basin_Code\"'
    table_assign_from='\"HKH_Basin_Pfaf_v3_poly\"'
    field_assign_from='lv3_code'
    conn=connect("host=localhost dbname=GGLIS user=postgres password=postgres")
    curs=conn.cursor()
    sql_str='select gid,\"Basin_Code\" from \"HKH_Glacial_Lakes_final\" order by gid;'
    curs.execute(sql_str)
    rows=curs.fetchall()
    for gid,basin_code in rows:
        sql_check='select gid,lv3_code from \"HKH_Basin_Pfaf_v3_poly\"'\
                 ' where st_Within((select centroid(the_geom) from \"HKH_Glacial_Lakes_final\" where gid='+str(gid)+'), the_geom);'
        curs.execute(sql_check)
        records=curs.fetchall()
        if len(records)==1:
            for new_id,lv3_code in records:
                sql_update="update \"HKH_Glacial_Lakes_final\" set \"Basin_Code\"='"+lv3_code+"' where gid="+str(gid)+";"
                curs.execute(sql_update)
            
    conn.commit()    
    curs.close()
    conn.close()
    
    print '----end-----'
