import mainui
from PyQt5 import QtGui, QtCore, QtWidgets
import sys


class MainApp(QtWidgets.QMainWindow, mainui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)

        self._scripts = ("guiGO.py", "liveSpectogram.py", "recordAudio.py")
        self._processes = []
        for script in self._scripts:
            process = QtCore.QProcess(self)
            process.readyReadStandardOutput.connect(self.on_readyReadStandardOutput)
            process.setProcessChannelMode(QtCore.QProcess.ForwardedChannels)
            process.setProgram('bash')
            process.setArguments(['-c', 'python3 {}'.format(script)])
            self._processes.append(process)

        self.exitapp()
        self.startApp()
        self.stopApp()

    def on_readyReadStandardOutput(self):
        self.output = self.sender().readAllStandardOutput()
        print(self.output)

    def startApp(self):
        for process in self._processes:
            self.start.clicked.connect(process.start)
            # self.start.clicked.connect(self.onstartclicked)

    def onstartclicked(self):
        self.text = "Recording Started"
        self.showOP.setText(self.text)

    def stopApp(self):
        for process in self._processes:
            self.stop.clicked.connect(process.kill)

    def exitapp(self):
        self.exit.clicked.connect(self.close)

    def closeEvent(self, event):
        for script in self._scripts:
            QtCore.QProcess.startDetached("bash", ["-c", "pkill -f {}".format(script)])
        super(MainApp, self).closeEvent(event)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainApp()
    w.show()
    sys.exit(app.exec_())
    print("Done")

