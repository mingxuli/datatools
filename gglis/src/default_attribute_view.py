# To change this template, choose Tools | Templates
# and open the template in the editor.
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class AttributeView(QTableView):
    def __init__(self,parent=None):
        super(AttributeView,self).__init__(parent)
        self.parent = parent
