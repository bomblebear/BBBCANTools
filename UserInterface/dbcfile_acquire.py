import tkinter as tk
from tkinter import filedialog

def dbcfile_acquire():
    '''打开选择文件夹对话框'''
    root = tk.Tk()
    root.withdraw()

    folderpath = filedialog.askdirectory() #获得选择好的文件夹
    filepath = filedialog.askopenfilename() #获得选择好的文件

    return filepath


if __name__ == '__main__':

    filepath = dbcfile_acquire()

    #print('Folderpath:',folderpath)
    print('Filepath:',filepath)
