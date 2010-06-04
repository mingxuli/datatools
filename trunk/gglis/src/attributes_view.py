# To change this template, choose Tools | Templates
# and open the template in the editor.
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from attributes_model import AttributesModel

class AttributesView(QTableView):
    def __init__(self,parent=None):
        super(AttributesView,self).__init__(parent)
        self.parent = parent
        self.model = AttributesModel()
        self.setModel(self.model)

    def actionOpenTable(self):




