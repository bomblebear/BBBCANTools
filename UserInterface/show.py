#coding=utf-8
#更新一次UI文件
from os import system
system('pyuic5 test.ui -o ./Ui_test.py')

#pyqt5
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_test import Ui_BBBCAN_Tool

#dbc file and process
from dbc_handler import *

from ui_handler import mywindow

import time
now = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime()) + " : "

if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()

    window.terminal.append('-------------------------------------------------------------------------------------------')
    window.terminal.append('---------https://github.com/bbbearman?tab=repositories--------')
    window.terminal.append('-------------------------------------------------------------------------------------------')
    window.terminal.append("start at : " + time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime()))
    
    sys.exit(app.exec_())



