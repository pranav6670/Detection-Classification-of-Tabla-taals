import GUI
from PyQt4 import QtGui, QtCore

import numpy as np
import sys
import time
import pyqtgraph


class ExampleApp(QtGui.QMainWindow, GUI.Ui_MainWindow):

    def __init__(self, parent=None):
        pyqtgraph.setConfigOption('background', 'w')
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.grFFT.plotItem.showGrid(True, True, 0.7)
        self.grPCM.plotItem.showGrid(True, True, 0.7)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    form.update() #start with something
    app.exec_()
    print("DONE")