# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'report.ui'
#
# Created: Thu Sep 09 12:16:14 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ReportDialog(object):
    def setupUi(self, ReportDialog):
        ReportDialog.setObjectName("ReportDialog")
        ReportDialog.resize(600, 400)
        self.verticalLayout = QtGui.QVBoxLayout(ReportDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableTitle = QtGui.QLabel(ReportDialog)
        self.tableTitle.setText("")
        self.tableTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.tableTitle.setObjectName("tableTitle")
        self.verticalLayout.addWidget(self.tableTitle)
        self.tableWidget = QtGui.QTableWidget(ReportDialog)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(ReportDialog)
        QtCore.QMetaObject.connectSlotsByName(ReportDialog)

    def retranslateUi(self, ReportDialog):
        ReportDialog.setWindowTitle(QtGui.QApplication.translate("ReportDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))

