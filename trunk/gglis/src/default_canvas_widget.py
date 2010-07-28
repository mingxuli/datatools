# To change this template, choose Tools | Templates
# and open the template in the editor.
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from default_trace_map_tool import TraceMapTool
from qgis.core import *
from qgis.gui import *

class CanvasWidget(QgsMapCanvas):
    def __init__(self,parent=None):
        super(CanvasWidget,self).__init__(parent)
        self.parent = parent
        self.vectorLayers = []
        settings = QSettings()
        self.database = settings.value("Application/database", "").toString()
        self.image = settings.value("Application/image","").toString()
        self.setCanvasColor(QColor(200, 200, 255))
        self.zoomInTool = QgsMapToolZoom(self, False)
        self.zoomOutTool = QgsMapToolZoom(self, True)
        self.zoomPanTool = QgsMapToolPan(self)
        self.mapIndentify = TraceMapTool(self)

    def loadInitialLayers(self):
        if not QFile.exists(self.database): return
        layers = []
        settings = QSettings();
        layerNames = settings.value("Application/layers").toStringList()
        parameters = "dbname='%s' table=\"%s\"(Geometry) sql="
        for name in layerNames:
            layer = QgsVectorLayer(parameters % (self.database, name), name, "spatialite")
            if layer.isValid():
                QgsMapLayerRegistry.instance().addMapLayer(layer)
                layers.append(layer)
                self.setExtent(layer.extent())
                self.loadStyle(layer)
        fileInfo = QFileInfo(self.image)
        baseName = fileInfo.baseName()
        rasterLayer = QgsRasterLayer(self.image, baseName)
        QgsMapLayerRegistry.instance().addMapLayer(rasterLayer)
        self.addLayers(layers,[rasterLayer])        
        self.setCurrentLayerByIndex(0)
        self.connect(rasterLayer, SIGNAL("repaintRequested()"), self, SLOT("refresh()"))
        self.setVisible(True)
        self.refresh()

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
        layers = [QgsMapCanvasLayer(layer) for layer in vectors] + [QgsMapCanvasLayer(layer) for layer in rasters]
        self.setLayerSet(layers)

    def loadStyle(self,layer):
        styleFolder = QgsApplication.prefixPath() + "//style//"
        qmlFile = styleFolder + layer.name() + ".qml"
        if QFile.exists(qmlFile):
            layer.loadNamedStyle(qmlFile)

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
