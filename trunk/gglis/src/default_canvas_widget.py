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
        self.layers = []
        self.dataFile = QgsApplication.prefixPath() + "//data//nepal.sqlite"
        self.setCanvasColor(QColor(200, 200, 255))
        self.zoomInTool = QgsMapToolZoom(self, False)
        self.zoomOutTool = QgsMapToolZoom(self, True)
        self.zoomPanTool = QgsMapToolPan(self)
        self.mapIndentify = TraceMapTool(self)
        self.connect(self, SIGNAL("afterLoadingLayers"), self.setCanvasLayerSet)        

    def loadInitialLayers(self):
        if not QFile.exists(self.dataFile): return
        parameters = "dbname='%s' table=\"%s\"(Geometry) sql="
        for name in ("nepal_glacial_lake_2009", "nepal_major_rivers", "nepal_sub_basin_boundary", "nepal_boundary"):
            layer = QgsVectorLayer(parameters % (self.dataFile, name), name, "spatialite")
            if layer.isValid():
                QgsMapLayerRegistry.instance().addMapLayer(layer)
                self.layers.append(layer)
                self.setExtent(layer.extent())
        fileName = "D://ICIMOD//v2//data//dem//ASTGTM_Nepal_color_shade.tif"
        fileInfo = QFileInfo(fileName)
        baseName = fileInfo.baseName()
        self.rlayer = QgsRasterLayer(fileName, baseName)
        QgsMapLayerRegistry.instance().addMapLayer(self.rlayer)
        self.connect(self.rlayer, SIGNAL("repaintRequested()"), self, SLOT("refresh()"))
        self.layers.append(self.rlayer)
        self.setVisible(True);
        self.refresh();
        self.emit(SIGNAL("afterLoadingLayers"), self.layers)

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

    def setCanvasLayerSet(self, layers):        
        canvasLayers = [QgsMapCanvasLayer(layer) for layer in layers]
        self.setLayerSet(canvasLayers)

    def changeCurrentLayer(self,currentLayer):        
        self.setCurrentLayer(currentLayer)


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
