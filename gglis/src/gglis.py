# To change this template, choose Tools | Templates
# and open the template in the editor.
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from default_main_window import MainWindow
import os
from qgis.core import *
from qgis.gui import *

def  homeDir():
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)

def main(argv):
    qgisPrefix =  homeDir()
    QApplication.setOrganizationName("ICIMOD");
    QApplication.setOrganizationDomain("icimod.org");
    QApplication.setApplicationName("GGLis");

    app = QApplication(argv, True)
    QgsApplication.setPrefixPath(qgisPrefix, True)
    QgsApplication.initQgis()

    window = MainWindow()
    window.show()

    app.exec_()
    QgsApplication.exitQgis()

if __name__ == "__main__":
    main(sys.argv)