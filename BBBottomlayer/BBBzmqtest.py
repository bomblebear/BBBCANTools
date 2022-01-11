#!/usr/bin/python
# -*-coding:utf-8-*-
from time import sleep
import zmq
import json
import threading

'''
main: "tcp://*:5555"
bus0: "tcp://*:5554"
bus1: "tcp://*:5553"
'''


class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, port):
        threading.Thread.__init__(self)
        self.port = port


    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数 
        print("starting the thread, port in {port}".format(port=self.port))

        context = zmq.Context()
        socket = context.socket(zmq.REP)
        #socket.bind("tcp://*:5554")
        socket.bind(self.port)

        while True:

            socket.recv()
            socket.send("this thread will continue send msg in {port}".format(port = self.port).encode("utf-8"))

            #print("yes")
            sleep(0.1)



if __name__ == "__main__":

    #子进程，用于持续向上位机发送接收到的CAN报文
    thread1 = myThread("tcp://*:5554")
    thread1.start()

    thread2 = myThread("tcp://*:5553")
    thread2.start()   


    #主进程：用于接收上位机的命令以及反馈信息
    context_main = zmq.Context()
    socket_main = context_main.socket(zmq.REP)
    socket_main.bind("tcp://*:5555")


    while True:
        message = socket_main.recv()
        msg = message.decode('utf-8')
        #print(msg)
        msg_json = json.loads(msg)
        print(msg_json)
        #logger.info('Zmq request from client recved: {}'.format(msg_json))
        #return_msg = ActionCommon(can_bus_obj, msg_json)
        socket_main.send("main port response!".encode("utf-8"))
        #logger.info('Zmq response from server sent: {}'.format(return_msg.encode('utf-8')))   
