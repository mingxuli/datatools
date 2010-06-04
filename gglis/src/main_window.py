# To change this template, choose Tools | Templates
# and open the template in the editor.
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from attributes_view import AttributesView
from canvas_widget import CanvasWidget
from layers_widget import LayersWidget
from qgis.core import *
from qgis.gui import *
from qrc_resources import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Glacier & Glacial Lake Information System")
        self.resize(800, 600)
        self.menuBar().addMenu("&File")
        self.canvas = CanvasWidget(self)
        self.setCentralWidget(self.canvas)
        self.layersWidget = LayersWidget(self)
        self.buildDockWidget(self.layersWidget, "Layers")
        self.attributeTable = AttributesView(self)
        self.buildDockWidget(self.attributeTable, "Attributes", Qt.BottomDockWidgetArea)
        self.initAction()
        self.sizeLabel = QLabel("Latitude:Longtitude")
        self.sizeLabel.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        status = self.statusBar()
        status.setSizeGripEnabled(False)
        status.addPermanentWidget(self.sizeLabel)
        status.showMessage("Ready", 5000)
        QTimer.singleShot(0, self.loadInitialLayers)

    def addActions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)

    def loadInitialLayers(self):
        dataFile = QgsApplication.prefixPath() + "//data//nepal.sqlite"
        if not QFile.exists(dataFile):return
        layer1 = QgsVectorLayer("dbname='" + dataFile + "' table=\"nepal_boundary\" (Geometry) sql=", "nepal_boundary", "spatialite")
        layer2 = QgsVectorLayer("dbname='" + dataFile + "' table=\"nepal_major_rivers\" (Geometry) sql=", "nepal_major_rivers", "spatialite")
        layer3 = QgsVectorLayer("dbname='" + dataFile + "' table=\"nepal_glacial_lake_2009\" (Geometry) sql=", "nepal_glacial_lake_2009", "spatialite")
        if not layer1.isValid():return
        print "loading..."

        QgsMapLayerRegistry.instance().addMapLayer(layer3)
        QgsMapLayerRegistry.instance().addMapLayer(layer2)
        QgsMapLayerRegistry.instance().addMapLayer(layer1)
        self.canvas.setExtent(layer2.extent())
        self.layers = []
        self.layers.append(layer3)
        self.layers.append(layer2)
        self.layers.append(layer1)
        self.setCanvasLayerSet(self.layers)
        self.layersWidget.initItems(self.layers)
        self.canvas.setVisible(True);
        self.canvas.refresh();
#        self.emit(SIGNAL("newLayer"), self.attributeTable)


    def updateTable(self):
        if self.canvas.isDrawing():
            return
        fieldCount, fields = self.getFieldsMetaInfo()
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
            for index, field in enumerate(fields):
                item = QTableWidgetItem()
                item.setData(Qt.DisplayRole, attributes.get(index))
                self.attributeTable.setItem(row, index, item)
        self.attributeTable.resizeColumnsToContents()

    def getFieldsMetaInfo(self):
        fields = []
        if not self.currentLayer:
            return 0, fields
        fieldMap = self.currentLayer.dataProvider().fields()
        for k, v in fieldMap.iteritems():
            fields.append(v.name())
        return len(fieldMap.keys()), fields

    def clear(self, table):
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

    def initAction(self):
        pass
#        self.actionOpenTable = QAction(QIcon(":mActionOpenTable.png"), "Attribute Table", self)
#        self.connect(self.actionOpenTable, SIGNAL("activated()"), self.updateTable)
#        self.connect(self, SIGNAL("newLayer"), self.clear)

    def printOk(self):
        print "OK"


    def buildDockWidget(self, dockedWidget, name, align=Qt.LeftDockWidgetArea):
        dock = QDockWidget(name, self)
        dock.setObjectName(name)
        dock.setAllowedAreas(align)
        dock.setWidget(dockedWidget)
        self.addDockWidget(align, dock);


    def openProperties(self):
        if self.canvas.isDrawing():
            return
        properties = MyLayerProperties(self.currentLayer, self)
        properties.show()


    def setCanvasLayerSet(self, layers):
        canvasLayers = [QgsMapCanvasLayer(layer) for layer in layers]
        self.canvas.setLayerSet(canvasLayers)
