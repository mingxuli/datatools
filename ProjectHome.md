为了便于用户使用数据，针对中国西部生态环境数据中心和地球系统科学数据共享网上的数据资源开发的一系列工具。
这些工具包括：
  * python/pic2kmz.py 将本地图片转换为kmz可是，可在google earth上浏览，也可以将文件拷贝给其他人浏览，不需要修改相关路径。
  * python/kml2shp.py 将kml转为shapefile的程序，特点是可以保留kml文件中的文件夹结构，这些结构存储在属性表中，也就表示，可以利用google 进行属性添加。
  * python/Tile\_Merge.py 对Tile图片进行拼接的程序，是GDAL2Tiles.py的后续处理程序，可对GDAL2Tiles切片后的数据进行拼接.