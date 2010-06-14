# To change this template, choose Tools | Templates
# and open the template in the editor.
from PyQt4.QtCore import *
from PyQt4.QtGui import *
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
        self.connect(self, SIGNAL("afterLoadingLayers"), self.setCanvasLayerSet)
        self.connect(self, SIGNAL("xyCoordinates(QgsPoint)"), self.showCoordinates)        

    def loadInitialLayers(self):
        if not QFile.exists(self.dataFile): return
        parameters = "dbname='%s' table=\"%s\"(Geometry) sql="
        for name in ("nepal_glacial_lake_2009", "nepal_major_rivers", "nepal_sub_basin_boundary", "nepal_boundary"):
            layer = QgsVectorLayer(parameters % (self.dataFile, name), name, "spatialite")
            if layer.isValid():
                QgsMapLayerRegistry.instance().addMapLayer(layer)
                self.layers.append(layer)
                self.setExtent(layer.extent())
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

    def setCanvasLayerSet(self, layers):
        print "setCanvasLayerSet"
        canvasLayers = [QgsMapCanvasLayer(layer) for layer in layers]
        self.setLayerSet(canvasLayers)

    def showCoordinates(self, point):
        self.parent.sizeLabel.setText("Coordinate: %.5f,%.5f" % (point.x(), point.y()))

    def changeCurrentLayer(self,currentLayer):
        print "mapcanvs change currentlayer"
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
    layout = QVBoxLayout()
    layout.addWidget(form)
    parent.setLayout(layout)
    parent.show()
    app.exec_()
    print parent.sizeLabel.method_calls
    QgsApplication.exitQgis()
