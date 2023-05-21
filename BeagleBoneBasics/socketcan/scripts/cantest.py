#!/usr/bin/python
import time
import can
import os
from threading import Timer

#====================================#
#=======Global Variables Here========#
#====================================#

#Variables
counter0=0
counter1=0

#Interrupt Timer
send_timer=0.5          #triggered every 500ms
receive_timer=0.2       #triggered every 200ms
mainloop_timer=0.01    #triggered every 5ms

#Received CAN dataframes

receive_msg0 = can.message.Message(arbitration_id = 0x00, data = [0,0,0,0,0,0,0,0])


receive_msg1 = 0
#Message IDs


#====================================#
#=======pack and send can frames=====#
#====================================#
def can0send(MsgID):
    
    global counter0
   
    bus = can.interface.Bus(channel='can0', bustype='socketcan')
    msg = can.Message(arbitration_id=MsgID, data=[counter0, 2, 3, 1, 3, 1, 4, 1], is_extended_id=False)
    bus.send(msg)
    
    counter0=(counter0+1)%256

def can1send(MsgID):
    
    global counter1
   
    bus = can.interface.Bus(channel='can1', bustype='socketcan')
    msg = can.Message(arbitration_id=MsgID, data=[counter1, 2, 3, 1, 3, 1, 4, 1], is_extended_id=False)
    bus.send(msg)
    
    counter1=(counter1+1)%256

#====================================#
#==========receive can frames========#
#====================================#
'''
note that blocking mode will affect the execution speed of the main loop,
so it must be placed in other threads(interrupts)
'''
def can0receive():
    global receive_msg0

    bus = can.interface.Bus(channel='can0', bustype='socketcan')
    message = bus.recv(send_timer)    # 0 == non-blocking 
    if message is not None:
        receive_msg0 = message


def can1receive():
    global receive_msg1

    bus = can.interface.Bus(channel='can1', bustype='socketcan')
    message = bus.recv(send_timer)    # 0 == non-blocking

    if message is not None:
        receive_msg1 = message



#====================================#
#==============main loop=============#
#====================================#
def main():

    #print('i can fresh very fast')
  
    print(receive_msg0)
    #print(receive_msg0.arbitration_id)
    #print(receive_msg0.data[0])


#-----Configure the Interrupt-----#
class RepeatingTimer(Timer):
    def run(self):
        while not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
            self.finished.wait(self.interval)



#====================================#
#===========Initialization===========#
#====================================#

if __name__ == '__main__':


    #---------Pin Configuration Here---------#

    print('Pin Configuring......')
    os.system('sh /home/debian/myProject/caninit_loopbackon')
    #os.system('sh /home/debian/myProject/caninit_loopbackoff')
    print('Pin Configure Finished !')

    print('sending can message now')

    #--------start can timers--------------------#

    SEND0 = RepeatingTimer(send_timer , can0send,(0x300,))
    SEND0.start()

    RECEIVE0 = RepeatingTimer(send_timer , can0receive)
    RECEIVE0.start()

    #--------start main timer----------------#
    print('main loop run now')
    MAINLOOP = RepeatingTimer(mainloop_timer , main)
    MAINLOOP.start()
