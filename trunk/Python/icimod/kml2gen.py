#convert kml to esri generate formate
import os
import string
from xml.dom.minidom import parse
workspace=u'D:\\Python\\GLOF\\'
kmlfile=u"F:\\KML\\22Mar\\river_one_v2_22mar.KML"
genfile=u"F:\\KML\\22Mar\\river_one_22mar.gen"

f=open(genfile,"w")

dom=parse(kmlfile)
root = dom.documentElement
xpath=u'//Linestring/coordinates'
nodes=root.getElementsByTagName('coordinates')

gid=1
for node in nodes:
    f.write(str(gid)+'\n')
    for childnode in node.childNodes:
        coors=childnode.data
        coors=string.split(coors)        
        for coor in coors:
            f.write(coor+'\n')
    f.write('end\n')
    gid=gid+1
    
f.write("end")
f.close()

print "---end---"
