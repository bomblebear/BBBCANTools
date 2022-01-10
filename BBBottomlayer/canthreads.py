#!/usr/bin/python
# -*-coding:utf-8-*-

from time import sleep
import threading
import ctypes
import inspect
from aenum import NoAliasEnum

import can
import logging

logger = logging.getLogger('BBBCAN')



class can_agent():

    def send_one(self, canchannel, msg_id, msg_data):

        bus = can.interface.Bus(channel = canchannel, bustype = 'socketcan')
        msg = can.Message(
            arbitration_id = msg_id , data= msg_data , is_extended_id = False
        )

        try:
            bus.send(msg)
        except can.CanError:
            logger.error("cannot send msg "+ str(msg_id))


    def send_cyclic(self, canchannel, msg_id, msg_data, cycletime):

        bus = can.interface.Bus(channel = canchannel, bustype = 'socketcan')
        msg = can.Message(
            arbitration_id = msg_id , data= msg_data , is_extended_id = False
        )

        try:
            task_attr = getattr( self, str(canchannel)+str(msg_id))
            logger.info('updating sending message ' + str(msg_id))
            task_attr.stop()
        except:
            pass
        
        try:
            setattr(self, str(canchannel)+str(msg_id) ,  bus.send_periodic(msg, cycletime*0.001) )
        except:
            logger.error("cannot send msg "+ str(msg_id))

        print(str(canchannel)+str(msg_id))



if __name__ =='__main__':

    print('start now')
    #send_one('can0', 0x310, b'\x00\x00\x00\x00\x00\x00\x00\x00')
    can_agent = can_agent()
    print('send one')
    can_agent.send_one('can0', 0x310, b'\x00\x00\x00\x00\x00\x00\x00\x00')
    
    print('send cyclic')
    can_agent.send_cyclic('can0', 0x310, b'\x00\x00\x00\x00\x00\x00\x00\x00',500)

    sleep(2)

    print('update send cyclic')

    can_agent.send_cyclic('can0', 0x310, b'\x00\x00\x00\x00\x00\x00\x00\x11',500)

    while True:
        pass
