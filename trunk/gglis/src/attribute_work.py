# To change this template, choose Tools | Templates
# and open the template in the editor.
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from pysqlite2 import dbapi2 as sqlite3
class AttributeWork(QThread):

    def __init__(self, parent=None):
        super(AttributeWork, self).__init__(parent)
        self.exiting = False
        settings = QSettings()
        self.dataFile = settings.value("Application/database", "").toString()

    def __del__(self):
        self.exiting = True
        self.wait()

    def getColumns(self, cur):
        fields = self.compositor.getColumns(cur)
        return fields

    def getDatas(self, cur, columns):
        datas = self.compositor.getDatas(cur,columns)
        return datas

    def run(self):
        if self.exiting or (not self.dataFile): return
        conn = sqlite3.connect(str(self.dataFile))
        conn.enable_load_extension(1)
        conn.load_extension('libspatialite-1.dll')
        cur = conn.cursor()
        fields = self.getColumns(cur)
        datas = self.getDatas(cur, fields)
        self.emit(SIGNAL("afterLoadingData"), fields, datas)