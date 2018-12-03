# python 18-11-30 leaf classification 실습과제

import numpy as np
import tensorflow as tf
import random
import os
import MySQLdb
import sqlite3
from sklearn.model_selection import train_test_split as tts

os.getcwd()
os.chdir('C:\\Users\\user\\Documents\\python project')

tf.set_random_seed(777)

# DB 생성, leaf 테이블 추가.
con = MySQLdb.connect(host='localhost', port=3306, db='mysql', user='root', passwd='1234')
c = con.cursor()

c.execute("create database leaf_all;")
c.execute("use leaf_all;")

create_table = """create table if not exists leaf
(class int,
 specimen_number int,
 eccentricity float,
 aspect_ratio float,
 elongation float,
 solidity float,
 stochastic_convexity float,
 isoperimetric_factor float,
 MID float,
 lobedness float,
 avg_intensity float,
 avg_contrast float,
 smoothness float,
 third_moment float,
 uniformity float,
 entropy float);"""

c.execute(create_table)

# 자신과 KPC002에 권한 부여
c.execute("grant all privileges on leaf_all.* to 'KPC001'@'localhost';")
c.execute("grant all privileges on leaf_all.* to 'KPC002'@'10.1.42.45';")
c.execute("flush privileges;")

# leaf.csv 파일 불러와 leaf_all DB에 데이터 입력
xy = np.loadtxt('leaf.csv', delimiter = ',', dtype = np.float32)

for row in xy:
    c.execute("insert into leaf values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", row)

con.commit()

# leaf_all DB로부터 데이터 다시 불러와서 텐서플로우로 분석
con2 = MySQLdb.connect(host='localhost', port=3306, db='leaf_all', user='KPC001', passwd='1234')
c2 = con2.cursor()

c2.execute("SELECT * FROM leaf;")
rows = c2.fetchall()

x = []
y = []
for row in rows:
    x.append(list(row[2:]))
    y.append(row[0])

x_tr, x_te, y_tr, y_te = tts(x, y, test_size = 0.3, random_state = 777, stratify = y)

x_tr, x_te, y_tr, y_te = np.array(x_tr, dtype = np.float32), np.array(x_te, dtype = np.float32), \
                         np.array(np.transpose(y_tr), dtype = np.int16), np.array(np.transpose(y_te), dtype = np.int16)

y_tr = tf.reshape(tf.one_hot(y_tr, 30), [-1, 30])

X = tf.placeholder(tf.float32, [None, 14])
Y = tf.placeholder(tf.float32, [None, 30])



# Layer 생성 / 각 계층 이름 생성

W1 = tf.Variable(tf.random_normal([14, 100], stddev = 0.1), name='weight1')
b1 = tf.Variable(tf.zeros([100]), name='bias1')
layer1 = tf.nn.relu(tf.matmul(X, W1) + b1)

W2 = tf.Variable(tf.random_normal([100, 30], stddev = 0.1), name='weight2')
b2 = tf.Variable(tf.zeros([30]), name='bias2')
layer2 = tf.nn.relu(tf.matmul(layer1, W2) + b2)

W8 = tf.Variable(tf.random_normal([30, 30], stddev = 0.1), name='weight8')
b8 = tf.Variable(tf.zeros([30]), name='bias8')
model = tf.matmul(layer2, W8) + b8
hypothesis = tf.sigmoid(model)


cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels = Y, logits = model))
optimizer = tf.train.AdamOptimizer(learning_rate = 0.000001)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

y_tr = sess.run(y_tr)



# 최적화 실행
for step in range(30000):
    sess.run(train, feed_dict = {X : x_tr, Y : y_tr})
    if step % 1000 == 0:
        print(step, sess.run(cost, feed_dict = {X : x_tr, Y : y_tr}))

    
# 예측값 및 정확도
predict = sess.run(tf.argmax(hypothesis, 1), feed_dict = {X : x_te})
accuracy = sess.run(tf.reduce_mean(tf.cast(tf.equal(predict, y_te), dtype=tf.float32)))
sess.run(hypothesis, feed_dict = {X : x_te})
print('predict :', predict, '\n', 'y_true :', y_te, '\n', 'accuracy :', accuracy)


# accuracy DB 만들고 권한 부여
c.execute("create database accuracyDB;")
c.execute("use accurayDB;")

c.execute("grant all privileges on accuracyDB.* to 'KPC001'@'localhost';")
c.execute("grant all privileges on accuracyDB.* to 'KPC002'@'10.1.42.45';")
c.execute("flush privileges;")

create_table = "create table if not exists accuray01 (Accuracy float);"
c.execute(create_table)

c.execute("insert into leaf values (%s);", [accuracy])