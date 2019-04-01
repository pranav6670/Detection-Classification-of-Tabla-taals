# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(449, 491)
        font = QtGui.QFont()
        font.setFamily("Tlwg Typo")
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 120, 121, 101))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../tabla_3_125x100.png"))
        self.label.setObjectName("label")
        self.analyze = QtWidgets.QPushButton(self.centralwidget)
        self.analyze.setGeometry(QtCore.QRect(310, 250, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(14)
        self.analyze.setFont(font)
        self.analyze.setStyleSheet("color: rgb(85, 0, 127);")
        self.analyze.setObjectName("analyze")
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setGeometry(QtCore.QRect(160, 140, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(14)
        self.stop.setFont(font)
        self.stop.setStyleSheet("color: rgb(150, 0, 0);\n"
"\n"
"")
        self.stop.setObjectName("stop")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(20, 140, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(14)
        self.start.setFont(font)
        self.start.setAutoFillBackground(True)
        self.start.setStyleSheet("color: rgb(0, 150, 0);\n"
"gridline-color: rgb(255, 170, 0);\n"
"")
        self.start.setObjectName("start")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 10, 411, 91))
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setAutoFillBackground(True)
        self.textBrowser.setStyleSheet("color: rgb(255, 170, 0);")
        self.textBrowser.setObjectName("textBrowser")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(310, 360, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Purisa")
        self.exit.setFont(font)
        self.exit.setStyleSheet("color: rgb(170, 0, 0);\n"
"selection-color: rgb(255, 0, 0);")
        self.exit.setObjectName("exit")
        self.showOP = QtWidgets.QTextEdit(self.centralwidget)
        self.showOP.setGeometry(QtCore.QRect(10, 210, 271, 211))
        self.showOP.setObjectName("showOP")
        self.textBrowser.raise_()
        self.label.raise_()
        self.analyze.raise_()
        self.start.raise_()
        self.stop.raise_()
        self.exit.raise_()
        self.showOP.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 449, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AD&C"))
        self.analyze.setText(_translate("MainWindow", "Analyze"))
        self.stop.setText(_translate("MainWindow", "Stop"))
        self.start.setText(_translate("MainWindow", "Start"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Purisa\'; font-size:16pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Automatic Detection and Classification of Tabla </span><span style=\" font-size:12pt; font-style:italic;\">taalas</span><span style=\" font-size:12pt;\"> from Indian Classical Music</span></p></body></html>"))
        self.exit.setText(_translate("MainWindow", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

