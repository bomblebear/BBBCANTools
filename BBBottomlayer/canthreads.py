#!/usr/bin/python
# -*-coding:utf-8-*-

from time import sleep

import can
from can.bus import BusState

import logging
import threading
import ctypes
import inspect

import zmq
import json


import re

logger = logging.getLogger('BBBCAN')




class can_agent():
    '''包含发送以及停止相应通道的报文'''
    def send_one(self, canchannel, msg_id, msg_data):
        '''发送单个报文'''
        bus = can.interface.Bus(channel = canchannel, bustype = 'socketcan')
        msg = can.Message(
            arbitration_id = msg_id , data= msg_data , is_extended_id = False
        )

        try:
            bus.send(msg)
        except can.CanError:
            logger.error("cannot send {ID} msg in {CAN} ".format(ID = hex(msg_id), CAN = canchannel))
        else:
            print("send one {ID} message in {CAN}".format(ID = hex(msg_id) , CAN = canchannel))       


    def send_cyclic(self, canchannel, msg_id, msg_data, cycletime):
        '''循环发送报文，根据ID和channel生成一个类的实例，用以对现存的总线上的报文进行管理：更新报文内容，停止发送'''
        bus = can.interface.Bus(channel = canchannel, bustype = 'socketcan')
        msg = can.Message(
            arbitration_id = msg_id , data= msg_data , is_extended_id = False
        )
        '''如果有现有报文，先停止后直接重新发送'''
        try:
            task_attr = getattr( self, str(canchannel)+str(msg_id))
            logger.info('updating sending {ID} message in {CAN}'.format(ID = hex(msg_id), CAN = canchannel))
            task_attr.stop()
        except:
            pass
        
        try:
            setattr(self, str(canchannel)+str(msg_id) ,  bus.send_periodic(msg, cycletime*0.001) )
        except:
            logger.error("cannot send {ID} msg in {CAN} ".format(ID = hex(msg_id), CAN = canchannel))
        else:
            print("start sending {ID} message in {CAN} every {time} ms".format(ID = hex(msg_id), CAN = canchannel, time = cycletime))


    def stop_cyclic(self, canchannel, msg_id):
        '''停止发送某ID的报文'''
        try:
            task_attr = getattr( self, str(canchannel)+str(msg_id))
            task_attr.stop()
        except:
            logger.error('there is no {ID} in {CAN}'.format(ID=msg_id, CAN = canchannel))
        else:
            print("stop sending {ID} message in {CAN}".format(ID = hex(msg_id), CAN = canchannel))
            logger.info("stop sending {ID} message in {CAN}".format(ID = msg_id, CAN = canchannel))   


#该线程用于接收所有CAN报文用以发送至zmq
#需要两路，一路用于CAN1，一路用于CAN2
class RecvThread(threading.Thread):   #继承父类threading.Thread
    def __init__(self,canbus,port):
        threading.Thread.__init__(self)
        self.canbus = canbus
        self.port = port


    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数 

        logger.info("starting the thread, port in {port}".format(port=self.port))

        context = zmq.Context()
        socket = context.socket(zmq.REP)
        #socket.bind("tcp://*:5554")
        socket.bind(self.port)
        
        bus = can.interface.Bus(channel = self.canbus, bustype = 'socketcan')

        while True:
            msg = bus.recv(1)
            if msg is not None:
                

                timestamp_str = str(msg.timestamp)
            
                msg_id_str = str(hex(msg.arbitration_id))
                canbus_str = msg.channel                    
                
                data_str = str(msg.data.hex())
                pattern = re.compile('.{2}')
                data_str = '-'.join(pattern.findall(data_str))
                '''
                python3.7只能上面这样，如果是python3.8：
                data_str = str(msg.data.hex(‘-’))    
                '''

                req = {
                    "timestamp": timestamp_str,
                    "msg_id": msg_id_str,
                    "data": data_str,
                    "bus": canbus_str, 
                    }

                socket.recv()
                #socket.send('yes'.encode("utf-8"))
                socket.send(json.dumps(req).encode('utf-8'))
                sleep(0.5)
                    


 
    def _async_raise(self, tid, exctype):
        """raises the exception, performs cleanup if needed"""
        tid = ctypes.c_long(tid)
        if not inspect.isclass(exctype):
            exctype = type(exctype)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
        if res == 0:
            raise ValueError("invalid thread id")
        elif res != 1:
            # """if it returns a number greater than one, you're in trouble,
            # and you should call it again with exc=NULL to revert the effect"""
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")
    
    
    def stop_thread(self):
        self._async_raise(self.ident, SystemExit)





if __name__ =='__main__':

    
    thread1 = RecvThread('can0',"tcp://*:5554")
    thread2 = RecvThread('can1',"tcp://*:5553")

    thread1.start()
    thread2.start()


    #send_one('can0', 0x310, b'\x00\x00\x00\x00\x00\x00\x00\x00')
    can_agent = can_agent()
    print('send one')
    can_agent.send_one('can0', 0x310, b'\x00\x00\x00\x00\x00\x00\x00\x00')

    print(type(b'\x00\x00\x00\x00\x00\x00\x00\x00'))
    
    can_agent.send_cyclic('can0', 0x310, b'\x00\x00\x00\x00\x00\x00\x00\x00',500)
    can_agent.send_cyclic('can1', 0x310, b'\x00\x00\x00\x00\x00\x00\x00\x00',500)

    sleep(2)

    print('update send cyclic')

    can_agent.send_cyclic('can0', 0x111, b'\x00\x00\x00\x00\x00\x00\x00\x11',500)
    can_agent.send_cyclic('can0', 0x333, b'\x00\x00\x00\x00\x00\x00\x00\x11',500)

    can_agent.send_cyclic('can1', 0x310, b'\x00\x00\x00\x00\x00\x00\x00\x11',500)
    can_agent.send_cyclic('can1', 0x345, b'\x00\x00\x00\x00\x00\x00\x00\x11',500)
    sleep(2)

    #can_agent.stop_cyclic('can0', 0x310)

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

