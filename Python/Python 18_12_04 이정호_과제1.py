# 이정호_과제1.py

import numpy as np
import MySQLdb
import sqlite3
import os

os.getcwd()
os.chdir('C:\\Users\\user\\Documents\\python project')

# 내 컴퓨터 Mysql Server에 연결
con = MySQLdb.connect(host='localhost', port=3306, db='mysql', user='root', passwd='1234')
c = con.cursor()

# BalanceDB 생성 및 사용
c.execute("create database BalanceDB;")
c.execute("use BalanceDB;")

# Balance_scale Table 생성
create_table = """create table if not exists Balance_scale
(Class_Name char(1),
 Left_Weight int,
 Left_Distance int,
 Right_Weight int,
 Right_Distance int);"""

c.execute(create_table)

# Balance-scale data 불러와서 Class name이 L인 데이터만 뽑기
data = np.array(np.loadtxt('balance-scale.csv', delimiter = ',', dtype = np.str))

Ldata = data[data[:, 0] == 'L']

# Balane_scale table에 데이터 입력 후 저장
for row in Ldata:
    c.execute("insert into Balance_scale values (%s, %s, %s, %s, %s);", row)
con.commit()

# BalanceDB로부터 Balance_scale Table 불러오기
c.execute("select * from Balance_scale;")
rows = c.fetchall()

# 불러온 Table Print
import time

start = time.time()
for row in rows:
    print(list(row))
end = time.time()

print(len(rows), 'rows in set', '<{:2f} sec>'.format(end - start))

