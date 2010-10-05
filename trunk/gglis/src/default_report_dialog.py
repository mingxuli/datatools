from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from ui_report_dialog import Ui_ReportDialog
from attribute_work import AttributeWork
from basin_report_compositor import BasinReportCompositor
from type_report_compositor import TypeReportCompositor

class ReportDialog(QDialog, Ui_ReportDialog):
    def __init__(self, parent=None):
        super(ReportDialog, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.thread = AttributeWork()
        self.connect(self.thread, SIGNAL("afterLoadingData"), self.addItems)
        
    def basinStatis(self,basin):
        compositor = BasinReportCompositor(self.parent.currentLayer().name(),basin)
        self.thread.compositor = compositor
        self.thread.start()
        
    def typeStatis(self):
        compositor = TypeReportCompositor(self.parent.currentLayer().name())
        self.thread.compositor = compositor
        self.thread.start()       
        
    def addItems(self,fields, datas):
        if not datas: return
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(len(fields))
        self.tableWidget.setRowCount(len(datas))
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidget.setHorizontalHeaderLabels(fields)
        for i in range(len(datas)):
            for j in range(len(datas[i])):                
                item = QTableWidgetItem()
                if isinstance(datas[i][j], basestring):
                    item.setText(datas[i][j])
                elif isinstance(datas[i][j],str):
                    item.setText(str(datas[i][j]))
                else:
                    item.setText(str(datas[i][j]))
                    item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
                self.tableWidget.setItem(i, j, item)  
        self.tableWidget.resizeColumnsToContents()
        self.show()           
        
    def closeEvent(self, e):
        if not self.thread.isFinished():
            e.ignore()        