# To change this template, choose Tools | Templates
# and open the template in the editor.
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from default_matplot_navigation_toolbar import NavigationToolbar
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from qgis.core import *
from qgis.gui import *
from ui_statis_dialog import Ui_StatisDialog

class StatisDialog(QDialog, Ui_StatisDialog):
    def __init__(self, parent=None):
        super(StatisDialog, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.plotTitle = "Frequency distribution"
        self.axisYTitle = "Count"

        self.tblStatistics.setColumnWidth(0, 213)
        self.tblStatistics.setColumnWidth(1, 90)

        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.figure.suptitle(self.plotTitle)
        self.canvas = FigureCanvas(self.figure)
        self.mpltoolbar = NavigationToolbar(self.canvas, self.widgetPlot)
        lstActions = self.mpltoolbar.actions()
        self.mpltoolbar.removeAction(lstActions[7])
        self.layoutPlot.addWidget(self.canvas)
        self.layoutPlot.addWidget(self.mpltoolbar)

        QObject.connect(self.cmbLayers, SIGNAL("currentIndexChanged(QString)"), self.updateFields)

        self.groupBox.hide()
        QObject.connect(self.chkGrid, SIGNAL("stateChanged(int)"), self.refreshPlot)
        QObject.connect(self.chkPlot, SIGNAL("stateChanged(int)"), self.refreshPlot)
        QObject.connect(self.btnRefresh, SIGNAL("clicked()"), self.refreshPlot)

        self.cmbLayers.clear()
        lstLayers = self.getLayersNames(self.parent.layers)
        self.cmbLayers.addItems(lstLayers)

        self.cmbFields.setCurrentIndex(-1)
        self.progressBar.setValue(0)
        QObject.connect(self.cmbFields, SIGNAL("activated(QString)"), self.startCalculation)
        QObject.connect(self.chkUseTextFields, SIGNAL("stateChanged(int)"), self.updateFields)


    def getLayersNames(self,layers):
        return [layer.name() for layer in layers]


    def updateFields(self):
        self.cmbFields.clear()

        self.tblStatistics.clearContents()
        self.tblStatistics.setRowCount(0)

        QObject.disconnect(self.chkGrid, SIGNAL("stateChanged(int)"), self.refreshPlot)
        QObject.disconnect(self.chkPlot, SIGNAL("stateChanged(int)"), self.refreshPlot)
        self.edMinX.setValue(0.0)
        self.edMaxX.setValue(0.0)
        self.chkGrid.setCheckState(Qt.Unchecked)
        self.chkPlot.setCheckState(Qt.Unchecked)
        self.groupBox.hide()
        self.axes.clear()
        QObject.connect(self.chkGrid, SIGNAL("stateChanged(int)"), self.refreshPlot)
        QObject.connect(self.chkPlot, SIGNAL("stateChanged(int)"), self.refreshPlot)

        currentIndex = self.cmbLayers.currentIndex()
        vLayer = self.parent.layers[currentIndex]
        lstFields = vLayer.dataProvider().fields()
        if self.chkUseTextFields.checkState(): # only numeric fields
            for i in lstFields:
                if lstFields[i].type() == QVariant.String:
                    self.cmbFields.addItem(unicode(lstFields[i].name()))
        else: # only text fields
            for i in lstFields:
                if lstFields[i].type() == QVariant.Int or lstFields[i].type() == QVariant.Double:
                    self.cmbFields.addItem(unicode(lstFields[i].name()))
        self.cmbFields.setCurrentIndex(-1)

    def startCalculation(self):
        QObject.disconnect(self.chkGrid, SIGNAL("stateChanged(int)"), self.refreshPlot)
        QObject.disconnect(self.chkPlot, SIGNAL("stateChanged(int)"), self.refreshPlot)
        self.edMinX.setValue(0.0)
        self.edMaxX.setValue(0.0)
        self.chkGrid.setCheckState(Qt.Unchecked)
        self.chkPlot.setCheckState(Qt.Unchecked)
        self.axes.clear()
        QObject.connect(self.chkGrid, SIGNAL("stateChanged(int)"), self.refreshPlot)
        QObject.connect(self.chkPlot, SIGNAL("stateChanged(int)"), self.refreshPlot)

        if self.cmbLayers.currentText() == "":
            QMessageBox.information(self, "Statist: Error", "Please specify target vector layer first")
        elif self.cmbFields.currentText() == "":
            QMessageBox.information(self, "Statist: Error", "Please specify target field first")
        else:
            vlayer = self.parent.layers[self.cmbLayers.currentIndex()]
            self.calculate(vlayer, self.cmbFields.currentText())

    def calculate(self, layer, fieldName):
        self.tblStatistics.clearContents()
        self.tblStatistics.setRowCount(0)
        self.threadCalc = WorkThread(self.parent, self, layer, fieldName)
        QObject.connect(self.threadCalc, SIGNAL("runFinished(PyQt_PyObject)"), self.runFinishedFromThread)
        QObject.connect(self.threadCalc, SIGNAL("runStatus(PyQt_PyObject)"), self.runStatusFromThread)
        QObject.connect(self.threadCalc, SIGNAL("runRange(PyQt_PyObject)"), self.runRangeFromThread)

        QObject.disconnect(self.btnStop, SIGNAL("clicked()"), self.toClipboard)
        self.btnStop.setText(self.tr("Cancel"))
        QObject.connect(self.btnStop, SIGNAL("clicked()"), self.cancelThread)
        self.btnStop.setEnabled(True)

        self.threadCalc.start()
        return True

    def toClipboard(self):
        txt = ""
        for i in range(len(self.results)):
            txt += self.results[i] + "\n"
        clipboard = QApplication.clipboard()
        clipboard.setText(txt)

    def refreshPlot(self):
        self.axes.clear()
        self.axes.grid(self.chkGrid.isChecked())
        if self.edMinX.value() == self.edMaxX.value():
            # histogram
            if not self.chkPlot.isChecked():
                self.axes.hist(self.valuesX, 18, alpha=0.5, histtype="bar")
            # plot
            else:
                n, bins, pathes = self.axes.hist(self.valuesX, 18, alpha=0.5, histtype="bar")
                self.axes.clear()
                self.axes.grid(self.chkGrid.isChecked())
                c = []
                for i in range(len(bins) - 1):
                    s = bins[i + 1] - bins[i]
                    c.append(bins[i] + (s / 2))

                self.axes.plot(c, n, "ro-")
        else:
            xRange = []
            if self.edMinX.value() > self.edMaxX.value():
                xRange.append(self.edMaxX.value())
                xRange.append(self.edMinX.value())
            else:
                xRange.append(self.edMinX.value())
                xRange.append(self.edMaxX.value())
            # histogram
            if not self.chkPlot.isChecked():
                self.axes.hist(self.valuesX, 18, xRange, alpha=0.5, histtype="bar")
            # plot
            else:
                n, bins, pathes = self.axes.hist(self.valuesX, 18, xRange, alpha=0.5, histtype="bar")
                self.axes.clear()
                self.axes.grid(self.chkGrid.isChecked())
                c = []
                for i in range(len(bins) - 1):
                    s = bins[i + 1] - bins[i]
                    c.append(bins[i] + (s / 2))

                self.axes.plot(c, n, "ro-")
                self.axes.set_xlim(xRange[0], xRange[1])
        self.axes.set_ylabel(self.axisYTitle)
        field = unicode(self.cmbFields.currentText())
        self.axes.set_xlabel(field)
        self.figure.autofmt_xdate()
        self.canvas.draw()

    def cancelThread(self):
        self.threadCalc.stop()

    def runFinishedFromThread(self, output):
        self.threadCalc.stop()
        self.results = output[0]

        n = len(self.results)
        self.tblStatistics.setRowCount(n)
        for r in range(n):
            tmp = self.results[r].split(":")
            item = QTableWidgetItem(tmp[0])
            self.tblStatistics.setItem(r, 0, item)
            item = QTableWidgetItem(tmp[1])
            self.tblStatistics.setItem(r, 1, item)
        self.tblStatistics.verticalHeader().hide()

        # enable copy to clipboard
        QObject.disconnect(self.btnStop, SIGNAL("clicked()"), self.cancelThread)
        self.btnStop.setText(self.tr ("Copy"))
        QObject.connect(self.btnStop, SIGNAL("clicked()"), self.toClipboard)

        self.axes.clear()
        self.axes.grid(self.chkGrid.isChecked())
        self.axes.set_ylabel(self.axisYTitle)
        field = unicode(self.cmbFields.currentText())
        self.axes.set_xlabel(field)
        self.valuesX = output[2]
        self.axes.hist(self.valuesX, 18, alpha=0.5, histtype="bar")
        self.figure.autofmt_xdate()
        self.canvas.draw()

        self.groupBox.show()
        return True

    def runStatusFromThread(self, status):
        self.progressBar.setValue(status)

    def runRangeFromThread(self, range_vals):
        self.progressBar.setRange(range_vals[0], range_vals[1])

class WorkThread(QThread):
    def __init__(self, parentThread, parentObject, vlayer, fieldName):
        QThread.__init__(self, parentThread)
        self.parent = parentObject
        self.running = False
        self.vlayer = vlayer
        self.fieldName = fieldName

    def run(self):
        self.running = True
        (lst, cnt, val) = self.statistics(self.vlayer, self.fieldName)
        self.emit(SIGNAL("runFinished(PyQt_PyObject)"), (lst, cnt, val))
        self.emit(SIGNAL("runStatus(PyQt_PyObject)"), 0)

    def stop(self):
        self.running = False

    def statistics(self, vlayer, fieldName):
        self.emit(SIGNAL("runStatus(PyQt_PyObject)"), 0)
        self.emit(SIGNAL("runRange(PyQt_PyObject)"), (0, 5000))
        values = []
        for i in range(5000):
            self.emit(SIGNAL("runStatus(PyQt_PyObject)"), i)
            values.append(i)

        lstStats = []
        lstStats.append( "Count:7")
        lstStats.append("Unique values:6")
        lstStats.append("Minimum value:1")
        lstStats.append("Maximum value:6")
        lstStats.append("Swing:4")
        lstStats.append("Sum:48")
        lstStats.append("Mean value:5")
        lstStats.append("Median value:4")
        lstStats.append("Standard deviation:2")
        lstStats.append("Coefficient of Variation:8")
        return (lstStats, [], values)

    def getFieldType(self, vlayer, fieldName):
        fields = vlayer.dataProvider().fields()
        for name, field in fields.iteritems():
            if field.name() == fieldName:
                return field.typeName()
    def getUniqueValsCount(self,vlayer, fieldIndex, useSelection):
        vprovider = vlayer.dataProvider()
        allAttrs = vprovider.attributeIndexes()
        vprovider.select(allAttrs)
        count = 0
        values = []
        if useSelection:
            selection = vlayer.selectedFeatures()
            for f in selection:
                if f.attributeMap()[fieldIndex].toString() not in values:
                    values.append(f.attributeMap()[fieldIndex].toString())
                    count += 1
        else:
            feat = QgsFeature()
            while vprovider.nextFeature(feat):
                if feat.attributeMap()[fieldIndex].toString() not in values:
                    values.append(feat.attributeMap()[fieldIndex].toString())
                    count += 1
        return count


if __name__ == "__main__":
    import sys
    from mock.mock import Mock
    app = QApplication(sys.argv)
    parent = QWidget()
    layers = []
    for i in range(4):
        layer = Mock()
        layer.name.return_value = "name %d" % (i)
        layers.append(layer)
    parent.layers = layers
    dialog = StatisDialog(parent)
    dialog.show()
    app.exec_()
    print parent.layers[0].method_calls
