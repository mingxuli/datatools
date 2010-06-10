#encoding=utf8
#! /usr/bin/python

import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from psycopg2 import connect
from string import *

if __name__ == "__main__":
    conn=connect("host=localhost dbname=GGLIS user= postgres password=postgres")
    curs=conn.cursor()
    sql_str="select gid,astext(the_geom) from \"Nepal_SubBasin_line\";"
    curs.execute(sql_str)
    records=curs.fetchall()
    coors_x=[]
    coors_y=[]
    for gid,wkt in records:
        wkt=wkt.replace('LINESTRING','')
        wkt=wkt.replace('(','')
        wkt=wkt.replace(')','')
        wkt=wkt.split(',')
        wkt=[rec.split(' ') for rec in wkt]

        x_coor=[float(rec[0]) for rec in wkt]
        y_coor=[float(rec[1]) for rec in wkt]
        coors_x.append(x_coor)
        coors_y.append(y_coor)
        
     

    sql_str="select \"Sub_Basin\",sum(\"Gl_Area\"),avg(\"Gl_Area\")"\
             " from \"Nepal_Glacial_Lake_2009_final\" group by \"Sub_Basin\" order by \"Sub_Basin\";"
    curs.execute(sql_str)
    records=curs.fetchall()
    Sub_Basin=[r[0] for r in records]
    Area=[r[1]*10 for r in records]
    points_x=[]
    points_y=[]
    for name in Sub_Basin:
        sql_str="select x(centroid(the_geom)),y(centroid(the_geom)) from \"Nepal_SubBasin\" where \"Sub_Basin\"='"+name+"';"   
        curs.execute(sql_str)
        records=curs.fetchall()
        points_x.append(records[0][0])
        points_y.append(records[0][1])
    plt.subplot(421)
    for i in range(len(coors_x)):        
        plt.plot(coors_x[i],coors_y[i],color='g')
    plt.scatter(points_x,points_y,s=Area,marker='o',c='r')
    plt.xlabel('longitude')
    plt.ylabel('latitude')
    plt.text(80.5,26.2,'a. All Type',fontsize=12)
    plt.scatter(86,29.5,s=20,marker='o',c='r')
    plt.text(86.2,29.4,'Total area')
    #Glacial erosion lake
    sql_str="select \"Sub_Basin\",sum(\"Gl_Area\"),avg(\"Gl_Area\")"\
             " from \"Nepal_Glacial_Lake_2009_final\" where \"Gl_Class\"='E(c)' or \"Gl_Class\"='E(v)' or \"Gl_Class\"='E(o)' group by \"Sub_Basin\" order by \"Sub_Basin\";"
    curs.execute(sql_str)
    records=curs.fetchall()
    Sub_Basin=[r[0] for r in records]
    Area=[r[1]*10 for r in records]
    points_x=[]
    points_y=[]
    for name in Sub_Basin:
        sql_str="select x(centroid(the_geom)),y(centroid(the_geom)) from \"Nepal_SubBasin\" where \"Sub_Basin\"='"+name+"';"   
        curs.execute(sql_str)
        records=curs.fetchall()
        points_x.append(records[0][0])
        points_y.append(records[0][1])
    plt.subplot(422)
    for i in range(len(coors_x)):        
        plt.plot(coors_x[i],coors_y[i],color='g')
    plt.scatter(points_x,points_y,s=Area,marker='o',c='r')
    plt.xlabel('longitude')
    plt.ylabel('latitude')
    plt.text(80.5,26.2,'b. Glacial erosion lake',fontsize=12)
    plt.scatter(86,29.5,s=20,marker='o',c='r')
    plt.text(86.2,29.4,'Total area')
    
    #End moraine dammed lake
    sql_str="select \"Sub_Basin\",sum(\"Gl_Area\"),avg(\"Gl_Area\")"\
             " from \"Nepal_Glacial_Lake_2009_final\" where \"Gl_Class\"='M(e)' group by \"Sub_Basin\" order by \"Sub_Basin\";"
    curs.execute(sql_str)
    records=curs.fetchall()
    Sub_Basin=[r[0] for r in records]
    Area=[r[1]*10 for r in records]
    points_x=[]
    points_y=[]
    for name in Sub_Basin:
        sql_str="select x(centroid(the_geom)),y(centroid(the_geom)) from \"Nepal_SubBasin\" where \"Sub_Basin\"='"+name+"';"   
        curs.execute(sql_str)
        records=curs.fetchall()
        points_x.append(records[0][0])
        points_y.append(records[0][1])
    plt.subplot(423)
    for i in range(len(coors_x)):        
        plt.plot(coors_x[i],coors_y[i],color='g')
    plt.scatter(points_x,points_y,s=Area,marker='o',c='r')
    plt.xlabel('longitude')
    plt.ylabel('latitude')
    plt.text(80.5,26.2,'c. End moraine dammed lake',fontsize=12)
    plt.scatter(86,29.5,s=20,marker='o',c='r')
    plt.text(86.2,29.4,'Total area')

    #lateral moraine dammed lake
    sql_str="select \"Sub_Basin\",sum(\"Gl_Area\"),avg(\"Gl_Area\")"\
             " from \"Nepal_Glacial_Lake_2009_final\" where \"Gl_Class\"='M(l)' group by \"Sub_Basin\" order by \"Sub_Basin\";"
    curs.execute(sql_str)
    records=curs.fetchall()
    Sub_Basin=[r[0] for r in records]
    Area=[r[1]*10 for r in records]
    points_x=[]
    points_y=[]
    for name in Sub_Basin:
        sql_str="select x(centroid(the_geom)),y(centroid(the_geom)) from \"Nepal_SubBasin\" where \"Sub_Basin\"='"+name+"';"   
        curs.execute(sql_str)
        records=curs.fetchall()
        points_x.append(records[0][0])
        points_y.append(records[0][1])
    plt.subplot(424)
    for i in range(len(coors_x)):        
        plt.plot(coors_x[i],coors_y[i],color='g')
    plt.scatter(points_x,points_y,s=Area,marker='o',c='r')
    plt.xlabel('longitude')
    plt.ylabel('latitude')
    plt.text(80.5,26.2,'d. Lateral moraine dammed lake',fontsize=12)
    plt.scatter(86,29.5,s=20,marker='o',c='r')
    plt.text(86.2,29.4,'Total area')
    #Glacier with lateral moraine dammed lake
    sql_str="select \"Sub_Basin\",sum(\"Gl_Area\"),avg(\"Gl_Area\")"\
             " from \"Nepal_Glacial_Lake_2009_final\" where \"Gl_Class\"='M(lg)' group by \"Sub_Basin\" order by \"Sub_Basin\";"
    curs.execute(sql_str)
    records=curs.fetchall()
    Sub_Basin=[r[0] for r in records]
    Area=[r[1]*10 for r in records]
    points_x=[]
    points_y=[]
    for name in Sub_Basin:
        sql_str="select x(centroid(the_geom)),y(centroid(the_geom)) from \"Nepal_SubBasin\" where \"Sub_Basin\"='"+name+"';"   
        curs.execute(sql_str)
        records=curs.fetchall()
        points_x.append(records[0][0])
        points_y.append(records[0][1])
    plt.subplot(425)
    for i in range(len(coors_x)):        
        plt.plot(coors_x[i],coors_y[i],color='g')
    plt.scatter(points_x,points_y,s=Area,marker='o',c='r')
    plt.xlabel('longitude')
    plt.ylabel('latitude')
    plt.text(80.5,26.2,'e. Glacier with lateral moraine dammed lake',fontsize=12)
    plt.scatter(86,29.5,s=20,marker='o',c='r')
    plt.text(86.2,29.4,'Total area')
    #Other moraine dammed lake
    sql_str="select \"Sub_Basin\",sum(\"Gl_Area\"),avg(\"Gl_Area\")"\
             " from \"Nepal_Glacial_Lake_2009_final\" where \"Gl_Class\"='M(o)' group by \"Sub_Basin\" order by \"Sub_Basin\";"
    curs.execute(sql_str)
    records=curs.fetchall()
    Sub_Basin=[r[0] for r in records]
    Area=[r[1]*10 for r in records]
    points_x=[]
    points_y=[]
    for name in Sub_Basin:
        sql_str="select x(centroid(the_geom)),y(centroid(the_geom)) from \"Nepal_SubBasin\" where \"Sub_Basin\"='"+name+"';"   
        curs.execute(sql_str)
        records=curs.fetchall()
        points_x.append(records[0][0])
        points_y.append(records[0][1])
    plt.subplot(426)
    for i in range(len(coors_x)):        
        plt.plot(coors_x[i],coors_y[i],color='g')
    plt.scatter(points_x,points_y,s=Area,marker='o',c='r')
    plt.xlabel('longitude')
    plt.ylabel('latitude')
    plt.text(80.5,26.2,'f. Other moraine dammed lake',fontsize=12)
    plt.scatter(86,29.5,s=20,marker='o',c='r')
    plt.text(86.2,29.4,'Total area')
    #Supra-glacial lake
    sql_str="select \"Sub_Basin\",sum(\"Gl_Area\"),avg(\"Gl_Area\")"\
             " from \"Nepal_Glacial_Lake_2009_final\" where \"Gl_Class\"='I(s)' group by \"Sub_Basin\" order by \"Sub_Basin\";"
    curs.execute(sql_str)
    records=curs.fetchall()
    Sub_Basin=[r[0] for r in records]
    Area=[r[1]*10 for r in records]
    points_x=[]
    points_y=[]
    for name in Sub_Basin:
        sql_str="select x(centroid(the_geom)),y(centroid(the_geom)) from \"Nepal_SubBasin\" where \"Sub_Basin\"='"+name+"';"   
        curs.execute(sql_str)
        records=curs.fetchall()
        points_x.append(records[0][0])
        points_y.append(records[0][1])
    plt.subplot(427)
    for i in range(len(coors_x)):        
        plt.plot(coors_x[i],coors_y[i],color='g')
    plt.scatter(points_x,points_y,s=Area,marker='o',c='r')
    plt.xlabel('longitude')
    plt.ylabel('latitude')
    plt.text(80.5,26.2,'g. Supra-glacial lake',fontsize=12)
    plt.scatter(86,29.5,s=20,marker='o',c='r')
    plt.text(86.2,29.4,'Total area')
    #Non-glacial lake
    sql_str="select \"Sub_Basin\",sum(\"Gl_Area\"),avg(\"Gl_Area\")"\
             " from \"Nepal_Glacial_Lake_2009_final\" where \"Gl_Class\"='O' group by \"Sub_Basin\" order by \"Sub_Basin\";"
    curs.execute(sql_str)
    records=curs.fetchall()
    Sub_Basin=[r[0] for r in records]
    Area=[r[1]*10 for r in records]
    points_x=[]
    points_y=[]
    for name in Sub_Basin:
        sql_str="select x(centroid(the_geom)),y(centroid(the_geom)) from \"Nepal_SubBasin\" where \"Sub_Basin\"='"+name+"';"   
        curs.execute(sql_str)
        records=curs.fetchall()
        points_x.append(records[0][0])
        points_y.append(records[0][1])
    plt.subplot(428)
    for i in range(len(coors_x)):        
        plt.plot(coors_x[i],coors_y[i],color='g')
    plt.scatter(points_x,points_y,s=Area,marker='o',c='r')
    plt.xlabel('longitude')
    plt.ylabel('latitude')
    plt.text(80.5,26.2,'h. Non-glacial lake',fontsize=12)
    plt.scatter(86,29.5,s=20,marker='o',c='r')
    plt.text(86.2,29.4,'Total area')
    
      
   

    
    conn.commit() 
    curs.close()
    conn.close()    

    
    plt.show()



    print 'end'
