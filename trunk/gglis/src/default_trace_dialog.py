# To change this template, choose Tools | Templates
# and open the template in the editor.
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from attribute_geometry_compositor import AttributeGeometryCompositor
from attribute_point_compositor import AttributePointCompositor
from attribute_work import AttributeWork
from qgis.core import *
from qgis.gui import *
from ui_trace_dialog import Ui_TraceDialog


class TraceDialog(QDialog, Ui_TraceDialog):
    def __init__(self, parent=None):
        super(TraceDialog, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.attributeWork = AttributeWork()
        self.highlightWork = AttributeWork()
        self.connect(self.attributeWork, SIGNAL("afterLoadingData"), self.addItems)
        self.connect(self.highlightWork, SIGNAL("afterLoadingData"), self.highlight)


    def loadAttribute(self,point):
        attributeCompositor = AttributePointCompositor(self.parent.currentLayer().name(),(point.x(),point.y()))
        self.attributeWork.compositor = attributeCompositor
        self.attributeWork.start()
        geometryCompositor = AttributeGeometryCompositor(self.parent.currentLayer().name(),(point.x(),point.y()))
        self.highlightWork.compositor = geometryCompositor
        self.highlightWork.start()

    def highlight(self,columns,datas):
        if not datas: return
        layer = self.parent.currentLayer()
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
            data = QTableWidgetItem()
            if isinstance(datas[i], basestring):
                data.setText(datas[i])
            else:
                data.setText(str(datas[i]))
            self.attributeTableWidget.setItem(i, 0, field)
            self.attributeTableWidget.setItem(i,1,data)
        self.show()        

    def closeEvent(self,e):
        if hasattr(self,"rb"):
            self.rb.reset()
        QApplication.restoreOverrideCursor()




