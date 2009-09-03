##metadata
import string
from psycopg2 import connect
from xml.dom.minidom import parse, parseString
conn = connect("dbname=water_meta user=postgres password=glacier")
curs=conn.cursor()
sql_str="""select b.categoryid,a.uuid,a.data 
    from metadata a full join metadatacateg b on a.id=b.metadataid 
    where a.istemplate='n'
    order by b.categoryid;"""
curs.execute(sql_str)
rows=curs.fetchall()
titles=[]
for gid,uuid,meta in rows:
    dom=parseString(meta)
    root=dom.documentElement
    title=root.getElementsByTagName('resTitle')[0]      
    for node in title.childNodes:
        titles.append(str(gid)+','+node.data+','+uuid)
for data in sorted(titles):
    print data
curs.close()
conn.close()
print 'end'
