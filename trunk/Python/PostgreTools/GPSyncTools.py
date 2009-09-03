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

##---------------------start script----------------------
##only for polygon
def import2pg(host,dbname,user,password,kmlfile,table_name,srid='4326'):
    print 'Program for import kml to postgres is  running>>>>>>>>>>>>>>>>'
    conn=connect("host="+host+" dbname="+dbname+" user="+user+" password="+password)
    curs=conn.cursor()
    sql_str="select gid from "+table_name+';'
    curs.execute(sql_str)
    rows=curs.fetchall()
    print 'Found ',len(rows),' geometrys in database:'
    if len(rows)>0:
        gid_list=[s[0] for s in rows]
        max_gid=max(gid_list)
    else:
        max_gid=0
        gid_list=[]

    dom=minidom.parse(kmlfile)
    root=dom.documentElement
    Placemark_List=root.getElementsByTagName('Placemark')
    print len(Placemark_List),' Placemarks in kmlfile'
    count_existed=0
    count_new=0
    count_overlap=0
    count_tobedel=0
    if Placemark_List.length==0:
        print 'no data in this kml file!' 
    else:
        for Placemark in Placemark_List:
            name_list=Placemark.getElementsByTagName('name')
            desc_list=Placemark.getElementsByTagName('description')
            Polygon_list=Placemark.getElementsByTagName('Polygon')
            if Polygon_list.length>0:
                Polygon=Polygon_list[0]
                outerBoundary=Polygon_list[0].getElementsByTagName('outerBoundaryIs')
                innerBoundary=Polygon_list[0].getElementsByTagName('innerBoundaryIs')
                polygon = ogr.Geometry(ogr.wkbPolygon)
                if outerBoundary.length>0:
                    coordinates=outerBoundary[0].getElementsByTagName('coordinates')
                    if coordinates.length>0:
                        coors=coordinates[0].firstChild.data
                        coors=string.split(coors)
                        outring = ogr.Geometry(ogr.wkbLinearRing)
                        for coor in coors:
                            coor=string.split(coor,',')                        
                            outring.AddPoint(float(coor[0]),float(coor[1]))                    
                        polygon.AddGeometry(outring)                    
                        outring.Destroy()
                if innerBoundary.length>0:
                    coordinates=innerBoundary[0].getElementsByTagName('coordinates')
                    if coordinates.length>0:
                        coors=coordinates[0].firstChild.data
                        coors=string.split(coors) 
                        inring.AddGeometry(ring)
                        for coor in coors:
                            coor=string.split(coor,',')
                            inring.AddPoint(float(coor[0]),float(coor[1]))
                        polygon.AddGeometry(inring)                    
                        inring.Destroy()
                polygon.SetCoordinateDimension(2)
                wkt=polygon.ExportToWkt()
                polygon.Destroy()
                ## compare lake with exist data in postgis
                sql_str="select gid,the_geom from "+table_name+" where st_equals(the_geom,GeomFromText('"+wkt+"',4326));"            
                curs.execute(sql_str)
                rows=curs.fetchall()
                ## if length of rows eq 0,then the lake in the kml is different from the data in postgis,maybe new one or modify lake.
                if len(rows)==0:
                    sql_str="select gid,flag from "+table_name+" where st_overlaps(the_geom,GeomFromText('"+wkt+"',"+srid+"));"            
                    curs.execute(sql_str)
                    Rows=curs.fetchall()                
                    if len(Rows)>0:                    
                        sql_str="insert into "+table_name+"(gid,the_geom,create_time,flag) values("+str(max_gid+1)+','+"GeomFromText('"+wkt+"',"+srid+"""),
    '"""+str(datetime.today())+"','overlap');"
                        curs.execute(sql_str)
                        max_gid=max_gid+1
                        count_overlap=count_overlap+1
                        for gid,flag in rows:
                            sql_str="update "+table_name+" set flag='overlap',modify_time='"+str(datetime.today())+"' where gid="+str(gid)+";"
                            curs.execute(sql_str)
                            gid_list.remove(gid)
                    else:                    
                        sql_str="insert into "+table_name+"(gid,the_geom,create_time,flag) values("+str(max_gid+1)+','+"GeomFromText('"+wkt+"',"+srid+"""),
    '"""+str(datetime.today())+"','new');"
                        curs.execute(sql_str)
                        max_gid=max_gid+1
                        count_new=count_new+1
                else:
                    if len(rows)==1:
                        for gid,flag in rows:
                            gid_list.remove(gid)
                        count_existed=count_existed+1
                    else:
                        for gid,flag in rows:
                            sql_str="update "+table_name+" set flag='duplicate',modify_time='"+str(datetime.today())+"' where gid="+str(gid)+";"
                            curs.execute(sql_str)
                            gid_list.remove(gid)
    count_tobedel=len(gid_list)
    if count_tobedel>0:
        for gid in gid_list:    
            sql_str="update "+table_name+" set flag='TobeDel',modify_time='"+str(datetime.today())+"' where gid="+str(gid)+";"
            curs.execute(sql_str)
        

    conn.commit() 
    curs.close()
    conn.close()
    print '  ',count_existed,' same as kml'
    print '  ',count_new,' add to database'
    print '  ',count_overlap,' overlap with kml'
    print '  ',count_tobedel,' need to del'
    message="  kml file has imported to postgre database"
    return message
