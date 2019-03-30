# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '3way.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(606, 532)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.raw = PlotWidget(self.centralwidget)
        self.raw.setGeometry(QtCore.QRect(20, 80, 561, 161))
        self.raw.setObjectName("raw")
        self.FFT = PlotWidget(self.centralwidget)
        self.FFT.setGeometry(QtCore.QRect(20, 310, 561, 161))
        self.FFT.setObjectName("FFT")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(18)
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 0, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 260, 68, 31))
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(18)
        font.setUnderline(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 170, 255);")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 606, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "*Raw audio"))
        self.label_2.setText(_translate("MainWindow", "*FFT"))

from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

