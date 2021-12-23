#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import filedialog
import cantools

def dbcfile_acquire():
    '''打开选择文件夹对话框'''
    root = tk.Tk()
    root.withdraw()

    #folderpath = filedialog.askdirectory() #获得选择好的文件夹
    filepath = filedialog.askopenfilename() #获得选择好的文件

    return filepath

def dbc_msg_list(candbc):
    msglist = []
    for msg in candbc.messages:
        msglist.append(str(msg.name))
    
    return msglist



if __name__ == '__main__':

    filepath = dbcfile_acquire()

    db = cantools.database.load_file(filepath) 

    list = dbc_msg_list(db)

    print(list)
    #print('Folderpath:',folderpath)
    print('Filepath:',filepath)
