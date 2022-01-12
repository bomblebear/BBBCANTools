#!/usr/bin/python
# -*-coding:utf-8-*-

from canthreads import *
from action_common import *



if __name__ =='__main__':
    

    thread1 = RecvThread('can0',"tcp://*:5554")
    thread2 = RecvThread('can1',"tcp://*:5553")

    thread1.start()
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
        #print(msg_json)
        #logger.info('Zmq request from client recved: {}'.format(msg_json))
        return_msg = actioncommon(msg_json)
        socket_main.send(return_msg.encode("utf-8"))
        #logger.info('Zmq response from server sent: {}'.format(return_msg.encode('utf-8')))