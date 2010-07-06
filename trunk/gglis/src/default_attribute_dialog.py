# To change this template, choose Tools | Templates
# and open the template in the editor.
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from default_attribute_model import AttributeModel
from default_attribute_view import AttributeView
from pysqlite2 import dbapi2 as sqlite3
from qgis.core import *
from qgis.gui import *
from ui_attribute_dialog import Ui_AttributeDialog

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
        self.thread.setFilter([column,value])
        self.loadingData()

    def addItems(self, fields, datas):
        self.comboBox.clear()
        self.comboBox.addItems(fields)

    def loadingData(self):        
        self.thread.currentLayer = self.parent.currentLayer
        self.thread.start()

    def updateModel(self, fields, datas):
        self.model = AttributeModel(fields, datas)
        self.tableView.setModel(self.model)
        self.tableView.resizeColumnsToContents()

class AttributeWork(QThread):
    def __init__(self, dataFile, parent=None):
        super(AttributeWork, self).__init__(parent)
        self.exiting = False
        self.dataFile = dataFile

    def __del__(self):
        self.exiting = True
        self.wait()

    def getFieldsMetaInfo(self, cur):
        fields = []
        cur.execute("PRAGMA table_info(%s)" % (self.currentLayer.name()))
        columns = cur.fetchall()
        for c in columns:
            if c[1] != 'Geometry':
                fields.append(c[1])
        return fields

    def getDatas(self, cur, names):
        columns = ",".join(names)
        if hasattr(self,"filter"):
            cur.execute("select %s from %s where %s='%s' order by gid" %(columns,self.currentLayer.name(),self.filter[0],self.filter[1]))
        elif hasattr(self,"point"):
            cur.execute("select %s from %s where MbrWithin(MakePoint(%f, %f,4326),Geometry)" %(columns,self.currentLayer.name(),self.point.x(), self.point.y()))
            return cur.fetchone()
        else:
            cur.execute("select %s from %s order by gid" % (columns, self.currentLayer.name()))
        return cur.fetchall()

    def run(self):
        if self.exiting: return
        conn = sqlite3.connect(str(self.dataFile))
        conn.enable_load_extension(1)
        conn.load_extension('libspatialite-1.dll')
        cur = conn.cursor()
        fields = self.getFieldsMetaInfo(cur)
        datas = self.getDatas(cur, fields)
        self.emit(SIGNAL("afterLoadingData"), fields, datas)

    def setFilter(self,filter):
        self.filter = filter

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
