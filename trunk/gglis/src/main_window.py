# To change this template, choose Tools | Templates
# and open the template in the editor.
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mainwindow_ui import Ui_MainWindow
from my_layerproperties import MyLayerProperties
from layer_legend import LayerLegend
from qgis.core import *
from qgis.gui import *
from qrc_resources import *


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Glacier & Glacial Lake Information System")
        
        self.buildCanvas()
        self.buildLayout()
        self.buildLegend()
        self.initAction()
        self.buildMenus()
        self.buildToolbar()
        self.initMapTool()
        self.buildAttributeDockWidget()
        QTimer.singleShot(0, self.loadInitialFile)

    def buildMenus(self):
        fileMenu = self.menuBar().addMenu("&File")
        explorMenu = self.menuBar().addMenu("&Explor")
        self.addActionsInMenu(explorMenu, (self.actionZoomIn,self.actionZoomOut,self.actionZoomFull,
                        self.actionPan, self.actionOpenTable))

    def addActionsInMenu(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)

    def zoomIn(self):
        self.canvas.setMapTool(self.toolZoomIn)

    def zoomOut(self):
        self.canvas.setMapTool(self.toolZoomOut)

    def pan(self):
        self.canvas.setMapTool(self.toolPan)

    def zoomFull(self):
        self.canvas.zoomToFullExtent()

    def loadInitialFile(self):
        dataFile = QgsApplication.prefixPath() + "//data//nepal.sqlite"
        if not QFile.exists(dataFile):return
        layer1 = QgsVectorLayer("dbname='"+dataFile+"' table=\"nepal_boundary\" (Geometry) sql=", "nepal_boundary", "spatialite")
        layer2 = QgsVectorLayer("dbname='"+dataFile+"' table=\"nepal_major_rivers\" (Geometry) sql=", "nepal_major_rivers", "spatialite")
        layer3 = QgsVectorLayer("dbname='"+dataFile+"' table=\"nepal_glacial_lake_2009\" (Geometry) sql=", "nepal_glacial_lake_2009", "spatialite")
        if not layer1.isValid():return
        print "loading..."
        
        QgsMapLayerRegistry.instance().addMapLayer(layer3)
        QgsMapLayerRegistry.instance().addMapLayer(layer2)
        QgsMapLayerRegistry.instance().addMapLayer(layer1)
        self.canvas.setExtent(layer1.extent())
        self.layers = []
        self.layers.append(layer3)
        self.layers.append(layer2)
        self.layers.append(layer1)
        self.setCanvasLayerSet(self.layers)
        self.legend.initItems(self.layers)
        self.setCurrentLayer(0)
        self.canvas.setVisible(True);
        self.canvas.refresh();
        self.emit(SIGNAL("newLayer"), self.attributeTable)


    def updateTable(self):
        if self.canvas.isDrawing():
            return
        fieldCount,fields = self.getFieldsMetaInfo()
        featureCount = self.currentLayer.dataProvider().featureCount()
        self.attributeTable.clear()
        self.attributeTable.setRowCount(featureCount)
        self.attributeTable.setColumnCount(fieldCount)
        self.attributeTable.setHorizontalHeaderLabels(fields)
        self.attributeTable.setAlternatingRowColors(True)
        self.attributeTable.setEditTriggers(QTableWidget.NoEditTriggers)
        self.attributeTable.setSelectionBehavior(QTableWidget.SelectRows)
        self.attributeTable.setSelectionMode(QTableWidget.SingleSelection)
        features = self.selectFeatures()
        for row, feature in enumerate(features):
            attributes = feature.attributeMap()
            for index,field in enumerate(fields):
                item = QTableWidgetItem()
                item.setData(Qt.DisplayRole, attributes.get(index))
                self.attributeTable.setItem(row, index, item)
        self.attributeTable.resizeColumnsToContents()

    def getFieldsMetaInfo(self):
        fields = []
        if not self.currentLayer:
            return 0,fields
        fieldMap = self.currentLayer.dataProvider().fields()
        for k, v in fieldMap.iteritems():
            fields.append(v.name())
        return len(fieldMap.keys()),fields

    def clear(self,table):
        table.clear()
        table.setRowCount(0)
        table.setColumnCount(0)

    def selectFeatures(self):
        features = []
        self.currentLayer.select(self.currentLayer.pendingAllAttributesList(), QgsRectangle(), False);
        f = QgsFeature()
        while(self.currentLayer.nextFeature(f)):
            features.append(f)
        return features

    def buildCanvas(self):
        self.canvas = QgsMapCanvas()
        self.canvas.setCanvasColor(QColor(200, 200, 255))
        self.canvas.enableAntiAliasing(True)
        self.canvas.show()

    def buildLayout(self):
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.addWidget(self.canvas, 0, 0)
        self.setCentralWidget(self.centralwidget)


    def initAction(self):
        self.actionZoomIn = QAction(QIcon(":mActionZoomIn.png"), "Zoom In", self)
        self.connect(self.actionZoomIn, SIGNAL("activated()"), self.zoomIn)

        self.actionZoomOut = QAction(QIcon(":mActionZoomOut.png"), "Zoom Out", self)
        self.connect(self.actionZoomOut, SIGNAL("activated()"), self.zoomOut)

        self.actionZoomFull = QAction(QIcon(":mActionZoomFullExtent.png"), "Zoom Full Extent", self)
        self.connect(self.actionZoomFull, SIGNAL("activated()"), self.zoomFull)

        self.actionPan = QAction(QIcon(":mActionPan.png"), "Pan", self)
        self.connect(self.actionPan, SIGNAL("activated()"), self.pan)

        self.actionOpenTable = QAction(QIcon(":mActionOpenTable.png"), "Attribute Table", self)
        self.connect(self.actionOpenTable, SIGNAL("activated()"), self.updateTable)

        self.connect(self.legend, SIGNAL("currentRowChanged(int)"), self.changeCurrentLayer)
        self.connect(self.legend, SIGNAL("intitemSelectionChanged()"), self.printOk)
        self.connect(self, SIGNAL("newLayer"), self.clear)       

    def printOk(self):
        print "OK"

    def buildToolbar(self):
        self.toolbar = self.addToolBar("Map")
        self.toolbar.addAction(self.actionZoomIn)
        self.toolbar.addAction(self.actionZoomOut)
        self.toolbar.addAction(self.actionZoomFull)
        self.toolbar.addAction(self.actionPan)
        self.toolbar.addAction(self.actionOpenTable)

    def initMapTool(self):
        self.toolPan = QgsMapToolPan(self.canvas)
        self.toolZoomIn = QgsMapToolZoom(self.canvas, False)
        self.toolZoomOut = QgsMapToolZoom(self.canvas, True)

    def buildAttributeDockWidget(self):
        attirbuteDockWidget = QDockWidget("Attribute", self)
        attirbuteDockWidget.setObjectName("AttributeDockWidget")
        attirbuteDockWidget.setAllowedAreas(Qt.BottomDockWidgetArea)
        self.attributeTable = QTableWidget(self)
        attirbuteDockWidget.setWidget(self.attributeTable)
        self.addDockWidget(Qt.BottomDockWidgetArea, attirbuteDockWidget)

    def buildLegend(self):
        self.legend = LayerLegend();
        
        self.legendDock = QDockWidget("Layers", self);
        self.legendDock.setObjectName("Legend");
        self.legendDock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea);
        self.legendDock.setWidget(self.legend);
        self.addDockWidget(Qt.LeftDockWidgetArea, self.legendDock);
        self.legendDock.show();
        self.canvas.refresh();

    def openProperties(self):
        if self.canvas.isDrawing():
            return
        properties = MyLayerProperties(self.currentLayer,self)
        properties.show()

    def setCurrentLayer(self, index):
        if index not in range(len(self.layers)):
            return
        self.currentLayer = self.layers[index]
        self.legend.setCurrentRow(index)
        self.canvas.setCurrentLayer(self.currentLayer)

    def changeCurrentLayer(self):
        index = self.legend.currentRow()
        print "current row changed", index
        self.setCurrentLayer(index)

    def setCanvasLayerSet(self,layers):
        canvasLayers = [QgsMapCanvasLayer(layer) for layer in layers]
        self.canvas.setLayerSet(canvasLayers)
