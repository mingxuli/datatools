用IDL编写的生成ASTER遥感影像索引图的程序
# 概要 #
> 这是一个2007年写的一个程序，用来把从HDF格式的Aster数据中生成shapefile格式的索引图.现在转移到代码库中。程序需要在IDL环境下运行，可在IDL6.X-7.x环境下的测试。请尽量不要修改程序文件名称，如需修改，请将程序名称与程序文件名称保持一致，否则会导致程序无法正常运行。
  * 源代码位置:http://code.google.com/p/datatools/source/browse/trunk/IDL/Aster/aster_footprint.pro
# 代码修改日志 #
  * v0.1  /2006-7-30:export shapefile using 'ENVI\_EVF\_TO\_SHAPEFILE' Routines
  * v0.2  /2006-7-30:export shapefile using IDL's 'IDLffShape' object,only read attribute of aster data
  * v0.3.1/2006-8-6:增加处理错误的代码
  * v0.4  /2007-2-1:在filename字段中只存储文件名，去掉了前面的路径，可以保证filename长度不会过长
  * v0.5  /2007-12-10:优化了部分，修订了输出shapefile文件无法在arcgis中打开的问题,增加了aster所属UTM分区的字段和aster中心位置字段

# ASTER属性信息说明 #
> HDF格式处理包括数据外，还包括属性信息，包括全局属性和每个层（波段）的属性。对于Aster数据，其图像四个角的位置信息存放在全局属性表中，本程序就是利用提取这些信息，然后生成shapefile文件的。
```
GROUP                  = SCENEFOURCORNERS

      OBJECT                 = UPPERLEFT
        NUM_VAL              = 2
        VALUE                = (37.5778999276982, 103.791291574291)
      END_OBJECT             = UPPERLEFT

      OBJECT                 = UPPERRIGHT
        NUM_VAL              = 2
        VALUE                = (37.4517375704332, 104.621551361705)
      END_OBJECT             = UPPERRIGHT

      OBJECT                 = LOWERLEFT
        NUM_VAL              = 2
        VALUE                = (37.0196378138701, 103.661625220573)
      END_OBJECT             = LOWERLEFT

      OBJECT                 = LOWERRIGHT
        NUM_VAL              = 2
        VALUE                = (36.8943161860939, 104.485971865434)
      END_OBJECT             = LOWERRIGHT

END_GROUP              = SCENEFOURCORNERS
```
# 使用说明 #
> 对应修改程序以下部分即可。
```
Pro aster_footprint

  ;*****************修改文件输入输出设置**************************
  workspace='D:\IDLWorkspace\aster\data\'                       ;Aster影像的存放地址
  logfile='D:\IDLWorkspace\aster\data\errlog.txt'               ;运行日志文件名及其存储位置
  shapefile='D:\IDLWorkspace\aster\data\ASTER_L1A_Indexmap.shp' ;输出的shapefile文件名及其存储位置
  boundary_file='D:\IDLWorkspace\boundary\boundary_poly.shp'    ;省界数据，用于判断aseter数据集是那个省份的
  ;*************************************************************
  ...
```
# 问题 #
> 当时为了判断aster是那个省份的，添加了一个省界数据和一些代码，后来发现并不合适，有时间这这部分代码去掉，或者改成子函数，变成可选的。
