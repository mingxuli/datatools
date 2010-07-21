# To change this template, choose Tools | Templates
# and open the template in the editor.
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from attribute_geometry_compositor import AttributeGeometryCompositor
from attribute_point_compositor import AttributePointCompositor
from attribute_work import AttributeWork
from default_matplot_navigation_toolbar import NavigationToolbar
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.patches import Polygon
from qgis.core import *
from qgis.gui import *
from ui_trace_dialog import Ui_TraceDialog


class TraceDialog(QDialog, Ui_TraceDialog):

    verts = [(86.574611, 27.678998), (86.5741, 27.67854), (86.573587, 27.678417), (86.573141, 27.678842), (86.573174, 27.679176), (86.573891, 27.679392), (86.574611, 27.678998)]

    def __init__(self, parent=None):
        super(TraceDialog, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.figure = Figure()
        self.figure.suptitle("Trace")
        self.canvas = FigureCanvas(self.figure)
        self.mpltoolbar = NavigationToolbar(self.canvas, self.widgetPlot)
        lstActions = self.mpltoolbar.actions()
        self.mpltoolbar.removeAction(lstActions[7])
        self.verticalLayout.addWidget(self.canvas)
        self.verticalLayout.addWidget(self.mpltoolbar)
        self.attributeWork = AttributeWork()
        self.highlightWork = AttributeWork()
        self.connect(self.attributeWork, SIGNAL("afterLoadingData"), self.addItems)
        self.connect(self.highlightWork, SIGNAL("afterLoadingData"), self.highlight)


    def loadAttribute(self,point):
        attributeCompositor = AttributePointCompositor(self.parent.currentLayer.name(),(point.x(),point.y()))
        self.attributeWork.compositor = attributeCompositor
        self.attributeWork.start()
        geometryCompositor = AttributeGeometryCompositor(self.parent.currentLayer.name(),(point.x(),point.y()))
        self.highlightWork.compositor = geometryCompositor
        self.highlightWork.start()

    def highlight(self,columns,datas):
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
        for row in range(5):
            row += 1
            ax = self.figure.add_subplot(5, 1, row)
            poly = Polygon(TraceDialog.verts, facecolor='0.8', edgecolor='k')
            ax.add_patch(poly)
            ax.axis([86.570, 86.579, 27.6780, 27.6799])
            ax.set_yticks([])
            ax.set_xticks([])
            ax.grid(True)
            ax.text(0.9, 0.5, row,
                 horizontalalignment='right',
                 verticalalignment='center',
                 transform=ax.transAxes)
            self.canvas.show()

    def closeEvent(self,e):
        if hasattr(self,"rb"):
            self.rb.reset()
        QApplication.restoreOverrideCursor()




