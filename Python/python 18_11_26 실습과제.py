# python 18-11-26 Logistic Classification 실습과제
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import math
import os

os.getcwd()
os.chdir('C:\\Users\\user\\Documents\\python project')

tf.set_random_seed(77)

# 759개 데이터, 총 9열
xy = np.loadtxt('data-03-diabetes.csv', delimiter = ',', dtype = np.float32)

# X 8열, y 1열 train, test 나누기
x_tr, y_tr, x_te, y_te = xy[:530, :-1], xy[:530, [-1]], xy[530:, :-1], xy[530:, [-1]]


X = tf.placeholder(tf.float32, shape = [None, 8])
Y = tf.placeholder(tf.float32, shape = [None, 1])

W = tf.Variable(tf.random_normal([8, 1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

## sigmoid 사용: tf.div(1, 1 + tf.exp(tf.matmul(-X, W)))
hypothesis = tf.sigmoid(tf.matmul(X, W) + b)

## logistic에서 쓰는 cost 함수
cost = tf.reduce_mean(-Y * tf.log(hypothesis) - (1-Y) * tf.log(1-hypothesis))
optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.1)
train = optimizer.minimize(cost)

sess =tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(50000):
    sess.run(train, feed_dict = {X : x_tr, Y : y_tr})
    if step % 1000 == 0:
        print(step, sess.run([cost, W, b], feed_dict = {X : x_tr, Y : y_tr}))
        
# 예측하기
predict = tf.cast(hypothesis > 0.5, dtype=tf.float32)   # tf.cast  
accuracy = tf.reduce_mean(tf.cast(tf.equal(predict, Y), dtype=tf.float32))

## Accuracy Report
h, p, a = sess.run([hypothesis, predict, accuracy], feed_dict = {X : x_te, Y : y_te})

print('W :\n', sess.run(W), '\n', 'b :', sess.run(b), '\n', 'accuracy :', a)

## 성능 향상을 위해서 할 수 있는 것?? => 학습 데이터 늘리기
x2_tr, y2_tr, x2_te, y2_te = xy[:709, :-1], xy[:709, [-1]], xy[709:, :-1], xy[709:, [-1]]


X2 = tf.placeholder(tf.float32, shape = [None, 8])
Y2 = tf.placeholder(tf.float32, shape = [None, 1])

W2 = tf.Variable(tf.random_normal([8, 1]), name='weight')
b2 = tf.Variable(tf.random_normal([1]), name='bias')

## sigmoid 사용: tf.div(1, 1 + tf.exp(tf.matmul(-X, W)))
hypothesis2 = tf.sigmoid(tf.matmul(X2, W2) + b2)

## logistic에서 쓰는 cost 함수
cost2 = tf.reduce_mean(-Y2 * tf.log(hypothesis2) - (1-Y2) * tf.log(1-hypothesis2))
optimizer2 = tf.train.GradientDescentOptimizer(learning_rate = 0.01)
train2 = optimizer2.minimize(cost2)

sess =tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(100000):
    sess.run(train2, feed_dict = {X2 : x2_tr, Y2 : y2_tr})
    if step % 1000 == 0:
        print(step, sess.run([cost2, W2, b2], feed_dict = {X2 : x2_tr, Y2 : y2_tr}))
        
# 예측하기
predict2 = tf.cast(hypothesis2 > 0.5, dtype=tf.float32)   # tf.cast  
accuracy2 = tf.reduce_mean(tf.cast(tf.equal(predict2, Y2), dtype=tf.float32))

## Accuracy Report
a2 = sess.run(accuracy2, feed_dict = {X2 : x2_te, Y2 : y2_te})

# 성능 0.8까지
print('W :\n', sess.run(W2), '\n', 'b :', sess.run(b2), '\n', 'accuracy :', a2)
