一个用python开发的将kml文件转换为shapefile的小工具.

# 介绍 #
目前已经存在很多种将kml和shapefile格式进行相互转换的工具,在ArcView3.x环境下可以再ESRI网站下载相关扩展，ArcGIS可以直接利用数据互操作工具，导入导出数据，利用QGIS的OGC Convert工具也可以进行相互转换。之所以开发这个工具基于以下考虑：
  * 保留kml中的文件夹结构，考虑到文件夹名称可以作为一种重要的属性信息进行利用，希望保存在shapefile的属性表中;
  * kml中的不同几何类型，一个kml文件中可以同时包括点、线、面三种类型，系统能够同时输出;
  * kml中的空placemark的问题，如Arcview很多进行kml转换的工具，遇到空的PlaceMark标签就会出错;
  * 汉字编码问题，有些工具不支持汉字，不支持GB2312编码;

# 使用说明 #
程序代码位于:http://code.google.com/p/datatools/source/browse/trunk/Python/GoogleTools/kml2shp.py
以下是主程序代码：
```
# python code
if __name__=="__main__":
    ##defined the input and output file    
    outpath='F:\\KML\\data_resource\\'
    ##define the encoding for chinese character
    look=codecs.lookup('gbk')
    
    ##for single file
    kmlfile=u'F:\\KML\\data_resource\\datasource.kml'
    result=kml2shp(kmlfile,outpath)
    print result
    ##for batch mode
##    workspace=u'C:\\TDDOWNLOAD\\kml\\地名\\kml\\'
##    filelist=glob(workspace+'*.kml')
##    for kmlfile in filelist:
##        print kmlfile+' is exporting...'
##        result=kml2shp(kmlfile,outpath)
##        print result
```
修改相关参数即可运行,这些参数包括
  * 修改outpath 定义输出的shapefile存储地址地址.不需要定义文件名，文件名自动定义为kml文件名+几何类型+.shp.
  * 修改look,定义输出的shapefile编码，如果包括汉字，在windows环境下建议使用gbk或gb2312编码
  * 修改for single file 部分，对单个kml文件进行处理
    * 修改kmlfile，定义输入的kml文件名
  * 修改for batch mode部分，进行批处理.记着要把前面的for single file 注释掉啊
    * 修改kml存储路径即可


# 存在问题 #
  * GB2312和UTF8编码问题
  * 
# TODO #
  * 变为命令行模式,用户不需要修改代码
  * 添加Usage 提示