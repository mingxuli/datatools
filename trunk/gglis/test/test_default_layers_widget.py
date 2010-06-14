# To change this template, choose Tools | Templates
# and open the template in the editor.

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from default_layers_widget import LayersWidget
from mock.mock import Mock
import unittest
import sys

class  TestDefaultLayersWidgetTestCase(unittest.TestCase):

    def setUp(self):
        self.app = QApplication(sys.argv)
        parent = QWidget()
        self.layers = []
        for i in range(4):
            layer = Mock()
            layer.name.return_value = "name %d" % (i)
            layer.geometryType.return_value = i
            self.layers.append(layer)
        parent.layers = self.layers
        self.widget = LayersWidget(parent)


    def testInitItems(self):
        self.widget.initItems(self.layers)
        self.assertEqual(self.widget.count(), 4)

    def testGetIconByGeometry(self):
        layer = self.layers[1]
        result = self.widget.getIconByGeometry(layer)
        self.assertEqual(result, ":/default/images/line.png")

    def testGetIconByGeometryWithType4(self):
        layer = self.layers[3]
        result = self.widget.getIconByGeometry(layer)
        self.assertEqual(result, "")
        

if __name__ == '__main__':
    unittest.main()

