# python 18-11-26 softmax Classification

# ReLU 함수
import matplotlib.pyplot as plt
import math

def ReLU(x):
    return max(0,x)

def sigmoid(x):
    return 1 / (1 + math.e**-x)

a, b, c = [], [], []
for i in range(-15,15):
    a.append(i)
    b.append(sigmoid(i))
    c.append(ReLU(i/10))
    
plt.plot(a, b)
plt.plot(a, c)
plt.show()    

# softmax multi classification
import numpy as np
import tensorflow as tf
import os

os.getcwd()
os.chdir('C:\\Users\\user\\Documents\\python project')

tf.set_random_seed(777)

# data set
x_data = [[1, 2, 1, 1],
          [2, 1, 3, 2],
          [3, 1, 3, 4],
          [4, 1, 5, 5],
          [1, 7, 5, 5],
          [1, 2, 5, 6],
          [1, 6, 6, 6],
          [1, 7, 7, 7]]

y_data = [[0, 0, 1],
          [0, 0, 1],
          [0, 0, 1],
          [0, 1, 0],
          [0, 1, 0],
          [0, 1, 0],
          [1, 0, 0],
          [1, 0, 0],]

X = tf.placeholder(tf.float32, shape = [None, 4])
Y = tf.placeholder(tf.float32, shape = [None, 3])

W = tf.Variable(tf.random_normal([4, 3]), name='weight')
b = tf.Variable(tf.random_normal([3]), name='bias')

## softmax hypothesis tf.nn.softmax
hypothesis = tf.nn.softmax(tf.matmul(X, W) + b)

# cost 함수
## 방법 1
cost = tf.reduce_mean(tf.reduce_sum(-Y * tf.log(hypothesis), axis = 1))
optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.1)
train = optimizer.minimize(cost)

## 방법 2 : hypothesis까지 한 번에 하는 방법
cost2 = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits = tf.matmul(X,W) + b, labels = Y))
optimizer2 = tf.train.GradientDescentOptimizer(learning_rate = 0.1)
train2 = optimizer.minimize(cost2)


# session 생성
## 방법 1
sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(40000):
    sess.run(train, feed_dict = {X : x_data, Y : y_data})
    if step % 500 == 0:
        print(step, sess.run([cost, W, b], feed_dict = {X : x_data, Y : y_data}))

## 방법 2
sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(40000):
    sess.run(train2, feed_dict = {X : x_data, Y : y_data})
    if step % 500 == 0:
        print(step, sess.run([cost2, W, b], feed_dict = {X : x_data, Y : y_data}))

# predict
p = sess.run(hypothesis, feed_dict = {X : [[1,2,1,1]]})
print(p, sess.run(tf.argmax(p, 1)))

p2 = sess.run(hypothesis, feed_dict = {X : [[1,2,1,1]]})
print(p2, sess.run(tf.argmax(p2, 1)))
