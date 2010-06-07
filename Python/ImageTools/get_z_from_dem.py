#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="Administrator"
__date__ ="$2010-5-21 15:41:48$"
import os

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from osgeo import ogr

qgisPrefix = os.getenv("abd")


def getBoundary():
    QgsApplication.setPrefixPath(qgisPrefix, True)
    QgsApplication.initQgis()
    layerPath = "D:/ICIMOD/v2/data/dataset/Nepal_Boundary.shp"
    layerName = "Nepal_Boundary"
    layerProvider = "ogr"
    vectorLayer = QgsVectorLayer(layerPath, layerName, layerProvider)
    fileInfo = QFileInfo("D:/ICIMOD/v2/data/dem/SRTM_Nepal.img")
    rasterLayer = QgsRasterLayer(fileInfo.filePath(), fileInfo.completeBaseName())
    if not vectorLayer.isValid():
        print "raster layer is not valid"
        return
    if not rasterLayer.isValid():
        print "raster layer is not valid"
        return
    f = QgsFeature()
    vectorLayer.featureAtId(0, f)
    resultMap = {}
    xyz = []
    i = 0
    while True:
        point = f.geometry().vertexAt(i)
        i += 1
        if point.x() == 0 and point.y() == 0:
            break;
        result, resultMap = rasterLayer.identify(point)
        if not result:
            break;
        for k, v in resultMap.iteritems():
           xyz.append((point.x(),point.y(),v))
    return xyz


def buildVectoryLayer():
    xyz = getBoundary()

    driver = ogr.GetDriverByName("ESRI Shapefile")

    inDs = driver.Open("D:/ICIMOD/v2/data/dataset/Nepal_Boundary.shp",0)
    inLayer = inDs.GetLayer(0)

    outDs = driver.CreateDataSource("D:/ICIMOD/v2/data/dataset/test/boundary_z.shp")
    outLayer = outDs.CreateLayer('boundary',None, ogr.wkbPolygon)

    layerDfn = inLayer.GetLayerDefn()
    for i in range(layerDfn.GetFieldCount()):
        fieldDfn = layerDfn.GetFieldDefn(i)
        fieldName = fieldDfn.GetNameRef()
        outLayer.CreateField(fieldDfn)
        print "append field name:", fieldName
    f = inLayer.GetFeature(0)
    newFeature = f.Clone()
    oRing  = ogr.Geometry(ogr.wkbLinearRing)
    for p in xyz:
        oRing.AddPoint(float(p[0]),float(p[1]),float(p[2]))
    ploygon = ogr.Geometry(ogr.wkbPolygon)
    ploygon.AddGeometry(oRing)
    newFeature.SetGeometry(ploygon)
    outLayer.CreateFeature(newFeature)
    print "add feature ", newFeature


    inLayer.Destroy()
    outLayer.Destroy()
    inDs.Destroy()
    outDs.Destroy()


if __name__ == "__main__":
    buildVectoryLayer()
    print "Hello World";
