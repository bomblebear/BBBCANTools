#pyqt5
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_test import Ui_MainWindow

#dbc file and process
from dbc_handler import *
import can
import cantools


import button_action


class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)


    #定义槽函数
    def Action(self):
        print('button is clicked !')
    #-------------------------------------------------#
    #------------------dbc 获取------------------------#
    #-------------------------------------------------#
    def button_action_dbc1(self):
        self.flag_OK1.setText('None!')
        try:
            dbc_filepath1 = dbcfile_acquire() 
            self.text_dbc1.setText(dbc_filepath1) #获取到的绝对路径显示在路径框中
        except:
            return 0 #对话框如果意外终止，直接退出

        try:
            self.db1 = cantools.database.load_file(dbc_filepath1) #对dbc进行解析
            msglist = dbc_msg_list(self.db1)
            self.comboBox_ch1_1.addItems(msglist);self.comboBox_ch1_1.setCurrentIndex(-1)
            self.comboBox_ch1_2.addItems(msglist);self.comboBox_ch1_2.setCurrentIndex(-1)
            self.comboBox_ch1_3.addItems(msglist);self.comboBox_ch1_3.setCurrentIndex(-1)
            self.comboBox_ch1_4.addItems(msglist);self.comboBox_ch1_4.setCurrentIndex(-1)
            self.comboBox_ch1_5.addItems(msglist);self.comboBox_ch1_5.setCurrentIndex(-1)
            
        except:
            self.text_dbc1.setText('file fromat error, plz select again') #获取到的绝对路径显示在路径框中
            self.flag_OK1.setText('Error!')
            self.terminal.append( '[error] [ch1] dbc1 file format error, please select again')
        else:
            self.flag_OK1.setText('dbc loaded!')
            self.terminal.append('[info] [ch1] dbc1 loaded')



    #channel 2
    def button_action_dbc2(self):
        self.flag_OK2.setText('None!')
        try:
            dbc_filepath2 = dbcfile_acquire() 
            self.text_dbc2.setText(dbc_filepath2) #获取到的绝对路径显示在路径框中
        except:
            return 0 #对话框如果意外终止，直接退出

        try:
            self.db2 = cantools.database.load_file(dbc_filepath2) #对dbc进行解析
            msglist = dbc_msg_list(self.db2)
            self.comboBox_ch2_1.addItems(msglist);self.comboBox_ch2_1.setCurrentIndex(-1)
            self.comboBox_ch2_2.addItems(msglist);self.comboBox_ch2_2.setCurrentIndex(-1)
            self.comboBox_ch2_3.addItems(msglist);self.comboBox_ch2_3.setCurrentIndex(-1)
            self.comboBox_ch2_4.addItems(msglist);self.comboBox_ch2_4.setCurrentIndex(-1)
            self.comboBox_ch2_5.addItems(msglist);self.comboBox_ch2_5.setCurrentIndex(-1)
            
        except:
            self.text_dbc2.setText('file fromat error, plz select again') #获取到的绝对路径显示在路径框中
            self.flag_OK2.setText('Error!')
            self.terminal.append( '[error] [ch2] dbc2 file format error, please select again')
        else:
            self.flag_OK2.setText('dbc loaded!')
            self.terminal.append('[info] [ch2] dbc2 loaded')   
        


    #-------------------------------------------------#
    #-----------------下拉选择按钮响应-------------------#
    #-------------------------------------------------#
    
    def msg_select_action_ch1_1(self):
        button_action.msg_select_action(self,"ch1_1")         
    def msg_select_action_ch1_2(self):
        button_action.msg_select_action(self,"ch1_2") 
    def msg_select_action_ch1_3(self):
        button_action.msg_select_action(self,"ch1_3") 
    def msg_select_action_ch1_4(self):
        button_action.msg_select_action(self,"ch1_4") 
    def msg_select_action_ch1_5(self):
        button_action.msg_select_action(self,"ch1_5")
    
    def msg_select_action_ch2_1(self):
        button_action.msg_select_action(self,"ch2_1")         
    def msg_select_action_ch2_2(self):
        button_action.msg_select_action(self,"ch2_2") 
    def msg_select_action_ch2_3(self):
        button_action.msg_select_action(self,"ch2_3") 
    def msg_select_action_ch2_4(self):
        button_action.msg_select_action(self,"ch2_4") 
    def msg_select_action_ch2_5(self):
        button_action.msg_select_action(self,"ch2_5")
    #-------------------------------------------------#
    #---------------保存更改按钮响应---------------------#
    #-------------------------------------------------#

    def msg_encode_action_ch1_1(self):
        button_action.msg_encode_action(self,"ch1_1")
    def msg_encode_action_ch1_2(self):
        button_action.msg_encode_action(self,"ch1_2")
    def msg_encode_action_ch1_3(self):
        button_action.msg_encode_action(self,"ch1_3")
    def msg_encode_action_ch1_4(self):
        button_action.msg_encode_action(self,"ch1_4")
    def msg_encode_action_ch1_5(self):
        button_action.msg_encode_action(self,"ch1_5")

    def msg_encode_action_ch2_1(self):
        button_action.msg_encode_action(self,"ch2_1")
    def msg_encode_action_ch2_2(self):
        button_action.msg_encode_action(self,"ch2_2")
    def msg_encode_action_ch2_3(self):
        button_action.msg_encode_action(self,"ch2_3")
    def msg_encode_action_ch2_4(self):
        button_action.msg_encode_action(self,"ch2_4")
    def msg_encode_action_ch2_5(self):
        button_action.msg_encode_action(self,"ch2_5")

    #-------------------------------------------------#
    #------------------发送一次按钮---------------------#
    #-------------------------------------------------#

    def send_action_once_ch1_1(self):
        button_action.send_action_once(self,"ch1_1")
    def send_action_once_ch1_2(self):
        button_action.send_action_once(self,"ch1_2")
    def send_action_once_ch1_3(self):
        button_action.send_action_once(self,"ch1_3")
    def send_action_once_ch1_4(self):
        button_action.send_action_once(self,"ch1_4")
    def send_action_once_ch1_5(self):
        button_action.send_action_once(self,"ch1_5")

    def send_action_once_ch2_1(self):
        button_action.send_action_once(self,"ch2_1")
    def send_action_once_ch2_2(self):
        button_action.send_action_once(self,"ch2_2")
    def send_action_once_ch2_3(self):
        button_action.send_action_once(self,"ch2_3")
    def send_action_once_ch2_4(self):
        button_action.send_action_once(self,"ch2_4")
    def send_action_once_ch2_5(self):
        button_action.send_action_once(self,"ch2_5")

    #-------------------------------------------------#
    #------------------持续发送按钮---------------------#
    #-------------------------------------------------#
    def send_action_cyclic_ch1_1(self):
        button_action.send_action_cyclic(self, "ch1_1")
    def send_action_cyclic_ch1_2(self):
        button_action.send_action_cyclic(self, "ch1_2")
    def send_action_cyclic_ch1_3(self):
        button_action.send_action_cyclic(self, "ch1_3")
    def send_action_cyclic_ch1_4(self):
        button_action.send_action_cyclic(self, "ch1_4")
    def send_action_cyclic_ch1_5(self):
        button_action.send_action_cyclic(self, "ch1_5")

    def send_action_cyclic_ch2_1(self):
        button_action.send_action_cyclic(self, "ch2_1")
    def send_action_cyclic_ch2_2(self):
        button_action.send_action_cyclic(self, "ch2_2")
    def send_action_cyclic_ch2_3(self):
        button_action.send_action_cyclic(self, "ch2_3")
    def send_action_cyclic_ch2_4(self):
        button_action.send_action_cyclic(self, "ch2_4")
    def send_action_cyclic_ch2_5(self):
        button_action.send_action_cyclic(self, "ch2_5")
