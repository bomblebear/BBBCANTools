import zmq
import sys
import json
from time import *
import threading
import ctypes
import inspect

from zmq.sugar import context, socket

debug_flag = 0


class ZmqClient(object):
    def __init__(self, address, port, rcv_timeout=2000, retry=3):
        # defaul recv timeout will be set to 2000 milliseconds
        """
        :param address: zmq server client address(ipv4 or known hostname)
        :param port: port zmq server binded to
        :param rec_timeout: recv resp timeout(milliseconds), will disconnect->reconnect->send again
        :param rec_timeout: retry times after recv timeout
        """
        self.rcv_timeout = rcv_timeout
        self.retry = retry
        self.address = address
        self.port = port
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.setsockopt(zmq.LINGER, 0)
        self.socket.setsockopt(zmq.RCVTIMEO, self.rcv_timeout)
        self.socket.connect("tcp://{addr}:{p}".format(addr=self.address, p=self.port))

    # def send_msg(self, msg_json, timeout=None, retry=None):
    def send_msg(self, msg_json, retry=None):
        #print(strftime("%Y-%m-%d %H:%M:%S", localtime()))
        # if timeout and timeout != self.rcv_timeout:
        #     self.rcv_timeout = timeout
        #     self.socket.close()
        #     sleep(1)
        #     self.socket = self.context.socket(zmq.REQ)
        #     self.socket.setsockopt(zmq.LINGER, 0)
        #     self.socket.setsockopt(zmq.RCVTIMEO, self.rcv_timeout)
        #     self.socket.connect("tcp://{addr}:{p}".format(addr=self.address, p=self.port))
        if retry and retry != self.retry:
            if retry > 0:
                self.retry = retry
        try_num = 0
        recv_msg = ""
        while try_num < self.retry and recv_msg == "":
            try:
                self.socket.send(json.dumps(msg_json).encode('utf-8'))
                recv_msg = self.socket.recv()
            except (zmq.error.Again, zmq.error.ZMQError) as e:
                print("{} zmq connection not available currently".format(strftime("%Y-%m-%d %H:%M:%S", localtime())))
                # self.socket.disconnect("tcp://{addr}:{p}".format(addr=self.address, p=self.port))
                self.socket.close()
                sleep(1)
                self.socket = self.context.socket(zmq.REQ)
                self.socket.setsockopt(zmq.LINGER, 0)
                self.socket.setsockopt(zmq.RCVTIMEO, self.rcv_timeout)
                self.socket.connect("tcp://{addr}:{p}".format(addr=self.address, p=self.port))
                try_num += 1
            else:
                return recv_msg
        return recv_msg

    def close_zmq(self):
        self.socket.close()


#主进程：用于接收上位机的命令以及反馈信息
zmq_main = ZmqClient('192.168.7.2', 5555, 10000, 5)  # timeout need to be set a bit longer
#子进程，用于持续向上位机发送接收到的CAN报文
zmq_1 = ZmqClient('192.168.7.2', 5554, 10000, 1)  # timeout need to be set a bit longer
zmq_2 = ZmqClient('192.168.7.2', 5553, 10000, 1)  # timeout need to be set a bit longer

#channel: "ch1_1"
def zmq_sentmsg_cmd(cmd_str, channel_str, msg_id_str, data_str, cycletime_ms_str, mywindow):
    req = {
    "action": cmd_str,
    "bus": "can"+str(int(channel_str[2])-1),
    "msg_id": msg_id_str,
    "data": data_str,
    "cycletime": cycletime_ms_str 
    }

    if mywindow.debugflag == 0:                  

        recv_msg = zmq_main.send_msg(req, 1)
        print(recv_msg)
    
    else:
        pass


#线程父类的重写也在这里定义
class RecvThread(threading.Thread):   #继承父类threading.Thread
    def __init__(self , zm_channel , tracewindow):
        threading.Thread.__init__(self)
        self.zmq = zm_channel
        self.tracewindow = tracewindow

    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数 

        while True:
        
            recv_msg = self.zmq.send_msg("trigger", 1)
            recv_msg = recv_msg.decode('utf-8')
            msg_json = json.loads(recv_msg)
            
            debugstr = '{chn}   {id}   {data}   {time}'.format( 
                chn  = msg_json.get('bus'),
                id   = msg_json.get('msg_id'),
                data = msg_json.get('data'),
                time = msg_json.get('timestamp')
                )

            try:
                self.tracewindow.append(debugstr)
                #print(recv_msg)
            except:
                print("no terminal now, please check the UI status")
 

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



#线程父类的重写也在这里定义
class RecvThread_Sub(threading.Thread):   #继承父类threading.Thread
    def __init__(self , ip_and_port, tracewindow):
        threading.Thread.__init__(self)
        self.addr = ip_and_port
        self.tracewindow = tracewindow

    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数 

        context = zmq.Context()
        socket = context.socket(zmq.SUB)
        socket.connect(self.addr)
        #socket.setsockopt_string(zmq.SUBSCRIBE,'')
        

        while True:
        
            recv_msg = socket.recv_string
            try:
                self.tracewindow.append(str(recv_msg))
                print(recv_msg)
            except:
                print("no terminal now, please check the UI status")
 

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









if __name__ == "__main__":
    
    req_0 = {
        "action": "bring_up"
    }
    req_1 = {
        "action": "read_single_msg",
        "bus": "CDC",
        "msg_name": "CGW_02"
    }

    thread1 = RecvThread( zmq_1 , None)
    thread1.start()
    
    thread2 = RecvThread( zmq_2 , None)
    thread2.start()
    
    #zm1 = ZmqClient('192.168.7.2', 5555, 10000, 5)  # timeout need to be set a bit longer
    
    recv_msg = zmq_main.send_msg(req_0, 5) 
    print(recv_msg)

