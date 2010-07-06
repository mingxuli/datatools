# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trace.ui'
#
# Created: Mon Jun 28 13:47:09 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_TraceDialog(object):
    def setupUi(self, TraceDialog):
        TraceDialog.setObjectName("TraceDialog")
        TraceDialog.resize(814, 434)
        self.horizontalLayout = QtGui.QHBoxLayout(TraceDialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.attributeTableWidget = QtGui.QTableWidget(TraceDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.attributeTableWidget.sizePolicy().hasHeightForWidth())
        self.attributeTableWidget.setSizePolicy(sizePolicy)
        self.attributeTableWidget.setMinimumSize(QtCore.QSize(200, 0))
        self.attributeTableWidget.setMaximumSize(QtCore.QSize(300, 16777215))
        self.attributeTableWidget.setObjectName("attributeTableWidget")
        self.attributeTableWidget.setColumnCount(2)
        self.attributeTableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.attributeTableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.attributeTableWidget.setHorizontalHeaderItem(1, item)
        self.horizontalLayout.addWidget(self.attributeTableWidget)
        self.widgetPlot = QtGui.QWidget(TraceDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetPlot.sizePolicy().hasHeightForWidth())
        self.widgetPlot.setSizePolicy(sizePolicy)
        self.widgetPlot.setMinimumSize(QtCore.QSize(340, 330))
        self.widgetPlot.setObjectName("widgetPlot")
        self.verticalLayout = QtGui.QVBoxLayout(self.widgetPlot)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layoutPlot = QtGui.QVBoxLayout()
        self.layoutPlot.setObjectName("layoutPlot")        
        self.horizontalLayout.addWidget(self.widgetPlot)

        self.retranslateUi(TraceDialog)
        QtCore.QMetaObject.connectSlotsByName(TraceDialog)

    def retranslateUi(self, TraceDialog):
        TraceDialog.setWindowTitle(QtGui.QApplication.translate("TraceDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.attributeTableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("TraceDialog", "键", None, QtGui.QApplication.UnicodeUTF8))
        self.attributeTableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("TraceDialog", "值", None, QtGui.QApplication.UnicodeUTF8))
