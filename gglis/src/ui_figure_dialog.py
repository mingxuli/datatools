# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'figure.ui'
#
# Created: Thu Sep 09 15:20:06 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_FigureDialog(object):
    def setupUi(self, FigureDialog):
        FigureDialog.setObjectName("FigureDialog")
        FigureDialog.resize(800, 500)
        self.verticalLayout = QtGui.QVBoxLayout(FigureDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.figureTitle = QtGui.QLabel(FigureDialog)
        self.figureTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.figureTitle.setObjectName("figureTitle")
        self.verticalLayout.addWidget(self.figureTitle)
        self.matplotLayout = QtGui.QVBoxLayout()
        self.matplotLayout.setObjectName("matplotLayout")
        self.verticalLayout.addLayout(self.matplotLayout)

        self.retranslateUi(FigureDialog)
        QtCore.QMetaObject.connectSlotsByName(FigureDialog)

    def retranslateUi(self, FigureDialog):
        FigureDialog.setWindowTitle(QtGui.QApplication.translate("FigureDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.figureTitle.setText(QtGui.QApplication.translate("FigureDialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

