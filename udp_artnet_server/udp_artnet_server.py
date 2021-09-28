# -*- coding: utf-8 -*-
import socket
from StupidArtnet import StupidArtnet
import time
import random
from datetime import datetime

# Arnet end host
target_ip = '192.168.1.77'
universe = 0
packet_size = 512
a = StupidArtnet(target_ip, universe, packet_size)

# check arnet info
print(a)

# udp server ip and port
host = '192.168.1.229'
port = 7889

def udpsocket():
    print ('wait shreknection on ', host, ':', port, sep='')
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # create socket
    sock.bind((host, port)) # server ip, port
    data, addr = sock.recvfrom(200)
    print ('server is received data:', data.decode())
    print ('send client ip and port: ', addr[0],':', addr[1], sep='')
    return data.decode()

def dmx_value():
    a.set_single_value(channel, 100)
    a.show()
    a.set_single_value(channel, 0)
    time.sleep(0.5)
    a.show()
    print("time =", datetime.now().time().strftime("%H:%M:%S"))
    print('ocel sends massage to', channel, 'dmx channel\n')

while 1:
    massage = udpsocket()
    if massage == 'heart': # channel 180 by udp from bright
        channel = 180
        dmx_value()
    elif massage == 'light': # channel 182 by udp from bright
        channel = 182
        dmx_value()
    elif massage == 'sun': # channel 184 by udp from bright
        channel = 184
        dmx_value()
    elif massage == 'shadows': # channel 181 by udp from bright
        channel = 181
        dmx_value()
    elif massage == 'ralley': # channel 183 by udp from resolume pc
        channel = 183
        dmx_value()
    elif massage == 'tunnel': # channel 185 by udp from vlc tunnel pc
        channel = 185
        dmx_value()
    else:
        pass
