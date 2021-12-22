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
        button_action.button_action_dbc(self, "1")

    def button_action_dbc2(self):
        button_action.button_action_dbc(self, "2")
        


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
