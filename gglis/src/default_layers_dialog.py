# To change this template, choose Tools | Templates
# and open the template in the editor.

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from ui_layers_dialog import Ui_LayersDialog

class LayersDialog(QDialog, Ui_LayersDialog):
    def __init__(self, parent=None):
        super(LayersDialog, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.initItems(parent)
        self.connect(self.layersWidget, SIGNAL("currentRowChanged(int)"), self.changeCurrentLayer)

    def changeCurrentLayer(self):
        index = self.layersWidget.currentRow()
        print "current row changed", index
        if index not in range(self.parent.layerCount()):
            return
        self.parent.setCurrentLayerByIndex(index)
        self.layersWidget.setCurrentRow(index)

    def initItems(self,mapCanvas):
        count = mapCanvas.layerCount()
        layers = []
        for index in range(count):
            layers.append(mapCanvas.layer(index))
        self.layersWidget.initItems(layers[0:-1])
    
