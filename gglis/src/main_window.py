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
        self.connect(self, SIGNAL("afterLoadingLayers"), self.showMessage)
        QTimer.singleShot(0, self.loadInitialLayers)

    def addActions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)

    def loadInitialLayers(self):
        dataFile = QgsApplication.prefixPath() + "//data//nepal.sqlite"
        if not QFile.exists(dataFile): return
        parameters = "dbname='%s' table=\"%s\"(Geometry) sql="
        for name in ("nepal_glacial_lake_2009", "nepal_major_rivers", "nepal_boundary"):
            layer = QgsVectorLayer(parameters % (dataFile,name),name,"spatialite")
            if layer.isValid():
                QgsMapLayerRegistry.instance().addMapLayer(layer)
                self.layers.append(layer)
                self.canvas.setExtent(layer.extent())
        self.canvas.setVisible(True);
        self.canvas.refresh();
        self.emit(SIGNAL("afterLoadingLayers"),self.layers)


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

    def printOk(self):
        print "OK"


    def buildDockWidget(self, dockedWidget, name, align=Qt.LeftDockWidgetArea):
        dock = QDockWidget(name, self)
        dock.setObjectName(name)
        dock.setAllowedAreas(align)
        dock.setWidget(dockedWidget)
        self.addDockWidget(align, dock);

    def showMessage(self):
        self.status.showMessage("Loaded layers", 5000)

