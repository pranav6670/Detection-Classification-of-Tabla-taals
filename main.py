import mainui
from PyQt5 import QtGui, QtCore

class MainApp(QtGui.QMainWindow, mainui.Ui_MainWindow):
    def __init__(self):
        print("test")