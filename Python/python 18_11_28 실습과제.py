# python 18-11-28 iris data multinomial Classification 실습과제

import numpy as np
import tensorflow as tf
import os
from collections import Counter
from sklearn.preprocessing import LabelEncoder


os.getcwd()
os.chdir('C:\\Users\\user\\Documents\\python project')

tf.set_random_seed(777)

xy = np.loadtxt('iris.csv', delimiter = ',', dtype = np.str , skiprows = 1)

# train, test data 임의로 분리(y data 값이 index에 영향을 받기 때문) 
samp = np.random.sample(range(len(xy)), len(xy))

x_tr, x_te, y_tr, y_te = xy[samp[:100], 1:-1], xy[samp[100:], 1:-1], xy[samp[:100], -1], xy[samp[100:], -1]

# y 3가지 명목형 변수 숫자로 label encoding 후 one hot encoding
le = LabelEncoder()
le.fit(np.unique(y_tr))

y_tr = le.transform(y_tr)
y_te = le.transform(y_te)

nclass = 3

y_tr = tf.reshape(tf.one_hot(y_tr, 3), [-1, nclass])


X = tf.placeholder(tf.float32, shape = [None, 4])
Y = tf.placeholder(tf.float32, shape = [None, nclass])

W = tf.Variable(tf.random_normal([4, nclass]), name='weight')
b = tf.Variable(tf.random_normal([nclass]), name='bias')

## softmax hypothesis tf.nn.softmax
hypothesis = tf.nn.softmax(tf.matmul(X, W) + b)

# cost 함수
cost = tf.reduce_mean(tf.reduce_sum(-Y * tf.log(hypothesis), axis = 1))
optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.01)
train = optimizer.minimize(cost)


# session 생성
sess = tf.Session()
sess.run(tf.global_variables_initializer())

y_tr = sess.run(y_tr)
y_te = sess.run(y_te)

for step in range(70000):
    sess.run(train, feed_dict = {X : x_tr, Y : y_tr})
    if step % 1000 == 0:
        print(step, sess.run([cost, W, b], feed_dict = {X : x_tr, Y : y_tr}))
        

predict = sess.run(tf.argmax(hypothesis, 1), feed_dict = {X : x_te})

accuracy = tf.reduce_mean(tf.cast(tf.equal(predict, y_te), dtype=tf.float32))

print('predict :', predict, '\n', 'y Truevalue :', y_te, '\n', 'accuracy :', sess.run(accuracy))

