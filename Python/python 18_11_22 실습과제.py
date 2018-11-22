# python 18_11_22 실습과제

import numpy as np
import tensorflow as tf
import MySQLdb
import sqlite3
import os

os.getcwd()
os.chdir('C:\\Users\\user\\Documents\\python project')
tf.set_random_seed(777)

## score data 파일을 numpy로 불러와 저장
xy = np.loadtxt('data-01-test-score.csv', unpack = True, delimiter = ',', dtype = np.float32)

# 합계와 평균 열 만들기
xy_total = sum(xy)
xy_average = xy_total / len(xy)

xy = np.r_[xy, [xy_total], [xy_average]]

xy = np.transpose(xy)

# DB 생성, score001 테이블 추가.
con = MySQLdb.connect(host='localhost', port=3306, db='mysql', user='root', passwd='1234')
c = con.cursor()

c.execute("create database scoreDB;")
c.execute("use scoreDB;")

create_table = """create table if not exists score001
(Quiz1 float,
 Quiz2 float,
 Midterm float,
 Final float,
 Total float,
 Averager float);"""

c.execute(create_table)

# score001 테이블에 xy 데이터 입력
for row in xy:
    c.execute("insert into score001 values (%s, %s, %s, %s, %s, %s);", row)

con.commit()

# score001 테이블 불러와 x, y 만들기
c.execute("select * from score001;")
rows = c.fetchall()

x = []
y = []
for row in rows:
    x.append(list(row[:3]))
    y.append(row[3])

x = np.array(x)
y = np.array(np.transpose([y]))

# x, y를 train 20개, test 5개로 각각 나눔
x_train, x_test = x[:20, :], x[20:, :]
y_train, y_test = y[:20, :], y[20:, :]

X = tf.placeholder(tf.float32, shape = [None, 3])
Y = tf.placeholder(tf.float32, shape = [None, 1])

W = tf.Variable(tf.random_normal([3, 1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

hypothesis = tf.matmul(X, W) + b

cost = tf.reduce_mean(tf.square(hypothesis - Y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.00001)
train = optimizer.minimize(cost)

sess =tf.Session()
sess.run(tf.global_variables_initializer())

# 학습
for step in range(100000):
    sess.run(train, feed_dict = {X : x_train, Y : y_train})
    if step % 1000 == 0:
        print(step, sess.run([cost, W, b], feed_dict = {X : x_train, Y : y_train}))

costv, Wv, bv = sess.run([cost, W, b], feed_dict = {X : x_train, Y : y_train})

y_pred = sess.run(hypothesis, feed_dict = {X : x_test}) # 예측 y값
residual = y_pred - y_test                                          # 예측 y - 실제 y 값 = 오차값
pred_cost = tf.reduce_mean(tf.square(residual))                     # 예측 cost
print('예측값 :', np.transpose(y_pred), '\n실제값 :', np.transpose(y_test), '\n오차값 :', \
      np.transpose(residual), '\n예측 비용 :', sess.run(pred_cost))

# cost table 생성
create_table2 = "create table if not exists cost (Cost float);"

c.execute(create_table2)

c.execute("insert into cost values (%s);", [sess.run(pred_cost)])
con.commit()
