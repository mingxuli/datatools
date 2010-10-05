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

    def initItems(self, layers,displayedLayers):
        for layer in layers:            
            item = QListWidgetItem(layer)
            item.setSizeHint(QSize(-1, 25))           
            item.setCheckState(self.isDisplay(layer,displayedLayers))
            self.addItem(item)        

    def getIconByGeometry(self, layer):
        if not isinstance(layer,QgsVectorLayer): return ""
        type = layer.geometryType()
        if type == 0: return ":/default/images/point.png"
        elif type == 1: return ":/default/images/line.png"
        elif type == 2: return ":/default/images/polygon.png"
        else: return ""
    
    def isDisplay(self,layer,displayedLayers):
        checked = False
        for d in displayedLayers:            
            if not layer.compare(d): 
                checked = True               
        if checked:
            return Qt.Checked 
        else:
            return Qt.Unchecked
         
        
    def getCheckedNames(self):
        names = [] 
        for index in range(self.count()):
            item = self.item(index)
            if item.checkState():
                name = item.text()
                names.append(name)
        return names
        

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
