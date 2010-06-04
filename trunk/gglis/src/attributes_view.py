# To change this template, choose Tools | Templates
# and open the template in the editor.
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from attributes_model import AttributesModel

class AttributesView(QTableView):
    def __init__(self,parent=None):
        super(AttributesView,self).__init__(parent)
        self.parent = parent
        self.model = AttributesModel()
        self.setModel(self.model)
        self.actionOpenTable = QAction(QIcon(":mActionOpenTable.png"), "Attribute Table", self)
        self.connect(self.actionOpenTable, SIGNAL("activated()"), self.updateModel)
        layerMenu = self.parent.menuBar().addMenu("&Layer")
        self.parent.addActions(layerMenu, (self.actionOpenTable,))
        attributeToolbar = self.parent.addToolBar("Attribute")
        attributeToolbar.addAction(self.actionOpenTable)

    def updateModel(self):
        pass




