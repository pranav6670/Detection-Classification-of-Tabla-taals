# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_1.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(757, 621)
        font = QtGui.QFont()
        font.setFamily("Tlwg Typo")
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../50211-200_24x24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 240, 237);")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(600, 340, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setBold(True)
        font.setWeight(75)
        self.exit.setFont(font)
        self.exit.setStyleSheet("QPushButton {\n"
"color: rgb(170, 0, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 13px;\n"
"background-color: rgb(255, 51, 51);\n"
"border-color: black;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(255, 138, 138);\n"
"}    ")
        self.exit.setObjectName("exit")
        self.title1 = QtWidgets.QLabel(self.centralwidget)
        self.title1.setGeometry(QtCore.QRect(0, 0, 711, 31))
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
        self.title2.setGeometry(QtCore.QRect(0, 32, 511, 31))
        font = QtGui.QFont()
        font.setFamily("Courier 10 Pitch")
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.title2.setFont(font)
        self.title2.setStyleSheet("color: rgb(0, 0, 127);")
        self.title2.setObjectName("title2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(260, 114, 111, 121))
        self.frame.setStyleSheet(".QFrame#frame{\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"background-color: rgb(205, 255, 193);\n"
"border-radius: 13px;\n"
"border-color: rgb(0, 0, 0);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.start = QtWidgets.QPushButton(self.frame)
        self.start.setGeometry(QtCore.QRect(15, 13, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        self.start.setFont(font)
        self.start.setAutoFillBackground(False)
        self.start.setStyleSheet("QPushButton {\n"
"    background-color: rgb(187, 255, 176); \n"
"    color: rgb(0, 170, 0); \n"
"        border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 13px;\n"
"    border-color: black;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(151, 255, 128);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(85, 255, 0);\n"
"}    ")
        self.start.setObjectName("start")
        self.stop = QtWidgets.QPushButton(self.frame)
        self.stop.setGeometry(QtCore.QRect(15, 67, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.stop.setFont(font)
        self.stop.setStyleSheet("QPushButton {\n"
"color: rgb(150, 0, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 13px;\n"
"border-color: black;\n"
"background-color: rgb(255, 119, 121);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 99, 78);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(255, 52, 52);\n"
"}    \n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.stop.setObjectName("stop")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 270, 221, 111))
        self.frame_2.setStyleSheet(".QFrame#frame_2{\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"background-color: rgb(167, 254, 255);\n"
"border-radius: 13px;\n"
"border-color: rgb(0, 0, 0);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.margin_har = QtWidgets.QSpinBox(self.frame_2)
        self.margin_har.setGeometry(QtCore.QRect(20, 60, 61, 41))
        self.margin_har.setStyleSheet("QSpinBox {\n"
"background-color: rgb(255, 254, 199);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"}\n"
"QSpinBox:up-button:hover {\n"
"background-color: rgb(202, 255, 179);\n"
"}\n"
"\n"
"QSpinBox:up-button:pressed {\n"
"background-color: rgb(39, 255, 6);\n"
"}\n"
"\n"
"QSpinBox:down-button:hover {\n"
"background-color: rgb(255, 138, 140);\n"
"}\n"
"\n"
"QSpinBox:down-button:pressed {\n"
"background-color: rgb(255, 26, 29);\n"
"}\n"
"")
        self.margin_har.setObjectName("margin_har")
        self.margin_per = QtWidgets.QSpinBox(self.frame_2)
        self.margin_per.setGeometry(QtCore.QRect(20, 10, 61, 41))
        self.margin_per.setStyleSheet("QSpinBox {\n"
"background-color: rgb(199, 202, 255);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"}\n"
"QSpinBox:up-button:hover {\n"
"background-color: rgb(202, 255, 179);\n"
"}\n"
"\n"
"QSpinBox:up-button:pressed {\n"
"background-color: rgb(39, 255, 6);\n"
"}\n"
"\n"
"QSpinBox:down-button:hover {\n"
"background-color: rgb(255, 138, 140);\n"
"}\n"
"\n"
"QSpinBox:down-button:pressed {\n"
"background-color: rgb(255, 26, 29);\n"
"}\n"
"")
        self.margin_per.setObjectName("margin_per")
        self.hpss = QtWidgets.QPushButton(self.frame_2)
        self.hpss.setGeometry(QtCore.QRect(100, 10, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setUnderline(False)
        self.hpss.setFont(font)
        self.hpss.setStyleSheet("QPushButton {\n"
"border-style: outset;\n"
"color: rgb(170, 85, 255);\n"
"border-width: 2px;\n"
"border-radius: 13px;\n"
"background-color: rgb(170, 170, 255);\n"
"border-color: black;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(255, 76, 241);\n"
"}    ")
        self.hpss.setObjectName("hpss")
        self.plot_hpss = QtWidgets.QPushButton(self.frame_2)
        self.plot_hpss.setGeometry(QtCore.QRect(100, 60, 101, 41))
        self.plot_hpss.setStyleSheet("QPushButton {\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"color: rgb(255, 85, 0);\n"
"border-radius: 13px;\n"
"border-color: black;\n"
"background-color: rgb(255, 170, 127);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 170, 0);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(255, 76, 241);\n"
"}    ")
        self.plot_hpss.setObjectName("plot_hpss")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(10, 429, 311, 131))
        self.frame_3.setStyleSheet("border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 13px;\n"
"background-color: rgb(249, 255, 181);\n"
"border-color: black;\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.optaala = QtWidgets.QTextEdit(self.frame_3)
        self.optaala.setGeometry(QtCore.QRect(190, 70, 111, 41))
        self.optaala.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 1px;\n"
"border-color: black;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
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
        self.recordlabel.setGeometry(QtCore.QRect(40, 90, 71, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.recordlabel.setFont(font)
        self.recordlabel.setStyleSheet("color: rgb(255, 0, 0);")
        self.recordlabel.setObjectName("recordlabel")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(13, 245, 251, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 0, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 408, 81, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_3.setObjectName("label_3")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(260, 90, 121, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(0, 170, 0);")
        self.label_9.setObjectName("label_9")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(10, 114, 241, 121))
        self.frame_4.setStyleSheet(".QFrame#frame_4{\n"
" border-style: outset;\n"
" background-color: rgb(255, 203, 193);\n"
" border-width: 2px;\n"
" border-radius: 13px;\n"
" border-color: rgb(0, 0, 0);\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_10 = QtWidgets.QLabel(self.frame_4)
        self.label_10.setGeometry(QtCore.QRect(10, 20, 151, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(170, 0, 0);\n"
"border-style: outset;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"border-color: rgb(0, 0, 0);\n"
" background-color: rgb(255, 203, 193);\n"
"")
        self.label_10.setObjectName("label_10")
        self.ip_rec = QtWidgets.QDial(self.frame_4)
        self.ip_rec.setGeometry(QtCore.QRect(20, 50, 51, 61))
        self.ip_rec.setStyleSheet("background-color: rgb(255, 98, 101);")
        self.ip_rec.setObjectName("ip_rec")
        self.recop = QtWidgets.QTextEdit(self.frame_4)
        self.recop.setGeometry(QtCore.QRect(160, 16, 61, 31))
        self.recop.setStyleSheet("color: rgb(170, 0, 0);\n"
"border-style: outset;\n"
"border-width: 0px;\n"
"background-color: rgb(255, 203, 193);\n"
"border-radius: 1px;\n"
"border-color: black;\n"
"")
        self.recop.setObjectName("recop")
        self.rec_start = QtWidgets.QPushButton(self.frame_4)
        self.rec_start.setGeometry(QtCore.QRect(93, 57, 131, 51))
        self.rec_start.setStyleSheet("QPushButton {\n"
"    background-color: rgb(187, 255, 176); \n"
"    color: rgb(0, 170, 0); \n"
"        border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 13px;\n"
"    border-color: black;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(151, 255, 128);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(85, 255, 0);\n"
"}    ")
        self.rec_start.setObjectName("rec_start")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(330, 510, 281, 51))
        self.label_11.setStyleSheet("border-style: outset;\n"
"color: rgb(0, 0, 0);\n"
"border-width: 1px;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 1px;\n"
"border-color: black;\n"
"")
        self.label_11.setObjectName("label_11")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(250, 250, 241, 131))
        self.frame_5.setStyleSheet(".QFrame#frame_5{\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 13px;\n"
"border-color: rgb(0, 0, 0);\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 61, 17))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(200, 14, 7)")
        self.label_4.setObjectName("label_4")
        self.status = QtWidgets.QTextEdit(self.frame_5)
        self.status.setGeometry(QtCore.QRect(81, 10, 151, 38))
        self.status.setStyleSheet("color: rgb(0, 150, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 13px;\n"
"border-color: black;\n"
"background-color: rgb(255, 217, 212);")
        self.status.setObjectName("status")
        self.marginvalue_per = QtWidgets.QTextBrowser(self.frame_5)
        self.marginvalue_per.setGeometry(QtCore.QRect(10, 60, 61, 31))
        self.marginvalue_per.setStyleSheet("border-style: outset;\n"
"border-width: 1px;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 1px;\n"
"border-color: black;\n"
"")
        self.marginvalue_per.setObjectName("marginvalue_per")
        self.marginvalue_har = QtWidgets.QTextEdit(self.frame_5)
        self.marginvalue_har.setGeometry(QtCore.QRect(80, 60, 61, 31))
        self.marginvalue_har.setStyleSheet("border-style: outset;\n"
"border-width: 1px;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 1px;\n"
"border-color: black;\n"
"")
        self.marginvalue_har.setObjectName("marginvalue_har")
        self.text_margin = QtWidgets.QLabel(self.frame_5)
        self.text_margin.setGeometry(QtCore.QRect(80, 93, 71, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(8)
        self.text_margin.setFont(font)
        self.text_margin.setStyleSheet("border-style: outset;\n"
"color: rgb(85, 0, 0);\n"
"border-width: 0px;\n"
"border-radius: 1px;\n"
"border-color: black;\n"
"")
        self.text_margin.setObjectName("text_margin")
        self.label_6 = QtWidgets.QLabel(self.frame_5)
        self.label_6.setGeometry(QtCore.QRect(10, 93, 61, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border-style: outset;\n"
"color: rgb(85, 0, 0);\n"
"border-width: 0px;\n"
"border-radius: 1px;\n"
"border-color: black;\n"
"")
        self.label_6.setObjectName("label_6")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 386, 701, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(370, 400, 221, 31))
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(510, 22, 201, 121))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("50211-200.png"))
        self.label.setObjectName("label")
        self.label.raise_()
        self.frame_4.raise_()
        self.frame_3.raise_()
        self.frame_2.raise_()
        self.frame.raise_()
        self.exit.raise_()
        self.title1.raise_()
        self.title2.raise_()
        self.recordlabel.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_9.raise_()
        self.label_11.raise_()
        self.frame_5.raise_()
        self.line.raise_()
        self.label_7.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 757, 25))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AD&C"))
        self.exit.setText(_translate("MainWindow", "Quit"))
        self.title1.setText(_translate("MainWindow", " Automatic Detection and Classification of Tabla"))
        self.title2.setText(_translate("MainWindow", " taalas from Indian Classical Music "))
        self.start.setText(_translate("MainWindow", "Start"))
        self.stop.setText(_translate("MainWindow", "Stop"))
        self.hpss.setText(_translate("MainWindow", "Separate"))
        self.plot_hpss.setText(_translate("MainWindow", "Show plots"))
        self.label_5.setText(_translate("MainWindow", "Classified Tabla taal :-"))
        self.analyze.setText(_translate("MainWindow", "Analyze"))
        self.recordlabel.setText(_translate("MainWindow", "Recording"))
        self.label_2.setText(_translate("MainWindow", "Harmonic & Percussive Separation"))
        self.label_3.setText(_translate("MainWindow", "Prediction"))
        self.label_9.setText(_translate("MainWindow", "Visualizations"))
        self.label_10.setText(_translate("MainWindow", "Number of seconds"))
        self.rec_start.setText(_translate("MainWindow", "Start"))
        self.label_11.setText(_translate("MainWindow", "This space is left blank for further usage"))
        self.label_4.setText(_translate("MainWindow", "Status :-"))
        self.text_margin.setText(_translate("MainWindow", "Margin @Har"))
        self.label_6.setText(_translate("MainWindow", "Margin @Per "))
        self.label_7.setText(_translate("MainWindow", "Area under devlopment"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
