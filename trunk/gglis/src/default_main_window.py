# To change this template, choose Tools | Templates
# and open the template in the editor.
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from default_canvas_widget import CanvasWidget
from default_resources import *
from default_layers_widget import LayersWidget
from qgis.core import *
from qgis.gui import *
from default_attribute_dialog import AttributeDialog
from default_statis_dialog import StatisDialog
from default_trace_dialog import TraceDialog
from ui_main_window import *


class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)        
        self.mapCanvas = CanvasWidget(self)
        self.mapCanvas.setBaseSize(QtCore.QSize(0, 0))
        self.mapCanvas.setObjectName("mapCanvas")
        self.layerListView = LayersWidget(self.mapCanvas)
        self.layerListView.setMaximumSize(QtCore.QSize(200, 16777215))
        self.layerListView.setBaseSize(QtCore.QSize(0, 0))
        self.layerListView.setObjectName("layerListView")
        self.horizontalLayout.addWidget(self.layerListView)
        self.horizontalLayout.addWidget(self.mapCanvas)

        self.sizeLabel = QLabel("Coordinate")
        self.sizeLabel.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        self.status = self.statusBar()
        self.status.setSizeGripEnabled(False)
        self.status.addPermanentWidget(self.sizeLabel)
        self.connect(self.actionZoomIn, SIGNAL("activated()"), self.mapCanvas.zoomIn)
        self.connect(self.actionZoomOut, SIGNAL("activated()"), self.mapCanvas.zoomOut)
        self.connect(self.actionFullExten, SIGNAL("activated()"), self.mapCanvas.zoomFull)
        self.connect(self.actionZoomPan, SIGNAL("activated()"), self.mapCanvas.pan)
        self.connect(self.actionTrace,SIGNAL("activated()"),self.mapCanvas.indentifyFeature)
        self.connect(self.mapCanvas, SIGNAL("afterLoadingLayers"), self.layerListView.initItems)
        self.connect(self.layerListView, SIGNAL("currentLayerChanged"), self.mapCanvas.changeCurrentLayer)
        self.connect(self.actionAttribute, SIGNAL("activated()"), self.showAttribute)
        self.connect(self.actionStatis, SIGNAL("activated()"), self.showStatis)
        self.connect(self.mapCanvas, SIGNAL("xyCoordinates(QgsPoint)"), self.showCoordinates)        
        self.connect(self.mapCanvas.mapIndentify, SIGNAL("indentifyTrace"), self.showTrace)
        QTimer.singleShot(0, self.mapCanvas.loadInitialLayers)

    def showAttribute(self):
        if self.mapCanvas.isDrawing(): return
        dialog = AttributeDialog(self.mapCanvas)
        self.actionAttribute.setEnabled(False)
        self.connect(dialog.thread, SIGNAL("finished()"), self.showOkayMessage)
        self.connect(dialog.thread, SIGNAL("terminated()"), self.showErrorMessage)
        dialog.loadingData()
        dialog.show()

    def showStatis(self):
        if self.mapCanvas.isDrawing(): return
        dialog = StatisDialog(self.mapCanvas)
        dialog.show()

    def showOkayMessage(self):
        self.actionAttribute.setEnabled(True)
        self.status.showMessage("Loaded attributes", 5000)

    def showErrorMessage(self):
        self.actionAttribute.setEnabled(True)
        self.status.showMessage("Oops, error occurs", 5000)

    def showCoordinates(self, point):
        self.sizeLabel.setText("Coordinate: %.5f,%.5f" % (point.x(), point.y()))

    def showTrace(self, point):
        if self.mapCanvas.isDrawing(): return
        dialog = TraceDialog(self.mapCanvas)
        dialog.loadAttribute(point)



