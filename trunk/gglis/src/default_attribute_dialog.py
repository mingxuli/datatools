# To change this template, choose Tools | Templates
# and open the template in the editor.
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from default_attribute_model import AttributeModel
from default_attribute_view import AttributeView
from qgis.core import *
from qgis.gui import *
from ui_attribute_dialog import Ui_AttributeDialog
from attribute_work import AttributeWork
from attribute_load_compositor import AttributeLoadCompositor
from attribute_search_compositor import AttributeSearchCompositor

class AttributeDialog(QDialog, Ui_AttributeDialog):
    def __init__(self, parent=None):
        super(AttributeDialog, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.tableView = AttributeView(self)
        self.tableView.setObjectName("attributeView")
        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 6)
        self.thread = AttributeWork(parent.dataFile)
        self.connect(self.thread, SIGNAL("afterLoadingData"), self.updateModel)
        self.connect(self.thread, SIGNAL("afterLoadingData"), self.addItems)
        self.connect(self.pushButton, SIGNAL("clicked()"), self.search)

    def search(self):
        value = self.lineEdit.displayText()
        column = self.comboBox.currentText()
        compositor = AttributeSearchCompositor(self.parent.currentLayer.name(),(column,value))
        self.thread.compositor = compositor
        self.thread.start()

    def addItems(self, fields, datas):
        self.comboBox.clear()
        self.comboBox.addItems(fields)

    def loadingData(self):
        compositor = AttributeLoadCompositor(self.parent.currentLayer.name())
        self.thread.compositor = compositor
        self.thread.start()

    def updateModel(self, fields, datas):
        self.model = AttributeModel(fields, datas)
        self.tableView.setModel(self.model)
        self.tableView.resizeColumnsToContents()

if __name__ =="__main__":
    import sys
    from mock.mock import Mock
    app = QApplication(sys.argv)
    parent = QWidget()
    parent.dataFile = "D://ICIMOD//GUI//v2//gglis//src//data//nepal.sqlite"
    parent.currentLayer = Mock()
    parent.currentLayer.name.return_value = "nepal_glacial_lake_2009"
    dialog = AttributeDialog(parent)
    dialog.loadingData()
    dialog.show()
    app.exec_()
    print parent.currentLayer.method_calls
