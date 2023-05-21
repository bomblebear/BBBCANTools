#! /bin/bash

#turn can0 and can1 down
sudo ifconfig can0 down
sudo ifconfig can1 down

#config can0 and can1 TX&RX pins
#------can0-------#
config-pin P9.20 can
config-pin P9.19 can
#------can1-------#
config-pin P9.26 can
config-pin P9.24 can

#-----set bitrate 500k  loopback on

sudo ip link set can0 type can bitrate 500000 loopback on
sudo ip link set can1 type can bitrate 500000 loopback on

#bring can0&can1 on
sudo ifconfig can0 up
sudo ifconfig can1 up

#end of code
