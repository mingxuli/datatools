#! /usr/bin/env python
#coding=utf-8
from qgis.core import QgsApplication

from PyQt4.QtCore import Qt
from PyQt4.QtGui import QApplication, QPixmap, QSplashScreen, QColor

from eric4config import getConfig

class SplashScreen(QSplashScreen):

    def __init__(self,qgisPrefix):
        p = qgisPrefix + "//data//icimod.png"
        pic = QPixmap(p)
        self.labelAlignment = Qt.Alignment(Qt.AlignBottom | Qt.AlignRight | Qt.AlignAbsolute)
        QSplashScreen.__init__(self, pic)
        self.show()
        QApplication.flush()
        
    def showMessage(self, msg):
        QSplashScreen.showMessage(self, msg, self.labelAlignment, QColor(Qt.white))
        QApplication.processEvents()
        
    def clearMessage(self):
        QSplashScreen.clearMessage(self)
        QApplication.processEvents()
