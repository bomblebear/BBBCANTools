#!/usr/bin/env python
# -*- coding: utf-8 -*-



#将封装好的bytearray进行CRC校验，处于安全性考虑，CRC待相关人员手动加入，这里我们直接返回原值
def CRC(canmsg):
    return canmsg




#将形如“00-00-00-00”（以“-”作分隔）的字符串拆分重组成为bytearray
def str2bytearray(str):
    datalist = []
    for item in str.split("-"):
        datalist.append(int(item,16))        #将输入的字符串以十六进制转为int类型
    #print(datalist)
    a = 0x00
    for i in range(len(datalist)):
        a = a | (datalist[i]<<(8*i))

    b = a.to_bytes(8, byteorder="little",signed = False)

    return b



if __name__ == "__main__":

    str = "00-11-00"
    canmsg = str2bytearray(str)
    print(canmsg)