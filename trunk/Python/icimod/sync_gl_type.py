#encoding=utf8
#sync data between google kml and postgis for glacier type

###############################################################################
# GPSyncTools
# Author:Wulizong
# Date:11/6/2009
# Description:Using this tools to Sync glacial lakes data between Google Earth and Postgis.
# For the glacial lake only polygon is usfull in the kml file.
# the polygon name store the glacial lake id and description tag used for glacial lake's attirbute
# History:

###############################################################################

import os,string,codecs,unicodedata
from datetime import *
from psycopg2 import connect
from osgeo import ogr
from xml.dom import minidom
import codecs
from types import *

##define global variable
global host,dbname,user,password,table_name,lookup
##---------------------start script----------------------


##Export to kml
def export2kml(host,dbname,user,password,table_name,out_kmlfile,folder_name):   
    print 'Program for export to kml from postgres is  running>>>>>>>>>>>>>>>>'
    
    conn=connect("host="+host+" dbname="+dbname+" user="+user+" password="+password)
    curs=conn.cursor()
    ##init kml object
    impl=minidom.getDOMImplementation()
    dom=impl.createDocument(None,'kml',None)
    root=dom.documentElement
    ns='http://earth.google.com/kml/2.1'
    Document_node=dom.createElement('Document')
    root.appendChild(Document_node)
    Doc_name=dom.createElement('name')
    Document_node.appendChild(Doc_name)
    ##add style
    Style_node=dom.createElement('Style')
    Document_node.appendChild(Style_node)
    Style_node.setAttribute('id','Default_PolyStyle')
    
    LineStyle=dom.createElement('LineStyle')
    Style_node.appendChild(LineStyle)
    color_node=dom.createElement('color')
    LineStyle.appendChild(color_node)
    Text=dom.createTextNode('ff0000ff')
    color_node.appendChild(Text)
    width_node=dom.createElement('width')
    LineStyle.appendChild(width_node)
    Text=dom.createTextNode('1')
    width_node.appendChild(Text)

    PolyStyle=dom.createElement('PolyStyle')
    Style_node.appendChild(PolyStyle)
    color_node=dom.createElement('color')
    PolyStyle.appendChild(color_node)
    Text=dom.createTextNode('ff0000ff')
    color_node.appendChild(Text)
    fill_node=dom.createElement('fill')
    PolyStyle.appendChild(fill_node)
    Text=dom.createTextNode('0')
    fill_node.appendChild(Text)
    outline_node=dom.createElement('outline')
    PolyStyle.appendChild(outline_node)
    Text=dom.createTextNode('1')
    outline_node.appendChild(Text)
    
    
    
    ##get table oid
    sql_str="""select attname from pg_attribute where attrelid=(select oid from pg_class where
relname='"""+table_name+"""') and attnum >-1 order by attnum;"""
    curs.execute(sql_str)
    rows=curs.fetchall()
    attrname=[rec[0] for rec in rows]
    attrname.remove('the_geom')
##    attrname.remove('centroid')
##    attrname.remove('flag_overlap')
##    attrname.remove('flag')
    attr_name=string.join(attrname,',')
    
    sql_str="select distinct "+folder_name+" from "+table_name+';'    
    curs.execute(sql_str)
    rows=curs.fetchall()
    print len(rows)
    flag_list=[rec[0] for rec in rows]    
    for name in flag_list:        
        Folder_node=dom.createElement('Folder')        
        Document_node.appendChild(Folder_node)
        name_node=dom.createElement('name')
        Folder_node.appendChild(name_node)
        Text=dom.createTextNode(str(name))
        name_node.appendChild(Text)
        
        name=name
        print name
        sql_str="select gid,askml(the_geom),"+attr_name+" from "+table_name+" where "+folder_name+"='"+name+"' order by gid;"
        curs.execute(sql_str)
        rows=curs.fetchall()
        for i in range(len(rows)):
            gid=rows[i][0]
            #flag=rows[i][1]            
            kml=rows[i][1]        
            desc_text="""<p align="center"><b><font size="4" color="#0000FF">Attributes</font></b></p><hr>
    <table border="1" width="100%">"""
            for index in range(len(attrname)):
                desc_text=desc_text+'<tr><td width="30%">'+attrname[index]+'</td><td>'+str(rows[i][index+2])+'</td></tr>'
            desc_text=desc_text+'</table><hr><div align="center">Create Time:'+str(date.today())+'</div><p align="center"><font color="#FF0000">&copy; 2009 ICIMOD</font></p>'
                
            Placemark_node=dom.createElement('Placemark')                           
            Folder_node.appendChild(Placemark_node)
            
##            styleUrl_node=dom.createElement('styleUrl')
##            Placemark_node.appendChild(styleUrl_node)
##            Text=dom.createTextNode('#Default_PolyStyle')
##            styleUrl_node.appendChild(Text)
                   
            name_node=dom.createElement('name')
            Placemark_node.appendChild(name_node)
            Text=dom.createTextNode(str(gid))
            name_node.appendChild(Text)
            
##            desc_node=dom.createElement('description')
##            Placemark_node.appendChild(desc_node)
##            Text=dom.createCDATASection(desc_text)
##            desc_node.appendChild(Text)
            
            kml_dom=minidom.parseString(kml)
            kml_node=kml_dom.documentElement
            Placemark_node.appendChild(kml_node)            
     
    
    f=open(out_kmlfile,'w')
    writer=codecs.lookup('utf8')[3](f)
    dom.writexml(writer,encoding='utf8')
    writer.close()
    curs.close()
    conn.close()
    message= out_kmlfile +" is exported"
    return message

if __name__=='__main__':
    ## variale for connect postgre
    host='localhost'
    dbname='glof'
    user='postgres'
    password='glacier'    
    #table_name='hkh_glacier_lakes'
    table_name='hkh_gl_type'
    lake_id='gid'
    attr='gl_type'
    ##define the geosystem code,default value is 4326 (=WGS84)
    srid='4326'
    ## defin the input and output kml file
    kmlfile='F:\KML\gl_type\gl_type.kml'
    out_kmlfile=kmlfile[0:-4]+'_'+string.replace(str(date.today()),':','')+'.kml'
    field_name='gl_type'

    ##
    result=export2kml(host,dbname,user,password,table_name,out_kmlfile,field_name)
    print result
    print "---end---"

