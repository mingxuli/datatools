# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_attribute.ui'
#
# Created: Mon Sep 13 22:15:29 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AttributeDialog(object):
    def setupUi(self, AttributeDialog):
        AttributeDialog.setObjectName("AttributeDialog")
        AttributeDialog.resize(600, 400)
        AttributeDialog.setModal(False)
        self.gridLayout = QtGui.QGridLayout(AttributeDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.listView = QtGui.QListView(AttributeDialog)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 0, 0, 1, 6)
        spacerItem = QtGui.QSpacerItem(164, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.label = QtGui.QLabel(AttributeDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.comboBox = QtGui.QComboBox(AttributeDialog)
        self.comboBox.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 2, 1, 1)
        self.compareComboBox = QtGui.QComboBox(AttributeDialog)
        self.compareComboBox.setObjectName("compareComboBox")
        self.compareComboBox.addItem("")
        self.compareComboBox.addItem("")
        self.compareComboBox.addItem("")
        self.compareComboBox.addItem("")
        self.gridLayout.addWidget(self.compareComboBox, 1, 3, 1, 1)
        self.lineEdit = QtGui.QLineEdit(AttributeDialog)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 4, 1, 1)
        self.pushButton = QtGui.QPushButton(AttributeDialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 5, 1, 1)

        self.retranslateUi(AttributeDialog)
        QtCore.QMetaObject.connectSlotsByName(AttributeDialog)

    def retranslateUi(self, AttributeDialog):
        AttributeDialog.setWindowTitle(QtGui.QApplication.translate("AttributeDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AttributeDialog", "Filter", None, QtGui.QApplication.UnicodeUTF8))
        self.compareComboBox.setItemText(0, QtGui.QApplication.translate("AttributeDialog", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.compareComboBox.setItemText(1, QtGui.QApplication.translate("AttributeDialog", "!=", None, QtGui.QApplication.UnicodeUTF8))
        self.compareComboBox.setItemText(2, QtGui.QApplication.translate("AttributeDialog", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.compareComboBox.setItemText(3, QtGui.QApplication.translate("AttributeDialog", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("AttributeDialog", "Search", None, QtGui.QApplication.UnicodeUTF8))

