from psycopg2 import connect
from pychartdir import *
from math import *
import string
conn=connect("host=localhost dbname=GGLIS user= postgres password=glacier")
curs=conn.cursor()
sql_str="select \"Gl_Area\",astext(st_centroid(the_geom)) from \"HKH_Glacial_Lakes_final\";"
curs.execute(sql_str)
rows=curs.fetchall()
area=[]
coor_x=[]
for data,coor in rows:
    area.append(data/1000000)
    coor=string.replace(coor,'POINT(','')
    coor=string.replace(coor,')','')
    coor=string.split(coor,' ')
    coor_x.append(float(coor[0]))

print coor_x[0]
# Create a XYChart object of size 450 x 420 pixels
c = XYChart(600, 400)

# Set the plotarea at (55, 65) and of size 350 x 300 pixels, with a light grey border
# (0xc0c0c0). Turn on both horizontal and vertical grid lines with light grey color
# (0xc0c0c0)
c.setPlotArea(55, 65, 550, 300, -1, -1, 0xc0c0c0, 0xc0c0c0, -1)

# Add a legend box at (50, 30) (top of the chart) with horizontal layout. Use 12 pts
# Times Bold Italic font. Set the background and border color to Transparent.
c.addLegend(50, 30, 0, "timesbi.ttf", 12).setBackground(Transparent)

# Add a title to the chart using 18 pts Times Bold Itatic font.
c.addTitle("Glacial lake size along the Longitude ", "timesbi.ttf", 18)

# Add a title to the y axis using 12 pts Arial Bold Italic font
c.yAxis().setTitle("Area(km2)", "arialbi.ttf", 12)

# Add a title to the x axis using 12 pts Arial Bold Italic font
c.xAxis().setTitle("Longitude (°)", "arialbi.ttf", 12)

# Set the axes line width to 3 pixels
c.xAxis().setWidth(3)
c.yAxis().setWidth(3)

# Add an orange (0xff9933) scatter chart layer, using 13 pixel diamonds as symbols
c.addScatterLayer(coor_x, area,"Glacial lake area", DiamondSymbol, 3,
    0xff9933)

# Add a green (0x33ff33) scatter chart layer, using 11 pixel triangles as symbols
#c.addScatterLayer(dataX1, dataY1, "Natural", TriangleSymbol, 11, 0x33ff33)

# Output the chart
c.makeChart("c://workspace//scatter.png")
print 'end'
