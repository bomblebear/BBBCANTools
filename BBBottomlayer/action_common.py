#!/usr/bin/python
# -*-coding:utf-8-*-


from re import A
from canthreads import *
import utils

cansim = can_agent()



def add_cyclic_msg(msg):

    #将字符串转成正确要求的格式
    msg['msg_id'] = int(msg.get('msg_id').replace("0x",""),16)
    msg['cycletime'] = float(msg.get('cycletime'))
    msg['data'] = utils.str2bytearray(msg.get('data'))


    channel = msg.get('bus')
    id = msg.get('msg_id')
    data = msg.get('data')
    cycletime = msg.get('cycletime')

    cansim.send_cyclic(channel,id,data,cycletime)
    
    return '[BBB] [info] add cyclic msg {ID} in {bus}'.format(ID = id, bus = channel)


def remove_cyclic_msg(msg):

    #将字符串转成正确要求的格式
    msg['msg_id'] = int(msg.get('msg_id').replace("0x",""),16)
    msg['cycletime'] = float(msg.get('cycletime'))
    msg['data'] = utils.str2bytearray(msg.get('data'))

    channel = msg.get('bus')
    id = msg.get('msg_id')

    cansim.stop_cyclic(channel, id)
    
    return '[BBB] [info] remove cyclic msg {ID} from {bus}'.format(ID = id, bus = channel)


def send_single_msg(msg):

    #将字符串转成正确要求的格式
    msg['msg_id'] = int(msg.get('msg_id').replace("0x",""),16)
    msg['cycletime'] = float(msg.get('cycletime'))
    msg['data'] = utils.str2bytearray(msg.get('data'))

    channel = msg.get('bus')
    id = msg.get('msg_id')
    data = msg.get('data')
    cycletime = msg.get('cycletime')

    cansim.send_one(channel, id, data)
    
    return '[BBB] [info] send one msg {ID} in {bus}'.format(ID = id, bus = channel)



'''
msg = {'action': 'add_cyclic_msg', 'bus': 'can0', 'msg_id': '0x321', 'data': '11-22-33-44-55-66-77-88', 'cycletime': '10'}
msg.get('action') = add_cyclic_msg
'''

def actioncommon(msg):
    action_matrix = {
        'add_cyclic_msg': add_cyclic_msg,
        'remove_cyclic_msg':remove_cyclic_msg,
        'send_single_msg':send_single_msg
        #updating
    }

    if not isinstance(msg,dict):
        logger.debug('type error: payload requires type dict, current is {}'.format(type(msg)))
        return '[BBB] [fail] payload requres type dict, current is {}'.format(type(msg))
    elif not msg.get('action'):
        return '[BBB] [fail] no ACITON in request!'
    elif msg.get('action') not in action_matrix.keys():
        return '[BBB] [fail]  action [{}] not supported'.format(msg.get('action'))
    else:
        return action_matrix.get(msg.get('action'))(msg)



if __name__ =='__main__':
    msg = msg = {'action': 'add_cyclic_msg', 'bus': 'can0', 'msg_id': '0x321', 'data': '11-00-11-00-11-00-11-00', 'cycletime': '10'}
    
    msg['msg_id'] = int(msg.get('msg_id').replace("0x",""),16)
    msg['cycletime'] = float(msg.get('cycletime'))
    msg['data'] = utils.str2bytearray(msg.get('data'))

    print(msg.get('msg_id'))
    print(msg.get('cycletime'))
    print(msg.get('data'))
    #print(actioncommon(msg))