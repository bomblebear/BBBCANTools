# 类CANoe工具开发

## 2022.Jan.17th
已经完成基本***demo1.0***的编写，可以：
1. 按dbc在每路can发送5个不同ID的报文；
2. 自定义发送2个不同ID的报文
3. python需使用python3.7及以上版本

需要修复的bug：
1. 当前用户勾选循环发送后，UI界面终止，BBB仍旧会不断发送；
2. 开机自启目前未配置；
3. 由于开发环境为ubuntu20.04，用户界面对windows适配不好，需要调整；
4. 总线负载过大时，界面会因为刷新过快而卡顿；

## BBB端的准备工作
### 1. 为BBB设备联网的开机配置工作
> https://www.ofitselfso.com/BeagleNotes/HowToConnectPocketBeagleToTheInternetViaUSB.php
   1. `sudo su` 进入管理员模式  
   2. `cd` 进入根目录
   3. `nano internetOverUSB`创建该文件并将以下内容复制进去 

```bash
#!/bin/bash
#
# Set the default gateway, nameservers and date
# automatically. This script needs to be
# called via init.d

## Add a default gateway
/sbin/route add default gw 192.168.7.1

## add the nameservers if necessary
grep -q 8.8.8.8 /etc/resolv.conf
if [ "$?" -ne "0" ]; then
        echo "nameserver 8.8.4.4" >> /etc/resolv.conf
        echo "nameserver 8.8.8.8" >> /etc/resolv.conf
fi

## set the date
/usr/sbin/ntpdate pool.ntp.org

## End of the settings script



##CAN卡的配置，loopback为off
#------------------------------#
#config can0 and can1 TX&RX pins
#------can0-------#
config-pin P9.20 can
config-pin P9.19 can
#------can1-------#
config-pin P9.26 can
config-pin P9.24 can

#-----set bitrate 500k  loopback on

sudo ip link set can0 type can bitrate 500000 loopback off restart-ms 100
sudo ifconfig can0 txqueuelen 1000

sudo ip link set can1 type can bitrate 500000 loopback off restart-ms 100
sudo ifconfig can1 txqueuelen 1000

#bring can0&can1 on
sudo ifconfig can0 up
sudo ifconfig can1 up

#end of code
```
   4. `chmod u+x internetOverUSB`设置可执行权限
   5. Create another file named internetOverUSB.sh and place it in the /etc/init.d directory. The contents should be:
```bash
#! /bin/sh

### BEGIN INIT INFO
# Provides: InternetOverUSB
# Required-Start: $all
# Required-Stop: $all
# Default-Start: 5
# Default-Stop: 0 1 6
# Short-Description: Enables Internet over USB cable
# Description: Enables access to the Internet over the Internet connection
# provided by the connected host
### END INIT INFO
case "$1" in
        start)
                sleep 20
                /root/internetOverUSB
        ;;
        stop)
                #no-op
        ;;
        *)
                #no-op
        ;;
esac

exit 0

```
   6. `chmod 755 /etc/init.d/internetOverUSB.sh` 
   7. `ln -s /etc/init.d/internetOverUSB.sh /etc/rc5.d/S99internetOverUSB.sh`
   8. `reboot`

### 2. Ubuntu主机的网络共享
```bash
sudo bash -c 'echo 1 > /proc/sys/net/ipv4/ip_forward'   #open ip tranfering 
sudo iptables -F
sudo iptables -P INPUT ACCEPT
sudo iptables -P FORWARD ACCEPT
sudo iptables -t nat -A POSTROUTING -o wlp4s0 -j MASQUERADE   #wlp4s0 internetcard name
```
### 3. BBB自启动代理程序
将整个BBBottomlayer文件夹拷入
   1. sudo vim /lib/systemd/system/can-agent.service
   2. 写入以下内容：
```bash
[Unit]
Description=Enable can agent at startup
After=generic-board-startup.service

[Service]
Type=simple
ExecStart=/usr/bin/python3 /home/debian/BBBottomlayer/py_main.py

[Install]
WantedBy=multi-user.target
```
   3.  激活服务
```bash
sudo systemctl daemon-reload
sudo systemctl enable can-agent.service
sudo reboot
```
   4. 重启后，检查service状态：`systemctl status can-agent`