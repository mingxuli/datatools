# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'metadata.ui'
#
# Created: Mon Jul 26 16:04:08 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore
from PyQt4 import QtGui
from file_tree_view import FileTreeView

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.mainLayout.setObjectName("mainLayout")
        self.leftLayout = QtGui.QVBoxLayout()
        self.leftLayout.setObjectName("leftLayout")
        self.fileComboBox = QtGui.QComboBox(self.centralwidget)
        self.fileComboBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.fileComboBox.setObjectName("fileComboBox")
        self.leftLayout.addWidget(self.fileComboBox)
        self.rightLayout = QtGui.QVBoxLayout()
        self.rightLayout.setObjectName("rightLayout")
        self.fileList = QtGui.QListWidget(self.centralwidget)
        self.fileList.setObjectName("fileList")
        self.rightLayout.addWidget(self.fileList)
        self.fileTree = FileTreeView(self.fileList,self.centralwidget)
        self.fileTree.setMaximumSize(QtCore.QSize(200, 16777215))
        self.fileTree.setObjectName("fileTree")
        self.leftLayout.addWidget(self.fileTree)
        self.mainLayout.addLayout(self.leftLayout)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.buttonHorizontalLayout = QtGui.QHBoxLayout()
        self.buttonHorizontalLayout.setObjectName("buttonHorizontalLayout")
        self.saveMetadataButton = QtGui.QPushButton(self.tab)
        self.saveMetadataButton.setMaximumSize(QtCore.QSize(70, 16777215))
        self.saveMetadataButton.setObjectName("saveMetadataButton")
        self.buttonHorizontalLayout.addWidget(self.saveMetadataButton)
        self.saveXmlButton = QtGui.QPushButton(self.tab)
        self.saveXmlButton.setMaximumSize(QtCore.QSize(70, 16777215))
        self.saveXmlButton.setObjectName("saveXmlButton")
        self.buttonHorizontalLayout.addWidget(self.saveXmlButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.buttonHorizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.buttonHorizontalLayout)
        self.plainText = QtGui.QTableWidget(self.tab)
        self.plainText.setObjectName("plainText")
        self.plainText.setColumnCount(0)
        self.plainText.setRowCount(0)
        self.verticalLayout.addWidget(self.plainText)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.rightLayout.addWidget(self.tabWidget)
        self.mainLayout.addLayout(self.rightLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.saveMetadataButton.setText(QtGui.QApplication.translate("MainWindow", "save", None, QtGui.QApplication.UnicodeUTF8))
        self.saveXmlButton.setText(QtGui.QApplication.translate("MainWindow", "save xml", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Metadata", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Tab 2", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
