# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1034, 875)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.closebutton = QtWidgets.QPushButton(self.centralwidget)
        self.closebutton.setEnabled(True)
        self.closebutton.setGeometry(QtCore.QRect(720, 740, 94, 27))
        font = QtGui.QFont()
        font.setItalic(False)
        font.setStrikeOut(False)
        self.closebutton.setFont(font)
        self.closebutton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.closebutton.setAutoFillBackground(False)
        self.closebutton.setObjectName("closebutton")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 340, 94, 27))
        self.pushButton.setObjectName("pushButton")
        self.DataBase = QtWidgets.QLabel(self.centralwidget)
        self.DataBase.setGeometry(QtCore.QRect(140, 30, 101, 31))
        self.DataBase.setObjectName("DataBase")
        self.button_dbc1 = QtWidgets.QPushButton(self.centralwidget)
        self.button_dbc1.setGeometry(QtCore.QRect(730, 30, 91, 31))
        self.button_dbc1.setObjectName("button_dbc1")
        self.text_dbc1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_dbc1.setGeometry(QtCore.QRect(250, 30, 471, 31))
        self.text_dbc1.setObjectName("text_dbc1")
        self.flag_OK1 = QtWidgets.QLabel(self.centralwidget)
        self.flag_OK1.setEnabled(True)
        self.flag_OK1.setGeometry(QtCore.QRect(840, 30, 51, 31))
        self.flag_OK1.setObjectName("flag_OK1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1034, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.closebutton.clicked.connect(MainWindow.close)
        self.pushButton.clicked.connect(MainWindow.Action)
        self.button_dbc1.clicked.connect(MainWindow.button_action_dbc1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.closebutton.setText(_translate("MainWindow", "closebutton"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.DataBase.setText(_translate("MainWindow", "dbc for can0"))
        self.button_dbc1.setText(_translate("MainWindow", "browser"))
        self.flag_OK1.setText(_translate("MainWindow", "None"))
