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
        MainWindow.resize(733, 625)
        font = QtGui.QFont()
        font.setFamily("Tlwg Typo")
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(530, 440, 171, 81))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setBold(True)
        font.setWeight(75)
        self.exit.setFont(font)
        self.exit.setStyleSheet("color: rgb(170, 0, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 13px;\n"
"background-color: rgb(255, 51, 51);\n"
"border-color: black;\n"
"")
        self.exit.setObjectName("exit")
        self.title1 = QtWidgets.QLabel(self.centralwidget)
        self.title1.setGeometry(QtCore.QRect(0, 10, 711, 31))
        font = QtGui.QFont()
        font.setFamily("Courier 10 Pitch")
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.title1.setFont(font)
        self.title1.setStyleSheet("color: rgb(0, 0, 127);")
        self.title1.setObjectName("title1")
        self.title2 = QtWidgets.QLabel(self.centralwidget)
        self.title2.setGeometry(QtCore.QRect(0, 30, 551, 51))
        font = QtGui.QFont()
        font.setFamily("Courier 10 Pitch")
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.title2.setFont(font)
        self.title2.setStyleSheet("color: rgb(0, 0, 127);")
        self.title2.setObjectName("title2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(520, 40, 201, 121))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Tabla_2_200x130.jpg"))
        self.label.setObjectName("label")
        self.status = QtWidgets.QTextEdit(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(520, 200, 201, 31))
        self.status.setStyleSheet("border-style: outset;\n"
"border-width: 1px;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 1px;\n"
"border-color: black;\n"
"")
        self.status.setObjectName("status")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(442, 205, 61, 17))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(200, 14, 7)")
        self.label_4.setObjectName("label_4")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(500, 270, 221, 131))
        self.frame.setStyleSheet("border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 13px;\n"
"border-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.start = QtWidgets.QPushButton(self.frame)
        self.start.setGeometry(QtCore.QRect(30, 16, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        self.start.setFont(font)
        self.start.setAutoFillBackground(False)
        self.start.setStyleSheet("color: rgb(0, 150, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"background-color: rgb(187, 255, 176);\n"
"border-radius: 13px;\n"
"border-color: black;\n"
"")
        self.start.setObjectName("start")
        self.stop = QtWidgets.QPushButton(self.frame)
        self.stop.setGeometry(QtCore.QRect(30, 73, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.stop.setFont(font)
        self.stop.setStyleSheet("color: rgb(150, 0, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"background-color: rgb(255, 119, 121);\n"
"border-radius: 13px;\n"
"border-color: black;\n"
"\n"
"")
        self.stop.setObjectName("stop")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 270, 481, 131))
        self.frame_2.setStyleSheet("border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 13px;\n"
"border-color: rgb(0, 0, 0);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.hpss = QtWidgets.QPushButton(self.frame_2)
        self.hpss.setGeometry(QtCore.QRect(110, 14, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setUnderline(False)
        self.hpss.setFont(font)
        self.hpss.setStyleSheet("border-style: outset;\n"
"color: rgb(170, 85, 255);\n"
"border-width: 2px;\n"
"border-radius: 13px;\n"
"background-color: rgb(170, 170, 255);\n"
"border-color: black;\n"
"")
        self.hpss.setObjectName("hpss")
        self.margin_per = QtWidgets.QSpinBox(self.frame_2)
        self.margin_per.setGeometry(QtCore.QRect(20, 10, 60, 41))
        self.margin_per.setStyleSheet("border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 0px;\n"
"border-color: black;\n"
"")
        self.margin_per.setObjectName("margin_per")
        self.margin_har = QtWidgets.QSpinBox(self.frame_2)
        self.margin_har.setGeometry(QtCore.QRect(20, 71, 60, 41))
        self.margin_har.setStyleSheet("border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 0px;\n"
"border-color: black;\n"
"")
        self.margin_har.setObjectName("margin_har")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(11, 49, 91, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 85, 255);\n"
"border-style: outset;\n"
"border-width: 0px;\n"
"border-radius: 1px;\n"
"border-color: black;\n"
"")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(10, 110, 141, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(85, 170, 127);\n"
"border-style: outset;\n"
"border-width: 0px;\n"
"border-radius: 2px;\n"
"border-color: black;\n"
"")
        self.label_8.setObjectName("label_8")
        self.marginvalue_per = QtWidgets.QTextBrowser(self.frame_2)
        self.marginvalue_per.setGeometry(QtCore.QRect(400, 10, 61, 41))
        self.marginvalue_per.setStyleSheet("border-style: outset;\n"
"border-width: 1px;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 1px;\n"
"border-color: black;\n"
"")
        self.marginvalue_per.setObjectName("marginvalue_per")
        self.marginvalue_har = QtWidgets.QTextEdit(self.frame_2)
        self.marginvalue_har.setGeometry(QtCore.QRect(400, 74, 61, 41))
        self.marginvalue_har.setStyleSheet("border-style: outset;\n"
"border-width: 1px;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 1px;\n"
"border-color: black;\n"
"")
        self.marginvalue_har.setObjectName("marginvalue_har")
        self.text_margin = QtWidgets.QLabel(self.frame_2)
        self.text_margin.setGeometry(QtCore.QRect(280, 85, 111, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.text_margin.setFont(font)
        self.text_margin.setStyleSheet("color: rgb(255, 85, 127);\n"
"border-style: outset;\n"
"border-width: 0px;\n"
"border-radius: 1px;\n"
"border-color: black;\n"
"")
        self.text_margin.setObjectName("text_margin")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(280, 20, 131, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 0, 127);\n"
"border-style: outset;\n"
"border-width: 0px;\n"
"border-radius: 1px;\n"
"border-color: black;\n"
"")
        self.label_6.setObjectName("label_6")
        self.plot_hpss = QtWidgets.QPushButton(self.frame_2)
        self.plot_hpss.setGeometry(QtCore.QRect(110, 75, 161, 41))
        self.plot_hpss.setStyleSheet("border-style: outset;\n"
"border-width: 2px;\n"
"color: rgb(255, 85, 0);\n"
"border-radius: 13px;\n"
"border-color: black;\n"
"background-color: rgb(255, 170, 127);\n"
"")
        self.plot_hpss.setObjectName("plot_hpss")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(10, 429, 421, 131))
        self.frame_3.setStyleSheet("border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 13px;\n"
"border-color: black;\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.optaala = QtWidgets.QTextEdit(self.frame_3)
        self.optaala.setGeometry(QtCore.QRect(180, 70, 231, 41))
        self.optaala.setStyleSheet("border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color: black;\n"
"")
        self.optaala.setObjectName("optaala")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(10, 74, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 85, 0);\n"
"border-style: outset;\n"
"border-width: 0px;\n"
"border-radius: 2px;\n"
"border-color: black;\n"
"")
        self.label_5.setObjectName("label_5")
        self.analyze = QtWidgets.QPushButton(self.frame_3)
        self.analyze.setGeometry(QtCore.QRect(10, 20, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        self.analyze.setFont(font)
        self.analyze.setStyleSheet("border-style: outset;\n"
"color: rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"border-radius: 13px;\n"
"border-color: black;\n"
"background-color: rgb(0, 170, 127);")
        self.analyze.setObjectName("analyze")
        self.recordlabel = QtWidgets.QLabel(self.centralwidget)
        self.recordlabel.setGeometry(QtCore.QRect(10, 88, 101, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.recordlabel.setFont(font)
        self.recordlabel.setStyleSheet("color: rgb(255, 0, 0);")
        self.recordlabel.setObjectName("recordlabel")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 245, 311, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 0, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 408, 101, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_3.setObjectName("label_3")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(510, 247, 121, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(0, 170, 0);")
        self.label_9.setObjectName("label_9")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(10, 114, 341, 121))
        self.frame_4.setStyleSheet("border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 13px;\n"
"border-color: rgb(0, 0, 0);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_10 = QtWidgets.QLabel(self.frame_4)
        self.label_10.setGeometry(QtCore.QRect(20, 26, 151, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(170, 0, 0);\n"
"border-style: outset;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"border-color: rgb(0, 0, 0);")
        self.label_10.setObjectName("label_10")
        self.rec_start = QtWidgets.QPushButton(self.frame_4)
        self.rec_start.setGeometry(QtCore.QRect(83, 68, 161, 41))
        self.rec_start.setStyleSheet("border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 13px;\n"
"border-color: black;\n"
"background-color: rgb(187, 255, 176);\n"
"color: rgb(0, 170, 0);\n"
"")
        self.rec_start.setObjectName("rec_start")
        self.ip_rec = QtWidgets.QDial(self.frame_4)
        self.ip_rec.setGeometry(QtCore.QRect(178, 2, 51, 61))
        self.ip_rec.setObjectName("ip_rec")
        self.recop = QtWidgets.QTextEdit(self.frame_4)
        self.recop.setGeometry(QtCore.QRect(250, 18, 71, 31))
        self.recop.setStyleSheet("border-style: outset;\n"
"border-width: 1px;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 1px;\n"
"border-color: black;\n"
"")
        self.recop.setObjectName("recop")
        self.frame_4.raise_()
        self.frame_3.raise_()
        self.frame_2.raise_()
        self.frame.raise_()
        self.exit.raise_()
        self.title1.raise_()
        self.title2.raise_()
        self.label.raise_()
        self.status.raise_()
        self.label_4.raise_()
        self.recordlabel.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_9.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 733, 26))
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
        self.exit.setText(_translate("MainWindow", "Quit"))
        self.title1.setText(_translate("MainWindow", " Automatic Detection and Classification of Tabla"))
        self.title2.setText(_translate("MainWindow", " taalas from Indian Classical Music "))
        self.label_4.setText(_translate("MainWindow", "Status :-"))
        self.start.setText(_translate("MainWindow", "Start"))
        self.stop.setText(_translate("MainWindow", "Stop"))
        self.hpss.setText(_translate("MainWindow", "Separate"))
        self.label_7.setText(_translate("MainWindow", "Percussive margin"))
        self.label_8.setText(_translate("MainWindow", "Harmonic margin"))
        self.text_margin.setText(_translate("MainWindow", "Margin @Har:-"))
        self.label_6.setText(_translate("MainWindow", "Margin @Per :-"))
        self.plot_hpss.setText(_translate("MainWindow", "Show plots"))
        self.label_5.setText(_translate("MainWindow", "Classified Tabla taal :-"))
        self.analyze.setText(_translate("MainWindow", "Analyze"))
        self.recordlabel.setText(_translate("MainWindow", "Recording"))
        self.label_2.setText(_translate("MainWindow", "Harmonic & Percussive Separation"))
        self.label_3.setText(_translate("MainWindow", "Prediction"))
        self.label_9.setText(_translate("MainWindow", "Visualizations"))
        self.label_10.setText(_translate("MainWindow", "Number of seconds"))
        self.rec_start.setText(_translate("MainWindow", "Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

