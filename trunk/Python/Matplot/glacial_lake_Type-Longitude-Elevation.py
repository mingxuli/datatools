#encoding=utf8
from psycopg2 import connect
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import string
if __name__=='__main__':
    conn=connect("host=localhost dbname=GGLIS user=postgres password=postgres")
    curs=conn.cursor()
    sql_str="select \"Gl_Area\",\"Gl_Class\",ele_srtm,x(centroid(the_geom)) from \"Nepal_Glacial_Lake_2009_final\";"
    curs.execute(sql_str)
    rows=curs.fetchall()
    fig=plt.figure()
    ax=fig.add_subplot(111)
    
    for area,gl_type,elev,longitude in rows:
        if gl_type=='E(c)':
            ax.scatter(longitude,elev,s=area*500,c='r')
        if gl_type=='E(v)':
            ax.scatter(longitude,elev,s=area*500,c='r')
        if gl_type=='E(o)':
            ax.scatter(longitude,elev,s=area*500,c='r')
        if gl_type=='M(e)':
            ax.scatter(longitude,elev,s=area*500,c='g')
        if gl_type=='M(l)':
            ax.scatter(longitude,elev,s=area*500,c='b')
        if gl_type=='M(lg)':
            ax.scatter(longitude,elev,s=area*500,c='c')
        if gl_type=='M(o)':
            ax.scatter(longitude,elev,s=area*500,c='m')
        if gl_type=='I(s)':
            ax.scatter(longitude,elev,s=area*500,c='y')
        if gl_type=='O':
            ax.scatter(longitude,elev,s=area*500,c='k',fill=False)
    
    ax.grid(True)        
    plt.xlabel('Glacial lake type',fontsize=12)
    plt.ylabel('Elevation(m)',fontsize=12)
    plt.ylim(3000,6000)
    plt.savefig('D:\GLOF\Documents\gl_area-type-longitude-ele.png',dpi=300,origentation='portrait')
    
    plt.show()
    conn.commit() 
    curs.close()
    conn.close()
    print 'end'
