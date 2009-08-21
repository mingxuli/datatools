#encoding=utf8
#convert kml to esri generate formate

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
##Import to database
def import2pg(kmlfile):
    print 'Program for import kml to postgres is  running>>>>>>>>>>>>>>>>'
    conn=connect("host="+host+" dbname="+dbname+" user="+user+" password="+password)
    curs=conn.cursor()
    sql_str="select gid from "+table_name+' order by gid;'
    curs.execute(sql_str)
    rows=curs.fetchall()
    print '    Found ',str(len(rows)),' records in database.'
    if len(rows)>0:
        gid_list=[s[0] for s in rows]
        max_gid=max(gid_list)
    else:
        max_gid=0
        gid_list=[]

        
    duplicate_list=[] ## use to store duplicate geomery gid
    dom=minidom.parse(kmlfile)
    root=dom.documentElement
    Placemark_List=root.getElementsByTagName('Placemark')
    print '    ',len(Placemark_List),' Placemarks in kmlfile'
    count_existed=0
    count_new=0
    count_overlap=0
    count_tobedel=0
    if Placemark_List.length==0:
        print '    no data in this kml file!' 
    else:
        for Placemark in Placemark_List:
            name_list=Placemark.getElementsByTagName('name')
            name=name_list[0].firstChild.data
            name=string.replace(name,'_',' ')           
            name=(lookup.encode(name))[0]
            
            desc_list=Placemark.getElementsByTagName('description')
            Point_list=Placemark.getElementsByTagName('Point')
            if Point_list.length>0:                
                coordinates=Point_list[0].getElementsByTagName('coordinates')
                if coordinates.length>0:
                    coor=coordinates[0].firstChild.data                    
                    Point = ogr.Geometry(ogr.wkbPoint)
                    coor=string.split(coor,',')                        
                    Point.AddPoint(float(coor[0]),float(coor[1]))
                Point.SetCoordinateDimension(2)
                wkt=Point.ExportToWkt()
                Point.Destroy()
                ## compare lake with exist data in postgis
                #sql_str="select gid,flag,name,log_modify from "+table_name+" where st_equals(the_geom,GeomFromText('"+wkt+"',4326)) order by gid;"
                sql_str="select gid,flag,name,log_modify from "+table_name+" where the_geom=GeomFromText('"+wkt+"',4326) order by gid;"
                curs.execute(sql_str)
                rows=curs.fetchall()
                
                ## if length of rows eq 0,then the placemark in the kml is different from the data in postgis database, then create a new one.
                if len(rows)==0:                    
                    sql_str="insert into "+table_name+"(gid,the_geom,create_time,flag,name) values("+str(max_gid+1)+','+"GeomFromText('"+wkt+"',"+srid+"""),
    '"""+str(datetime.today())+"','New','"+name+"');"
                    curs.execute(sql_str)
                    max_gid=max_gid+1
                    count_new=count_new+1
                else:
                    ## if length of rows eq 1, it's means the Placemark same as the Geom in database.
                    if len(rows)==1:                        
                        for gid,flag,old_name,log in rows:
                            #old_name=(lookup.encode(old_name))[0]                            
                            if name==old_name:
                                
                                sql_str="update "+table_name+" set flag='Old',modify_time='"+str(datetime.today())+"' where gid="+str(gid)+";"
                                curs.execute(sql_str)
                                gid_list.remove(gid)
                            else:
                                if type(log) is NoneType:
                                    log=''                                
                                log=log+'\n'+'least name:'+old_name+'  modify_time:'+str(datetime.today())
                                sql_str="update "+table_name+" set name='"+name+"',log_modify='"+log+"',flag='Name_Changed',modify_time='"+str(datetime.today())+"' where gid="+str(gid)+";"
                                curs.execute(sql_str)
                        count_existed=count_existed+1
                    else:
                    ## if length of rows great than 1,it's mean there are duplicate geom in database,and need to delete one.
                        duplicate_gid=[]
                        for gid,flag,name,log in rows:                            
                            gid_list.remove(gid)
                            duplicate_gid.append(str(gid))
                        duplicate_gid=sorted(duplicate_gid)
                        duplicate_gid='Duplicate:'+string.join(duplicate_gid,',')
                        sql_str="update "+table_name+" set flag='"+duplicate_gid+"',modify_time='"+str(datetime.today())+"' where gid="+str(gid)+";"
                        curs.execute(sql_str)
                
    print '    Insert new geometry completed!'
    
    ## indentify the geom need to be delete
    count_tobedel=len(gid_list)
    if count_tobedel>0:
        for gid in gid_list:    
            sql_str="update "+table_name+" set flag='To_be_Del',modify_time='"+str(datetime.today())+"' where gid="+str(gid)+";"
            curs.execute(sql_str)
    conn.commit()
    print '    The step checking geomerty that need to be delete is completed!'    
    

    ##where st_overlaps(the_geom,GeomFromText('"+wkt+"',"+srid+"))
        
 

    conn.commit() 
    curs.close()
    conn.close()
    print '  ',count_existed,' same as kml'
    print '  ',count_new,' add to database'
    print '  ',count_overlap,' overlap with kml'
    print '  ',count_tobedel,' need to del'
    message="  kml file has imported to postgre database"
    return message

