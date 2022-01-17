import zmq
import sys
import json
from time import *
from PyQt5 import QtCore, QtWidgets

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
                print("{time} {port} zmq connection not available currently".format(time = strftime("%Y-%m-%d %H:%M:%S", localtime()), port = self.port))
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
#zmq_1 = ZmqClient('192.168.7.2', 5554, 10000, 1)  # timeout need to be set a bit longer
#zmq_2 = ZmqClient('192.168.7.2', 5553, 10000, 1)  # timeout need to be set a bit longer

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

        mywindow.terminal.append(recv_msg.decode('utf-8'))
        
        #print(recv_msg)
    
    else:
        pass




class RecvThreadSub(QtCore.QThread):   #继承父类threading.Thread

    sinout = QtCore.pyqtSignal(dict, QtWidgets.QTextBrowser)    #定义发送给主线程的信号

    def __init__(self,ip_and_port , tracewindow, parent=None ,):
        super(RecvThreadSub, self).__init__(parent)
        #设置工作状态与初始num数值
        self.working = True
        self.num = 0
        self.addr = ip_and_port
        self.tracewindow = tracewindow       

    def __del__(self):
        #线程状态改变与线程终止
        self.working = False
        self.wait()

    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数 

        context = zmq.Context()
        socket = context.socket(zmq.SUB)
        socket.connect(self.addr)
        #socket.connect('tcp://192.168.7.2:5554')
        socket.setsockopt_unicode(zmq.SUBSCRIBE,'')


        trace = {}   #empty dictionary

        while True:
            
            try:
                msg_json = socket.recv_json()
                debugstr = '{chn}   {id}   {data}   {time}'.format( 
                    chn  = msg_json.get('bus'),
                    id   = msg_json.get('msg_id'),
                    data = msg_json.get('data'),
                    time = msg_json.get('timestamp')
                    )
                #用ID作键，值为以上的字符串
                trace[msg_json.get('msg_id')] = debugstr
            except:
                pass

            try:
                if msg_json.get('bus') == '0':
                    pass
                else:
                    #self.tracewindow.append(debugstr)
                    self.sinout.emit(trace , self.tracewindow)

            except:
                print("no terminal now, please check the UI status")
            


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

