# python 18_11_23 실습과제

# 집값 예측하기

import numpy as np
import tensorflow as tf
import os

os.getcwd()
os.chdir('C:\\Users\\user\\Documents\\python project')
tf.set_random_seed(777)

# boston train, test, predict 데이터 불러오기
xy_train = np.loadtxt('boston_train.csv', delimiter = ',', dtype = np.float32, skiprows = 1)
xy_test = np.loadtxt('boston_test.csv', delimiter = ',', dtype = np.float32, skiprows = 1)
x_pred = np.loadtxt('boston_predict.csv', delimiter = ',', dtype = np.float32, skiprows = 1)

# x와 y로 나누기
x_train, y_train, x_test, y_test = xy_train[:, :9], np.transpose([xy_train[:, 9]]), xy_test[:, :9], np.transpose([xy_test[:, 9]])


X = tf.placeholder(tf.float32, shape = [None, 9])
Y = tf.placeholder(tf.float32, shape = [None, 1])

W = tf.Variable(tf.random_normal([9, 1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

hypothesis = tf.matmul(X, W) + b

cost = tf.reduce_mean(tf.square(hypothesis - Y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.000001)
train = optimizer.minimize(cost)

sess =tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(200000):
    sess.run(train, feed_dict = {X : x_train, Y : y_train})
    if step % 2000 == 0:
        print(step, sess.run([cost, W, b], feed_dict = {X : x_train, Y : y_train}))

costv, Wv, bv = sess.run([cost, W, b], feed_dict = {X : x_train, Y : y_train})

yte_pred = sess.run(hypothesis, feed_dict = {X : x_test})
residual = yte_pred - y_test
pred_cost = sess.run(tf.reduce_mean(tf.square(residual)))

print('예측값 :', np.transpose(yte_pred), '\n실제값 :', np.transpose(y_test), '\n오차값 :', \
      np.transpose(residual), '\n예측 비용 :', pred_cost)

y_pred = sess.run(hypothesis, feed_dict = {X : x_pred})

xy_pred = np.hstack((x_pred, y_pred))

header = open('boston_train.csv', 'r').readline().rstrip('\n')

np.savetxt('boston_ypredict.csv', xy_pred, delimiter = ',', header =  header)
