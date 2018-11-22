# python 18_11_22 code

# Multi_Variable Linear Regression

import tensorflow as tf
import numpy as np

tf.set_random_seed(777)
# 다변량 데이터 / 각 변수를 리스트로 사용(불ㅡㅡ편)
x1d = [73, 93, 89, 96, 73]
x2d = [80, 88, 91, 98, 66]
x3d = [75, 93, 90, 100, 70]

yd = [152, 185, 180, 196, 142]

x1 = tf.placeholder(tf.float32)
x2 = tf.placeholder(tf.float32)
x3 = tf.placeholder(tf.float32)

y = tf.placeholder(tf.float32)

W1 = tf.Variable(tf.random_normal([1]), name='weight1')
W2 = tf.Variable(tf.random_normal([1]), name='weight2')
W3 = tf.Variable(tf.random_normal([1]), name='weight3')
b = tf.Variable(tf.random_normal([1]), name='bias')

hypothesis = x1 * W1 + x2 * W2 + x3 * W3 + b

cost = tf.reduce_mean(tf.square(hypothesis - y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.00001)
train = optimizer.minimize(cost)

sess =tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(100000):
    sess.run(train, feed_dict = {x1 : x1d, x2 : x2d, x3 : x3d, y : yd})
    if step % 1000 == 0:
        print(step, sess.run(cost, feed_dict = {x1 : x1d, x2 : x2d, x3 : x3d, y : yd}))

fcost, fW1, fW2, fW3, fb = sess.run([cost, W1, W2, W3, b], feed_dict = {x1 : x1d, x2 : x2d, x3 : x3d, y : yd})

print(sess.run(hypothesis, feed_dict = {x1 : x1d, x2 : x2d, x3 : x3d}), '\n', yd)


# Matrix 사용 / tf.matmul() : 행렬 곱

Xd = np.transpose([[73, 93, 89, 96, 73],
               [80, 88, 91, 98, 66],
               [75, 93, 90, 100, 70]])
Xd
Yd = np.transpose([yd])

X = tf.placeholder(tf.float32, shape = [None, 3])

Y = tf.placeholder(tf.float32, shape = None)

W4 = tf.Variable(tf.random_normal([3, 1]), name='weight4')
b2 = tf.Variable(tf.random_normal([1]), name='bias2')

hypothesis2 = tf.matmul(X, W4) + b2

cost2 = tf.reduce_mean(tf.square(hypothesis2 - Y))
optimizer2 = tf.train.GradientDescentOptimizer(learning_rate = 0.00001)
train2 = optimizer2.minimize(cost2)


sess =tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(100000):
    sess.run(train2, feed_dict = {X : Xd, Y : Yd})
    if step % 1000 == 0:
        print(step, sess.run(cost2, feed_dict = {X : Xd, Y : Yd}))


print(sess.run(hypothesis2, feed_dict = {X : Xd, Y : Yd}), '\n',yd, '\n', sess.run([cost2, W4, b2], feed_dict = {X : Xd, Y : Yd}))