##covert to kml
def export2kml(host,dbname,user,password,table_name,out_kmlfile,folder_name):   
    print 'Program for export to kml from postgres is  running>>>>>>>>>>>>>>>>'
    
    conn=connect("host="+host+" dbname="+dbname+" user="+user+" password="+password)
    curs=conn.cursor()
    ##
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
    attrname.remove('centroid')
    attr_name=string.join(attrname,',')
    
    sql_str="select gid,flag,"+folder_name+",askml(the_geom),"+attr_name+" from "+table_name+';'
    curs.execute(sql_str)
    rows=curs.fetchall()
    Folder_name=[rec[2] for rec in rows]
    FolderNode_list=[]
    FolderList=list(set(Folder_name))
    for name in FolderList:        
        Folder_node=dom.createElement('Folder')
        FolderNode_list.append(Folder_node)
        Document_node.appendChild(Folder_node)
        name_node=dom.createElement('name')
        Folder_node.appendChild(name_node)
        Text=dom.createTextNode(str(name))
        name_node.appendChild(Text)
    ##overlap folder
    Overlap_node=dom.createElement('Folder')    
    Document_node.appendChild(Overlap_node)
    name_node=dom.createElement('name')
    Overlap_node.appendChild(name_node)
    Text=dom.createTextNode('Overlap')
    name_node.appendChild(Text)
    ##delete folder
    Del_node=dom.createElement('Folder')    
    Document_node.appendChild(Del_node)
    name_node=dom.createElement('name')
    Del_node.appendChild(name_node)
    Text=dom.createTextNode('To Delete')
    name_node.appendChild(Text)
    for i in range(len(rows)):
        gid=rows[i][0]
        flag=rows[i][1]
        folder=rows[i][2]
        kml=rows[i][3]        
        desc_text="""<p align="center"><b><font size="4" color="#0000FF">Attributes</font></b></p><hr>
<table border="1" width="100%">"""
        for index in range(len(attrname)):
            desc_text=desc_text+'<tr><td width="30%">'+attrname[index]+'</td><td>'+str(rows[i][index+4])+'</td></tr>'
        desc_text=desc_text+'</table><hr><div align="center">Create Time:'+str(date.today())+'</div><p align="center"><font color="#FF0000">&copy; 2009 ICIMOD</font></p>'
            
        Placemark_node=dom.createElement('Placemark')
        index=FolderList.index(folder)               
        FolderNode_list[index].appendChild(Placemark_node)
        
        styleUrl_node=dom.createElement('styleUrl')
        Placemark_node.appendChild(styleUrl_node)
        Text=dom.createTextNode('#Default_PolyStyle')
        styleUrl_node.appendChild(Text)
               
        name_node=dom.createElement('name')
        Placemark_node.appendChild(name_node)
        Text=dom.createTextNode(str(gid))
        name_node.appendChild(Text)
        
        desc_node=dom.createElement('description')
        Placemark_node.appendChild(desc_node)
        Text=dom.createCDATASection(desc_text)
        desc_node.appendChild(Text)
        
        kml_dom=minidom.parseString(kml)
        kml_node=kml_dom.documentElement
        Placemark_node.appendChild(kml_node)
        
        if flag=='overlap':
            Overlap_node.appendChild(Placemark_node)
            styleUrl_node=dom.createElement('styleUrl')
            Placemark_node.appendChild(styleUrl_node)
            Text=dom.createTextNode('#Default_PolyStyle')
            styleUrl_node.appendChild(Text)   
            name_node=dom.createElement('name')
            Placemark_node.appendChild(name_node)
            Text=dom.createTextNode(str(gid))
            name_node.appendChild(Text)
        
            desc_node=dom.createElement('description')
            Placemark_node.appendChild(desc_node)
            Text=dom.createCDATASection(desc_text)
            desc_node.appendChild(Text)
        
            kml_dom=minidom.parseString(kml)
            kml_node=kml_dom.documentElement
            Placemark_node.appendChild(kml_node)
        if flag=='TobeDel':
            Del_node.appendChild(Placemark_node)
            styleUrl_node=dom.createElement('styleUrl')
            Placemark_node.appendChild(styleUrl_node)
            Text=dom.createTextNode('#Default_PolyStyle')
            styleUrl_node.appendChild(Text)       
            name_node=dom.createElement('name')
            Placemark_node.appendChild(name_node)
            Text=dom.createTextNode(str(gid))
            name_node.appendChild(Text)
            
            desc_node=dom.createElement('description')
            Placemark_node.appendChild(desc_node)
            Text=dom.createCDATASection(desc_text)
            desc_node.appendChild(Text)
            
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
    table_name='hkh_glacial_lakes'
    lake_id='gid'
    attr='lake_name'
    ##define the geosystem code,default value is 4326 (=WGS84)
    srid='4326'
    ## defin the input and output kml file
    kmlfile='d:\\kml\\hkh_glacier_lake_21_Aug.kml'
    out_kmlfile=kmlfile[0:-4]+'_'+string.replace(str(date.today()),':','')+'.kml'
    field_name='datasource'    
    
    result=import2pg(host,dbname,user,password,kmlfile,table_name)
    print result
    ##
    ##result=export2kml(host,dbname,user,password,table_name,out_kmlfile,field_name)
    ##print result
print "---end---"





















