# -*- coding: utf-8 -*-
# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="Administrator"
__date__ ="$2010-7-23 10:13:56$"
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qrc_metadata import *
from ui_metadata import Ui_MainWindow
import formats
class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        drivers = self.getDrivers()
        self.fileComboBox.addItems(drivers)
        self.model = QFileSystemModel()
        self.fileTree.setModel(self.model)
        self.dir = QtCore.QDir(self.fileComboBox.currentText())
        self.model.setRootPath(self.dir.path())
        self.model.setNameFilterDisables(False)
        self.model.setNameFilters(['*.abcdefgh']) #todo: refactor, it's a joke.
        self.fileTree.header().hideSection(1)
        self.fileTree.header().hideSection(2)
        self.fileTree.header().hideSection(3)
        self.connect(self.actionExit,SIGNAL("activated()"),self.close)
        self.connect(self.fileList,SIGNAL("itemDoubleClicked(QListWidgetItem *)"),self.showMetadata)

    def getDrivers(self):
        drives = QDir.drives ()
        return [drive.filePath() for drive in drives]

    def showMetadata(self,item):
        file = item.text()
        ds = formats.Open(file)
        self.plainText.clear()
        self.plainText.setColumnCount(2)
        self.plainText.setRowCount(len(ds.fields))
        self.plainText.setHorizontalHeaderLabels(["Field","Value"])
        for x,field in enumerate(ds.fields):            
            td1 = QTableWidgetItem(field)
            td1.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            td2 = QTableWidgetItem(ds.metadata[field])
            td2.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.plainText.setItem(x, 0, td1)
            self.plainText.setItem(x, 1, td2)
        self.plainText.resizeColumnsToContents()


if __name__ == "__main__":
    import sys
    QApplication.setOrganizationName("WestGIS");
    QApplication.setOrganizationDomain("westgis.ac.cn");
    QApplication.setApplicationName("metadata");

    app = QApplication(sys.argv, True)
    window = MainWindow()
    window.show()
    app.exec_()