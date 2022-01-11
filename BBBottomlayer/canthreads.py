#!/usr/bin/python
# -*-coding:utf-8-*-

from time import sleep

import can
from can.bus import BusState

import logging
import threading
import ctypes
import inspect

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
    def __init__(self,canbus):
        threading.Thread.__init__(self)
        self.canbus = canbus


    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数 
        bus = can.interface.Bus(channel = self.canbus, bustype = 'socketcan')

        #bus.state = BusState.PASSIVE

        try:
            while True:
                msg = bus.recv(1)
                if msg is not None:
                    print(msg)


        except KeyboardInterrupt:
            pass  # exit normally

 
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

    
    thread1 = RecvThread('can0')
    thread2 = RecvThread('can1')

    thread1.start()
    thread2.start()


    #send_one('can0', 0x310, b'\x00\x00\x00\x00\x00\x00\x00\x00')
    can_agent = can_agent()
    print('send one')
    can_agent.send_one('can0', 0x310, b'\x00\x00\x00\x00\x00\x00\x00\x00')
    
    can_agent.send_cyclic('can0', 0x310, b'\x00\x00\x00\x00\x00\x00\x00\x00',500)
    can_agent.send_cyclic('can1', 0x310, b'\x00\x00\x00\x00\x00\x00\x00\x00',500)

    sleep(2)

    print('update send cyclic')

    can_agent.send_cyclic('can0', 0x310, b'\x00\x00\x00\x00\x00\x00\x00\x11',500)
    can_agent.send_cyclic('can1', 0x310, b'\x00\x00\x00\x00\x00\x00\x00\x11',500)
    sleep(2)

    can_agent.stop_cyclic('can0', 0x310)

    thread1.stop_thread()
    thread2.stop_thread()

