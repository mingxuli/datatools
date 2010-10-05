# To change this template, choose Tools | Templates
# and open the template in the editor.
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from default_trace_map_tool import TraceMapTool
from qgis.core import *
from qgis.gui import *
import os
from version import DEFAULT_DATABASE
from version import DEFAULT_IMAGE
from version import DEFAULT_LAYERS
from version import detectHDem
from version import resolution

class CanvasWidget(QgsMapCanvas):
    def __init__(self,parent=None):
        super(CanvasWidget,self).__init__(parent)
        self.parent = parent                         
        self.database = DEFAULT_DATABASE
        self.image = DEFAULT_IMAGE   
        self.layerIds = {}
        self.highResolution = False
        self.setCanvasColor(QColor(222, 222, 222))
        self.zoomInTool = QgsMapToolZoom(self, False)
        self.zoomOutTool = QgsMapToolZoom(self, True)
        self.zoomPanTool = QgsMapToolPan(self)
        self.mapIndentify = TraceMapTool(self)        
        self.connect(self,SIGNAL("scaleChanged(double)"),self.showScale)

    def loadInitialLayers(self,splash):
        if not QFile.exists(self.database): return
        layers = []
        layerNames = DEFAULT_LAYERS
        parameters = "dbname='%s' table=\"%s\"(geometry) sql="        
        for name in layerNames:
            splash.showMessage(unicode('loading vector layer %s' % name))
            layer = QgsVectorLayer(parameters % (self.database, name), name, "spatialite")
            if layer.isValid():
                QgsMapLayerRegistry.instance().addMapLayer(layer)
                self.layerIds[layer.name()] =layer.getLayerID()
                layers.append(layer)
                if name=='glacial_lake':                                     
                    self.setExtent(layer.extent())
                self.loadStyle(layer)
        splash.showMessage(unicode('loading raster layer'))
        fileInfo = QFileInfo(self.image)
        baseName = fileInfo.baseName()
        rasterLayer = QgsRasterLayer(self.image, baseName)
        QgsMapLayerRegistry.instance().addMapLayer(rasterLayer)
        self.layerIds[rasterLayer.name()] =rasterLayer.getLayerID()
        self.dem = detectHDem()        
        if self.dem:
            fileInfo = QFileInfo(self.dem)
            baseName = fileInfo.baseName()
            demLayer = QgsRasterLayer(self.dem, baseName)
            QgsMapLayerRegistry.instance().addMapLayer(demLayer)
            self.layerIds[demLayer.name()] =demLayer.getLayerID()        

    def refreshCanvas(self,splash,layers,rasterLayers):
                                    
        self.addLayers(layers,rasterLayers)        
        self.setCurrentLayerByIndex(0)
        for r in rasterLayers:                        
            self.connect(r, SIGNAL("repaintRequested()"), self, SLOT("refresh()"))        
        if splash: splash.showMessage(unicode('refresh canvas'))        
        self.setVisible(True)        
        self.refresh()
        
        
    def showScale(self,scale):
        names = self.getDisplayedLayers()
        if not names: return 
        if scale > resolution and (not self.highResolution):
            return
        elif scale < resolution and self.highResolution:
            return
        vLayers,rLayers = self.getMapLayers(names)
        self.refreshCanvas(None,vLayers,rLayers)                            
        

    def zoomIn(self):
        self.setMapTool(self.zoomInTool)

    def zoomOut(self):
        self.setMapTool(self.zoomOutTool)

    def pan(self):
        self.setMapTool(self.zoomPanTool)

    def zoomFull(self):
        self.zoomToFullExtent()

    def indentifyFeature(self):        
        self.setMapTool(self.mapIndentify)

    def setCurrentLayerByIndex(self, index):
        layer = self.layer(index)
        self.setCurrentLayer(layer)

    def addLayers(self,vectors,rasters):
        layers = []
        if vectors:
            layers += [QgsMapCanvasLayer(layer) for layer in vectors]
        if rasters:
            layers += [QgsMapCanvasLayer(layer) for layer in rasters]
        self.setLayerSet(layers)

    def loadStyle(self,layer):
        fileName = layer.name() + ".qml"
        qmlFile = QgsApplication.prefixPath()+"\\style\\"+fileName               
        if QFile.exists(qmlFile):
            layer.loadNamedStyle(qmlFile)
            
    def getDisplayedLayers(self):
        count = self.layerCount()
        displayedLayers = []
        for index in range(count):
            name=self.layer(index).name()
            if not name.compare('background_h'): name=QString('background')
            displayedLayers.append(name)
        return displayedLayers
    
    def getMapLayers(self,names):        
        vLayers,rLayers = [],[]
        register = QgsMapLayerRegistry.instance()
        for name in names:          
            if not name.compare(QString('background')):
                self.highResolution = False
                id = self.layerIds.get(name)                
                if self.scale() < resolution and self.dem:
                    self.highResolution = True
                    id = self.layerIds.get(QString('background_h'))
                rLayers.append(register.mapLayer(id))
            else:
                id = self.layerIds.get(name)                
                vLayers.append(register.mapLayer(id))
        return vLayers,rLayers
            

if __name__ == "__main__":
    import sys
    from mock.mock import Mock
    qgisPrefix = "D://ICIMOD//GUI//v2//gglis//src//"

    app = QApplication(sys.argv)
    QgsApplication.setPrefixPath(qgisPrefix, True)
    QgsApplication.initQgis()

    parent = QDialog()
    parent.sizeLabel = Mock(spec=['setText'])
    form = CanvasWidget(parent)
    form.dataFile = "D://ICIMOD//GUI//v2//gglis//src//data//nepal.sqlite"
    form.loadInitialLayers()
    emitPoint = QgsMapToolEmitPoint(form)
    form.setMapTool(emitPoint)
    QObject.connect(emitPoint, SIGNAL("canvasClicked(QgsPoint &, Qt::MouseButton)"), form.showTrace)
    layout = QVBoxLayout()
    layout.addWidget(form)
    parent.setLayout(layout)
    parent.show()
    app.exec_()
    print parent.sizeLabel.method_calls
    QgsApplication.exitQgis()
