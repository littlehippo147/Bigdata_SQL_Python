# python 18-11-26 Logistic Classification

import tensorflow as tf
import matplotlib.pyplot as plt
import math

def sigmoid(x):
    return 1 / (1 + math.e**-x)

print(sigmoid(-10))
print(sigmoid(0))
print(sigmoid(10))

xx, yy = [], []
for i in range(-50,51):
    xx.append(i)
    yy.append(sigmoid(i/5))

plt.plot(xx, yy, 'ro')
plt.show()

# logistic regression
x_data = [[1,2],    # 6 by 2
          [2,3],
          [3,1],
          [4,3],
          [5,3],
          [6,2]]

y_data = [[0],      # 6 by 1
          [0],
          [0],
          [1],
          [1],
          [1]]

X = tf.placeholder(tf.float32, shape = [None, 2])
Y = tf.placeholder(tf.float32, shape = [None, 1])

W = tf.Variable(tf.random_normal([2, 1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

## sigmoid 사용: tf.div(1, 1 + tf.exp(tf.matmul(-X, W)))
hypothesis = tf.sigmoid(tf.matmul(X, W) + b)

## logistic에서 쓰는 cost 함수
cost = tf.reduce_mean(-Y * tf.log(hypothesis) - (1-Y) * tf.log(1-hypothesis))
optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.1)
train = optimizer.minimize(cost)

sess =tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(100000):
    sess.run(train, feed_dict = {X : x_data, Y : y_data})
    if step % 1000 == 0:
        print(step, sess.run([cost, W, b], feed_dict = {X : x_data, Y : y_data}))
        
## Accuracy computation
predict = tf.cast(hypothesis > 0.5, dtype=tf.float32)   # tf.cast 
accuracy = tf.reduce_mean(tf.cast(tf.equal(predict, Y), dtype=tf.float32))

## Accuracy Report
h, p, a = sess.run([hypothesis, predict, accuracy], feed_dict = {X : x_data, Y : y_data})

print('hypothesis :\n', h, '\n', 'predict :\n', p, '\n', 'accuracy :', a)
