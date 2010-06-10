# To change this template, choose Tools | Templates
# and open the template in the editor.
import sqlite3

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from attributes_model import AttributesModel
from qgis.core import *
from qgis.gui import *


class AttributesView(QTableView):
    def __init__(self,parent=None):
        super(AttributesView,self).__init__(parent)
        self.parent = parent
        self.actionOpenTable = QAction(QIcon(":mActionOpenTable.png"), "Attribute Table", self)
        self.connect(self.actionOpenTable, SIGNAL("activated()"), self.loadingData)
        layerMenu = self.parent.menuBar().addMenu("&Layer")
        self.parent.addActions(layerMenu, (self.actionOpenTable,))
        attributeToolbar = self.parent.addToolBar("Attribute")
        attributeToolbar.addAction(self.actionOpenTable)
        self.thread = AttributeWork(parent.dataFile)
        self.connect(self.thread, SIGNAL("finished()"), self.showOkayMessage)
        self.connect(self.thread, SIGNAL("terminated()"), self.showErrorMessage)
        self.connect(self.thread, SIGNAL("afterLoadingData"), self.updateModel)

    def loadingData(self):
        if self.parent.canvas.isDrawing(): return
        self.actionOpenTable.setEnabled(False)
        self.thread.currentLayer = self.parent.currentLayer
        self.thread.start()

    def updateModel(self,fields,datas):
        self.model = AttributesModel(fields,datas)
        self.setModel(self.model)
        self.resizeColumnsToContents()

    def showOkayMessage(self):
        self.actionOpenTable.setEnabled(True)
        self.parent.status.showMessage("Loaded attributes", 5000)

    def showErrorMessage(self):
        self.actionOpenTable.setEnabled(True)
        self.parent.status.showMessage("Oops", 5000)

class AttributeWork(QThread):
    def __init__(self,dataFile,parent=None):
        super(AttributeWork,self).__init__(parent)
        self.exiting = False
        self.dataFile = dataFile

    def __del__(self):
        self.exiting = True
        self.wait()

    def getFieldsMetaInfo(self,cur):
        fields = []
        cur.execute("PRAGMA table_info(%s)" % (self.currentLayer.name()))
        columns = cur.fetchall()
        for c in columns:
            if c[1] !='Geometry':
                fields.append(c[1])
        return fields

    def getDatas(self,cur,names):
        columns = ",".join(names)
        cur.execute("select %s from %s order by gid" % (columns, self.currentLayer.name()))
        return cur.fetchall()

    def run(self):
        if self.exiting: return
        conn = sqlite3.connect(str(self.dataFile))
        cur = conn.cursor()
        fields = self.getFieldsMetaInfo(cur)
        datas = self.getDatas(cur, fields)
        self.emit(SIGNAL("afterLoadingData"),fields,datas)




