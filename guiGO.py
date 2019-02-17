import GUI
from PyQt4 import QtGui, QtCore
import audioBackend
import numpy as np
import sys
import time
import pyqtgraph


class ExampleApp(QtGui.QMainWindow, GUI.Ui_MainWindow):

    def __init__(self, parent=None):
        pyqtgraph.setConfigOption('background', 'w')
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.raw.plotItem.showGrid(True, True, 0.7)
        self.FFT.plotItem.showGrid(True, True, 0.7)
        self.maxFFT = 0
        self.maxPCM = 0
        self.ear = audioBackend.PNstream()

    def update(self):

        # rawdata = self.ear.data
        # FFTdata = self.ear.fftx
        self.maxFFT = np.max(np.abs(self.ear.fft))
        pen = pyqtgraph.mkPen(color='g')
        self.raw.plot(self.ear.data, self.ear.data_int, pen=pen, clear=True)
        pen = pyqtgraph.mkPen(color='r')
        self.FFT.plot(self.ear.fftx, self.ear.fft / self.maxFFT, pen=pen, clear=True )
        QtCore.QTimer.singleShot(1, self.update)  # QUICKLY repeat





if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    form.update()
    app.show()#start with something
    app.exec_()
    print("DONE")

