import zmq
import sys
import json
from time import *


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
        print(strftime("%Y-%m-%d %H:%M:%S", localtime()))
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




if __name__ == "__main__":
    req_0 = {
        "action": "bring_up"
    }
    req_1 = {
        "action": "read_single_msg",
        "bus": "CDC",
        "msg_name": "CGW_02"
    }
    req_2 = {
        "action": "listen_cyclic_msg",
        "bus": "CDC",
        "msg_name": "CGW_02",
        "listen_period": 5  # in seconds
    }
    zm = ZmqClient('192.168.7.2', 5555, 10000, 5)  # timeout need to be set a bit longer
    recv_msg = zm.send_msg(req_0, 5) 
    print(recv_msg)
    # sleep(10)
    # print(zm.send_msg(req_1, 4))
    # sleep(5)
    # print(zm.send_msg(req_2, 6))