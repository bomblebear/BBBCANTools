#!/usr/bin/python
#更新一次UI文件
from os import system
system('pyuic5 test.ui -o Ui_test.py')

#pyqt5
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_test import Ui_MainWindow

#dbc file and process
from dbcfile_acquire import dbcfile_acquire
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
        except:
            self.text_dbc1.setText('file fromat error, plz select again') #获取到的绝对路径显示在路径框中
            self.flag_OK1.setText('Error!')
        else:
            self.flag_OK1.setText('OK!')


if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())




