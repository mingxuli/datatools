#encoding=utf8
#! /usr/bin/python
from psycopg2 import connect
from numpy import random,arange
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
def bar_chart(records,size_level):
    Area=[rec[0] for  rec in records]
    Gl_Type=[rec[1] for rec in records]
    Total_Area=sum(Area)
    Total_Number=len(Area)
    max_area=max(Area)

    O_Area_level=[]
    O_Count_level=[]
    E_Area_level=[]
    E_Count_level=[]
    Is_Area_level=[]
    Is_Count_level=[]
    Me_Area_level=[]
    Me_Count_level=[]
    Ml_Area_level=[]
    Ml_Count_level=[]
    Mlg_Area_level=[]
    Mlg_Count_level=[]
    Mo_Area_level=[]
    Mo_Count_level=[]
    O_Area_level=[]
    O_Count_level=[]
    plt.figure(figsize=(14,12))
    for value in size_level:
        temp_area=sum([a for a,b in records if a<value and b=='O'])/Total_Area*100
        temp_count=sum([1 for a,b in records if a<value and b=='O'])/float(Total_Number)*100
        O_Area_level.append(temp_area)
        O_Count_level.append(temp_count)
        
        temp_area=sum([a for a,b in records if a<value and (b=='E(c)' or b=='E(v)' or b=='E(o)')])/Total_Area*100
        temp_count=sum([1 for a,b in records if a<value and (b=='E(c)' or b=='E(v)' or b=='E(o)')])/float(Total_Number)*100
        E_Area_level.append(temp_area)
        E_Count_level.append(temp_count)

        temp_area=sum([a for a,b in records if a<value and b=='I(s)'])/Total_Area*100
        temp_count=sum([1 for a,b in records if a<value and b=='I(s)'])/float(Total_Number)*100
        Is_Area_level.append(temp_area)
        Is_Count_level.append(temp_count)

        temp_area=sum([a for a,b in records if a<value and b=='M(e)'])/Total_Area*100
        temp_count=sum([1 for a,b in records if a<value and b=='M(e)'])/float(Total_Number)*100
        Me_Area_level.append(temp_area)
        Me_Count_level.append(temp_count)

        temp_area=sum([a for a,b in records if a<value and b=='M(l)'])/Total_Area*100
        temp_count=sum([1 for a,b in records if a<value and b=='M(l)'])/float(Total_Number)*100
        Ml_Area_level.append(temp_area)
        Ml_Count_level.append(temp_count)

        temp_area=sum([a for a,b in records if a<value and b=='M(lg)'])/Total_Area*100
        temp_count=sum([1 for a,b in records if a<value and b=='M(lg)'])/float(Total_Number)*100
        Mlg_Area_level.append(temp_area)
        Mlg_Count_level.append(temp_count)

        temp_area=sum([a for a,b in records if a<value and b=='M(o)'])/Total_Area*100
        temp_count=sum([1 for a,b in records if a<value and b=='M(o)'])/float(Total_Number)*100
        Mo_Area_level.append(temp_area)
        Mo_Count_level.append(temp_count)
        
    size_level.append(max_area)
    O_Area_level.append(sum([a for a,b in records if b=='O'])/Total_Area*100)
    O_Count_level.append(sum([1 for a,b in records if b=='O'])/float(Total_Number)*100)
    
    E_Area_level.append(sum([a for a,b in records if b=='E(c)' or b=='E(v)' or b=='E(o)'])/Total_Area*100)
    E_Count_level.append(sum([1 for a,b in records if b=='E(c)' or b=='E(v)' or b=='E(o)'])/float(Total_Number)*100)
    
    Is_Area_level.append(sum([a for a,b in records if b=='I(s)'])/Total_Area*100)
    Is_Count_level.append(sum([1 for a,b in records if b=='I(s)'])/float(Total_Number)*100)

    Me_Area_level.append(sum([a for a,b in records if b=='M(e)'])/Total_Area*100)
    Me_Count_level.append(sum([1 for a,b in records if b=='M(e)'])/float(Total_Number)*100)

    Ml_Area_level.append(sum([a for a,b in records if b=='M(l)'])/Total_Area*100)
    Ml_Count_level.append(sum([1 for a,b in records if b=='M(l)'])/float(Total_Number)*100)
    
    Mlg_Area_level.append(sum([a for a,b in records if b=='M(lg)'])/Total_Area*100)
    Mlg_Count_level.append(sum([1 for a,b in records if b=='M(lg)'])/float(Total_Number)*100)
    
    Mo_Area_level.append(sum([a for a,b in records if b=='M(o)'])/Total_Area*100)
    Mo_Count_level.append(sum([1 for a,b in records if b=='M(o)'])/float(Total_Number)*100)
    
    ind=np.arange(len(size_level))
    width = 0.9
    
    plt.subplot(211)
    # Supra Glacial Lake
    Area_level=Is_Area_level    
    bar_Is_1=plt.bar(ind,Area_level,width,color='b')
    #Glacial Erosion Lake
    bottom_area=Area_level    
    Area_level=E_Area_level    
    bar_E_1=plt.bar(ind,Area_level,width,bottom_area,color='r')    
    #Other Moraine Dammed lake
    bottom_area=[bottom_area[i]+Area_level[i] for i in range(len(Area_level))]   
    Area_level=Mo_Area_level    
    bar_Mo_1=plt.bar(ind,Area_level,width,bottom_area,color='m')
    #End Moraine Dammed lake
    bottom_area=[bottom_area[i]+Area_level[i] for i in range(len(Area_level))]    
    Area_level=Me_Area_level    
    bar_Me_1=plt.bar(ind,Area_level,width,bottom_area,color='y')
    #Lateral Moraine Dammed Lake
    bottom_area=[bottom_area[i]+Area_level[i] for i in range(len(Area_level))]    
    Area_level=Ml_Area_level    
    bar_Ml_1=plt.bar(ind,Area_level,width,bottom_area,color='g')
    #Glacier with Lateral Moraine Dammed Lake
    bottom_area=[bottom_area[i]+Area_level[i] for i in range(len(Area_level))]    
    Area_level=Mlg_Area_level    
    bar_Mlg_1=plt.bar(ind,Area_level,width,bottom_area,color='c')
    #Non-Glaial Lake
    bottom_area=[bottom_area[i]+Area_level[i] for i in range(len(Area_level))]    
    Area_level=O_Area_level    
    bar_O_1=plt.bar(ind,Area_level,width,bottom_area,color='k',edgecolor='r')
    #
    plt.xlabel('Glacial Lake Area($km^2$)')
    plt.ylabel('Total Glacial Lake Area(%)')
    plt.xticks(ind+1,size_level)    
    plt.text(width/2.0,90,'Glacial Lake Area:'+str(Total_Area)+'$km^2$',ha='left', va='bottom')    
    
    
    plt.subplot(212)
    # Supra Glacial Lake    
    Count_level=Is_Count_level
    bar_Is_2=plt.bar(ind,Count_level,width,color='b')
    #Glacial Erosion Lake    
    bottom_count=Count_level    
    Count_level=E_Count_level
    bar_E_2=plt.bar(ind,Count_level,width,bottom_count,color='r')    
    #Other Moraine Dammed lake    
    bottom_count=[bottom_count[i]+Count_level[i] for i in range(len(Count_level))]    
    Count_level=Mo_Count_level
    bar_Eo_2=plt.bar(ind,Count_level,width,bottom_count,color='m')
    #End Moraine Dammed lake
    bottom_area=[bottom_area[i]+Area_level[i] for i in range(len(Area_level))]
    bottom_count=[bottom_count[i]+Count_level[i] for i in range(len(Count_level))]
    Area_level=Me_Area_level
    Count_level=Me_Count_level
    bar_Me_2=plt.bar(ind,Count_level,width,bottom_count,color='y')
    #Lateral Moraine Dammed Lake
    bottom_area=[bottom_area[i]+Area_level[i] for i in range(len(Area_level))]
    bottom_count=[bottom_count[i]+Count_level[i] for i in range(len(Count_level))]
    Area_level=Ml_Area_level
    Count_level=Ml_Count_level
    bar_Ml_2=plt.bar(ind,Count_level,width,bottom_count,color='g')
    #Glacier with Lateral Moraine Dammed Lake
    bottom_area=[bottom_area[i]+Area_level[i] for i in range(len(Area_level))]
    bottom_count=[bottom_count[i]+Count_level[i] for i in range(len(Count_level))]
    Area_level=Mlg_Area_level
    Count_level=Mlg_Count_level
    bar_Mlg_2=plt.bar(ind,Count_level,width,bottom_count,color='c')
    #Non-Glaial Lake
    bottom_area=[bottom_area[i]+Area_level[i] for i in range(len(Area_level))]
    bottom_count=[bottom_count[i]+Count_level[i] for i in range(len(Count_level))]
    Area_level=O_Area_level
    Count_level=O_Count_level
    bar_O_2=plt.bar(ind,Count_level,width,bottom_count,color='k',edgecolor='r')
    #    
    plt.xlabel('Glacial Lake Area($km^2$)')
    plt.ylabel('Total Glacial Lake Number(%)')
    plt.xticks(ind+1,size_level)    
    plt.text(width/2.0,90,'Glacial Lake Number:'+str(Total_Number),ha='left', va='bottom')

    plt.legend((bar_Is_1[0],\
                bar_E_1[0],\
                bar_Mo_1[0],\
                bar_Me_1[0],\
                bar_Ml_1[0],\
                bar_Mlg_1[0],\
                bar_O_1[0],),\
               ('Supra-glacial lake',\
                'Glacier erosion lake',\
                'Other moraine dammed lake',\
                'End moraine dammed lake',\
                'Lateral moraine dammed lake',\
                'Glacier with moraine dammed lake',\
                'Non-glacial lake'),\
               loc="upper left",ncol=3,bbox_to_anchor = (-0.05,2.48),markerscale=0.5)
    plt.savefig('D:\\GLOF\\Documents\\glacial_lake_size_level.png',dpi=300)
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
    size_level=[0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.6,0.7,0.8,0.9,1.0]   
    # plot
    bar_chart(rows,size_level)
    #histograme(area,100)    
    print 'end'
