#encoding=utf8
#需要用到的模块包括:
#GDAL,ChartDirect和numpy
try:
    from osgeo import ogr,gdal
except:
    import ogr,gdal
import numpy
from pychartdir import *
shapefile='D:\SRTM\line.shp'
srtm='D:\SRTM\srtm_54_07.tif'
chartfile='D:\SRTM\chart.png'
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
print cols,rows,bands
geotransform = dataset.GetGeoTransform()
x0=geotransform[0] #x起点
y0=geotransform[3] #y起点
ps_x=geotransform[1]
ps_y=geotransform[5]
band=dataset.GetRasterBand(1)
# 初始化画板
chart=XYChart(600,400)
chart.setRoundedFrame()
chart.setPlotArea(60,20,520,320)
data=[]
x_array=[]
max_data=[]
for i in range(num_Feature):
    feature=layer.GetFeature(i)
    geom= feature.GetGeometryRef()
    for index in range(geom.GetPointCount()):
        x=geom.GetX(index)
        y=geom.GetY(index)
        x_offset=int((x - x0)/ps_x)
        y_offset=int((y - y0)/ps_y)
        value=band.ReadAsArray(x_offset,y_offset,1,1)
        data.append(value[0,0])
        x_array.append(x)
    for index in range(cols):
        value=band.ReadAsArray(index,0,1,rows)
        max_data.append(max(value))
    feature.Destroy()
dataSource.Destroy()
chart.xAxis().setTitle("Longitude/ °","Arialbd.ttf",10)
chart.yAxis().setTitle("Elevation/m","Arialbd.ttf",10) 
layer=chart.addLineLayer2()
layer.addDataSet(data)
layer.addDataSet(max_data)
layer.setXData(x_array)
chart.makeChart(chartfile)
  
print 'end'
