import socket
import os
import time
import subprocess
import sys
from datetime import datetime

while 1:
    now = str(datetime.now().time())
    morning = '17:59:59.630000'
    if now >= morning:
        break
    else:
        time.sleep(0.05)

subprocess.Popen(['C:\\APP\\startvlc.bat'])

while 1:
    byte_message = bytes("tunnel", "utf-8")
    opened_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    opened_socket.sendto(byte_message, ("192.168.1.229", 7889))
    now = datetime.now().time()
    print("time =", now)
    time.sleep(556)
