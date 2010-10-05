# To change this template, choose Tools | Templates
# and open the template in the editor.
import sys

from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QString
from default_main_window import MainWindow
from default_splash_screen import SplashScreen
import os
from qgis.core import QgsApplication
from version import homeDir
from version import LAYERS


def main(argv):    
    names = []
    for n in LAYERS:
        names.append(QString(n))
    qgisPrefix =  homeDir()        
    QApplication.setOrganizationName("ICIMOD");
    QApplication.setOrganizationDomain("icimod.org");
    QApplication.setApplicationName("Glacial Lakes Viewer");

    app = QApplication(argv, True)
    splash = SplashScreen(qgisPrefix)
    splash.showMessage(unicode("starting..."))
    QgsApplication.setPrefixPath(qgisPrefix, True)
    QgsApplication.initQgis()        
    window = MainWindow(splash)
    window.mapCanvas.loadInitialLayers(splash)
    layers,rLayers = window.mapCanvas.getMapLayers(names)       
    window.show()    
    window.mapCanvas.refreshCanvas(splash,layers,rLayers)
    del splash

    app.exec_()
    QgsApplication.exitQgis()

if __name__ == "__main__":
    main(sys.argv)