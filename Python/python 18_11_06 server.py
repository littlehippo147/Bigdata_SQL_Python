# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 10:50:21 2018

@author: user
"""

import socket

s = socket.socket()
host = socket.gethostname()
port = 3000
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))

s.listen(5)
sw = None

while True:
    if sw is None:
        print('[연결 대기...] ')
        sw, addr = s.accept()
        print(' 연결합니다 : ', addr)
        
    else:
        print(' client에서 받은 메시지 : ', end = ' ')
        print((sw.recv(1024)).decode('utf-8'))
        msg = input(' client에게 보낼 메시지 : ')
        sw.send(msg.encode('utf-8'))