import mainui
from PyQt5 import QtGui, QtCore, QtWidgets
import sys
import subprocess


class MainApp(QtWidgets.QMainWindow, mainui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)
        self.startApp()
        self.exitapp()

    def multipleopen(self):
        self.output = subprocess.check_output(['bash', '-c', "python3 guiGO.py & python3 liveSpectogram.py &"])

    def startApp(self):
        self.start.clicked.connect(self.multipleopen)

    def exitapp(self):
        self.exit.clicked.connect(QtCore.QCoreApplication.instance().quit)


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = MainApp()
    form.show()
    form.update()  # start with something
    app.exec_()
    print("DONE")
