#利用python和GDAL开发的金字塔图片镶嵌处理工具，可以将GDAL2Tiles切割后的数据进行拼接.

# 功能说明 #

> GDAL工具GDAL2Tiles可以将遥感图像进行金字塔化处理，处理后的数据按缩放级别分别存储，切割后每个tile大小是固定的，无数据区域按无值区处理。此外还提供了KML、Google map和Openlayer三种服务和一个元数据说明文件。在利用GDAL2Tiles将单景遥感数据进行金字塔化处理后，可以利用本程序进行拼接。
# 使用说明 #
  * 需要用到gdal模块和PYNumic模块,可在python网站下载
  * 程序参数说明：在主程序部分(即name="main"部分),修改:
  * workspace=u"D:\\website\\TMS\\" #输入文件目录
  * outpath=u"D:\\website\\out\\"   #输出文件目录
  * gdal\_translate=u"C:\\gdalwin32-1.6\\bin\\gdal\_translate.exe" #gdal\_translate工具的目录
  * 设置KML文件的超级链接地址,有些web服务器对大小写敏感,所以请注意大小写
    * 如果是本地地址则用files:///c:\tms\,
    * 如果使用web地址，则用kml\_url="http://map.westgis.ac.cn/tms/test/"
  * 输入路径和输出路径
  * 输入路径的文件夹结构,如输入目录为d:\input,Tile输出结果应该并列的位于该目录下,且该目录下不应有其他文件,另外在拼接前清确认所有待拼接的分幅数据的缩放等级是一样的(目录中5,6,7,8即为缩放等级):
```
D:\input\
 ├─N-46-30
 │  ├─5
 │  │  ├─xx
 │  │  └─xx
 │  ├─6
 │  │  ├─xx
 │  │  └─xx
 │  ├─7
 │  │  ├─xx
 │  │  └─xx
 │  ├─8
 │  │  ├─xx
 │  │  └─xx
 │  ├─x
 │  │  ├─xx
 │  │  └─xx
 │  ├─doc.kml
 │  ├─googlemaps.html
 │  ├─openlayers.html
 │  └─tilemapresource.xml
 ├─N-46-35
 │  ├─5
 │  │  ├─xx
 │  │  └─xx
 │  ├─6
 │  │  ├─xx
 │  │  └─xx
 │  ├─7
 │  │  ├─xx
 │  │  └─xx
 │  ├─8
 │  │  ├─xx
 │  │  └─xx
 │  ├─x
 │  │  ├─xx
 │  │  └─xx
 │  ├─doc.kml
 │  ├─googlemaps.html
 │  ├─openlayers.html
 │  └─tilemapresource.xml
```
  * 输出路径不应放在输入路径的下面,否则的话，程序可能陷入死循环.
  * 部分拼接结果如果要与其他分幅数据继续拼接,则可将部分拼接结果作为一个目录，与其他分幅目录并列,再行拼接皆可
  * 如果只修改kml的服务器地址,则将原来的输出目录作为输入目录，再行本程序即可
# 代码修改日志 #
  * 2009-7-1 v0.1  可以进行拼接了,输出结果合并了kml文件和xml元数据文件,googlemap和openlayer没有合并,仅用随意选取了一个
# 存在的问题 #
  * 需要调用gdal\_translate.exe可执行程序，窗口晃得眼都花了
# TODO #