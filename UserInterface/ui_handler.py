#pyqt5
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_test import Ui_MainWindow

#dbc file and process
from dbc_handler import *
import can
import cantools


import utils


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
            db1 = cantools.database.load_file(dbc_filepath1) #对dbc进行解析
            self.db1 = db1
            msglist_1 = dbc_msg_list(db1)
            self.comboBox_ch1_1.addItems(msglist_1);self.comboBox_ch1_1.setCurrentIndex(-1)
            self.comboBox_ch1_2.addItems(msglist_1);self.comboBox_ch1_2.setCurrentIndex(-1)
            self.comboBox_ch1_3.addItems(msglist_1);self.comboBox_ch1_3.setCurrentIndex(-1)
            self.comboBox_ch1_4.addItems(msglist_1);self.comboBox_ch1_4.setCurrentIndex(-1)
            self.comboBox_ch1_5.addItems(msglist_1);self.comboBox_ch1_5.setCurrentIndex(-1)
            
        except:
            self.text_dbc1.setText('file fromat error, plz select again') #获取到的绝对路径显示在路径框中
            self.flag_OK1.setText('Error!')
            self.terminal.append( '[error] dbc1 file format error, please select again')
        else:
            self.flag_OK1.setText('dbc loaded!')
            self.terminal.append('[info] dbc1 loaded')



    #channel 2 再说，先整一路
    def button_action_dbc2(self):
        self.flag_OK2.setText('None!')
        try:
            dbc_filepath2 = dbcfile_acquire() 
            self.text_dbc2.setText(dbc_filepath2) #获取到的绝对路径显示在路径框中
        except:
            return 0 #对话框如果意外终止，直接退出

        try:
            db2 = cantools.database.load_file(dbc_filepath2) #对dbc进行解析
            self.db2 = db2
            msglist_2 = dbc_msg_list(db2)
            
        except:
            self.text_dbc2.setText('file fromat error, plz select again') #获取到的绝对路径显示在路径框中
            self.flag_OK2.setText('Error!')
            self.terminal.append( now + 'dbc2 file format error, please select again')
        else:
            self.flag_OK2.setText('dbc loaded!')
            self.terminal.append(now + 'dbc1 loaded')        
        


    #-------------------------------------------------#
    #-----------------下拉选择按钮响应-------------------#
    #-------------------------------------------------#
    
    def msg_select_action_ch1_1(self):
        utils.msg_select_action(self,"ch1_1")         
    def msg_select_action_ch1_2(self):
        utils.msg_select_action(self,"ch1_2") 
    def msg_select_action_ch1_3(self):
        utils.msg_select_action(self,"ch1_3") 
    def msg_select_action_ch1_4(self):
        utils.msg_select_action(self,"ch1_4") 
    def msg_select_action_ch1_5(self):
        utils.msg_select_action(self,"ch1_5")
    #-------------------------------------------------#
    #---------------保存更改按钮响应---------------------#
    #-------------------------------------------------#

    def msg_encode_action_ch1_1(self):
        utils.msg_encode_action(self,"ch1_1")

    def msg_encode_action_ch1_2(self):
        utils.msg_encode_action(self,"ch1_2")

    def msg_encode_action_ch1_3(self):
        utils.msg_encode_action(self,"ch1_3")

    def msg_encode_action_ch1_4(self):
        utils.msg_encode_action(self,"ch1_4")

    def msg_encode_action_ch1_5(self):
        utils.msg_encode_action(self,"ch1_5")

    #-------------------------------------------------#
    #------------------发送一次按钮---------------------#
    #-------------------------------------------------#

    def send_action_once_ch1_1(self):
        utils.send_action_once(self,"ch1_1")
    def send_action_once_ch1_2(self):
        utils.send_action_once(self,"ch1_2")
    def send_action_once_ch1_3(self):
        utils.send_action_once(self,"ch1_3")
    def send_action_once_ch1_4(self):
        utils.send_action_once(self,"ch1_4")
    def send_action_once_ch1_5(self):
        utils.send_action_once(self,"ch1_5")

    #-------------------------------------------------#
    #------------------持续发送按钮---------------------#
    #-------------------------------------------------#
    def send_action_cyclic_ch1_1(self):
        if self.checkbox_ch1_1.isChecked():
            try:
                selected_msgname = self.comboBox_ch1_1.currentText()               #获取当前选中的message
                selected_msg = self.db1.get_message_by_name(selected_msgname)
                self.terminal.append('[info] send cyclic '+ str(hex(selected_msg.frame_id)) +" "+ self.cycletime_ch1_1.text()+"ms  "+  str(self.packedmsg_ch1_1.hex('-')) )
            except:
                self.terminal.append('[error] please verify the data you want to send!')
        else:
            self.terminal.append('[info] stop send cyclic message now')

    def send_action_cyclic_ch1_2(self):
        if self.checkbox_ch1_2.isChecked():
            try:
                selected_msgname = self.comboBox_ch1_2.currentText()               #获取当前选中的message
                selected_msg = self.db1.get_message_by_name(selected_msgname)
                self.terminal.append('[info] send cyclic '+ str(hex(selected_msg.frame_id)) +" "+ self.cycletime_ch1_2.text()+"ms  "+  str(self.packedmsg_ch1_2.hex('-')) )
            except:
                self.terminal.append('[error] please verify the data you want to send!')
        else:
            self.terminal.append('[info] stop send cyclic message now')
    def send_action_cyclic_ch1_3(self):
        pass
    def send_action_cyclic_ch1_4(self):
        pass
    def send_action_cyclic_ch1_5(self):
        pass