#pyqt5
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_test import Ui_MainWindow

#dbc file and process
from dbc_handler import *
import can
import cantools

class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)


    #定义槽函数
    def Action(self):
        print('button is clicked !')
    
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
        else:
            self.flag_OK1.setText('dbc loaded!')



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
        else:
            self.flag_OK2.setText('dbc loaded!')        
        


    def msg_select_action_ch1_1(self):
        selected_msgname = self.comboBox_ch1_1.currentText()
        selected_msg = self.db1.get_message_by_name(selected_msgname)
        #cycle time 更新显示
        try:
            cycletime = str(selected_msg.cycle_time)
        except:
            cycletime = '0'
        self.cycletime_ch1_1.setText(cycletime)
        

        self.signal_edit_window.clear()
        try:  
            for i in range(len(selected_msg.signals)):
                #print("\"%s\"" % selected_msg.signals[i].name + " : "+"0"+" , ")
                self.signal_edit_window.appendPlainText("\"%s\"" % selected_msg.signals[i].name + " : "+"0"+" , ")
        except:
            pass


    def msg_select_action_ch1_2(self):
        pass
    def msg_select_action_ch1_3(self):
        pass
    def msg_select_action_ch1_4(self):
        pass
    def msg_select_action_ch1_5(self):
        pass