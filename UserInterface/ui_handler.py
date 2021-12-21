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
        


    #-------------------------------------------------#
    #-----------------下拉选择按钮响应-------------------#
    #-------------------------------------------------#

    def msg_select_action_ch1_1(self):
        selected_msgname = self.comboBox_ch1_1.currentText()
        selected_msg = self.db1.get_message_by_name(selected_msgname)
        #cycle time 更新显示
        try:
            cycletime = str(selected_msg.cycle_time)
        except:
            cycletime = '0'
        self.cycletime_ch1_1.setText(cycletime)
        self.datafiled_refresh_save_ch1_1.setText('Edit')  #切换message的时候，重新开启编辑
        #self.signal_edit_window.clear()                    #清空右侧栏

        self.packedmsg_ch1_1 = b'\x00\x00\x00\x00\x00\x00\x00\x00'
        self.editflag_ch1 = 0  # 1表示有人正在编辑状态，还未保存
        
        

    def msg_select_action_ch1_2(self):
        selected_msgname = self.comboBox_ch1_2.currentText()
        selected_msg = self.db1.get_message_by_name(selected_msgname)
        #cycle time 更新显示
        try:
            cycletime = str(selected_msg.cycle_time)
        except:
            cycletime = '0'
        self.cycletime_ch1_2.setText(cycletime)
        self.datafiled_refresh_save_ch1_2.setText('Edit')
        #self.signal_edit_window.clear()

        self.packedmsg_ch1_2 = b'\x00\x00\x00\x00\x00\x00\x00\x00'

    def msg_select_action_ch1_3(self):
        pass
    def msg_select_action_ch1_4(self):
        pass
    def msg_select_action_ch1_5(self):
        pass


    #-------------------------------------------------#
    #---------------保存更改按钮响应---------------------#
    #-------------------------------------------------#

    def msg_encode_action_ch1_1(self):
        selected_msgname = self.comboBox_ch1_1.currentText()               #获取当前选中的message
        selected_msg = self.db1.get_message_by_name(selected_msgname)
        
        text = self.datafiled_refresh_save_ch1_1.text()
        flag = 0

        if text == 'Edit'and self.editflag_ch1 == 0: #如果有其他栏正在编辑，不能进入
            self.signal_edit_window.clear()  #先清空屏幕
            decoded_dict = self.db1.decode_message(selected_msg.frame_id, self.packedmsg_ch1_1,decode_choices=False)
            for key in decoded_dict.keys():
                self.signal_edit_window.appendPlainText(key+" : "+str(decoded_dict[key]))
            flag = 1
            self.terminal.append('Editing in ch1')
            self.editflag_ch1 = 1

        if text == 'Save':
            tt = self.signal_edit_window.toPlainText().split('\n')
            signal_dict = {}
            
            for item in tt:   
                signal_dict[item.split(":")[0].strip(" ")] = float(item.split(":")[1])
                #print(type(item.split(":")[0]),type(float(item.split(":")[1])),type(1.1))

            try:    
                self.packedmsg_ch1_1 = selected_msg.encode(signal_dict)  #报文打包
                #print(self.packedmsg_ch1_1.hex('-'))
                self.datafield_overview_ch1_1.setText(str(self.packedmsg_ch1_1.hex('-')))                #打包好的报文显示
            except:
                self.terminal.append('Error in encode in ch1, try again!')
            else:
                self.terminal.append('Encode completely in ch1')
                self.editflag_ch1 = 0
                flag = 2
        
        if flag == 1:
            self.datafiled_refresh_save_ch1_1.setText('Save')
        elif flag == 2:
            self.datafiled_refresh_save_ch1_1.setText('Edit')
        flag = 0
        

    def msg_encode_action_ch1_2(self):
        selected_msgname = self.comboBox_ch1_2.currentText()               #获取当前选中的message
        selected_msg = self.db1.get_message_by_name(selected_msgname)
        
        text = self.datafiled_refresh_save_ch1_2.text()
        flag = 0

        if text == 'Edit'and self.editflag_ch1 == 0: #如果有其他栏正在编辑，不能进入
            self.signal_edit_window.clear()  #先清空屏幕
            decoded_dict = self.db1.decode_message(selected_msg.frame_id, self.packedmsg_ch1_2,decode_choices=False)
            for key in decoded_dict.keys():
                self.signal_edit_window.appendPlainText(key+" : "+str(decoded_dict[key]))
            flag = 1
            self.terminal.append('Editing in ch1')
            self.editflag_ch1 = 1

        if text == 'Save':
            tt = self.signal_edit_window.toPlainText().split('\n')
            signal_dict = {}
            
            for item in tt:   
                signal_dict[item.split(":")[0].strip(" ")] = float(item.split(":")[1])
                #print(type(item.split(":")[0]),type(float(item.split(":")[1])),type(1.1))

            try:    
                self.packedmsg_ch1_2 = selected_msg.encode(signal_dict)  #报文打包
                #print(self.packedmsg_ch1_1.hex('-'))
                self.datafield_overview_ch1_2.setText(str(self.packedmsg_ch1_2.hex('-')))                        #打包好的报文显示
            except:
                self.terminal.append('Error in encode in ch1, try again!')
            else:
                self.terminal.append('Encode completely in ch1')
                self.editflag_ch1 = 0
                flag = 2
        
        if flag == 1:
            self.datafiled_refresh_save_ch1_2.setText('Save')
        elif flag == 2:
            self.datafiled_refresh_save_ch1_2.setText('Edit')
        flag = 0

    def msg_encode_action_ch1_3(self):
        pass

    def msg_encode_action_ch1_4(self):
        pass

    def msg_encode_action_ch1_5(self):
        pass


