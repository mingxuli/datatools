#encoding=utf8
#! /usr/bin/python

import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from psycopg2 import connect

def main(a,b,d,c,e):
    horizontalHist = [(v) for (k,v) in c.iteritems()]
    verticalHist = [(math.log(v)+80) for (k, v) in e.iteritems()]
    matplotlib.rcParams['axes.unicode_minus'] = False
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(a[0], b[0], s=d[0], alpha=0.75,label='area < 0.1',color='c')
    ax.scatter(a[1], b[1], s=d[1], alpha=0.75, label='0.1 < area < 0.5', color='b')
    ax.scatter(a[2], b[2], s=d[2], alpha=0.75, label='0.5 < area < 1', color='m')
    ax.scatter(a[3], b[3], s=d[3], alpha=0.75, label='area > 1', color='r')
    ax.bar(c.keys(), horizontalHist,width=0.5,label='Horizontal area',alpha=0.2,color='b')
    ax.barh(e.keys(), verticalHist, height=500, label='Vertical area',alpha=0.2,color='m')
    ax.set_xlim(80, 90)
    ax.set_ylim(0,6000)
    ax.legend(loc = 5)
    ax.grid(True)
    plt.xlabel("longitude")
    plt.ylabel("altitude")
    plt.show()

def calHorizontalArea(x,area,c,factor=100):
    for i in range(20):        
        from_num = 80+0.5*i
        to_num = from_num + 0.5
        if x > from_num and x < to_num:
            if c.has_key(from_num):
                c[from_num] = c.get(from_num)+area*factor
            else:
                c[from_num] = area*factor

def calVerticalArea(x, area, c, factor=1):
    for i in range(8):
        from_num = 2000 + 500 * i
        to_num = from_num + 500
        if x > from_num and x < to_num:            
            if c.has_key(from_num):
                c[from_num] = c.get(from_num) + area * factor
            else:
                c[from_num] = area * factor


if __name__ == "__main__":
    conn=connect("host=localhost dbname=GGLIS user= postgres password=postgres")
    curs=conn.cursor()
    sql_str="select \"Gl_Area\",x(centroid(the_geom)) from \"Nepal_Glacial_Lake_2009_final\";"
    curs.execute(sql_str)
    records=curs.fetchall()
    conn.commit() 
    curs.close()
    conn.close()
    area =[ r[0] for r in records]
    longitude=[ r[1] for r in records]
    n, bins, patches = plt.hist(area, 500, normed=1, facecolor='g', alpha=0.75)
    plt.show()
    win.show_all()
    gtk.main()


    #main(a,b,d,horizontalC,verticalC)
