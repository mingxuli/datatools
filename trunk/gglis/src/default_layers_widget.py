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
        type = layer.geometryType()
        if type == 0: return ":/default/images/point.png"
        elif type == 1: return ":/default/images/line.png"
        elif type == 2: return ":/default/images/polygon.png"
        else: return ""

    def changeCurrentLayer(self):
        index = self.currentRow()
        print "current row changed", index
        if index not in range(len(self.parent.layers)):
            return
        self.parent.currentLayer = self.parent.layers[index]
        self.setCurrentRow(index)
        self.emit(SIGNAL("currentLayerChanged"), self.parent.currentLayer)

if __name__ == "__main__":
    import sys
    from mock.mock import Mock
    app = QApplication(sys.argv)
    parent = QDialog()
    layers = []
    for i in range(4):
        layer = Mock()
        layer.name.return_value = "name %d" % (i)
        layer.geometryType.return_value = i
        layers.append(layer)
    parent.layers = layers
    form = LayersWidget(parent)
    form.initItems(layers)
    layout = QVBoxLayout()
    layout.addWidget(form)
    parent.setLayout(layout)
    parent.show()
    app.exec_()
    print parent.layers[0].method_calls

    print "hello worldcup"