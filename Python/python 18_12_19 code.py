# cnn_basic.py

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data

tf.set_random_seed(777)

mnist = input_data.read_data_sets('Data/mnist/', one_hot = True)

learning_rate = 0.001
training_epoch = 15     # 1 epoch : tranning data를 한 번 다 학습한 것
batch_size = 100
keep_prob = tf.placeholder(tf.float32)

X = tf.placeholder(tf.float32, shape = [None, 784])
X_img = tf.reshape(X, [-1, 28, 28, 1]) # 1 28 28 1 image
Y = tf.placeholder(tf.float32, shape = [None, 10])

# Layer 1, X_img : (1, 28, 28, 1), Filter : (3, 3, 1, 32), stride : (1, 1), padding : 'SAME'
# out_img: (?, 14, 14, 32)
W1 = tf.Variable(tf.random_normal([3, 3, 1, 32]), name = 'weight1')
L1 = tf.nn.conv2d(X_img, W1, strides = [1, 1, 1, 1], padding = 'SAME')
# conv L1 : (?, 28, 28, 32)
# (N-F) / stride + 1 = (29-2) / 1 + 1 = 28

L1 = tf.nn.relu(L1)
L1 = tf.nn.max_pool(L1, ksize = [1, 2, 2, 1], strides = [1, 2, 2, 1], padding = 'SAME')
L1 = tf.nn.dropout(L1, keep_prob = keep_prob)
# Maxpool L1 : (?, 14, 14, 32)
# (N-F) / stride + 1 : (29-2) / 2 + 1 = 14

# Layer 2, X_img : (?, 14, 14, 32), Filter : (3, 3, 32, 64), stride : (1, 1), padding : 'SAME'
W2 = tf.Variable(tf.random_normal([3, 3, 32, 64]), name = 'weight2')
L2 = tf.nn.conv2d(L1, W2, strides = [1, 1, 1, 1], padding = 'SAME')
# conv L2 : (?, 14, 14, 64)
# (N-F) / stride + 1 = (15-2) / 1 + 1 = 14

L2 = tf.nn.relu(L2)
L2 = tf.nn.max_pool(L2, ksize = [1, 2, 2, 1], strides = [1, 2, 2, 1], padding = 'SAME')
L2 = tf.nn.dropout(L2, keep_prob = keep_prob)
# Maxpool L2 : (?, 7, 7, 64)
# (N-F) / stride + 1 : (15-2) / 2 + 1 = 7
#L2_flat = tf.reshape(L2, [-1, 7*7*64])


# Layer 3, X_img : (?, 7, 7, 64), Filter : (3, 3, 64, 128), stride : (1, 1), padding : 'SAME'
W3 = tf.Variable(tf.random_normal([3, 3, 64, 128]), name = 'weight3')
L3 = tf.nn.conv2d(L2, W3, strides = [1, 1, 1, 1], padding = 'SAME')
# conv L3 : (?, 7, , 64)
# (N-F) / stride + 1 = (15-2) / 1 + 1 = 14
L3 = tf.nn.relu(L3)
L3 = tf.nn.max_pool(L3, ksize = [1, 2, 2, 1], strides = [1, 2, 2, 1], padding = 'SAME')
L3 = tf.nn.dropout(L3, keep_prob = keep_prob)
# Maxpool L3 : (?, 14, 14, 32)
# (N-F) / stride + 1 : (29-2) / 2 + 1 = 14
L3_flat = tf.reshape(L3, [-1,4*4*128])

# FC(Fully Connected) Layer
# Layer 4
W4 = tf.get_variable("W4", shape = [4 * 4 * 128, 625], initializer = tf.contrib.layers.xavier_initializer())
b4 = tf.Variable(tf.random_normal([625]), name = 'bias4')
L4 = tf.nn.relu(tf.matmul(L3_flat, W4) + b4)
L4 = tf.nn.dropout(L4, keep_prob = keep_prob)

# Output Layer 
W5 = tf.get_variable("W5", shape = [625, 10], initializer = tf.contrib.layers.xavier_initializer())
b5 = tf.Variable(tf.random_normal([10]), name = 'bias5')
model = tf.matmul(L4, W5) + b5
hypothesis = tf.nn.softmax(model)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels = Y, logits = model))
optimizer = tf.train.AdamOptimizer(learning_rate = 0.01)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for epoch in range(training_epoch):
    
    # 550 = 55000/100
    total_batch = int(mnist.train.num_examples / batch_size)
    avg_cost = 0
    for i in range(total_batch):
        # mini batch : 최초 55000개의 데이터에서 100개를 무작위 비복원 추출 반복
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        cost_val, _ = sess.run([cost, train], feed_dict = {X : batch_xs, Y : batch_ys, keep_prob : 0.7})
        avg_cost += cost_val / total_batch

    print('Epoch :', '%04d'%(epoch + 1), 'cost :', '{:9f}'.format(avg_cost))
    
# test 전체 예측    
predict = tf.argmax(hypothesis, 1)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predict, tf.argmax(Y, 1)), dtype = tf.float32))

a = sess.run(accuracy, feed_dict = {X : mnist.test.images, Y : mnist.test.labels, keep_prob : 0.7})
print('accuracy :', a)

# 랜덤 1개 값 예측
r = random.randint(0, mnist.test.num_examples - 1)
print('random :', r, 'Label :', sess.run(tf.argmax(mnist.test.labels[r:r+1],1)))
print('Prediction :', sess.run(predict, feed_dict = {X : mnist.test.images[r:r+1], keep_prob : 1}))

# matplotlib : imshow()
plt.imshow(mnist.test.images[r:r+1].reshape(28, 28), cmap = 'Greys', interpolation = 'nearest') # 흑백 2차원 보간법
plt.show()



