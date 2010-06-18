#encoding=utf8
from psycopg2 import connect
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import string
if __name__=='__main__':
    conn=connect("host=localhost dbname=GGLIS user=postgres password=postgres")
    curs=conn.cursor()
    sql_str="select \"Gl_Area\",\"Gl_Class\",ele_srtm from \"Nepal_Glacial_Lake_2009_final\";"
    curs.execute(sql_str)
    rows=curs.fetchall()
    ind=[1000,2000,3000,4000,5000,6000,7000,8000,9000]
    ticks=['E(c)','E(v)','E(o)','M(e)','M(l)','M(lg)','M(o)','I(s)','O']
    fig=plt.figure()
    ax=fig.add_subplot(111)
    
    for area,gl_type,elev in rows:
        if gl_type=='E(c)':
            ax.scatter(1000,elev,s=area*500,c='r')
        if gl_type=='E(v)':
            ax.scatter(2000,elev,s=area*500,c='r')
        if gl_type=='E(o)':
            ax.scatter(3000,elev,s=area*500,c='r')
        if gl_type=='M(e)':
            ax.scatter(4000,elev,s=area*500,c='g')
        if gl_type=='M(l)':
            ax.scatter(5000,elev,s=area*500,c='b')
        if gl_type=='M(lg)':
            ax.scatter(6000,elev,s=area*500,c='c')
        if gl_type=='M(o)':
            ax.scatter(7000,elev,s=area*500,c='m')
        if gl_type=='I(s)':
            ax.scatter(8000,elev,s=area*500,c='y')
        if gl_type=='O':
            ax.scatter(9000,elev,s=area*500,c='k')
    
    ax.grid(True)        
    plt.xlabel('Glacial lake type',fontsize=12)
    plt.ylabel('Elevation(m)',fontsize=12)
    plt.xticks(ind,ticks,fontsize=11)
    plt.ylim(3000,6000)
    plt.savefig('D:\GLOF\Documents\gl_area_type_ele.png',dpi=300,origentation='portrait')
    
    plt.show()
    conn.commit() 
    curs.close()
    conn.close()
    print 'end'
