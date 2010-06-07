#encoding=utf8
# To change this template, choose Tools | Templates
# and open the template in the editor.
import Image,os,sys
from osgeo import gdal
from osgeo.gdalconst import *
from numpy import *
if __name__ == "__main__":
    format = "GTiff"
    driver = gdal.GetDriverByName(format)
    driver.Register()
    filename = "H:\\v2\\data\\dem\\ASTGTM_Nepal_color_shade.TIF"
    dataset = gdal.Open(filename, GA_ReadOnly)
    geotransform = dataset.GetGeoTransform()
    originX,originY = geotransform[0],geotransform[3]
    pixelWidth,pixelHeight = geotransform[1],geotransform[5]
    offsetX = int((81.404-originX)/pixelWidth)
    offsetY = int((30.337-originY)/pixelHeight)
    sizeX = int((81.421-81.404)/pixelWidth)
    sizeY = int((30.337-30.347)/pixelHeight)
    bands = dataset.RasterCount
    images = []
    band_1 = dataset.GetRasterBand(1)
    data_1 = band_1.ReadAsArray(offsetX,offsetY,sizeX,sizeY)
    print data_1
    data_1 = data_1.astype(float)
    band_2 = dataset.GetRasterBand(2)
    data_2 = band_2.ReadAsArray(offsetX,offsetY,sizeX,sizeY)
#    data_2 = data_2.astype(Numeric.Float)
    band_3 = dataset.GetRasterBand(3)
    data_3 = band_3.ReadAsArray(offsetX,offsetY,sizeX,sizeY)
#    data_3 = data_3.astype(Numeric.Float)
    out_filename="D:\\Workspace\\a1.tif"
    out_driver = gdal.GetDriverByName('GTiff')
    out_driver.Register()
    outDataset = out_driver.Create(out_filename, sizeX,sizeY, 1, GDT_Float32)
    outBand_1 = outDataset.GetRasterBand(1)
    ##outBand_2 = outDataset.GetRasterBand(2)
    ##outBand_3 = outDataset.GetRasterBand(3)
    outBand_1.WriteArray(data_1, 0, 0)
    ##outBand_2.WriteArray(data_2, 0, 0)
    ##outBand_3.WriteArray(data_3, 0, 0)
    outBand_1.FlushCache()
    outBand_1.GetStatistics(0, 1)
    ##outBand_2.FlushCache()
    ##outBand_3.FlushCache()
    outdataset=None
    print '------end------'


    

