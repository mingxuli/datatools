# To change this template, choose Tools | Templates
# and open the template in the editor.
import sys
import os,string,codecs,unicodedata
from psycopg2 import connect



def filter(fields):
    myFields = fields
    for i in [1,2,3,6,7,8,9,10,11,12,13]:
        myFields[i] = myFields[i].replace("'", "\\'")
    return myFields

if __name__ == "__main__":
    conn=connect("host=localhost dbname=GLOF user=postgres password=welcome")
    curs=conn.cursor()
    ##db = pg.DB("GLOF", "192.168.1.101", 5432, None, None, "postgres", "welcome")
    log_file = open('C://TDDownload//allCountries//countriesLog.txt', 'w')
    f=open('C://TDDownload//allCountries//allCountries.txt', 'r')
    i = 0
    for line in f:
        line = line.replace("'","\\'")
        fields = line.split('\t')            
        if len(fields[-5]) == 0: fields[-5] = 0
        if len(fields[-4]) == 0: fields[-4] = 0
        if len(fields[-3]) == 0: fields[-5] = 0
        fields[-1] = fields[-1].strip()
        ##myFields = filter(fields)
        try:
            sql_str="INSERT INTO all_countries (geonameid,city_name,asciiname,alternatenames,latitude,longitude,feature_class,feature_code,country_code,cc2,admin1_code,admin2_code,admin3_code,admin4_code,population,elevation,gtopo30,timezone,modification_date) values ('%s',E'%s',E'%s',E'%s','%s','%s',E'%s',E'%s',E'%s',E'%s',E'%s',E'%s',E'%s',E'%s','%s','%s','%s','%s','%s')" % tuple(fields)
            curs.execute(sql_str)
            conn.commit()
        except Exception:
            print 'error',i
            log_file.write(line)
            
        if i % 10000 == 0: print i
        i += 1
    log_file.close()
    f.close()
    curs.close()
print 'end'
