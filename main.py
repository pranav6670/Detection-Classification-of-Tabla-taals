import mainui
from PyQt5 import QtGui, QtCore, QtWidgets
import librosa

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

        self.status.setFont(QtGui.QFont("Trebuchet MS", 10))
        self.startApp()
        self.stopApp()
        self.exitapp()
        self.margincalc()
        self.onseparateclick()

    def on_readyReadStandardOutput(self):
        self.output = self.sender().readAllStandardOutput()
        print(self.output)

    def margincalc(self):
        self.margin.setMinimum(0)
        self.margin.setMaximum(10)
        self.margin.valueChanged.connect(self.valuechange)

    def valuechange(self):
        self.marginvalue.setTextColor(QtGui.QColor(255, 0, 0))
        self.font = QtGui.QFont()
        self.font.setFamily("Trebuchet MS")
        self.font.setPointSize(18)
        self.marginvalue.setFont(self.font)
        self.marginvalue.setText(str(self.margin.value()))

    def hpssop(self):
        self.file = "file.wav"
        self.y, self.sr = librosa.load(self.file)
        self.margin_hpss = self.margin.value()
        self.harmonic, self.percussive = librosa.effects.hpss(self.y, margin=self.margin_hpss)
        librosa.output.write_wav("harmonic.wav", self.harmonic, self.sr)
        librosa.output.write_wav("percussive.wav", self.percussive, self.sr)

    def onseparateclick(self):
        self.hpss.clicked.connect(self.hpssop)

    def startApp(self):
        for process in self._processes:
            self.start.clicked.connect(process.start)
            self.start.clicked.connect(self.onstartclicked)

    def onstartclicked(self):
        self.status.setTextColor(QtGui.QColor(0, 250, 0))
        self.text = "Recording Started"
        self.status.setText(self.text)

    def stopApp(self):
        for process in self._processes:
            self.stop.clicked.connect(process.kill)
            self.stop.clicked.connect(self.onstopclicked)

    def onstopclicked(self):
        self.status.setTextColor(QtGui.QColor(250, 0, 0))
        self.text = "Recording Stopped"
        self.status.setText(self.text)

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
