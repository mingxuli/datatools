# To change this template, choose Tools | Templates
# and open the template in the editor.

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

class TraceMapTool(QgsMapTool):
    def __init__(self,parent):
        super(TraceMapTool, self).__init__(parent)

    def canvasReleaseEvent(self,e):
        if self.canvas().isDrawing(): return
        layer = self.canvas().currentLayer()
        point = self.toLayerCoordinates(layer,e.pos());        
        self.emit(SIGNAL("indentifyTrace"), point)

    def activate(self):
        self.canvas().setCursor(Qt.PointingHandCursor)