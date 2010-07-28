#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__ = "Administrator"
__date__ = "$2010-5-20 12:18:15$"

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

class LayersWidget(QListWidget):
    def __init__(self, parent=None):
        super(LayersWidget, self).__init__(parent)
        self.parent = parent

    def initItems(self, layers):
        for layer in layers:
            item = QListWidgetItem(layer.name())
            item.setSizeHint(QSize(-1, 25))
            typeOfIcon = self.getIconByGeometry(layer)
            item.setIcon(QIcon(typeOfIcon))
            self.addItem(item)
        self.setCurrentRow(0)

    def getIconByGeometry(self, layer):
        if not isinstance(layer,QgsVectorLayer): return ""
        type = layer.geometryType()
        if type == 0: return ":/default/images/point.png"
        elif type == 1: return ":/default/images/line.png"
        elif type == 2: return ":/default/images/polygon.png"
        else: return ""

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
