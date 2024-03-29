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

sudo ip link set can0 type can bitrate 500000 loopback on restart-ms 100
sudo ifconfig can0 txqueuelen 1000

sudo ip link set can1 type can bitrate 500000 loopback on restart-ms 100
sudo ifconfig can1 txqueuelen 1000

#bring can0&can1 on
sudo ifconfig can0 up
sudo ifconfig can1 up

#end of code
