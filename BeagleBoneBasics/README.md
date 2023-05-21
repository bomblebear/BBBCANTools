## Exploring in BeagleBone

[Getting Start with BeagleBone](https://cebbs.iceasy.com/forum.php?mod=viewthread&tid=9659)

**user:debian**

### 1.login into beaglebone

`ssh debian@192.168.7.2`

### 2.set the route from beglebone to internet

#### 2.1 set route from beaglebone to linux
`sudo /sbin/route add default gw 192.168.7.1`

use `ip route show` to see details

#### 2.2 set route from internet to bealgebong within linux

********
**In Ubuntu Host** you need to:
```bash
sudo bash -c 'echo 1 > /proc/sys/net/ipv4/ip_forward'
sudo iptables -F
sudo iptables -P INPUT ACCEPT
sudo iptables -P FORWARD ACCEPT
sudo iptables -t nat -A POSTROUTING -o wlp4s0 -j MASQUERADE
```
********
**In BeagleBone Host** you need to:
this can do automatically [How To Connect PocketBeagle To The Internet Via USB](https://www.ofitselfso.com/BeagleNotes/HowToConnectPocketBeagleToTheInternetViaUSB.php)
```bash
sudo nano /etc/resolv.conf

domain localdomain
search localdomain
nameserver 8.8.8.8
nameserver 8.8.4.4
```
*********

### 2.login as root
`sudo su` and back to debian with `login debian`

### 3.cloud9 IDE
you can login into BeagleBone with http://192.168.7.2/ide.html

repository:`debian@beaglebone:/var/lib/cloud9$ `


