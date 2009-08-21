## read gpx
from xml.dom.minidom import parse

gpxfile='D:\\GPS_test\\Menris_GPS.gpx'

dom=parse(gpxfile)
root=dom.documentElement

## for waypoint
wpt_list=root.getElementsByTagName('wpt')
for Node in wpt_list:
    lat=Node.getAttribute('lat')
    lon=Node.getAttribute('lon')
    ele_list=Node.getElementsByTagName('ele')
    ele=0
    if ele_list.length>0:
        ele=ele_list[0].firstChild.data
    name_list=Node.getElementsByTagName('name')
    name=''
    if name_list.length>0:
        name=name_list[0].firstChild.data
    print lon,lat,ele,name
