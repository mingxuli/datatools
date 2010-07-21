# To change this template, choose Tools | Templates
# and open the template in the editor.
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from attribute_work import AttributeWork
from qgis.core import QgsApplication
from ui_settings_dialog import Ui_SettingsDialog
from table_name_compositor import TableNameCompositor

class SettingsDialog(QDialog,Ui_SettingsDialog):
    def __init__(self,parent=None):
        super(SettingsDialog,self).__init__(parent)
        self.setupUi(self)
        self.databasePath.setReadOnly(True)
        self.imagePath.setReadOnly(True)
        self.listWidget.setDragDropMode(QListWidget.InternalMove)
        settings = QSettings()
        databasePath = settings.value("Application/database","").toString()
        imagePath = settings.value("Application/image","").toString()
        layerNames = settings.value("Application/layers").toStringList()
        self.databasePath.setText(databasePath)
        self.imagePath.setText(imagePath)
        self.addLayerNames(layerNames)
        self.thread = AttributeWork()
        self.connect(self.databaseBrowseButton,SIGNAL("clicked()"),self.showDatabaseBrowser)
        self.connect(self.imageBrowseButton,SIGNAL("clicked()"),self.showImageBrowser)
        self.connect(self.databasePath,SIGNAL("textChanged(QString)"),self.loadTables)
        self.connect(self.thread, SIGNAL("afterLoadingData"), self.addItems)

    def showDatabaseBrowser(self):
        self.showFileDialog("sqlite", self.databasePath)
        
    def showImageBrowser(self):
        self.showFileDialog("tif", self.imagePath)

    def showFileDialog(self,type,lineEditor):
        dir = QgsApplication.prefixPath() + "//data"
        formats = ["*.%s" % unicode(type)]
        fileName = unicode(QFileDialog.getOpenFileName(self, "Choose Files", dir, "files (%s)" % " ".join(formats)))
        if fileName:
            lineEditor.setText(fileName)

    def loadTables(self):
        compositor = TableNameCompositor("geometry_columns")
        self.thread.dataFile = self.databasePath.text()
        self.thread.compositor = compositor
        self.thread.start()

    def addItems(self, fields, datas):
        names = [data[0] for data in datas]
        self.addLayerNames(names)

    def addLayerNames(self,names):
        self.listWidget.clear()
        for data in names:
            item = QListWidgetItem(data)
            item.setSizeHint(QSize(-1, 25))
            item.setCheckState(Qt.Checked)
            self.listWidget.addItem(item)

    def accept(self):
        settings = QSettings()
        settings.setValue("Application/database", QVariant(self.databasePath.text()))
        settings.setValue("Application/image", QVariant(self.imagePath.text()))
        items = []
        for index in xrange(self.listWidget.count()):
            item = self.listWidget.item(index)
            if item.checkState():
                items.append(item.text())
        settings.setValue("Application/layers", QVariant(items))
        QDialog.accept(self)



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    dialog = SettingsDialog()
    dialog.show()
    app.exec_()