##Export to kml
def export2kml(out_kmlfile):   
    print 'Program for export to kml from postgres is  running>>>>>>>>>>>>>>>>'
    
    conn=connect("host="+host+" dbname="+dbname+" user="+user+" password="+password)
    curs=conn.cursor()
    ##define the encoding
    
    
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
    Style_node.setAttribute('id','Default_PointStyle')
    IconStyle=dom.createElement('IconStyle')
    Style_node.appendChild(IconStyle)
    color=dom.createElement('color')
    Style_node.appendChild(color)
    Text=dom.createTextNode('ff00ffaa')
    color.appendChild(Text)
    
    scale=dom.createElement('scale')
    Style_node.appendChild(scale)
    Text=dom.createTextNode('ff00ffaa')
    scale.appendChild(Text)
    
    Icon=dom.createElement('Icon')
    Style_node.appendChild(Icon)
    
    href=dom.createElement('href')
    Icon.appendChild(href)
    Text=dom.createTextNode('http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png')
    href.appendChild(Text)
    
    LabelStyle=dom.createElement('LabelStyle')
    Style_node.appendChild(LabelStyle)
    
    color=dom.createElement('color')
    LabelStyle.appendChild(color)
    Text=dom.createTextNode('ffffaa00')
    color.appendChild(Text)

    
    sql_str="select gid,name,askml(the_geom) from "+table_name+' order by name;'    
    curs.execute(sql_str)
    rows=curs.fetchall()
    
    for gid,name,kml in rows:       
        name=unicode(name,'utf8')        
        #name=(lookup.encode(name))[3]
        #print name
        desc_text=str(gid)
        Placemark_node=dom.createElement('Placemark')                           
        Document_node.appendChild(Placemark_node)            
        styleUrl_node=dom.createElement('styleUrl')
        Placemark_node.appendChild(styleUrl_node)
        Text=dom.createTextNode('#Default_PointStyle')
        styleUrl_node.appendChild(Text)
        
        name_node=dom.createElement('name')
        Placemark_node.appendChild(name_node)
        Text=dom.createTextNode(name)
        name_node.appendChild(Text)
            
##        desc_node=dom.createElement('description')
##        Placemark_node.appendChild(desc_node)
##        Text=dom.createCDATASection(desc_text)
##        desc_node.appendChild(Text)
            
        kml_dom=minidom.parseString(kml)
        kml_node=kml_dom.documentElement
        Placemark_node.appendChild(kml_node)            
     
    
    f=open(out_kmlfile,'w')
    writer=codecs.lookup('utf8')[3](f)
    #writer=f
    dom.writexml(writer,encoding='utf8',newl='\n')
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
    srid='4326'
    table_name='hkh_glacier_type'
    encoding='utf8'
    lookup=codecs.lookup(encoding)
    ## define the table name which store glacier lake name
      
    
    ##import kml file
    #input_kmlfile=r'F:\KML\Glacier_lake_names\Glacier_lake_names.kml'
    #result=import2pg(input_kmlfile)

    ##output kml file
    kmlfile=r'F:\KML\gl_type\Glacier_type_'+str(date.today())+'.kml'
    print kmlfile
    result=export2kml(kmlfile)
    print result
print "---end---"





















