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
        MainWindow.resize(1046, 875)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.signal_edit_window = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.signal_edit_window.setGeometry(QtCore.QRect(760, 180, 261, 301))
        self.signal_edit_window.setObjectName("signal_edit_window")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 150, 711, 371))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.comboBox_ch1_1 = QtWidgets.QComboBox(self.tab)
        self.comboBox_ch1_1.setGeometry(QtCore.QRect(20, 40, 171, 27))
        self.comboBox_ch1_1.setObjectName("comboBox_ch1_1")
        self.comboBox_ch1_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_ch1_2.setGeometry(QtCore.QRect(20, 90, 171, 27))
        self.comboBox_ch1_2.setObjectName("comboBox_ch1_2")
        self.comboBox_ch1_3 = QtWidgets.QComboBox(self.tab)
        self.comboBox_ch1_3.setGeometry(QtCore.QRect(20, 140, 171, 27))
        self.comboBox_ch1_3.setObjectName("comboBox_ch1_3")
        self.comboBox_ch1_4 = QtWidgets.QComboBox(self.tab)
        self.comboBox_ch1_4.setGeometry(QtCore.QRect(20, 190, 171, 27))
        self.comboBox_ch1_4.setObjectName("comboBox_ch1_4")
        self.button_send_ch1_1 = QtWidgets.QPushButton(self.tab)
        self.button_send_ch1_1.setGeometry(QtCore.QRect(200, 40, 71, 27))
        self.button_send_ch1_1.setObjectName("button_send_ch1_1")
        self.button_send_ch1_2 = QtWidgets.QPushButton(self.tab)
        self.button_send_ch1_2.setGeometry(QtCore.QRect(200, 90, 71, 27))
        self.button_send_ch1_2.setObjectName("button_send_ch1_2")
        self.button_send_ch1_3 = QtWidgets.QPushButton(self.tab)
        self.button_send_ch1_3.setGeometry(QtCore.QRect(200, 140, 71, 27))
        self.button_send_ch1_3.setObjectName("button_send_ch1_3")
        self.button_send_ch1_4 = QtWidgets.QPushButton(self.tab)
        self.button_send_ch1_4.setGeometry(QtCore.QRect(200, 190, 71, 27))
        self.button_send_ch1_4.setObjectName("button_send_ch1_4")
        self.checkbox_ch1_1 = QtWidgets.QCheckBox(self.tab)
        self.checkbox_ch1_1.setGeometry(QtCore.QRect(290, 40, 98, 25))
        self.checkbox_ch1_1.setObjectName("checkbox_ch1_1")
        self.checkbox_ch1_2 = QtWidgets.QCheckBox(self.tab)
        self.checkbox_ch1_2.setGeometry(QtCore.QRect(290, 90, 98, 25))
        self.checkbox_ch1_2.setObjectName("checkbox_ch1_2")
        self.checkbox_ch1_3 = QtWidgets.QCheckBox(self.tab)
        self.checkbox_ch1_3.setGeometry(QtCore.QRect(290, 140, 98, 25))
        self.checkbox_ch1_3.setObjectName("checkbox_ch1_3")
        self.checkbox_ch1_4 = QtWidgets.QCheckBox(self.tab)
        self.checkbox_ch1_4.setGeometry(QtCore.QRect(290, 190, 98, 25))
        self.checkbox_ch1_4.setObjectName("checkbox_ch1_4")
        self.cycletime_ch1_1 = QtWidgets.QLineEdit(self.tab)
        self.cycletime_ch1_1.setGeometry(QtCore.QRect(390, 40, 51, 27))
        self.cycletime_ch1_1.setObjectName("cycletime_ch1_1")
        self.cycletime_ch1_2 = QtWidgets.QLineEdit(self.tab)
        self.cycletime_ch1_2.setGeometry(QtCore.QRect(390, 90, 51, 27))
        self.cycletime_ch1_2.setObjectName("cycletime_ch1_2")
        self.cycletime_ch1_3 = QtWidgets.QLineEdit(self.tab)
        self.cycletime_ch1_3.setGeometry(QtCore.QRect(390, 140, 51, 27))
        self.cycletime_ch1_3.setObjectName("cycletime_ch1_3")
        self.cycletime_ch1_4 = QtWidgets.QLineEdit(self.tab)
        self.cycletime_ch1_4.setGeometry(QtCore.QRect(390, 190, 51, 27))
        self.cycletime_ch1_4.setObjectName("cycletime_ch1_4")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 10, 101, 19))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(480, 10, 141, 19))
        self.label_2.setObjectName("label_2")
        self.comboBox_ch1_5 = QtWidgets.QComboBox(self.tab)
        self.comboBox_ch1_5.setGeometry(QtCore.QRect(20, 240, 171, 27))
        self.comboBox_ch1_5.setObjectName("comboBox_ch1_5")
        self.button_send_ch1_5 = QtWidgets.QPushButton(self.tab)
        self.button_send_ch1_5.setGeometry(QtCore.QRect(200, 240, 71, 27))
        self.button_send_ch1_5.setObjectName("button_send_ch1_5")
        self.checkbox_ch1_5 = QtWidgets.QCheckBox(self.tab)
        self.checkbox_ch1_5.setGeometry(QtCore.QRect(290, 240, 98, 25))
        self.checkbox_ch1_5.setObjectName("checkbox_ch1_5")
        self.cycletime_ch1_5 = QtWidgets.QLineEdit(self.tab)
        self.cycletime_ch1_5.setGeometry(QtCore.QRect(390, 240, 51, 27))
        self.cycletime_ch1_5.setObjectName("cycletime_ch1_5")
        self.datafield_overview_ch1_1 = QtWidgets.QTextEdit(self.tab)
        self.datafield_overview_ch1_1.setGeometry(QtCore.QRect(460, 40, 191, 31))
        self.datafield_overview_ch1_1.setObjectName("datafield_overview_ch1_1")
        self.datafield_overview_ch1_2 = QtWidgets.QTextEdit(self.tab)
        self.datafield_overview_ch1_2.setGeometry(QtCore.QRect(460, 90, 191, 31))
        self.datafield_overview_ch1_2.setObjectName("datafield_overview_ch1_2")
        self.datafield_overview_ch1_3 = QtWidgets.QTextEdit(self.tab)
        self.datafield_overview_ch1_3.setGeometry(QtCore.QRect(460, 140, 191, 31))
        self.datafield_overview_ch1_3.setObjectName("datafield_overview_ch1_3")
        self.datafield_overview_ch1_4 = QtWidgets.QTextEdit(self.tab)
        self.datafield_overview_ch1_4.setGeometry(QtCore.QRect(460, 190, 191, 31))
        self.datafield_overview_ch1_4.setObjectName("datafield_overview_ch1_4")
        self.datafield_overview_ch1_5 = QtWidgets.QTextEdit(self.tab)
        self.datafield_overview_ch1_5.setGeometry(QtCore.QRect(460, 240, 191, 31))
        self.datafield_overview_ch1_5.setObjectName("datafield_overview_ch1_5")
        self.datafiled_refresh_save_ch1_1 = QtWidgets.QPushButton(self.tab)
        self.datafiled_refresh_save_ch1_1.setGeometry(QtCore.QRect(660, 40, 41, 31))
        self.datafiled_refresh_save_ch1_1.setObjectName("datafiled_refresh_save_ch1_1")
        self.datafiled_refresh_save_ch1_2 = QtWidgets.QPushButton(self.tab)
        self.datafiled_refresh_save_ch1_2.setGeometry(QtCore.QRect(660, 90, 41, 31))
        self.datafiled_refresh_save_ch1_2.setObjectName("datafiled_refresh_save_ch1_2")
        self.datafiled_refresh_save_ch1_3 = QtWidgets.QPushButton(self.tab)
        self.datafiled_refresh_save_ch1_3.setGeometry(QtCore.QRect(660, 140, 41, 31))
        self.datafiled_refresh_save_ch1_3.setObjectName("datafiled_refresh_save_ch1_3")
        self.datafiled_refresh_save_ch1_4 = QtWidgets.QPushButton(self.tab)
        self.datafiled_refresh_save_ch1_4.setGeometry(QtCore.QRect(660, 190, 41, 31))
        self.datafiled_refresh_save_ch1_4.setObjectName("datafiled_refresh_save_ch1_4")
        self.datafiled_refresh_save_ch1_5 = QtWidgets.QPushButton(self.tab)
        self.datafiled_refresh_save_ch1_5.setGeometry(QtCore.QRect(660, 240, 41, 31))
        self.datafiled_refresh_save_ch1_5.setObjectName("datafiled_refresh_save_ch1_5")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.comboBox_ch2_1 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_ch2_1.setGeometry(QtCore.QRect(20, 20, 87, 27))
        self.comboBox_ch2_1.setObjectName("comboBox_ch2_1")
        self.tabWidget.addTab(self.tab_2, "")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 10, 781, 121))
        self.groupBox.setObjectName("groupBox")
        self.flag_OK2 = QtWidgets.QLabel(self.groupBox)
        self.flag_OK2.setEnabled(True)
        self.flag_OK2.setGeometry(QtCore.QRect(680, 80, 141, 31))
        self.flag_OK2.setObjectName("flag_OK2")
        self.text_dbc1 = QtWidgets.QTextBrowser(self.groupBox)
        self.text_dbc1.setGeometry(QtCore.QRect(130, 40, 431, 31))
        self.text_dbc1.setObjectName("text_dbc1")
        self.button_dbc1 = QtWidgets.QPushButton(self.groupBox)
        self.button_dbc1.setGeometry(QtCore.QRect(570, 40, 91, 31))
        self.button_dbc1.setObjectName("button_dbc1")
        self.DataBase1 = QtWidgets.QLabel(self.groupBox)
        self.DataBase1.setGeometry(QtCore.QRect(20, 40, 101, 31))
        self.DataBase1.setObjectName("DataBase1")
        self.flag_OK1 = QtWidgets.QLabel(self.groupBox)
        self.flag_OK1.setEnabled(True)
        self.flag_OK1.setGeometry(QtCore.QRect(680, 40, 121, 31))
        self.flag_OK1.setObjectName("flag_OK1")
        self.button_dbc2 = QtWidgets.QPushButton(self.groupBox)
        self.button_dbc2.setGeometry(QtCore.QRect(570, 80, 91, 31))
        self.button_dbc2.setObjectName("button_dbc2")
        self.DataBase2 = QtWidgets.QLabel(self.groupBox)
        self.DataBase2.setGeometry(QtCore.QRect(20, 80, 101, 31))
        self.DataBase2.setObjectName("DataBase2")
        self.text_dbc2 = QtWidgets.QTextBrowser(self.groupBox)
        self.text_dbc2.setGeometry(QtCore.QRect(130, 80, 431, 31))
        self.text_dbc2.setObjectName("text_dbc2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(830, 10, 171, 131))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(40, 30, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.closebutton = QtWidgets.QPushButton(self.groupBox_2)
        self.closebutton.setEnabled(True)
        self.closebutton.setGeometry(QtCore.QRect(40, 80, 101, 41))
        font = QtGui.QFont()
        font.setItalic(False)
        font.setStrikeOut(False)
        self.closebutton.setFont(font)
        self.closebutton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.closebutton.setAutoFillBackground(False)
        self.closebutton.setStyleSheet("color: rgb(239, 41, 41)")
        self.closebutton.setObjectName("closebutton")
        self.refresh_diag = QtWidgets.QTextBrowser(self.centralwidget)
        self.refresh_diag.setGeometry(QtCore.QRect(760, 490, 261, 31))
        self.refresh_diag.setObjectName("refresh_diag")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.closebutton.clicked.connect(MainWindow.close)
        self.pushButton.clicked.connect(MainWindow.Action)
        self.button_dbc1.clicked.connect(MainWindow.button_action_dbc1)
        self.button_dbc2.clicked.connect(MainWindow.button_action_dbc2)
        self.comboBox_ch1_1.currentIndexChanged['QString'].connect(MainWindow.msg_select_action_ch1_1)
        self.comboBox_ch1_2.currentIndexChanged['QString'].connect(MainWindow.msg_select_action_ch1_2)
        self.comboBox_ch1_3.currentIndexChanged['QString'].connect(MainWindow.msg_select_action_ch1_3)
        self.comboBox_ch1_4.currentIndexChanged['QString'].connect(MainWindow.msg_select_action_ch1_4)
        self.comboBox_ch1_5.currentIndexChanged['QString'].connect(MainWindow.msg_select_action_ch1_5)
        self.datafiled_refresh_save_ch1_1.clicked.connect(MainWindow.msg_encode_action_ch1_1)
        self.datafiled_refresh_save_ch1_2.clicked.connect(MainWindow.msg_encode_action_ch1_2)
        self.datafiled_refresh_save_ch1_3.clicked.connect(MainWindow.msg_encode_action_ch1_3)
        self.datafiled_refresh_save_ch1_4.clicked.connect(MainWindow.msg_encode_action_ch1_4)
        self.datafiled_refresh_save_ch1_5.clicked.connect(MainWindow.msg_encode_action_ch1_5)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_send_ch1_1.setText(_translate("MainWindow", "send"))
        self.button_send_ch1_2.setText(_translate("MainWindow", "send"))
        self.button_send_ch1_3.setText(_translate("MainWindow", "send"))
        self.button_send_ch1_4.setText(_translate("MainWindow", "send"))
        self.checkbox_ch1_1.setText(_translate("MainWindow", "Cyclic/ms"))
        self.checkbox_ch1_2.setText(_translate("MainWindow", "Cyclic/ms"))
        self.checkbox_ch1_3.setText(_translate("MainWindow", "Cyclic/ms"))
        self.checkbox_ch1_4.setText(_translate("MainWindow", "Cyclic/ms"))
        self.label.setText(_translate("MainWindow", "MsgName/ID"))
        self.label_2.setText(_translate("MainWindow", "DatafiledOverview"))
        self.button_send_ch1_5.setText(_translate("MainWindow", "send"))
        self.checkbox_ch1_5.setText(_translate("MainWindow", "Cyclic/ms"))
        self.datafiled_refresh_save_ch1_1.setText(_translate("MainWindow", "Edit"))
        self.datafiled_refresh_save_ch1_2.setText(_translate("MainWindow", "Edit"))
        self.datafiled_refresh_save_ch1_3.setText(_translate("MainWindow", "Edit"))
        self.datafiled_refresh_save_ch1_4.setText(_translate("MainWindow", "Edit"))
        self.datafiled_refresh_save_ch1_5.setText(_translate("MainWindow", "Edit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.groupBox.setTitle(_translate("MainWindow", "add dbc files here"))
        self.flag_OK2.setText(_translate("MainWindow", "None"))
        self.button_dbc1.setText(_translate("MainWindow", "browser"))
        self.DataBase1.setText(_translate("MainWindow", "dbc for can1"))
        self.flag_OK1.setText(_translate("MainWindow", "None"))
        self.button_dbc2.setText(_translate("MainWindow", "browser"))
        self.DataBase2.setText(_translate("MainWindow", "dbc for can2"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Diagnostic"))
        self.pushButton.setText(_translate("MainWindow", "Connect"))
        self.closebutton.setText(_translate("MainWindow", "Exit"))
