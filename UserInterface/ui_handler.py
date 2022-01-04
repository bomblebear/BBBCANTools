#!/usr/bin/env python
# -*- coding: utf-8 -*-

#pyqt5
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_test import Ui_BBBCAN_Tool

#dbc file and process
from dbc_handler import *
import can
import cantools


import button_action


class mywindow(QtWidgets.QMainWindow, Ui_BBBCAN_Tool):
    
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)


    #定义槽函数
    def Action(self):
        print('button is clicked !')

    #-------------------------------------------------#
    #------------------zmq连接BBB-·--------------------#
    #-------------------------------------------------#
    def connectBBB(self):
        button_action.connectBBBact(self)


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


    #-------------------------------------------------#
    #--------------自定义报文编辑按钮--------------------#
    #-------------------------------------------------#

    def edit_custom_ch1_1(self):
        button_action.edit_custom(self,"ch1_1")
    def edit_custom_ch1_2(self):
        button_action.edit_custom(self,"ch1_2")
    def edit_custom_ch2_1(self):
        button_action.edit_custom(self,"ch2_1")
    def edit_custom_ch2_2(self):
        button_action.edit_custom(self,"ch2_2")


    #-------------------------------------------------#
    #--------------自定义报文发送一次按钮-----------------#
    #-------------------------------------------------#  

    def send_action_once_custom_ch1_1(self):
        button_action.send_action_once_custom(self,"ch1_1")
    def send_action_once_custom_ch1_2(self):
        button_action.send_action_once_custom(self,"ch1_2")
    def send_action_once_custom_ch2_1(self):
        button_action.send_action_once_custom(self,"ch2_1")
    def send_action_once_custom_ch2_2(self):
        button_action.send_action_once_custom(self,"ch2_2")

    #-------------------------------------------------#
    #--------------自定义报文循环发送按钮-----------------#
    #-------------------------------------------------#  

    def send_action_cyclic_custom_ch1_1(self):
        button_action.send_action_cyclic_custom(self,"ch1_1")
    def send_action_cyclic_custom_ch1_2(self):
        button_action.send_action_cyclic_custom(self,"ch1_2")
    def send_action_cyclic_custom_ch2_1(self):
        button_action.send_action_cyclic_custom(self,"ch2_1")
    def send_action_cyclic_custom_ch2_2(self):
        button_action.send_action_cyclic_custom(self,"ch2_2")










