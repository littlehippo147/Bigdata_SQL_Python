# 18_11_20 실습과제
import csv
import MySQLdb
import sqlite3
import sys
import os
import numpy as np
import pandas as pd
import tensorflow as tf

os.getcwd()
os.chdir('C:\\Users\\user\\Documents\\python project')

# cars.csv를 읽어서 carsDB에 저장
input_file = 'cars.csv'
output_file = 'cars_predict001.csv'

con = MySQLdb.connect(host='localhost', port=3306, db='mysql', user='root', passwd='1234')
c = con.cursor()

c.execute("create database carsDB;")
c.execute("use carsDB;")
c.execute("grant all privileges on carsDB.* to 'KPC001'@'localhost';")
c.execute("flush privileges;")

create_table = """create table if not exists cars
(speed float,
 dist float);"""

c.execute(create_table)

file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader)
for row in file_reader:
	data = []
	for column_index in range(len(header)):
		data.append(row[column_index])
	c.execute("INSERT INTO cars VALUES (%s, %s);", data)

con.commit()

# 필요한 유저들에 권한 부여
c.execute("grant all privileges on carsDB.* to 'KPC002'@'10.1.42.45';")
c.execute("flush privileges;")


# 예측할 데이터 테이블 만들기
pred = [i for i in range(30, 280, 5)]
len(pred)

pred = pd.DataFrame(pred)
pred.to_csv(output_file, header = False, index = False)


# carsDB 접속해 데이터 볼러운 후 텐서플로 학습시키기
## DB에서 테이블을 불러와 python workspace 상에 저장
con = MySQLdb.connect(host='localhost', port=3306, db='carsDB', user='KPC001', passwd='1234')
c = con.cursor()

c.execute("SELECT * FROM cars")
rows = c.fetchall()

speed = []  # x 변수
dist = []   # y 변수
for row in rows:
    speed.append(row[0])
    dist.append(row[1])

## 텐서플로 학습
X = tf.placeholder(tf.float32, shape = [None])
Y = tf.placeholder(tf.float32, shape = [None])

W = tf.Variable(tf.random_normal([1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

hypothesis = X * W + b

cost =  tf.reduce_mean(tf.square(hypothesis - Y))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(30000):
    sess.run(train, feed_dict = {X:speed, Y:dist})
    if step % 100 == 0 :
        print(step,sess.run(cost, feed_dict = {X:speed, Y:dist}),sess.run(W),sess.run(b))
        
W_val, b_val = sess.run(W), sess.run(b) # 결정된 W, b 값

## 예측할 데이터 불러와서 예측한 결과값 합치기
data = pd.read_csv(output_file, header = None)    # 예측할 데이터

data[1] = sess.run(hypothesis, feed_dict = {X:data[0]})

data.columns = ['speed', 'dist']

data.to_csv(output_file, header = True, index = False)

## cars_predict 파일 저장할 cars_predDB와 table 생성
c.execute("create database cars_predDB;")
c.execute("use cars_predDB;")
c.execute("grant all privileges on cars_predDB.* to 'KPC001'@'localhost';")
c.execute("grant all privileges on carsDB.* to 'KPC002'@'10.1.42.45';")
c.execute("flush privileges;")

create_table2 = """create table if not exists cars_pred01
(speed float,
 dist float);"""

c.execute(create_table2)

## cars_predict 저장
file_reader = csv.reader(open(output_file, 'r'), delimiter=',')
header = next(file_reader)
for row in file_reader:
	data = []
	for column_index in range(len(header)):
		data.append(row[column_index])
	c.execute("INSERT INTO cars_pred01 VALUES (%s, %s);", data)

con.commit()
