# python 18-11-27 softmax multinomial Classification 실습과제

import numpy as np
import tensorflow as tf
import os

os.getcwd()
os.chdir('C:\\Users\\user\\Documents\\python project')

tf.set_random_seed(777)

# X 변수 16개, y 변수 1개, 121개 데이터
xy = np.loadtxt('data-04-zoo.csv', delimiter = ',', dtype = np.float32, skiprows = 19)

x_tr, x_te, y_oh, y_true = xy[:71, :-1], xy[71:, :-1], xy[:71, -1], xy[71:, -1]

# y를 one hot 형태로 바꿔주기 session 실행
y_oh = tf.reshape(tf.one_hot(y_oh, 7), [-1, 7])
sess = tf.Session()
y = sess.run(y_oh)


X = tf.placeholder(tf.float32, shape = [None, 16])
Y = tf.placeholder(tf.float32, shape = [None, 7])

W = tf.Variable(tf.random_normal([16, 7]), name='weight')
b = tf.Variable(tf.random_normal([7]), name='bias')

## softmax hypothesis tf.nn.softmax
hypothesis = tf.nn.softmax(tf.matmul(X, W) + b)

# cost 함수
cost = tf.reduce_mean(tf.reduce_sum(-Y * tf.log(hypothesis), axis = 1))
optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.01)
train = optimizer.minimize(cost)


# session 생성
sess.run(tf.global_variables_initializer())

for step in range(150000):
    sess.run(train, feed_dict = {X : x_tr, Y : y_tr})
    if step % 1000 == 0:
        print(step, sess.run([cost, W, b], feed_dict = {X : x_tr, Y : y}))
        

predict = sess.run(tf.argmax(hypothesis, 1), feed_dict = {X : x_te})

accuracy = tf.reduce_mean(tf.cast(tf.equal(predict, y_true), dtype=tf.float32))

print('predict :', predict, '\n', 'y_True :', y_true, '\n', 'accuracy :', sess.run(accuracy))


