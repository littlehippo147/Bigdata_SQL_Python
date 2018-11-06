# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 11:13:49 2018

@author: user
"""

from tkinter import *
from decimal import *
from math import *

window = Tk()
window.title("MyCalculator")
top_row = Frame(window)
top_row.grid(row=0, column=0, columnspan=3, sticky=N)
display = Entry(top_row, width=80, bg="light yellow")
display.grid()

# 숫자 프레임
num_pad = Frame(window)
num_pad.grid(row=1, column=0, sticky=W)
num_pad_list = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', '=']
r = 0
c = 0
for btn_text in num_pad_list:
    def cmd(x=btn_text):
        click(x)
    Button(num_pad, text=btn_text, width=6, command=cmd).grid(row=r, column=c)
    c = c + 1
    if c > 2:
        c = 0
        r = r + 1
# 연산자 프레임

operator = Frame(window)
operator.grid(row=1, column=2, sticky=W)
operator_list = [
    '*', '/',
    '+', '-',
    '(', ')',
    'C',',']
r = 0
c = 0
for btn_text in operator_list:
    def cmd(x=btn_text):
        click(x)
    Button(operator, text=btn_text, width=6, command=cmd).grid(row=r, column=c)
    c = c + 1
    if c > 1:
        c = 0
        r = r + 1

# 상수 프레임
constants = Frame(window)
constants.grid(row=3, column=0, sticky=W)
constants_list = [
    'pi', 'e', 'ans']
r = 0
c = 0
for btn_text in constants_list:
    def cmd(x=btn_text):
        click(x)
    Button(constants, text=btn_text, width=6, command=cmd).grid(row=r, column=c)
    c = c + 1
    if c > 2:
        c = 0
        r = r + 1

# 통계 프레임
stat = Frame(window)
stat.grid(row=3, column=1, sticky=W)
stat_list = ['data', 'entry', 'complete']
r = 0
c = 0
for btn_text in stat_list:
    def cmd(x=btn_text):
        click(x)
    Button(stat, text=btn_text, width=9, command=cmd).grid(row=r, column=c)
    c= c + 1

# 함수 프레임
functions = Frame(window)
functions.grid(row=1, column=1, sticky=W)
functions_list = [
    'n!', 'to bin',
    'from bin', 'mean',
    'var', 'sd',
    '√', 'x^2',
    'ln', 'log',
    '10^x', '1/x']
r = 0
c = 0
for btn_text in functions_list:
    def cmd(x=btn_text):
        click(x)
    Button(functions, text=btn_text, width=9, command=cmd).grid(row=r, column=c)
    c = c + 1
    if c > 2:
        c = 0
        r = r + 1

# 필요 함수
def mean(n):
    return sum(n) / len(n)
def var(n):
    j=0
    t=mean(n)
    for i in n:
        n[j]=n[j]-t
        n[j]=n[j]*n[j]
        j=j+1
    return mean(n)
def factorial(n):
    n=int(n)
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
def to_binary(n):
    n=int(n)
    n=bin(n)
    return n[2:]
def from_binary(n):
    n=int(n,2)
    return n

# 키 정의
def click(key):
    global N
    if key == '=':
        try:
            result = str(eval(display.get()))[0:10]
            display.insert(END, " = " + result)
        except:
            display.insert(END, " --> Error!")
    elif key == "C":
        display.delete(0, END)
    elif key == constants_list[0]:
        display.insert(END, pi)
    elif key == constants_list[1]:
        display.insert(END, exp(1))
    elif key == functions_list[0]:
        n = display.get()
        display.delete(0, END)
        display.insert(END, factorial(n))
    elif key == functions_list[1]:
        n = display.get()
        display.delete(0, END)
        display.insert(END, to_binary(n))
    elif key == functions_list[2]:
        n = display.get()
        display.delete(0, END)
        display.insert(END, from_binary(n))
    elif key == functions_list[3]:
        display.delete(0, END)
        display.insert(END, mean(N))
    elif key == functions_list[4]:
        display.delete(0, END)
        display.insert(END, var(N))
    elif key == functions_list[5]:
        display.delete(0, END)
        display.insert(END, sqrt(var(N)))
    elif key == functions_list[6]:
        n = display.get()
        display.delete(0, END)
        x=float(n)
        display.insert(END, sqrt(x))
    elif key == functions_list[7]:
        n = display.get()
        display.delete(0, END)
        x = float(n)
        display.insert(END, x * x)
    elif key == functions_list[8]:
        n = display.get()
        display.delete(0, END)
        x = float(n)
        display.insert(END, log(x))
    elif key == functions_list[9]:
        n = display.get()
        display.delete(0, END)
        x = float(n)
        display.insert(END, log10(x))
    elif key == functions_list[10]:
        n = display.get()
        display.delete(0, END)
        x = float(n)
        display.insert(END, 10 ** x)
    elif key == functions_list[11]:
        n = display.get()
        display.delete(0, END)
        x = float(n)
        display.insert(END, 1 / x)
    elif key == 'data':
        display.delete(0, END)
        N = []
    elif key == 'entry':
        N.append(float(display.get()))
        display.delete(0, END)
    elif key == 'complete':
        N.append(float(display.get()))
        display.delete(0, END)
        display.insert(END, N)
    else:
        display.insert(END, key)

window.mainloop()