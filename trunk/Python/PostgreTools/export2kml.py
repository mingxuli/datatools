import os,string,codecs,unicodedata
from psycopg2 import connect
from osgeo import ogr
from xml.dom import minidom
from datetime import *

def export_basin_boundary_poly(basin_code,outpath):    
    kml_file=outpath+'bound_'+basin_code+'.kml'   
       
    conn=connect("host=localhost dbname=GGLIS user=postgres password=postgres")
    curs=conn.cursor()

    sql_str="select gid,askml(the_geom) from \"HKH_Basin_Pfaf_v3_poly\" where lv3_code='"+basin_code+"';"
    curs.execute(sql_str)
    rows=curs.fetchall()
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


    for i in range(len(rows)):
        gid=rows[i][0]
        kml=rows[i][1]
        Placemark_node=dom.createElement('Placemark')
        Document_node.appendChild(Placemark_node)
        
        name_node=dom.createElement('name')
        Placemark_node.appendChild(name_node)
        Text=dom.createTextNode(str(gid))
        name_node.appendChild(Text)  
        
        kml_dom=minidom.parseString(kml)
        kml_node=kml_dom.documentElement
        Placemark_node.appendChild(kml_node)       
                  
    
    f=open(kml_file,'w')
    writer=codecs.lookup('utf8')[3](f)
    dom.writexml(writer,encoding='utf8')
    writer.close()
    curs.close()
    conn.close()
    print '---export boundary----'

def export_basin_boundary_line(outpath):    
    kml_file=outpath+'bound_line.kml'   
       
    conn=connect("host=localhost dbname=GGLIS user=postgres password=postgres")
    curs=conn.cursor()

    sql_str="select gid,askml(the_geom) from \"HKH_Basin_Boundary_v4_line\";"
    curs.execute(sql_str)
    rows=curs.fetchall()
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


    for i in range(len(rows)):
        gid=rows[i][0]
        kml=rows[i][1]
        Placemark_node=dom.createElement('Placemark')
        Document_node.appendChild(Placemark_node)
        
        name_node=dom.createElement('name')
        Placemark_node.appendChild(name_node)
        Text=dom.createTextNode(str(gid))
        name_node.appendChild(Text)  
        
        kml_dom=minidom.parseString(kml)
        kml_node=kml_dom.documentElement
        Placemark_node.appendChild(kml_node)       
                  
    
    f=open(kml_file,'w')
    writer=codecs.lookup('utf8')[3](f)
    dom.writexml(writer,encoding='utf8')
    writer.close()
    curs.close()
    conn.close()
    print '---basin boundary line exported!----'
def export_gl_outline(basin_code,outpath):    
    kml_file=outpath+'gl_'+basin_code+'.kml'   
       
    conn=connect("host=localhost dbname=GGLIS user=postgres password=postgres")
    curs=conn.cursor()

    sql_str="select a.gid,askml(a.the_geom) from \"HKH_Glacial_Lakes_final\" a, \"HKH_Basin_Pfaf_v3_poly\" b "\
            "where st_within(centroid(a.the_geom),b.the_geom) and b.lv3_code='"+basin_code+"' order by a.gid;"

    curs.execute(sql_str)
    rows=curs.fetchall()
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


    for i in range(len(rows)):
        gid=rows[i][0]
        kml=rows[i][1]
        Placemark_node=dom.createElement('Placemark')
        Document_node.appendChild(Placemark_node)
        
        name_node=dom.createElement('name')
        Placemark_node.appendChild(name_node)
        Text=dom.createTextNode(str(gid))
        name_node.appendChild(Text)  
        
        kml_dom=minidom.parseString(kml)
        kml_node=kml_dom.documentElement
        Placemark_node.appendChild(kml_node)       
                  
    
    f=open(kml_file,'w')
    writer=codecs.lookup('utf8')[3](f)
    dom.writexml(writer,encoding='utf8')
    writer.close()
    curs.close()
    conn.close()
    print '---glacial lake outline exported!----'

def export_gl_centroid(basin_code,outpath):    
    kml_file=outpath+'gl_'+basin_code+'_p.kml'   
       
    conn=connect("host=localhost dbname=GGLIS user=postgres password=postgres")
    curs=conn.cursor()

    sql_str="select a.gid,askml(centroid(a.the_geom)) from \"HKH_Glacial_Lakes_final\" a, \"HKH_Basin_Pfaf_v3_poly\" b "\
            "where st_within(centroid(a.the_geom),b.the_geom) and b.lv3_code='"+basin_code+"' and \"Gl_Class\" is null order by a.gid;"

    curs.execute(sql_str)
    rows=curs.fetchall()
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


    for i in range(len(rows)):
        gid=rows[i][0]
        kml=rows[i][1]
        Placemark_node=dom.createElement('Placemark')
        Document_node.appendChild(Placemark_node)
        
        name_node=dom.createElement('name')
        Placemark_node.appendChild(name_node)
        Text=dom.createTextNode(str(gid))
        name_node.appendChild(Text)  
        
        kml_dom=minidom.parseString(kml)
        kml_node=kml_dom.documentElement
        Placemark_node.appendChild(kml_node)
                  
    
    f=open(kml_file,'w')
    writer=codecs.lookup('utf8')[3](f)
    dom.writexml(writer,encoding='utf8')
    writer.close()
    curs.close()
    conn.close()
    print '---glacial lake centroid exported!----'
if __name__=='__main__':
    basin_code='In97'
    outpath='C:\\gl_class\\'
    export_gl_outline(basin_code,outpath)
    export_gl_centroid(basin_code,outpath)
    export_basin_boundary_line(outpath)
    print 'end'
