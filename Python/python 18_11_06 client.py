# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 10:51:22 2018

@author: user
"""

import socket
s = socket.socket()
host = socket.gethostname()
port = 3000
s.connect((host, port))
print( ' 연결합니다 : ', host)

while True:
    msg = input(' server에게 보낼 메시지 : ')
    s.send(msg.encode('utf-8'))
    print(' server에서 받은 메시지 : ', end = ' ')
    print((s.recv(1024)).decode('utf-8'))
