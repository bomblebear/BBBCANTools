#!/usr/bin/python
# -*-coding:utf-8-*-
from time import sleep
import zmq
import json
import threading


class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name


    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数 
        print("starting the thread "+ str(self.name))

        context2 = zmq.Context()
        socket2 = context2.socket(zmq.REP)
        socket2.bind("tcp://*:5554")

        while True:

            socket2.recv()

            socket2.send("this thread will continue send msg".encode("utf-8"))

            #print("yes")
            sleep(0.1)



if __name__ == "__main__":

    #子进程，用于持续向上位机发送接收到的CAN报文
    thread1 = myThread("zmqtest")
    thread1.start()


    #主进程：用于接收上位机的命令以及反馈信息
    context1 = zmq.Context()
    socket1 = context1.socket(zmq.REP)
    socket1.bind("tcp://*:5555")


    while True:
        message = socket1.recv()
        msg = message.decode('utf-8')
        #print(msg)
        msg_json = json.loads(msg)
        print(msg_json)
        #logger.info('Zmq request from client recved: {}'.format(msg_json))
        #return_msg = ActionCommon(can_bus_obj, msg_json)
        socket1.send("server response!".encode("utf-8"))
        #logger.info('Zmq response from server sent: {}'.format(return_msg.encode('utf-8')))   
