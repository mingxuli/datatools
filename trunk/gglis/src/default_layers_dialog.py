# To change this template, choose Tools | Templates
# and open the template in the editor.

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from ui_layers_dialog import Ui_LayersDialog
from version import LAYERS

class LayersDialog(QDialog, Ui_LayersDialog):
    def __init__(self, mapVectorLayer,mapRasterLayer,parent=None):
        super(LayersDialog, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent        
        self.initItems()      
        self.connect(self.layersWidget, SIGNAL("itemClicked(QListWidgetItem *)"), self.processItemclick)

    def initItems(self):
        layers = []
        for l in LAYERS:
            layers.append(QString(l))
        displayedLayers = self.parent.getDisplayedLayers()
        self.layersWidget.initItems(layers,displayedLayers)
        
    def processItemclick(self,item):
        if item.checkState() == Qt.Checked:
            item.setCheckState(Qt.Unchecked)
        else:
            item.setCheckState(Qt.Checked)            
        
    def accept(self):
        vLayers, rasterLayer = [],None
        names = self.layersWidget.getCheckedNames()
        vLayers,rLayers = self.parent.getMapLayers(names)
        self.parent.refreshCanvas(None,vLayers,rLayers)                            
        QDialog.accept(self)
    
