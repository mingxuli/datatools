#encoding=utf8
#! /usr/bin/python
from psycopg2 import connect
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import string
def histograme(area,bins):
    bins=50
    plt.hist(area, bins, normed=1, facecolor='g', alpha=0.75)
    plt.title('Histogram of Glacial Lake Size',fontsize=14,fontweight='bold')    
    plt.xlabel('Glacial Lake Area($km^2$)')
    plt.ylabel('Probability')
    plt.show()
def bar_chart(area,size_level):
    area_min=min(area)    
    area_max=max(area)
    area_level=[]
    lower_area=area_min
    for level in size_level:
        temp_area=[a for a in area if a>lower_area and a<level]
        print sum(temp_area)
        lower_area=level
        
    
if __name__ == "__main__":
    conn=connect("host=localhost dbname=GGLIS user=postgres password=postgres")
    curs=conn.cursor()
    sql_str="select gid,\"Gl_Area\" from \"Nepal_Glacial_Lake_2009_final\";"
    curs.execute(sql_str)
    rows=curs.fetchall()
    conn.commit() 
    curs.close()
    conn.close()
    # plot 
    area=[rec[1] for  rec in rows]
    size_level=[0,001,0.01,0.02,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1,0.15,0.2,0.5,1,2]
    bar_chart(area,size_level)
    #histograme(area,100)
    print 'end'
