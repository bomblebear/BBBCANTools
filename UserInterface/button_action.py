from typing import ChainMap, get_args
from PyQt5 import QtCore, QtGui, QtWidgets
import can
import cantools


#-------------------------------------------------#
#---------------下拉选择按钮响应函数-----------------#
#-------------------------------------------------#
def msg_select_action(mywindow,channel):
    canchannel = channel[0:-2]
    comboBox_attr = getattr(mywindow, "comboBox_"+channel,None )
    selected_msgname = comboBox_attr.currentText()                         #获取当前选中的messgae
    if canchannel == "ch1":
        selected_msg = mywindow.db1.get_message_by_name(selected_msgname)
    else:
        selected_msg = mywindow.db2.get_message_by_name(selected_msgname)
    
    #cycle time 更新显示
    try:
        cycletime = str(selected_msg.cycle_time)
    except:
        cycletime = '0'

    cycletime_attr = getattr(mywindow,"cycletime_"+channel,None)
    cycletime_attr.setText(cycletime)
    
    datafiled_refresh_save_attr = getattr(mywindow,"datafiled_refresh_save_"+channel,None)
    datafiled_refresh_save_attr.setText('Edit')  #切换message的时候，重新开启编辑
    

    setattr(mywindow,"packedmsg_"+channel,b'\x00\x00\x00\x00\x00\x00\x00\x00')
    setattr(mywindow,"editflag_"+canchannel,0)     # 1表示有人正在编辑状态，还未保存


#-------------------------------------------------#
#---------------保存更改按钮响应---------------------#
#-------------------------------------------------#
def msg_encode_action(mywindow,channel):
    canchannel = channel[0:-2]
    comboBox_attr = getattr(mywindow, "comboBox_"+channel,None )
    selected_msgname = comboBox_attr.currentText()                         #获取当前选中的messgae
    if canchannel == "ch1":
        selected_msg = mywindow.db1.get_message_by_name(selected_msgname)
    else:
        selected_msg = mywindow.db2.get_message_by_name(selected_msgname)
    

    datafiled_refresh_save_attr = getattr(mywindow,"datafiled_refresh_save_"+channel,None)
    text = datafiled_refresh_save_attr.text()
    #text = mywindow.datafiled_refresh_save_ch1_1.text()
    flag = 0

    if text == 'Edit'and getattr(mywindow,"editflag_"+canchannel,None) == 0: #如果有其他栏正在编辑，不能进入
        mywindow.signal_edit_window.clear()  #先清空屏幕

        #decoded_dict = mywindow.db1.decode_message(selected_msg.frame_id, mywindow.packedmsg_ch1_1,decode_choices=False)
        
        if canchannel == "ch1":
            decoded_dict = mywindow.db1.decode_message(selected_msg.frame_id, getattr(mywindow,"packedmsg_"+channel),decode_choices=False)
        if canchannel == "ch2":
            decoded_dict = mywindow.db2.decode_message(selected_msg.frame_id, getattr(mywindow,"packedmsg_"+channel),decode_choices=False)

        
        for key in decoded_dict.keys():
            mywindow.signal_edit_window.appendPlainText(key+" : "+str(decoded_dict[key]))
        flag = 1
        mywindow.terminal.append('[info] ['+ canchannel +'] Editing')
        
        setattr(mywindow,"editflag_"+canchannel,1)


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

            if canchannel == "ch1":
                selected_msg = mywindow.db1.get_message_by_name(selected_msgname)
            else:
                selected_msg = mywindow.db2.get_message_by_name(selected_msgname)

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

    if checkbox_attr.isChecked():
        try:
            selected_msgname = comboBox_attr.currentText()               #获取当前选中的message
            if canchannel == "ch1":
                selected_msg = mywindow.db1.get_message_by_name(selected_msgname)
            else:
                selected_msg = mywindow.db2.get_message_by_name(selected_msgname)
            
            mywindow.terminal.append('[info] ['+ canchannel +'] send cyclic '+ str(hex(selected_msg.frame_id)) +" "+ cycletime_attr.text()+"ms  "+  str(getattr(mywindow, "packedmsg_"+channel).hex('-')) )
        except:
            mywindow.terminal.append('[error] ['+ canchannel +'] please verify the data you want to send!')
    else:
        mywindow.terminal.append('[info] ['+ canchannel +'] stop send cyclic message now')





