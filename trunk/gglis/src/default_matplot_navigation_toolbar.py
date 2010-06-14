# To change this template, choose Tools | Templates
# and open the template in the editor.
from PyQt4 import Qt
from PyQt4 import QtCore
from PyQt4 import QtGui
import matplotlib
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg
import os

class NavigationToolbar(NavigationToolbar2QTAgg):
    def _init_toolbar(self):
        self.basedir = os.path.join(matplotlib.rcParams['datapath'], 'images')

        a = self.addAction(self._icon('home.png'), 'Home', self.home)
        a.setToolTip('Reset original view')
        a = self.addAction(self._icon('back.png'), 'Back', self.back)
        a.setToolTip('Back to previous view')
        a = self.addAction(self._icon('forward.png'), 'Forward', self.forward)
        a.setToolTip('Forward to next view')
        self.addSeparator()
        a = self.addAction(self._icon('move.png'), 'Pan', self.pan)
        a.setToolTip('Pan axes with left mouse, zoom with right')
        a = self.addAction(self._icon('zoom_to_rect.png'), 'Zoom', self.zoom)
        a.setToolTip('Zoom to rectangle')
        self.addSeparator()
        a = self.addAction(self._icon('subplots.png'), 'Subplots',
                           self.configure_subplots)
        a.setToolTip('Configure subplots')
        a = self.addAction(self._icon('filesave.png'), 'Save',
                           self.save_figure)
        a.setToolTip('Save the figure')

        self.buttons = {}

        # Add the x,y location widget at the right side of the toolbar
        # The stretch factor is 1 which means any resizing of the toolbar
        # will resize this label instead of the buttons.
        if self.coordinates:
            self.locLabel = QtGui.QLabel("", self)
            self.locLabel.setAlignment(
                                       QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
            self.locLabel.setSizePolicy(
                                        QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,
                                        QtGui.QSizePolicy.Ignored))
            labelAction = self.addWidget(self.locLabel)
            labelAction.setVisible(True)

        # reference holder for subplots_adjust window
        self.adj_window = None



