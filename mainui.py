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
        MainWindow.resize(793, 623)
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
        self.exit.setGeometry(QtCore.QRect(670, 486, 101, 71))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setBold(True)
        font.setWeight(75)
        self.exit.setFont(font)
        self.exit.setStyleSheet("QPushButton {\n"
"color: rgb(170, 0, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30px;\n"
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
        self.title1.setGeometry(QtCore.QRect(0, 10, 741, 31))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.title1.setFont(font)
        self.title1.setStyleSheet("color: rgb(0, 0, 127);\n"
"font: 12pt \"Comfortaa\";")
        self.title1.setObjectName("title1")
        self.title2 = QtWidgets.QLabel(self.centralwidget)
        self.title2.setGeometry(QtCore.QRect(7, 50, 541, 31))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.title2.setFont(font)
        self.title2.setStyleSheet("color: rgb(0, 0, 127);\n"
"font: 12pt \"Comfortaa\";")
        self.title2.setObjectName("title2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 290, 111, 121))
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
"\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(85, 255, 0);\n"
"\n"
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
"\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(255, 52, 52);\n"
"\n"
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
        self.frame_2.setGeometry(QtCore.QRect(144, 295, 221, 111))
        self.frame_2.setStyleSheet(".QFrame#frame_2{\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 13px;\n"
"    background-color: rgb(206, 234, 255);\n"
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
        self.margin_har.setSingleStep(1)
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
        self.frame_3.setGeometry(QtCore.QRect(10, 454, 311, 131))
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
        self.optaala.setGeometry(QtCore.QRect(190, 72, 111, 41))
        self.optaala.setStyleSheet("\n"
"background-color: rgb(249, 255, 181);\n"
"border-radius: 1px;\n"
"border-color: black;\n"
"border-style: outset;\n"
"border-width: 0px;\n"
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
        self.analyze.setStyleSheet("\n"
"QPushButton {\n"
"border-style: outset;\n"
"color: rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"border-radius: 13px;\n"
"border-color: black;\n"
"background-color: rgb(0, 170, 127);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(187, 255, 176); \n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(255, 76, 241);\n"
"}    ")
        self.analyze.setObjectName("analyze")
        self.recordlabel = QtWidgets.QLabel(self.centralwidget)
        self.recordlabel.setGeometry(QtCore.QRect(80, 108, 71, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.recordlabel.setFont(font)
        self.recordlabel.setStyleSheet("color: rgb(255, 0, 0);")
        self.recordlabel.setObjectName("recordlabel")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(155, 270, 191, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 0, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 432, 81, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_3.setObjectName("label_3")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(17, 270, 101, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(0, 170, 0);")
        self.label_9.setObjectName("label_9")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(10, 130, 241, 121))
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
        self.ip_rec.setGeometry(QtCore.QRect(20, 50, 61, 61))
        self.ip_rec.setStyleSheet("background-color: rgb(255, 98, 101);")
        self.ip_rec.setObjectName("ip_rec")
        self.rec_start = QtWidgets.QPushButton(self.frame_4)
        self.rec_start.setGeometry(QtCore.QRect(93, 67, 131, 41))
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
"    border-color: green;\n"
"\n"
"}    ")
        self.rec_start.setObjectName("rec_start")
        self.recop = QtWidgets.QTextEdit(self.frame_4)
        self.recop.setGeometry(QtCore.QRect(151, 16, 71, 31))
        self.recop.setStyleSheet("border-style: outset;\n"
"color: rgb(170, 0, 0);\n"
"background-color: rgb(255, 203, 193);\n"
"border-width: 0px;\n"
"border-radius: 13px;\n"
"border-color: rgb(0, 0, 0);")
        self.recop.setObjectName("recop")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(278, 123, 261, 121))
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
        self.status.setGeometry(QtCore.QRect(81, 14, 171, 40))
        self.status.setStyleSheet("color: rgb(0, 150, 0);\n"
"border-style: outset;\n"
"border-width: 0px;\n"
"border-radius: 13px;\n"
"border-color: black;\n"
"background-color: rgb(255, 240, 237);")
        self.status.setObjectName("status")
        self.marginvalue_per = QtWidgets.QTextBrowser(self.frame_5)
        self.marginvalue_per.setGeometry(QtCore.QRect(10, 60, 61, 31))
        self.marginvalue_per.setStyleSheet("border-style: outset;\n"
"border-width: 0px;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 1px;\n"
"border-color: black;\n"
"background-color: rgb(255, 240, 237);\n"
"")
        self.marginvalue_per.setObjectName("marginvalue_per")
        self.marginvalue_har = QtWidgets.QTextEdit(self.frame_5)
        self.marginvalue_har.setGeometry(QtCore.QRect(80, 60, 61, 31))
        self.marginvalue_har.setStyleSheet("border-style: outset;\n"
"border-width: 0px;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 1px;\n"
"border-color: black;\n"
"background-color: rgb(255, 240, 237);")
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(570, 90, 191, 151))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("final_tabla.png"))
        self.label.setObjectName("label")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(390, 300, 381, 91))
        self.frame_6.setStyleSheet(".QFrame#frame_6{\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"background-color: rgb(255, 240, 237);\n"
"border-radius: 13px;\n"
"border-color: rgb(0, 0, 0);\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.datadis = QtWidgets.QPushButton(self.frame_6)
        self.datadis.setGeometry(QtCore.QRect(9, 10, 131, 27))
        self.datadis.setStyleSheet("QPushButton {\n"
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
"    border-color: green;\n"
"\n"
"}    ")
        self.datadis.setObjectName("datadis")
        self.mfcccoe = QtWidgets.QPushButton(self.frame_6)
        self.mfcccoe.setGeometry(QtCore.QRect(10, 50, 171, 27))
        self.mfcccoe.setStyleSheet("\n"
"QPushButton {\n"
"border-style: outset;\n"
"color: rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"border-radius: 13px;\n"
"border-color: black;\n"
"background-color: rgb(0, 170, 127);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(187, 255, 176); \n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(255, 76, 241);\n"
"}    ")
        self.mfcccoe.setObjectName("mfcccoe")
        self.fastft = QtWidgets.QPushButton(self.frame_6)
        self.fastft.setGeometry(QtCore.QRect(270, 10, 91, 27))
        self.fastft.setStyleSheet("QPushButton {\n"
"color: rgb(150, 0, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 13px;\n"
"border-color: black;\n"
"background-color: rgb(255, 119, 121);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 99, 78);\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(255, 52, 52);\n"
"\n"
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
        self.fastft.setObjectName("fastft")
        self.timedata = QtWidgets.QPushButton(self.frame_6)
        self.timedata.setGeometry(QtCore.QRect(150, 10, 111, 27))
        self.timedata.setStyleSheet("QPushButton {\n"
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
        self.timedata.setObjectName("timedata")
        self.fbe = QtWidgets.QPushButton(self.frame_6)
        self.fbe.setGeometry(QtCore.QRect(190, 50, 171, 27))
        self.fbe.setStyleSheet("QPushButton {\n"
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
        self.fbe.setObjectName("fbe")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(510, 270, 141, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 170, 0);")
        self.label_7.setObjectName("label_7")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(120, 268, 20, 151))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(370, 268, 20, 151))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(0, 254, 781, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(10, 418, 771, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(256, 110, 20, 141))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(540, 50, 20, 211))
        self.line_6.setStyleSheet("")
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(0, 96, 541, 16))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(550, 40, 231, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(770, 50, 20, 211))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(328, 430, 20, 181))
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        self.frame_7.setGeometry(QtCore.QRect(360, 460, 271, 111))
        self.frame_7.setStyleSheet(".QFrame#frame_7{\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"background-color: rgb(255, 240, 237);\n"
"border-radius: 13px;\n"
"border-color: rgb(0, 0, 0);\n"
"}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.cnn_sum = QtWidgets.QPushButton(self.frame_7)
        self.cnn_sum.setGeometry(QtCore.QRect(10, 10, 120, 40))
        self.cnn_sum.setStyleSheet("QPushButton {\n"
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
"    border-color: green;\n"
"\n"
"}    ")
        self.cnn_sum.setObjectName("cnn_sum")
        self.lstm_sum = QtWidgets.QPushButton(self.frame_7)
        self.lstm_sum.setGeometry(QtCore.QRect(10, 60, 120, 40))
        self.lstm_sum.setStyleSheet("QPushButton {\n"
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
"    border-color: green;\n"
"\n"
"}    ")
        self.lstm_sum.setObjectName("lstm_sum")
        self.lstm_graph = QtWidgets.QPushButton(self.frame_7)
        self.lstm_graph.setGeometry(QtCore.QRect(136, 10, 120, 40))
        self.lstm_graph.setStyleSheet("QPushButton {\n"
"color: rgb(150, 0, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 13px;\n"
"border-color: black;\n"
"background-color: rgb(255, 119, 121);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 99, 78);\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(255, 52, 52);\n"
"\n"
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
        self.lstm_graph.setObjectName("lstm_graph")
        self.cnn_graph = QtWidgets.QPushButton(self.frame_7)
        self.cnn_graph.setGeometry(QtCore.QRect(136, 60, 120, 40))
        self.cnn_graph.setStyleSheet("QPushButton {\n"
"color: rgb(150, 0, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 13px;\n"
"border-color: black;\n"
"background-color: rgb(255, 119, 121);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 99, 78);\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(255, 52, 52);\n"
"\n"
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
        self.cnn_graph.setObjectName("cnn_graph")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(420, 433, 151, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 170, 0);")
        self.label_8.setObjectName("label_8")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(640, 430, 20, 181))
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_7.raise_()
        self.line_4.raise_()
        self.line_6.raise_()
        self.line_8.raise_()
        self.line_10.raise_()
        self.line_5.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.label_9.raise_()
        self.label.raise_()
        self.frame_3.raise_()
        self.frame_2.raise_()
        self.frame.raise_()
        self.exit.raise_()
        self.title1.raise_()
        self.title2.raise_()
        self.recordlabel.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.frame_5.raise_()
        self.frame_4.raise_()
        self.frame_6.raise_()
        self.label_7.raise_()
        self.line_3.raise_()
        self.frame_7.raise_()
        self.line_9.raise_()
        self.label_8.raise_()
        self.line_11.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AD&C"))
        self.exit.setText(_translate("MainWindow", "Quit"))
        self.title1.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Automatic Detection and Classification of tabla</span></p></body></html>"))
        self.title2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">taalas from Indian Classical Music </span></p></body></html>"))
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
        self.label_4.setText(_translate("MainWindow", "Status :-"))
        self.text_margin.setText(_translate("MainWindow", "Margin @Har"))
        self.label_6.setText(_translate("MainWindow", "Margin @Per "))
        self.datadis.setText(_translate("MainWindow", "Data Distribution"))
        self.mfcccoe.setText(_translate("MainWindow", "MFCC Coefficients"))
        self.fastft.setText(_translate("MainWindow", "FFT"))
        self.timedata.setText(_translate("MainWindow", "Raw"))
        self.fbe.setText(_translate("MainWindow", "Filter Bank Energies"))
        self.label_7.setText(_translate("MainWindow", "Data Visualizations"))
        self.cnn_sum.setText(_translate("MainWindow", "CNN Summary"))
        self.lstm_sum.setText(_translate("MainWindow", "LSTM Summary"))
        self.lstm_graph.setText(_translate("MainWindow", "LSTM Graph"))
        self.cnn_graph.setText(_translate("MainWindow", "CNN Graph"))
        self.label_8.setText(_translate("MainWindow", "Model Visualizations"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
