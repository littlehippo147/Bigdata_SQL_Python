# -*- coding: utf-8 -*-
"""
Python 18_11_06

"""

# turtle 
from turtle import *
t.forward(90)
t.right(90)
t.forward(90)
t.right(45)
t.left(45)
t.color("blue")

color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

import time

clear()
color('red')
goto(-50, -50)
for i in range(10, 150, 10):
    time.sleep(1)
    circle(i)


# 크롤링
import webbrowser as wb
url = 'https://www.naver.com/'
wb.open(url)

from urllib import request as req
import datetime as dt
import bs4

r = req.urlopen("https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
soup = bs4.BeautifulSoup(r, "html.parser")
now = dt.datetime.now()

print("==============================================================")
print("* {}년 {}월 {}일 날씨 정보 ***************************".format(now.year, now.month, now.day))

print("==============================================================")
print("    도 시    날 씨              온    도  ")
print("==============================================================")

for i in soup.select("location"):
    name = i.select_one("city").string
    wf = i.select_one("wf").string
    tmn = i.select_one("tmn").string
    tmx = i.select_one("tmx").string
    
    print(" {:<6s}  {:>8s}         {:2}도 ~ {:2}도".format(name, wf, tmn, tmx))

print("==============================================================")


## chat
### server.py
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
        
### client.py
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


## calc modules myMod
    
def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multi(a, b):
    return a * b

def divi(a, b):
    return a // b
        
## calc
        
from myMod import *
while ( True ) :
        
    print(' ** 간단 계산기 ** ')
    print(' 종료 하려면 : 0 ')
    print(' **************** ')
    number1 = int(input(' 첫번째 수 : '))
    
    if ( number1 == 0 ):
        print(' Good - Bye! ')
        break
    oper = str(input(' +, -, *, / : '))
    number2 = int(input(' 두번째 수 : '))
    
    if ( oper == '+' ):
        res = plus( number1, number2 )
    elif ( oper == '-' ):
        res = minus( number1, number2 )
    elif ( oper == '*' ):
        res = multi( number1, number2 )
    elif ( oper == '/' ):
        res = divi( number1, number2 )
    else:
        print('{} 연산자 없음'.format(oper))
        
    print(' 결과 : {} {} {} = {}'.format(number1, oper, number2, res))
    
# 
import pyinstaller
import Django




