# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layers.ui'
#
# Created: Wed Jul 21 15:40:55 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore
from PyQt4 import QtGui
from default_layers_widget import LayersWidget

class Ui_LayersDialog(object):
    def setupUi(self, LayersDialog):
        LayersDialog.setObjectName("LayersDialog")
        LayersDialog.resize(200, 200)
        self.verticalLayout = QtGui.QVBoxLayout(LayersDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layersWidget = LayersWidget(LayersDialog)
        self.layersWidget.setObjectName("layersWidget")
        self.verticalLayout.addWidget(self.layersWidget)

        self.retranslateUi(LayersDialog)
        QtCore.QMetaObject.connectSlotsByName(LayersDialog)

    def retranslateUi(self, LayersDialog):
        LayersDialog.setWindowTitle(QtGui.QApplication.translate("LayersDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))

