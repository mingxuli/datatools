# To change this template, choose Tools | Templates
# and open the template in the editor.
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class StatisticsWidget(QObject):
    def __init__(self,parent=None):
        super(StatisticsWidget,self).__init__(parent)
        self.parent = parent
        self.actionPan = QAction(QIcon(":mActionPan.png"), "Pan", self)
        self.connect(self.actionPan, SIGNAL("activated()"), self.pan)

        statistics = parent.menuBar().addMenu("&Statistics")
        areaStatistics = statistics.addMenu("&Area")
        parent.addActions(areaStatistics, self.areaStatisticsActions())

    def areaStatisticsActions(self):
        return (self.actionPan,)

    def pan(self):
        print "-----pan--------"
