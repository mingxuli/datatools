# To change this template, choose Tools | Templates
# and open the template in the editor.
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class AttributesModel(QAbstractTableModel):
    def __init__(self,headerFields,datas,parent=None):
        super(AttributesModel,self).__init__(parent)
        self.headerFields = headerFields
        self.datas = datas

    def rowCount(self, index=QModelIndex()):
        return len(self.datas)

    def columnCount(self, index=QModelIndex()):
        return len(self.headerFields)

    def data(self, index=QModelIndex, role=Qt.DisplayRole):
        if not index.isValid():
            print "not is valid"
            return QVariant()
        if index.row() >= len(self.datas):
            print ">="
            return QVariant()
        if role == Qt.DisplayRole:
            return QVariant(self.datas[index.row()][index.column()])
        else:
            return QVariant()

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return QVariant()
        if orientation == Qt.Horizontal:
            return QVariant(self.headerFields[section])
        else:
            return QVariant("%s" % (section + 1, ))