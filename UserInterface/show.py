#coding=utf-8
#更新一次UI文件
from os import system
system('pyuic5 test.ui -o ./Ui_test.py')

#pyqt5
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_test import Ui_MainWindow

#dbc file and process
from dbc_handler import *
import can
import cantools

from ui_handler import mywindow

if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())




