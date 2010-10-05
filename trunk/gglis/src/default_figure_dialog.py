from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from ui_figure_dialog import Ui_FigureDialog
from default_matplot_navigation_toolbar import NavigationToolbar
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from pysqlite2 import dbapi2 as sqlite3
from math import log
from version import DEFAULT_DATABASE


class FigureDialog(QDialog, Ui_FigureDialog):
    def __init__(self, parent=None):
        super(FigureDialog, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)        
        self.canvas = FigureCanvas(self.figure)
        self.widgetPlot = QWidget()
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetPlot.sizePolicy().hasHeightForWidth())
        self.widgetPlot.setSizePolicy(sizePolicy)
        self.widgetPlot.setMinimumSize(QSize(340, 330))
        self.widgetPlot.setObjectName("widgetPlot")
        
        self.mpltoolbar = NavigationToolbar(self.canvas,self.widgetPlot)
        lstActions = self.mpltoolbar.actions()
        self.mpltoolbar.removeAction(lstActions[7])
        self.matplotLayout.addWidget(self.canvas)
        self.matplotLayout.addWidget(self.mpltoolbar)        

        settings = QSettings()
        self.dataFile = settings.value("Application/database", QVariant(DEFAULT_DATABASE)).toString()        
        
    def draw(self):
        conn = sqlite3.connect(str(self.dataFile))
        conn.enable_load_extension(1)
        conn.load_extension('libspatialite-1.dll')
        cur = conn.cursor()  
        colours = ['black','magenta','blue','red','pink','yellow','purple','brown','beige','rosybrown', 'slateblue', 'thistle']
        types = {'na':'p','mlg':'h','no':'8','ev':'+','id':'x','mo':'s','me':'o','is':'^','ec':'>','eo':'<','nl':'v','ml':'d'}
        props = dict(alpha=0.75, edgecolors='none')
        index,syms = 0,[]   
        for k,v in types.items():            
            x,y,a = self.getLakers(cur,k)
            syms.append(self.axes.scatter(x,y,c=colours[index], s=a, marker=v,label=k ,**props))
            index += 1   
        
        self.axes.legend(syms,('0','1','2','3','4','5','6','7','8','9','10','11'))        
        self.axes.set_xlabel('Longitude')
        self.axes.set_ylabel('Altitude')
        cur.close()
        conn.close()
        self.canvas.draw()        
    
    def getLakers(self,cur,type):
        xs,ys,areas = [],[],[]
        sql = '''select X(Centroid(geometry)), altitude, gl_area from glacial_lake where gl_class='%s' ''' % type  
        cur.execute(sql)                 
        for (x,y,a) in cur:
            xs.append(x)  
            ys.append(y)
            areas.append(log(a,1.1)+30)         
        return (xs,ys,areas)    
    
    def closeEvent(self,e):
        QApplication.restoreOverrideCursor()
