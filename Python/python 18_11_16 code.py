# 실습과제 KPC001
import csv
import MySQLdb
import sqlite3
import sys
import os
import pandas
from datetime import datetime, date

os.getcwd()
os.chdir('C:\\Users\\user\\Documents\\python project')


## 서버 1에서 CSV 파일 불러와 저장
input_file = 'supplier_data.csv'

con = MySQLdb.connect(host='localhost', port=3306, db='my_sup', user='KPC001', passwd='1234')
c = con.cursor()

c.execute("create database My_Sup;")
c.execute("use My_Sup;")
c.execute("create user 'KPC001'@'localhost' identified by '1234';")
c.execute("grant all privileges on My_Sup.* to 'KPC001'@'localhost';")
c.execute("flush privileges;")

create_table = """create table if not exists suppliers
(supplier_name varchar(20),
invoice_number varchar(20),
part_number varchar(20),
cost float,
purchase_date date);"""

c.execute(create_table)

file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader)
for row in file_reader:
	data = []
	for column_index in range(len(header)):
		if column_index < 4:
			data.append(str(row[column_index]).lstrip('$')\
			.replace(',', '').strip())
		else:
			a_date = datetime.date(datetime.strptime(\
			str(row[column_index]), '%m/%d/%y'))
			# %Y: year is 2016; %y: year is 15
			a_date = a_date.strftime('%Y-%m-%d')
			data.append(a_date)
	print(data)
	c.execute("INSERT INTO Suppliers VALUES (%s, %s, %s, %s, %s);", data)

con.commit()

c.execute("UPDATE suppliers SET supplier_name = 'KPC001';")

c.execute("create user 'KPC002'@'10.1.42.45' identified by '1234';")
c.execute("grant all privileges on My_Sup.* to 'KPC002'@'10.1.42.45';")
c.execute("flush privileges;")


con.commit()

## 서버 4로부터 TABLE 불러와 저장
import csv
import MySQLdb
import sys


con=MySQLdb.connect(host='10.1.42.61',port=3306,db='my_sup',user='KPC001',passwd='1234')
c=con.cursor()

# c.execute("""UPDATE Suppliers SET Supplier_Name = 'kpc003';""")

c.execute("SELECT * FROM Suppliers")
rows = c.fetchall()

con2=MySQLdb.connect(host='localhost',port=3306,db='my_sup',user='KPC001',passwd='1234')
c2=con2.cursor()

create_file = """create table if not exists suppliers2
(supplier_name varchar(20),
invoice_number varchar(20),
part_number varchar(20),
cost float,
purchase_date date);"""

c2.execute(create_file)

for row in rows:
    c2.execute("""INSERT INTO Suppliers2 VALUES (%s, %s, %s, %s, %s);""", row)



con2.commit()

## 마지막으로 불러와 내 서버에 저장된 데이터 CSV 파일로 저장
output_file = "Team5_이정호.csv"
f = open(output_file, 'w', newline = '')
filewriter = csv.writer(f, delimiter = ',')
header = ['supplier name', 'invoice number', 'part number', 'cost', 'purchase date']
filewriter.writerow(header)

for row in rows:
    filewriter.writerow(row)
f.close()

###########################################################
t = [1, 10, 5, 9, 7, 8]
t.sort()
t

## gate 함수
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = w1 * x1 + w2 * x2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

print(AND(0,0))
print(AND(0,1))
print(AND(1,0))
print(AND(1,1))

def NAND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = w1 * x1 + w2 * x2
    if tmp <= theta:
        return 1
    elif tmp > theta:
        return 0

print(NAND(0,0))
print(NAND(0,1))
print(NAND(1,0))
print(NAND(1,1))


def OR(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.4
    tmp = w1 * x1 + w2 * x2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

print(OR(0,0))
print(OR(0,1))
print(OR(1,0))
print(OR(1,1))

def XOR(x1, x2):     # 심층에 은닉 층에서 분류 (퍼셉트론의 기초개념?)
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

print(XOR(0,0))
print(XOR(0,1))
print(XOR(1,0))
print(XOR(1,1))

# Cost 함수
from math import *
import matplotlib.pylab as plt

def cost(x, y, w):
    c = 0
    for i in range(len(x)):
        hx = w * x[i]
        loss = (hx - y[i]) ** 2
        c += loss
    return c / len(x)

        
x = [1, 2, 3]
y = [5, 6, 7]

print(cost(x, y, -1)) 
print(cost(x, y, 0))
print(cost(x, y, 1))
print(cost(x, y, 2))
print(cost(x, y, 3))
print(cost(x, y, 5))
print(cost(x, y, 4))
print(cost(x, y, 3.5))
print(cost(x, y, 3.2))
print(cost(x, y, 3.1))
print(cost(x, y, 2.5))
print(cost(x, y, 2.8))
print(cost(x, y, 2.9))
print(cost(x, y, 2.7))
print(cost(x, y, 2.71))
print(cost(x, y, 2.72))
print(cost(x, y, 2.713))
print(cost(x, y, 2.7134))
print(cost(x, y, e))

for i in range(-30, 50):
    w = i / 10
    c = cost(x,y,w)
    print(w,c)
    plt.plot(w, c, 'ro')
plt.show()


# 미분 : 순간 변화량, 기울기
def gradient_descent(x, y, w):
    c = 0
    for i in range(len(x)):
        hx = w * x[i]
        loss = (hx - y[i]) * x[i]
        c += loss
    return c / len(x)


