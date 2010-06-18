#encoding=utf8
#! /usr/bin/python
from psycopg2 import connect
from numpy import random,arange
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import string
def pie_chart(Records):
    Area=[rec[0] for rec in Records]
    Gl_Type=[rec[1] for rec in Records]
    Total_Area=sum(Area)
    Total_Number=len(Area)
    Area_Min=min(Area)
    Area_Max=max(Area)
    
    colors=('b', 'g', 'r', 'c', 'm', 'y', 'k')
    labels_legend=('Glacial ersion lake', 'End morain dammed lake', 'Lateral moraine dammed lake', 'glacier with lateral moraine dammed lake',\
            'Other moraine dammed lake', 'Surpa-glacial lake', 'Non-glacial lake')
    Area_Type_E=sum([a for a,b in Records if b=='E(o)' or b=='E(c)' or b=='E(v)'])
    Area_Type_Me=sum([a for a,b in Records if b=='M(e)'])
    Area_Type_Ml=sum([a for a,b in Records if b=='M(l)'])
    Area_Type_Mlg=sum([a for a,b in Records if b=='M(lg)'])
    Area_Type_Mo=sum([a for a,b in Records if b=='M(o)'])
    Area_Type_Is=sum([a for a,b in Records if b=='I(s)'])
    Area_Type_O=sum([a for a,b in Records if b=='O'])
    #Glacial lake Number
    Count_Type_E=sum([1 for a,b in Records if b=='E(o)' or b=='E(c)' or b=='E(v)'])
    Count_Type_Me=sum([1 for a,b in Records if b=='M(e)'])
    Count_Type_Ml=sum([1 for a,b in Records if b=='M(l)'])
    Count_Type_Mlg=sum([1 for a,b in Records if b=='M(lg)'])
    Count_Type_Mo=sum([1 for a,b in Records if b=='M(o)'])
    Count_Type_Is=sum([1 for a,b in Records if b=='I(s)'])
    Count_Type_O=sum([1 for a,b in Records if b=='O'])

    Area_array=[Area_Type_E,Area_Type_Me,Area_Type_Ml,Area_Type_Mlg,Area_Type_Mo,Area_Type_Is,Area_Type_O]
    Count_array=[Count_Type_E,Count_Type_Me,Count_Type_Ml,Count_Type_Mlg,Count_Type_Mo,Count_Type_Is,Count_Type_O]
 
    plt.subplot(121)
    pie_1=plt.pie(Area_array,colors=colors,labels=Area_array,shadow=True,labeldistance=1.1)
    plt.xlabel('A. Glacial Lake Area($km^2$)',fontsize=14)
    plt.legend(pie_1[0],labels_legend,loc="upper left",ncol=3,bbox_to_anchor=[0,1.08])

    plt.subplot(122)
    pie_2=plt.pie(Count_array,colors=colors,labels=Count_array,shadow=True,labeldistance=1.1)
    plt.xlabel('B. Glacial Lake Number',fontsize=14)
    
    

    plt.show()

        
    
if __name__ == "__main__":
    conn=connect("host=localhost dbname=GGLIS user=postgres password=postgres")
    curs=conn.cursor()
    sql_str="select \"Gl_Area\",\"Gl_Class\" from \"Nepal_Glacial_Lake_2009_final\";"
    curs.execute(sql_str)
    rows=curs.fetchall()
    conn.commit() 
    curs.close()
    conn.close()
    print len(rows) 
    Area=[rec[0] for  rec in rows]
    Gl_Type=[rec[1] for rec in rows]
    
    pie_chart(rows) 
    print 'end'
