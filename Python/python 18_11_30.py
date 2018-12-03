# python 18_11_30 nn_ReLU_softmax

import tensorflow as tf
import numpy as np

tf.set_random_seed(777)

x_data = np.array([[0,0],
          [1,0],
          [1,1],
          [0,0],
          [0,0],
          [0,1]])

y_data = np.array([[1,0,0],
          [0,1,0],
          [0,0,1],
          [1,0,0],
          [1,0,0],
          [0,0,1]])

X = tf.placeholder(tf.float32, [None, 2])
Y = tf.placeholder(tf.float32, [None, 3])

W1 = tf.Variable(tf.random_uniform([2,10]), name='weight1')
b1 = tf.Variable(tf.random_normal([10]), name='bias1')

L1 = tf.nn.relu(tf.add(tf.matmul(X, W1), b1))

W2 = tf.Variable(tf.random_uniform([10,3]), name='weight2')
b2 = tf.Variable(tf.random_normal([3]), name='bias2')

model = tf.add(tf.matmul(L1, W2), b2)
hypothesis = tf.nn.relu(model)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels = Y, logits = model))
optimizer = tf.train.AdamOptimizer(learning_rate = 0.01)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(2001):
    cost_val, W1_val, b1_val, W2_val, b2_val, _ = sess.run([cost, W1, b1, W2, b2, train], \
                                                            feed_dict={X:x_data, Y:y_data})
    if step % 200 == 0:
        print(step, cost_val, W1_val, b1_val, W2_val, b2_val)



predict = sess.run(tf.argmax(hypothesis, 1), feed_dict = {X : x_data})

accuracy = sess.run(tf.reduce_mean(tf.cast(tf.equal(predict, tf.argmax(y_data, 1)), dtype=tf.float32)))

print('predict :', predict, '\n', 'accuracy :', accuracy)


