#! /usr/bin/env python
#coding=utf-8
from PyQt4.QtCore import pyqtSignal,QVariant
from PyQt4.QtGui import QAction

class QBasinStatisAction(QAction): 
    loadStatisSignal = pyqtSignal(QVariant)       
    def __init__(self,icon,name,parent=None):
        super(QBasinStatisAction,self).__init__(icon,name,parent) 
        self.triggered.connect(lambda x: self.loadStatisSignal.emit(self.data()))
