# To change this template, choose Tools | Templates
# and open the template in the editor.
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from qrc_resources import *

class CanvasWidget(QgsMapCanvas):
    def __init__(self, parent=None):
        super(CanvasWidget, self).__init__(parent)
        self.parent = parent
        self.setCanvasColor(QColor(200, 200, 255))
        self.enableAntiAliasing(True)
        self.zoomInTool = QgsMapToolZoom(self, False)
        self.zoomOutTool = QgsMapToolZoom(self, True)
        self.zoomPanTool = QgsMapToolPan(self)
        self.actionZoomIn = QAction(QIcon(":mActionZoomIn.png"), "Zoom In", self)
        self.connect(self.actionZoomIn, SIGNAL("activated()"), self.zoomIn)
        self.actionZoomOut = QAction(QIcon(":mActionZoomOut.png"), "Zoom Out", self)
        self.connect(self.actionZoomOut, SIGNAL("activated()"), self.zoomOut)
        self.actionZoomFull = QAction(QIcon(":mActionZoomFullExtent.png"), "Zoom Full Extent", self)
        self.connect(self.actionZoomFull, SIGNAL("activated()"), self.zoomFull)
        self.actionPan = QAction(QIcon(":mActionPan.png"), "Pan", self)
        self.connect(self.actionPan, SIGNAL("activated()"), self.pan)

        explorMenu = parent.menuBar().addMenu("&Explor")
        parent.addActions(explorMenu, self.mapActions())

        mapToolBar = parent.addToolBar("Map")
        parent.addActions(mapToolBar, self.mapActions())

    def zoomIn(self):
        self.setMapTool(self.zoomInTool)

    def zoomOut(self):
        self.setMapTool(self.zoomOutTool)

    def pan(self):
        self.setMapTool(self.zoomPanTool)

    def zoomFull(self):
        self.zoomToFullExtent()

    def mapActions(self):
        return (self.actionZoomIn, self.actionZoomOut, self.actionZoomFull, self.actionPan)