# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(806, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.rawAudio = QtGui.QGraphicsView(self.centralwidget)
        self.rawAudio.setObjectName(_fromUtf8("rawAudio"))
        self.verticalLayout.addWidget(self.rawAudio)
        spacerItem = QtGui.QSpacerItem(20, 70, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.fftPlot = QtGui.QGraphicsView(self.centralwidget)
        self.fftPlot.setObjectName(_fromUtf8("fftPlot"))
        self.verticalLayout.addWidget(self.fftPlot)
        self.start = QtGui.QPushButton(self.centralwidget)
        self.start.setObjectName(_fromUtf8("start"))
        self.verticalLayout.addWidget(self.start)
        self.stop = QtGui.QPushButton(self.centralwidget)
        self.stop.setObjectName(_fromUtf8("stop"))
        self.verticalLayout.addWidget(self.stop)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 806, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.start.setText(_translate("MainWindow", "Start!!", None))
        self.stop.setText(_translate("MainWindow", "Stop!!", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
