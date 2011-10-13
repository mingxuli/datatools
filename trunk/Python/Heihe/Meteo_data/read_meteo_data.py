#encoding=utf8
#read meteo data
import glob
import pg

print 'start runing...'

filelist=glob.glob("D:\\TDDOWNLOAD\\1951-2009\\*.txt")
station_code='52323'
var_code='V10201'
var_name="\"Pressure_Max\""
conn=pg.connect(host='210.77.68.252',dbname='heihe',user='wlz',passwd='$(^&@(*')
year_list=[]

date_list=[]
var_list=[]
for filename in filelist:
    f=open(filename,'r')
    i=0
    for line in f:
        if i==0:
            header=line.split('\t')
            index=0
            for j in range(len(header)):
                if header[j]==var_code:
                    index=j
        if i>0 and index>0:
            fields=line.split(',')
            if fields[0]==station_code:
                year_list.append(fields[1])
                date_list.append(fields[1]+'-'+fields[2]+'-'+fields[3])
                var_list.append(fields[index])
            
        i=i+1
print station_code
for i in range(len(date_list)):
    
    sql_str="select %s from \"Heihe_Meteorological_Data_daily\" where \"Station_Code\"='%s' and \"Obs_Date\"='%s'" % (var_name,station_code,date_list[i])
    
    #if float(var_list[i])-float(conn.query(sql_str).getresult()[0][0])>1:  
    #print date_list[i],var_list[i],conn.query(sql_str).getresult()[0][0]
    if int(year_list[i])<2000:
        update_sql="update \"Heihe_Meteorological_Data_daily\" set %s=%s where \"Station_Code\"='%s' and \"Obs_Date\"='%s' " % (var_name,var_list[i],station_code,date_list[i])
        conn.query(update_sql)
conn.close()
print 'end'

##                   
##  "Pressure_Avg" real, -- 平均气压
##  "Pressure_Max" real, -- 最高气压
##  "Pressure_Min" real, -- 最低气压
##  "Temperature_Avg" real, -- 平均气温
##  "Temperature_Max" real, -- 最高气温
##  "Temperature_Miin" real, -- 最低气温
##  "Humidity_Avg" real, -- 平均相对湿度
##  "Humidity_Min" real, -- 最小相对湿度
##  "Precipitation_Sum" real, -- 20-20时降水量
##  "Wind_Speed_Avg" real, -- 平均风速
##  "Wind_Speed_Max" real, -- 最大风速（10分钟平均风速）
##  "Max_Speed_Direction" real, -- 最大风速的风向
##  "Wind_Speed_Maximum" real, -- 极大风速
##  "Maximum_Speed_Direction" real, -- 极大风速的风向
##  "Sunlight" real, -- 日照时数
##  "Julian_Day" integer,
##  "DOY" integer,

## v01000 V04001 V04002 V04003 V10201 V10202 V12001 V12052 V12053 V13003 V13007 V13201 V11002 V11042 V11212 V11041 V11043 V14032 V10004 
## 台站 年 月 日 日最高本站气压 日最低本站气压 平均气温 日最高气温 日最低气温 平均相对湿度 最小相对湿度 20-20时降水量 平均风速 最大风速(10分钟平均风速) 最大风速的风向 极大风速 极大风速的风向 日照时数 平均本站气压 

