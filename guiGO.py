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
        self.hear = audioBackend.PNstream(rate=44100, updatesPerSecond=20)
        self.hear.stream_start()
        self.maxraw = 0
        self.maxFFT = 0

    def update(self):
        if not self.hear.data is None and not self.hear.fft is None:

            maxraw = np.max(np.abs(self.hear.data))
            if maxraw > self.maxraw:
                self.maxraw = maxraw
                self.raw.plotItem.setRange(yRange=[-maxraw, maxraw])

            if np.max(self.hear.fft) > self.maxFFT:
                self.maxFFT = np.max(np.abs(self.hear.fft))
                self.FFT.plotItem.setRange(yRange=[0, 1])

            pen = pyqtgraph.mkPen(color='r')
            self.raw.plot(self.hear.datax, self.hear.data, pen=pen, clear=True)
            pen = pyqtgraph.mkPen(color='r')
            self.grFFT.plot(self.hear.fftx, self.hear.fft/self.maxFFT, pen=pen, clear=True)
        QtCore.QTimer.singleShot(1, self.update)  # QUICKLY repeat


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    form.update() #start with something
    app.exec_()
    print("DONE")