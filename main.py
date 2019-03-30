import mainui
from PyQt5 import QtGui, QtCore, QtWidgets
import sys



class MainApp(QtWidgets.QMainWindow, mainui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)

        self._process = QtCore.QProcess(self)
        self._process.readyReadStandardOutput.connect(self.on_readyReadStandardOutput)
        self._process.setProcessChannelMode(QtCore.QProcess.ForwardedChannels)
        self._process.setProgram('bash')
        self._process.setArguments(['-c', 'python3 guiGO.py & python3 liveSpectogram.py &'])

        self.exitapp()
        self.startApp()

    def on_readyReadStandardOutput(self):
        self.output = self._process.readAllStandardOutput()
        print(self.output)


    def startApp(self):
        self.start.clicked.connect(self._process.start)

    def stopApp(self):
        self.stop.clicked.connect(self._process.terminate)

    def exitapp(self):
        self.exit.clicked.connect(QtCore.QCoreApplication.instance().quit)


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = MainApp()
    form.show()
    form.update()  # start with something
    app.exec_()

