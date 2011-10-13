#encoding=utf8
import xlrd
import pg
from types import *

if __name__=='__main__':
    conn=pg.connect(host='210.77.68.252',dbname='heihe',user='wlz',passwd='$(^&@(*')
    table_name='\"Heihe_Groundwater_data\"'
    filename=u'D:\dixiashui\地下水\地下水\逐日\甘州区\单井\苗圃(39550035).xls'
    workbook=xlrd.open_workbook(filename)
    month_list=[1,2,3,4,5,6,7,8,9,10,11,12]
    
    # 井名称，编码，海拔高度
    station_code='39550035'    
    station_name='苗圃'
    print station_name,station_code
    
    years=[1988,1989,1990,1991,1992,1993]
    for year in years:    
        print year
        sheet=workbook.sheet_by_name(str(year))        
        elevation=float(sheet.cell_value(2,7))
        #观测日期
        observ_date=[]
        for month in month_list:
            observ_date.append(str(year)+'-'+str(month)+'-'+str(int(sheet.cell_value(5,1))))
            observ_date.append(str(year)+'-'+str(month)+'-'+str(int(sheet.cell_value(6,1))))
            observ_date.append(str(year)+'-'+str(month)+'-'+str(int(sheet.cell_value(7,1))))
            observ_date.append(str(year)+'-'+str(month)+'-'+str(int(sheet.cell_value(8,1))))
            observ_date.append(str(year)+'-'+str(month)+'-'+str(int(sheet.cell_value(9,1))))
            observ_date.append(str(year)+'-'+str(month)+'-'+str(int(sheet.cell_value(10,1))))

        #初始化id
        result=conn.query('select max(id) from \"Heihe_Groundwater_data\"' )
        max_gid=result.getresult()
        max_gid=max_gid[0][0]
        if type(max_gid) is NoneType:
            gid=0
        else:
            gid=max_gid+1
        #埋深    
        rows=[5,6,7,8,9,10]
        cols=[2,3,4,5,6,7,8,10,11,12,13,14]
        Burial_depth=[]
        for i in rows:
            for j in cols:
                value=sheet.cell_value(i,j)
                if value=='':
                    value=-1
                else:
                    value=value            
                Burial_depth.append(value)
        rows=[35,36,37,38,39,40]
        cols=[2,3,4,5,6,7,8,10,11,12,13]
        water_level=[]
        for i in rows:
            for j in cols:
                value2=sheet.cell_value(i,j)
                if value2=='':
                    value2=-1
                else:
                    value2=value2            
                water_level.append(value2)
        #插入
        for i in range(len(Burial_depth)):
            depth=Burial_depth[i]
            date=observ_date[i]
            level=water_level[i]
            fields=[gid,station_code,station_name,elevation,date,depth,level]
            insert_sql='insert into '\
                        +table_name+\
                        " (id,\"Station_Code\",\"Station_Name\",\"Elevation\",\"Observ_Date\",\"Burial_Depth\",\"Water_Level\") values(%d,'%s','%s',%f,'%s',%f,%f)" % tuple(fields)
            #print insert_sql
            conn.query(insert_sql)
            gid=gid+1
    conn.close()
    print 'end' 
