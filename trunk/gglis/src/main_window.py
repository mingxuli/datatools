# To change this template, choose Tools | Templates
# and open the template in the editor.
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from attributes_view import AttributesView
from canvas_widget import CanvasWidget
from layers_widget import LayersWidget
from statistics_widget import StatisticsWidget
from qgis.core import *
from qgis.gui import *
from qrc_resources import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Glacier & Glacial Lake Information System")
        self.resize(800, 600)
        self.menuBar().addMenu("&File")
        self.dataFile = QgsApplication.prefixPath() + "//data//nepal.sqlite"
        self.layers = []
        self.canvas = CanvasWidget(self)
        self.setCentralWidget(self.canvas)
        self.layersWidget = LayersWidget(self)
        self.buildDockWidget(self.layersWidget, "Layers")
        self.attributeTable = AttributesView(self)
        self.buildDockWidget(self.attributeTable, "Attributes", Qt.BottomDockWidgetArea)
        self.sizeLabel = QLabel()
        self.sizeLabel.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        self.status = self.statusBar()
        self.status.setSizeGripEnabled(False)
        self.status.addPermanentWidget(self.sizeLabel)        
        self.menuBar().addMenu("&Detection")
        self.menuBar().addMenu("&Post process")
        self.statistics = StatisticsWidget(self)
        self.menuBar().addMenu("&Help")
        self.connect(self, SIGNAL("afterLoadingLayers"), self.showMessage)
        QTimer.singleShot(0, self.loadInitialLayers)

    def addActions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)

    def loadInitialLayers(self):        
        if not QFile.exists(self.dataFile): return
        parameters = "dbname='%s' table=\"%s\"(Geometry) sql="
        for name in ("nepal_glacial_lake_2009", "nepal_major_rivers", "nepal_sub_basin_boundary", "nepal_boundary"):
            layer = QgsVectorLayer(parameters % (self.dataFile,name),name,"spatialite")
            if layer.isValid():
                QgsMapLayerRegistry.instance().addMapLayer(layer)
                self.layers.append(layer)
                self.canvas.setExtent(layer.extent())
#        fileName = "D://ICIMOD//v2//data//dem//nepal_color_shade.tif"
#        fileInfo = QFileInfo(fileName)
#        baseName = fileInfo.baseName()
#        self.rlayer = QgsRasterLayer(fileName, baseName)
#        if self.rlayer.isValid():
#            QgsMapLayerRegistry.instance().addMapLayer(self.rlayer)
#        self.layers.append(self.rlayer)
#        self.connect(self.rlayer, SIGNAL("repaintRequested()"), self.canvas, SLOT("refresh()"));
        self.canvas.setVisible(True);
        self.canvas.refresh();
        self.emit(SIGNAL("afterLoadingLayers"),self.layers)

    def buildDockWidget(self, dockedWidget, name, align=Qt.LeftDockWidgetArea):
        dock = QDockWidget(name, self)
        dock.setObjectName(name)
        dock.setAllowedAreas(align)
        dock.setWidget(dockedWidget)
        self.addDockWidget(align, dock);

    def showMessage(self):
        self.status.showMessage("Loaded layers", 5000)


