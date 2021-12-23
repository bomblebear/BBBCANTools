#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import ChainMap, get_args
from PyQt5 import QtCore, QtGui, QtWidgets
import can
import cantools
from dbc_handler import dbcfile_acquire,dbc_msg_list

#-------------------------------------------------#
#-------------------dbc获取函数--------------------#
#-------------------------------------------------#
def button_action_dbc(mywindow, channelnum):
    flag_OK_attr = getattr(mywindow, "flag_OK"+channelnum, None)
    flag_OK_attr.setText('None!')
    
    try:
        dbc_filepath = dbcfile_acquire()  #对话框获取路径

        text_dbc_attr = getattr(mywindow, "text_dbc"+channelnum, None)
        text_dbc_attr.setText(dbc_filepath)     #获取到的绝对路径显示在路径框中

    except:
        return 0 #对话框如果意外终止，直接退出函数

    try:
        setattr(mywindow, "db"+channelnum, cantools.database.load_file(dbc_filepath))   #对dbc进行解析
        
        msglist = dbc_msg_list(cantools.database.load_file(dbc_filepath))
        #range(5), 0,1,2,3,4        
        for i in range(5):

                        
            comboBox_attr = getattr(mywindow, "comboBox_ch"+channelnum+"_"+str(i+1), None)
            comboBox_attr.clear()            #清空下拉框
            comboBox_attr.addItems(msglist)  #加入msg列表
            comboBox_attr.setCurrentIndex(-1) #设置当前无目标被选中

            
            cycletime_attr = getattr(mywindow,"cycletime_ch"+channelnum+"_"+str(i+1),None)
            cycletime_attr.setText("")

    except:
        text_dbc_attr.setText('file fromat error, plz select again') #获取到的绝对路径显示在路径框中
        flag_OK_attr.setText('Error!')
        mywindow.terminal.append( '[error] [ch'+channelnum+'] dbc file format error, please select again')
    else:
        flag_OK_attr.setText('dbc loaded!')
        mywindow.terminal.append('[info] [ch'+channelnum+'] dbc loaded')



#-------------------------------------------------#
#---------------下拉选择按钮响应函数-----------------#
#-------------------------------------------------#
def msg_select_action(mywindow,channel):
    
    canchannel = channel[0:-2]

    comboBox_attr = getattr(mywindow, "comboBox_"+channel,None )
    selected_msgname = comboBox_attr.currentText()                         #获取当前选中的messgae

    try:
        db_attr = getattr(mywindow, "db"+channel[2])
        selected_msg = db_attr.get_message_by_name(selected_msgname)
    except:
        #mywindow.terminal.append('[error] ['+ canchannel +'] dbc file error! Please check')
        pass

    #cycle time 更新显示
    try:
        cycletime = str(selected_msg.cycle_time)
    except:
        cycletime = '0'

    cycletime_attr = getattr(mywindow,"cycletime_"+channel,None)
    cycletime_attr.setText(cycletime)
    
    try:
        datafiled_refresh_save_attr = getattr(mywindow,"datafiled_refresh_save_"+channel,None)
        datafiled_refresh_save_attr.setText('Edit')  #切换message的时候，重新开启编辑
    except:
        pass

    setattr(mywindow,"packedmsg_"+channel,b'\x00\x00\x00\x00\x00\x00\x00\x00')
    setattr(mywindow,"editflag_"+canchannel,0)     # 1表示有人正在编辑状态，还未保存


