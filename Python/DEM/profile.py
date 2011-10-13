#encoding=utf8
#需要用到的模块包括:
#GDAL,ChartDirect和numpy
try:
    from osgeo import ogr,gdal
except:
    import ogr,gdal
from numpy import *
import matplotlib
import matplotlib.pyplot as plt
from math import *
shapefile='D:\Heihe\profile_line_Project.shp'
srtm='D:\Heihe\Heihe_Boundary\SRTM\heihe_srtm_albers.img'

#打开矢量数据
driver = ogr.GetDriverByName('ESRI Shapefile')
dataSource = driver.Open(shapefile, 0)
if dataSource is None:
    print '无法打开文件:' + shapefile
    sys.exit(1) #如果发生错误则推出
layer=dataSource.GetLayer()
num_Feature=layer.GetFeatureCount()

#打开DEM
gdal.AllRegister()
dataset=gdal.Open(srtm)
if dataset is None:
    print '无法打开文件:'+ srtm
    sys.exit(1) #如果发生错误则推出
cols=dataset.RasterXSize
rows=dataset.RasterYSize
bands=dataset.RasterCount

geotransform = dataset.GetGeoTransform()
x0=geotransform[0] #x起点
y0=geotransform[3] #y起点
ps_x=geotransform[1]
ps_y=geotransform[5]
band=dataset.GetRasterBand(1)
ele_array=[]
x_array=[]
x1=0
y1=0
ele1=0
for i in range(num_Feature):
    feature=layer.GetFeature(i)
    geom= feature.GetGeometryRef()
    for index in range(geom.GetPointCount()):
        x=geom.GetX(index)
        y=geom.GetY(index)
        x_offset=int((x - x0)/ps_x)
        y_offset=int((y - y0)/ps_y)
        value=band.ReadAsArray(x_offset,y_offset,1,1)
        ele_array.append(value[0,0])
        distance=sqrt((x-x1)*(x-x1)+(y-y1)*(y-y1))
        x_array.append(sqrt(x*x+y*y))
        ele=value[0][0]
        x1=x
        y1=y
        
        h=float(ele-ele1)
        print distance, ele, h, degrees(atan(h/distance))
        ele1=ele
    feature.Destroy()
dataSource.Destroy()
#value=band.ReadAsArray(0,0,cols,rows)
#max_data=list(amax(value,axis=0))
#layer2_mark=list(x0+arange(cols)*ps_x)
#mean_data=list(mean(value,axis=0))

#chart.xAxis().setTitle("Longitude/ °","Arialbd.ttf",10)
#chart.yAxis().setTitle("Elevation/m","Arialbd.ttf",10) 
#layer1=chart.addLineLayer2()
#layer1.addDataSet(data)
#layer1.setXData(x_array)
#layer2=chart.addLineLayer2()
#layer2.addDataSet(max_data)
#layer2.setXData(layer2_mark)
#layer3=chart.addLineLayer2()
#layer3.addDataSet(mean_data)
#layer3.setXData(layer2_mark)
#chart.makeChart(chartfile)

print 'end'
