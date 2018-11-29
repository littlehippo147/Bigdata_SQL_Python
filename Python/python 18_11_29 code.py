# python 18-11-29 XOR Deep learning 실습과제

import numpy as np
import tensorflow as tf
import os
import random


os.getcwd()
os.chdir('C:\\Users\\user\\Documents\\python project')

tf.set_random_seed(777)

# XOR Deep
x_data = [[0,0],
          [0,1],
          [1,0],
          [1,1]]

y_data = [[0],
          [1],
          [1],
          [0]]
np.shape(x_data)
x_data = np.array(x_data, dtype=np.float32)
y_data = np.array(y_data, dtype=np.float32)

# global step 설정, 전체 실행 단계
global_step = tf.Variable(0, trainable = False, name = 'global_step')

X = tf.placeholder(tf.float32, shape = [None, 2])
Y = tf.placeholder(tf.float32, shape = [None, 1])

# Layer 생성 / 각 계층 이름 생성
with tf.name_scope('layer1'):
    W1 = tf.Variable(tf.random_normal([2, 10]), name='weight1')
    b1 = tf.Variable(tf.random_normal([10]), name='bias1')
    layer1 = tf.sigmoid(tf.matmul(X, W1) + b1)
    # 가중치, 편향 별 히스토그램
    w1_hist = tf.summary.histogram("weights1", W1)
    b1_hist = tf.summary.histogram("biases1", b1)
    layer1_hist = tf.summary.histogram("layer1", layer1)

with tf.name_scope('layer2'):
    W2 = tf.Variable(tf.random_normal([10, 10]), name='weight2')
    b2 = tf.Variable(tf.random_normal([10]), name='bias2')
    layer2 = tf.sigmoid(tf.matmul(layer1, W2) + b2)

    w2_hist = tf.summary.histogram("weights2", W2)
    b2_hist = tf.summary.histogram("biases2", b2)
    layer2_hist = tf.summary.histogram("layer2", layer2)

with tf.name_scope('layer3'):
    W3 = tf.Variable(tf.random_normal([10, 10]), name='weight3')
    b3 = tf.Variable(tf.random_normal([10]), name='bias3')
    layer3 = tf.sigmoid(tf.matmul(layer2, W3) + b3)

    w3_hist = tf.summary.histogram("weights3", W3)
    b3_hist = tf.summary.histogram("biases3", b3)
    layer3_hist = tf.summary.histogram("layer3", layer3)

with tf.name_scope('output'):
    W4 = tf.Variable(tf.random_normal([10, 1]), name='weight4')
    b4 = tf.Variable(tf.random_normal([1]), name='bias4')
    hypothesis = tf.sigmoid(tf.matmul(layer3, W4) + b4)

    w4_hist = tf.summary.histogram("weights4", W4)
    b4_hist = tf.summary.histogram("biases4", b4)
    hypothesis_hist = tf.summary.histogram("hypothesis", hypothesis)
    
with tf.name_scope('optimizer'):
    cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1-Y) * tf.log(1-hypothesis))
    optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.1)
    train = optimizer.minimize(cost, global_step = global_step)

sess = tf.Session()

sess.run(tf.global_variables_initializer())

# 손실값, 예측값, 정확도 추적 / (summary 수집)
tf.summary.scalar('cost', cost)
predict = sess.run(tf.cast(hypothesis > 0.5, dtype=tf.float32), feed_dict = {X : x_data})
accuracy = tf.reduce_mean(tf.cast(tf.equal(predict, y_data), dtype=tf.float32))
accuracy_summ = tf.summary.scalar("accuracy", accuracy)

# 텐서 수집 및 저장할 디렉토리 설정
merged = tf.summary.merge_all()
writer = tf.summary.FileWriter('./logs', sess.graph)

# 최적화 실행
for step in range(10000):
    sess.run(train, feed_dict = {X : x_data, Y : y_data})
    if step % 200 == 0:
        print(step, sess.run([cost, W1, b1, W2, b2], feed_dict = {X : x_data, Y : y_data}))
    
    
    summary = sess.run(merged, feed_dict = {X : x_data, Y : y_data}) # 모아둔 텐서의 값 계산하여 수집
    writer.add_summary(summary, global_step = sess.run(global_step)) # 아까 지정한 디렉토리에 저장









