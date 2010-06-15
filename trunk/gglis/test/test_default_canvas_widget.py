# To change this template, choose Tools | Templates
# and open the template in the editor.

import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from default_canvas_widget import CanvasWidget
from mock.mock import *
from qgis.core import *
from qgis.gui import *
import unittest


class  TestDefaultCcanvasWidgetTestCase(unittest.TestCase):
    def setUp(self):
        QgsMapToolZoom = Mock()
        QgsMapToolPan = Mock()        
        qgisPrefix = "D://ICIMOD//GUI//v2//gglis//src//"
        self.app = QApplication(sys.argv)
        QgsApplication.setPrefixPath(qgisPrefix, True)
        QgsApplication.initQgis()
        self.canvas = CanvasWidget()
    

    def tearDown(self):
        pass

    def testInitLayers(self):
        QFile = Mock()
        QgsVectorLayer = Mock()
#        self.canvas.loadInitialLayers()
        self.assertEqual(self.canvas.layers, 3)

if __name__ == '__main__':
    unittest.main()

