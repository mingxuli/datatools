#encoding=utf8
#read glacial lake centorid from postgis and get the elevation from dem data(srtm or aster gdem), at last store/updating these value into database. 
#需要用到的模块包括:
#GDAL,ChartDirect和numpy
try:
    from osgeo import ogr,gdal
except:
    import ogr,gdal
from numpy import *
from psycopg2 import connect
def point_from_postgis(host,dbname,user,password,table_name,gid,geometry):
    ## connect to postgres/postgis
    conn=connect("host="+host+" dbname="+dbname+" user="+user+" password="+password)
    curs=conn.cursor()
    sql_str="select gid,centroid(the_geom) from" +table_name +";"
    print sql_str

if __name__=='__main__':

    point_from_postgis()

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
        feature.Destroy()
    dataSource.Destroy()
    value=band.ReadAsArray(0,0,cols,rows)
    max_data=list(amax(value,axis=0))
    layer2_mark=list(x0+arange(cols)*ps_x)
    mean_data=list(mean(value,axis=0))

    chart.xAxis().setTitle("Longitude/ °","Arialbd.ttf",10)
    chart.yAxis().setTitle("Elevation/m","Arialbd.ttf",10) 
    layer1=chart.addLineLayer2()
    layer1.addDataSet(data)
    layer1.setXData(x_array)
    layer2=chart.addLineLayer2()
    layer2.addDataSet(max_data)
    layer2.setXData(layer2_mark)
    layer3=chart.addLineLayer2()
    layer3.addDataSet(mean_data)
    layer3.setXData(layer2_mark)
    chart.makeChart(chartfile)

    print 'end'
