#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="Administrator"
__date__ ="$2010-4-26 12:10:27$"

import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from ui_layerpropertiesbase import Ui_LayerPropertiesBase

class MyLayerProperties(QDialog,Ui_LayerPropertiesBase):
    def __init__(self,layer,parent=None):
        super(MyLayerProperties,self).__init__(parent)
        self.layer = layer
        self.setupUi(self)
        self.setupLegendTypeCombobox()
        self.connect(self.legendtypecombobox,SIGNAL("currentIndexChanged(int)"),self.ab)

    def setupLegendTypeCombobox(self):
        self.legendtypecombobox.addItem("Single Symbol")

    def ab(self):
        print "ok"


if __name__ == "__main__":
    print "Hello world"