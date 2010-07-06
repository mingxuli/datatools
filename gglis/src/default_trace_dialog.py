# To change this template, choose Tools | Templates
# and open the template in the editor.
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from default_attribute_dialog import AttributeWork
from default_matplot_navigation_toolbar import NavigationToolbar
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from pysqlite2 import dbapi2 as sqlite3
from qgis.core import *
from qgis.gui import *
from ui_trace_dialog import Ui_TraceDialog


class TraceDialog(QDialog, Ui_TraceDialog):
    def __init__(self, parent=None):
        super(TraceDialog, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.attributeWork = AttributeWork(parent.dataFile)
        self.highlightWork = HighlightWork(parent.dataFile)
        self.connect(self.attributeWork, SIGNAL("afterLoadingData"), self.addItems)
        self.connect(self.highlightWork,SIGNAL("afterLoadingGeometry"),self.highlight)
        self.figure = Figure()
        self.figure.suptitle("Trace")
        self.canvas = FigureCanvas(self.figure)
        self.mpltoolbar = NavigationToolbar(self.canvas, self.widgetPlot)
        lstActions = self.mpltoolbar.actions()
        self.mpltoolbar.removeAction(lstActions[7])
        self.verticalLayout.addWidget(self.canvas)
        self.verticalLayout.addWidget(self.mpltoolbar)


    def loadAttribute(self,point):
        #todo: need refactor
        self.attributeWork.currentLayer = self.parent.currentLayer
        self.attributeWork.point = point
        self.attributeWork.start()
        
        self.highlightWork.currentLayer = self.parent.currentLayer
        self.highlightWork.point = point
        self.highlightWork.start()

    def highlight(self,datas):
        if not datas: return
        layer = self.parent.currentLayer
        g = QgsGeometry.fromWkt(datas[0])
        self.rb = QgsRubberBand(self.parent, g.type() == QGis.Polygon)
        self.rb.setToGeometry(g, layer)
        self.rb.setWidth(2)
        self.rb.setColor(Qt.red)
        self.rb.show()

    def addItems(self,fields, datas):
        if not datas: return
        self.attributeTableWidget.clear()
        self.attributeTableWidget.setColumnCount(2)
        self.attributeTableWidget.setRowCount(len(fields))
        self.attributeTableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.attributeTableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.attributeTableWidget.setHorizontalHeaderLabels(("Key","Value"))
        for i in range(len(fields)):
            field = QTableWidgetItem(fields[i])
            data = QTableWidgetItem(unicode(str(datas[i])))
            self.attributeTableWidget.setItem(i, 0, field)
            self.attributeTableWidget.setItem(i,1,data)
        self.show()

    def closeEvent(self,e):
        if hasattr(self,"rb"):
            self.rb.reset()
        QApplication.restoreOverrideCursor()

#todo: refactor--get an abstract class from AttributeWork,HighlightWork
class HighlightWork(QThread):
    def __init__(self, dataFile, parent=None):
        super(HighlightWork, self).__init__(parent)
        self.exiting = False
        self.dataFile = dataFile

    def __del__(self):
        self.exiting = True
        self.wait()

    def getDatas(self, cur):
        cur.execute("select AsText(Geometry) from %s where MbrWithin(MakePoint(%f, %f,4326),Geometry)" % (self.currentLayer.name(), self.point.x(), self.point.y()))
        return cur.fetchone()

    def run(self):
        if self.exiting: return
        conn = sqlite3.connect(str(self.dataFile))
        conn.enable_load_extension(1)
        conn.load_extension('libspatialite-1.dll')
        cur = conn.cursor()
        datas = self.getDatas(cur)
        self.emit(SIGNAL("afterLoadingGeometry"), datas)



