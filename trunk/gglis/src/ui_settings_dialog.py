# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created: Thu Jul 15 14:02:50 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SettingsDialog(object):
    def setupUi(self, Ui_SettingsDialog):
        Ui_SettingsDialog.setObjectName("Ui_SettingsDialog")
        Ui_SettingsDialog.resize(600, 400)
        self.gridLayout_2 = QtGui.QGridLayout(Ui_SettingsDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.buttonBox = QtGui.QDialogButtonBox(Ui_SettingsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(Ui_SettingsDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(Ui_SettingsDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(Ui_SettingsDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.databasePath = QtGui.QLineEdit(Ui_SettingsDialog)
        self.databasePath.setObjectName("databasePath")
        self.gridLayout.addWidget(self.databasePath, 0, 1, 1, 1)
        self.imagePath = QtGui.QLineEdit(Ui_SettingsDialog)
        self.imagePath.setObjectName("imagePath")
        self.gridLayout.addWidget(self.imagePath, 1, 1, 1, 1)
        self.listWidget = QtGui.QListWidget(Ui_SettingsDialog)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 2, 1, 1, 2)
        self.databaseBrowseButton = QtGui.QPushButton(Ui_SettingsDialog)
        self.databaseBrowseButton.setObjectName("databaseBrowseButton")
        self.gridLayout.addWidget(self.databaseBrowseButton, 0, 2, 1, 1)
        self.imageBrowseButton = QtGui.QPushButton(Ui_SettingsDialog)
        self.imageBrowseButton.setObjectName("imageBrowseButton")
        self.gridLayout.addWidget(self.imageBrowseButton, 1, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Ui_SettingsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Ui_SettingsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Ui_SettingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Ui_SettingsDialog)

    def retranslateUi(self, Ui_SettingsDialog):
        Ui_SettingsDialog.setWindowTitle(QtGui.QApplication.translate("Ui_SettingsDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Ui_SettingsDialog", "Database", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Ui_SettingsDialog", "Image", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Ui_SettingsDialog", "Layer Name", None, QtGui.QApplication.UnicodeUTF8))
        self.databaseBrowseButton.setText(QtGui.QApplication.translate("Ui_SettingsDialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.imageBrowseButton.setText(QtGui.QApplication.translate("Ui_SettingsDialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))