#-------------------------------------------------#
#---------------保存更改按钮响应---------------------#
#-------------------------------------------------#
def msg_encode_action(mywindow,channel):
    canchannel = channel[0:-2]
    comboBox_attr = getattr(mywindow, "comboBox_"+channel,None )
    selected_msgname = comboBox_attr.currentText()                         #获取当前选中的messgae
    try:
        db_attr = getattr(mywindow, "db"+channel[2])
        selected_msg = db_attr.get_message_by_name(selected_msgname)
    
        datafiled_refresh_save_attr = getattr(mywindow,"datafiled_refresh_save_"+channel,None)
        text = datafiled_refresh_save_attr.text()
    except:
        text = "Edit"   #出错时，不可进入编辑状态
        mywindow.terminal.append('[error] ['+ canchannel +'] There is no message selected, please check it')
    
    #text = mywindow.datafiled_refresh_save_ch1_1.text()
    flag = 0

    if text == 'Edit'and getattr(mywindow,"editflag_"+canchannel,None) == 0: #如果有其他栏正在编辑，不能进入
        mywindow.signal_edit_window.clear()  #先清空屏幕
        mywindow.signal_edit_window_2.clear()

        #decoded_dict = mywindow.db1.decode_message(selected_msg.frame_id, mywindow.packedmsg_ch1_1,decode_choices=False)
        try:
            decoded_dict = db_attr.decode_message(selected_msg.frame_id, getattr(mywindow,"packedmsg_"+channel),decode_choices=False)
            decoded_dict_2 = db_attr.decode_message(selected_msg.frame_id, getattr(mywindow,"packedmsg_"+channel),decode_choices=True)
        
            for key in decoded_dict.keys():
                mywindow.signal_edit_window.appendPlainText(key+" : "+str(decoded_dict[key]))
                mywindow.signal_edit_window_2.appendPlainText(key+" : "+str(decoded_dict_2[key]))
            flag = 1
            mywindow.terminal.append('[info] ['+ canchannel +'] Editing')
            
            setattr(mywindow,"editflag_"+canchannel,1)
        except:
            pass


    if text == 'Save':
        tt = mywindow.signal_edit_window.toPlainText().split('\n')
        signal_dict = {}
        
        for item in tt:   
            signal_dict[item.split(":")[0].strip(" ")] = float(item.split(":")[1])
            #print(type(item.split(":")[0]),type(float(item.split(":")[1])),type(1.1))

        try:    
            setattr(mywindow, "packedmsg_"+channel,selected_msg.encode(signal_dict))  #报文打包
            
            datafield_overview_attr = getattr(mywindow, "datafield_overview_"+channel, None)
            datafield_overview_attr.setText(str(getattr(mywindow, "packedmsg_"+channel).hex('-')))  #打包好的报文显示
            #mywindow.datafield_overview_ch1_1.setText(str(mywindow.packedmsg_ch1_1.hex('-')))        
        except:
            mywindow.terminal.append('[error] ['+ canchannel +'] Error in encode, try again!')
        else:
            mywindow.terminal.append('[info] ['+ canchannel +'] Encode completely')
            
            setattr(mywindow,"editflag_"+canchannel, 0)
            
            flag = 2
    
    if flag == 1:
        datafiled_refresh_save_attr.setText('Save')
        datafiled_refresh_save_attr.setStyleSheet("color: red")
    elif flag == 2:
        datafiled_refresh_save_attr.setText('Edit')
        datafiled_refresh_save_attr.setStyleSheet("color: black")
        send_action_cyclic(mywindow, channel)    #如果此时报文正在发送，而且成功修改了一次报文内容，需要将报文内容更新发送至总线
        mywindow.edit_and_send_flag = 1
    flag = 0
    

#-------------------------------------------------#
#---------------发送一次按钮响应---------------------#
#-------------------------------------------------#
def send_action_once(mywindow,channel):
    canchannel = channel[0:-2]
    checkbox_attr = getattr(mywindow, "checkbox_"+channel, None)
    comboBox_attr = getattr(mywindow, "comboBox_"+channel, None)

    if not checkbox_attr.isChecked():
        try:
            selected_msgname = comboBox_attr.currentText()               #获取当前选中的message

            db_attr = getattr(mywindow, "db"+channel[2])
            selected_msg = db_attr.get_message_by_name(selected_msgname)

            mywindow.terminal.append('[info] ['+ canchannel +'] send once '+ str(hex(selected_msg.frame_id)) +"  "+  str(getattr(mywindow, "packedmsg_"+channel).hex('-')) )
        except:
            mywindow.terminal.append('[error] ['+ canchannel +'] please verify the data you want to send!')
    else:
        mywindow.terminal.append('[warning] ['+ canchannel +'] cannot send once when this message sending cyclicly!')


#-------------------------------------------------#
#---------------循环发送按钮响应---------------------#
#-------------------------------------------------#
def send_action_cyclic(mywindow,channel):
    canchannel = channel[0:-2]
    checkbox_attr = getattr(mywindow, "checkbox_"+channel, None)
    comboBox_attr = getattr(mywindow, "comboBox_"+channel, None)
    cycletime_attr = getattr(mywindow, "cycletime_"+channel, None)

    try:
        if checkbox_attr.isChecked():
            try:
                selected_msgname = comboBox_attr.currentText()               #获取当前选中的message
                db_attr = getattr(mywindow, "db"+channel[2])
                selected_msg = db_attr.get_message_by_name(selected_msgname)
                
                mywindow.terminal.append('[info] ['+ canchannel +'] send cyclic '+ str(hex(selected_msg.frame_id)) +" "+ cycletime_attr.text()+"ms  "+  str(getattr(mywindow, "packedmsg_"+channel).hex('-')) )
            except:
                mywindow.terminal.append('[error] ['+ canchannel +'] please verify the data you want to send!')
        elif mywindow.edit_and_send_flag == 0:
            mywindow.terminal.append('[info] ['+ canchannel +'] stop send cyclic message now')
        else:
            mywindow.edit_and_send_flag = 0
    except:
        mywindow.edit_and_send_flag = 0





