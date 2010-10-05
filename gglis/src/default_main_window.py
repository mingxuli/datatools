# To change this template, choose Tools | Templates
# and open the template in the editor.
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from default_attribute_dialog import AttributeDialog
from default_layers_dialog import LayersDialog
from default_resources import *
from default_report_dialog import ReportDialog
from default_figure_dialog import FigureDialog
from default_trace_dialog import TraceDialog
from default_help_form import HelpForm
from default_basin_action import QBasinAction
from default_basin_statis_action import QBasinStatisAction
import platform
from qgis.core import *
from qgis.gui import *
from ui_main_window import *


class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,splash=None,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)         
        splash.showMessage(unicode("initialize signal and slot"))
        self.initBasinMenu() 
        self.initQuickQuery()      
        self.sizeLabel = QLabel("Coordinate")
        self.sizeLabel.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        self.status = self.statusBar()
        self.status.setSizeGripEnabled(False)
        self.status.addPermanentWidget(self.sizeLabel)
        mirrorGroup = QActionGroup(self)
        self.actionZoomIn.setCheckable(True)
        self.actionZoomOut.setCheckable(True)        
        self.actionZoomPan.setCheckable(True)
        self.actionIdenty.setCheckable(True)
        mirrorGroup.addAction(self.actionZoomIn)
        mirrorGroup.addAction(self.actionZoomOut)        
        mirrorGroup.addAction(self.actionZoomPan)
        mirrorGroup.addAction(self.actionIdenty)
        self.mapVectorLayers = {}
        self.mapRasterLayers = {}
        self.connect(self.actionZoomIn, SIGNAL("activated()"), self.mapCanvas.zoomIn)
        self.connect(self.actionZoomOut, SIGNAL("activated()"), self.mapCanvas.zoomOut)
        self.connect(self.actionFullExten, SIGNAL("activated()"), self.mapCanvas.zoomFull)
        self.connect(self.actionZoomPan, SIGNAL("activated()"), self.mapCanvas.pan)
        self.connect(self.actionAttribute, SIGNAL("activated()"), self.showAttribute)        
        self.connect(self.actionStatisType, SIGNAL("activated()"), self.showTypeStatis)                
        self.connect(self.actionLayers,SIGNAL("activated()"),self.showLayers)
        self.connect(self.mapCanvas, SIGNAL("xyCoordinates(QgsPoint)"), self.showCoordinates)
        self.connect(self.actionIdenty, SIGNAL("activated()"), self.mapCanvas.indentifyFeature)
        self.connect(self.mapCanvas.mapIndentify, SIGNAL("indentifyTrace"), self.showTrace)
        self.connect(self.runSqlButton,SIGNAL("clicked()"),self.queryFeatures)
        self.connect(self.quickComboBox,SIGNAL("currentIndexChanged(int)"),self.changeSql)
        self.connect(self.actionAbout, SIGNAL("activated()"), self.helpAbout)
        self.connect(self.actionHelp, SIGNAL("activated()"), self.helpHelp)
        self.connect(self.actionClose,SIGNAL("activated()"),self.close)        

    def showAttribute(self):
        if self.mapCanvas.isDrawing(): return
        dialog = AttributeDialog(self.mapCanvas)
        self.actionAttribute.setEnabled(False)
        self.connect(dialog.thread, SIGNAL("finished()"), self.showOkayMessage)
        self.connect(dialog.thread, SIGNAL("terminated()"), self.showErrorMessage)
        dialog.loadingData()
        dialog.show()

    def showBasinStatis(self,data):
        if self.mapCanvas.isDrawing(): return
        dialog = ReportDialog(self.mapCanvas)
        dialog.tableTitle.setText('<b></i>Glacial lakes in HKH region</i></b>')
        dialog.basinStatis(data)
        dialog.show()
        
    def showTypeStatis(self):
        if self.mapCanvas.isDrawing(): return
        dialog = ReportDialog(self.mapCanvas)
        dialog.tableTitle.setText('<b><i>Glacial lake type in HKH region</i></b>')
        dialog.typeStatis()
        dialog.show()        
        
    def changeSql(self,index):
        if self.mapCanvas.isDrawing(): return
        sql = self.quickComboBox.itemData(index).toString()
        self.sqlConsole.clear()
        self.sqlConsole.setText(sql)
                

    def showOkayMessage(self):
        self.actionAttribute.setEnabled(True)
        self.status.showMessage("Loaded attributes", 5000)

    def showErrorMessage(self):
        self.actionAttribute.setEnabled(True)
        self.status.showMessage("Oops, error occurs", 5000)

    def showCoordinates(self, point):
        self.sizeLabel.setText("Coordinate: %.5f,%.5f" % (point.x(), point.y()))

    def showTrace(self, point):
        if self.mapCanvas.isDrawing(): return
        dialog = TraceDialog(self.mapCanvas)
        dialog.loadAttribute(point)

    def showLayers(self):
        if self.mapCanvas.isDrawing(): return
        dialog = LayersDialog(self.mapVectorLayers,self.mapRasterLayers,self.mapCanvas)
        dialog.show()

    def queryFeatures(self):
        if self.mapCanvas.isDrawing(): return
        where = self.sqlConsole.text()
        if not where: return
        layer = self.mapCanvas.currentLayer()
        sql = "select id from %s where %s" % (layer.name(), where)
        layer.setSubsetString(where)
        self.mapCanvas.setExtent(layer.extent())
        layer.triggerRepaint()

    def helpAbout(self):
        QMessageBox.about(self, "GGLIS",
                          """<b>GGLIS</b> v 0.99
                <p>Copyright &copy; 2010 ICIMOD.
                All rights reserved.</p>
                <p>Python %s - Qt %s - PyQt %s on %s</p>""" % (
                          platform.python_version(),
                          QT_VERSION_STR, PYQT_VERSION_STR, platform.system()))

    def helpHelp(self):
        form = HelpForm("index.html", self)
        form.show()
        
    def initBasinMenu(self):
        self.quickView.clear()                
        basins = {'all':'All basins','Am':'Amu Darya','Br':'Brahmaputra','Ga':'Ganges','In':'Indus','Ir':'Irrawaddy'}
        for k,v in basins.iteritems():
            action = QBasinAction(QIcon(":/default/images/polygon.png"), v, self)
            action.setData(QVariant(k))            
            action.loadBasinSignal.connect(self.loadBasin)                        
            self.quickView.addAction(action)
            statisAction = QBasinStatisAction(QIcon(":/default/images/polygon.png"), v, self)
            statisAction.setData(QVariant(k))            
            statisAction.loadStatisSignal.connect(self.showBasinStatis)                        
            self.menuBasinStatis.addAction(statisAction)
            
    def initQuickQuery(self):
        self.quickComboBox.clear()
        basins = {
                    '':'',
                    'Rest Query':'1=1',                    
                    'Larger lakes':'''gl_area > 0.1''',
                    'Glacial erosion lakes':'''gl_class like 'E%' ''',
                    'Moraine dammed lakes':'''gl_class like 'M%' ''',
                    'Ice dammed lakes':'''gl_class like 'I%' ''',
                    'Non-glacial lakes':'''gl_class like 'I%' '''
                }        
        for k,v in basins.iteritems():
            self.quickComboBox.addItem(k,QVariant(v))         
            
    def loadBasin(self,data):
        basin = data.toString() 
        where = "basin_code like '"+basin+"%'"        
        if basin=='all':
            where = ''        
        layer = self.mapCanvas.currentLayer()        
        layer.setSubsetString(where)
        self.mapCanvas.setExtent(layer.extent())
        layer.triggerRepaint()
        

        