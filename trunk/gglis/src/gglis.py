# To change this template, choose Tools | Templates
# and open the template in the editor.
import sys

import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from default_main_window import MainWindow

def  homeDir():
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)
#    return "C:\\Program Files\\Quantum GIS Enceladus"

def main(argv):
    qgisPrefix =  homeDir()
    app = QApplication(argv, True)
    QgsApplication.setPrefixPath(qgisPrefix, True)
    QgsApplication.initQgis()

    window = MainWindow()
    window.show()

    app.exec_()
    QgsApplication.exitQgis()

if __name__ == "__main__":
    main(sys.argv)