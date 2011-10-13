#coding=utf8
#assign data by location
from psycopg2 import connect

if __name__=='__main__':
    host='localhost'
    dbname='GGLIS'
    user='postgres'
    password='postgres'
    conn=connect("host=localhost dbname=GGLIS user=postgres password=postgres")
    curs=conn.cursor()
    
    sql_str='select gid,sub_basin from \"Nepal_gl_2010\" order by gid;'
    curs.execute(sql_str)
    rows=curs.fetchall()
    for gid,basin_code in rows:
        sql_check='select gid,\"Sub_Basin\" from \"Nepal_SubBasin\"'\
                 ' where st_Within((select centroid(the_geom) from \"Nepal_gl_2010\" where gid='+str(gid)+'), the_geom);'
        curs.execute(sql_check)
        records=curs.fetchall()
        if len(records)==1:
            for new_id,basin1_code in records:
                sql_update="update \"Nepal_gl_2010\" set sub_basin='"+basin1_code+"' where gid="+str(gid)+";"
                curs.execute(sql_update)
            
    conn.commit()    
    curs.close()
    conn.close()
    
    print '----end-----'
