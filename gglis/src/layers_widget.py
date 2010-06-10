#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__ = "Administrator"
__date__ = "$2010-5-20 12:18:15$"

from PyQt4.QtCore import *
from PyQt4.QtGui import *


class LayersWidget(QListWidget):
    def __init__(self, parent=None):
        super(LayersWidget, self).__init__(parent)
        self.parent = parent
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.dropAction = Qt.MoveAction
        self.connect(self, SIGNAL("currentRowChanged(int)"), self.changeCurrentLayer)
        self.connect(self.parent, SIGNAL("afterLoadingLayers"), self.initItems)

    def initItems(self, layers):
        for layer in layers:
            item = QListWidgetItem(layer.name())
            item.setSizeHint(QSize(-1, 25))
            typeOfIcon = self.getIconByGeometry(layer)
            item.setIcon(QIcon(typeOfIcon))
            item.setCheckState(Qt.Checked)
            self.addItem(item)
        self.setCurrentRow(0)

    def getIconByGeometry(self, layer):
        if layer.type() == 1: return "mActionPan.png"
        type =layer.geometryType()
        if type == 0: return ":point.png"
        elif type == 1: return ":polyline.png"
        elif type == 2: return ":polygon.png"
        else: return ""

    def changeCurrentLayer(self):
        index = self.currentRow()
        print "current row changed", index
        if index not in range(len(self.parent.layers)):
            return
        self.parent.currentLayer = self.parent.layers[index]
        self.setCurrentRow(index)
        self.parent.canvas.setCurrentLayer(self.parent.currentLayer)



if __name__ == "__main__":
    print "Hello World";
