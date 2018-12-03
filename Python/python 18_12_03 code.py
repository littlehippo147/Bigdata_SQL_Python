# python 18_12_03 mnist_softmax

import tensorflow as tf
import numpy
from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt
import random 

tf.set_random_seed(777)

mnist = input_data.read_data_sets('Data/mnist/', one_hot = True)

learning_rate = 0.01
training_epoch = 15
batch_size = 100

X = tf.placeholder(tf.float32, [None, 784]) # 28 X 28 픽셀
Y = tf.placeholder(tf.float32, [None, 10])

W1 = tf.Variable(tf.random_normal([784, 10]), name='weight1')
b1 = tf.Variable(tf.random_normal([10]), name='bias1')
model = tf.matmul(X, W1) + b1
hypothesis = tf.nn.softmax(tf.matmul(X, W1) + b1)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels = Y, logits = model))
optimizer = tf.train.AdamOptimizer(learning_rate = 0.01)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

# start traning
for epoch in range(training_epoch):
    
    # 550 = 55000/100
    total_batch = int(mnist.train.num_examples / batch_size)
    avg_cost = 0
    for i in range(total_batch):
        # mini batch : 최초 55000개의 데이터에서 100개를 무작위 비복원 추출 반복
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        cost_val, _ = sess.run([cost, train], feed_dict = {X : batch_xs, Y : batch_ys})
        avg_cost += cost_val / total_batch

    print('Epoch :', '%04d'%(epoch + 1), 'cost :', '{:9f}'.format(avg_cost))


# accuracy computation

predict = tf.argmax(hypothesis, 1)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predict, tf.argmax(Y, 1)), dtype = tf.float32))

a = sess.run(accuracy, feed_dict = {X : mnist.test.images, Y : mnist.test.labels})

print('accuracy :', a)

################
## Layer 늘려보기
###############

W1 = tf.Variable(tf.random_normal([784, 256]), name='weight1')
b1 = tf.Variable(tf.random_normal([256]), name='bias1')

L1 = tf.sigmoid(tf.matmul(X, W1) + b1)

W2 = tf.Variable(tf.random_normal([256, 256]), name='weight2')
b2 = tf.Variable(tf.random_normal([256]), name='bias2')

L2 = tf.sigmoid(tf.matmul(L1, W2) + b2)

W3 = tf.Variable(tf.random_normal([256, 10]), name='weight3')
b3 = tf.Variable(tf.random_normal([10]), name='bias3')
model = tf.matmul(L2, W3) + b3
hypothesis = tf.nn.softmax(tf.matmul(L2, W3) + b3)


cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels = Y, logits = model))
optimizer = tf.train.AdamOptimizer(learning_rate = 0.01)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

# start traning
for epoch in range(training_epoch):
    
    # 550 = 55000/100
    total_batch = int(mnist.train.num_examples / batch_size)
    avg_cost = 0
    for i in range(total_batch):
        # mini batch : 최초 55000개의 데이터에서 100개를 무작위 비복원 추출 반복
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        cost_val, _ = sess.run([cost, train], feed_dict = {X : batch_xs, Y : batch_ys})
        avg_cost += cost_val / total_batch

    print('Epoch :', '%04d'%(epoch + 1), 'cost :', '{:9f}'.format(avg_cost))


# accuracy computation

predict = tf.argmax(hypothesis, 1)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predict, tf.argmax(Y, 1)), dtype = tf.float32))

a = sess.run(accuracy, feed_dict = {X : mnist.test.images, Y : mnist.test.labels})

print('train images total number:',mnist.train.num_examples)
print('test images total number:',mnist.test.num_examples)
print('accuracy :', a) # 정확도 0.9646


# predict
r = random.randint(0,mnist.test.num_examples - 1) # 0-9999 ramdom int number
print('random:',r,'Label:',sess.run(tf.argmax(mnist.test.labels[r:r+1],1)))

print('Prediction:',sess.run(predict,feed_dict={X:mnist.test.images[r:r+1]}))

# matplotlib : imshow()
plt.imshow(mnist.test.images[r:r+1].reshape(28,28),\
           cmap='Greys',interpolation='nearest') # 흑백, 2차원 보간법
plt.show()


## sigmoid 대신 relu 쓰기
W1 = tf.Variable(tf.random_normal([784, 256]), name='weight1')
b1 = tf.Variable(tf.random_normal([256]), name='bias1')

L1 = tf.nn.relu(tf.matmul(X, W1) + b1)

W2 = tf.Variable(tf.random_normal([256, 256]), name='weight2')
b2 = tf.Variable(tf.random_normal([256]), name='bias2')

L2 = tf.nn.relu(tf.matmul(L1, W2) + b2)

W3 = tf.Variable(tf.random_normal([256, 10]), name='weight3')
b3 = tf.Variable(tf.random_normal([10]), name='bias3')
model = tf.matmul(L2, W3) + b3
hypothesis = tf.nn.softmax(tf.matmul(L2, W3) + b3)


cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels = Y, logits = model))
optimizer = tf.train.AdamOptimizer(learning_rate = 0.01)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

# start traning
for epoch in range(training_epoch):
    
    # 550 = 55000/100
    total_batch = int(mnist.train.num_examples / batch_size)
    avg_cost = 0
    for i in range(total_batch):
        # mini batch : 최초 55000개의 데이터에서 100개를 무작위 비복원 추출 반복
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        cost_val, _ = sess.run([cost, train], feed_dict = {X : batch_xs, Y : batch_ys})
        avg_cost += cost_val / total_batch

    print('Epoch :', '%04d'%(epoch + 1), 'cost :', '{:9f}'.format(avg_cost))


# accuracy computation

predict = tf.argmax(hypothesis, 1)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predict, tf.argmax(Y, 1)), dtype = tf.float32))

a = sess.run(accuracy, feed_dict = {X : mnist.test.images, Y : mnist.test.labels})

print('train images total number:',mnist.train.num_examples)
print('test images total number:',mnist.test.num_examples)
print('accuracy :', a) # 정확도 0.9623


# predict
r = random.randint(0,mnist.test.num_examples - 1) # 0-9999 ramdom int number
print('random:',r,'Label:',sess.run(tf.argmax(mnist.test.labels[r:r+1],1)))

print('Prediction:',sess.run(predict,feed_dict={X:mnist.test.images[r:r+1]}))

# matplotlib : imshow()
plt.imshow(mnist.test.images[r:r+1].reshape(28,28),\
           cmap='Greys',interpolation='nearest') # 흑백, 2차원 보간법
plt.show()

#########################################################
# deep_learning, Xavier Initialize 사용 / 좋은 초깃값 설정
########################################################
learning_rate = 0.001
training_epoch = 15
batch_size = 100

X = tf.placeholder(tf.float32,shape=[None,784]) # 28*28 픽셀
Y = tf.placeholder(tf.float32,shape=[None,10])

## Drop out
#keep_prob = tf.placeholder(tf.float32)


# (?,784) * (784,512) = (?,512)
# W1 = tf.Variable(tf.random_normal([784,512]),name='weight1')
W1 = tf.get_variable("W1",shape=[784,512], initializer = tf.contrib.layers.xavier_initializer())
b1 = tf.Variable(tf.random_normal([512]),name='bias1')
# L1 = tf.sigmoid(tf.matmul(X,W1) + b1) # (?,512)
L1 = tf.nn.relu(tf.matmul(X,W1) + b1)
# L1 = tf.nn.dropout(L1,keep_prob=keep_prob)


# (?,512) * (512,512) = (?,512)
# W2 = tf.Variable(tf.random_normal([512,512]),name='weight2')
W2 = tf.get_variable("W2", shape=[512, 512], initializer=tf.contrib.layers.xavier_initializer())
b2 = tf.Variable(tf.random_normal([512]),name='bias2')
# L2 = tf.sigmoid(tf.matmul(L1,W2) + b2) # (?,512)
L2 = tf.nn.relu(tf.matmul(L1,W2) + b2)
# L2 = tf.nn.dropout(L2,keep_prob=keep_prob)

# (?,512) * (512,512) = (?,512)
# W3 = tf.Variable(tf.random_normal([512,512]),name='weight3')
W3 = tf.get_variable("W3", shape=[512, 512], initializer=tf.contrib.layers.xavier_initializer())
b3 = tf.Variable(tf.random_normal([512]),name='bias3')
L3 = tf.nn.relu(tf.matmul(L2,W3) + b3)
# L3 = tf.nn.dropout(L3,keep_prob=keep_prob)

# (?,512) * (512,512) = (?,512)
# W4 = tf.Variable(tf.random_normal([512,512]),name='weight4')
W4 = tf.get_variable("W4", shape=[512, 512], initializer=tf.contrib.layers.xavier_initializer())
b4 = tf.Variable(tf.random_normal([512]),name='bias4')
L4 = tf.nn.relu(tf.matmul(L3,W4) + b4)
# L4 = tf.nn.dropout(L4,keep_prob=keep_prob)

# (?,512) * (512,10) = (?,10)
# W3 = tf.Variable(tf.random_normal([512,512]),name='weight3')
W5 = tf.get_variable("W5", shape=[512,10], initializer=tf.contrib.layers.xavier_initializer())
b5 = tf.Variable(tf.random_normal([10]),name='bias5')

model = tf.matmul(L4,W5) + b5
hypothesis = tf.nn.softmax(model)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=Y, logits=model))

optimizer = tf.train.AdamOptimizer(learning_rate = learning_rate)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

# start training
for epoch in range(training_epoch): 
    avg_cost = 0

    total_batch = int(mnist.train.num_examples/batch_size)
    for i in range(total_batch):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        cost_value,_ = sess.run([cost,train],feed_dict={X:batch_xs,Y:batch_ys})
        avg_cost += cost_value/total_batch

    print('Epoch:','%04d'%(epoch + 1) ,'cost:','{:9f}'.format(avg_cost))


# accuracy computation
predict = tf.argmax(hypothesis,1)
correct_predict = tf.equal(predict,tf.argmax(Y,1))
accuracy = tf.reduce_mean(tf.cast(correct_predict,dtype=tf.float32))

a = sess.run(accuracy,feed_dict={X:mnist.test.images,Y:mnist.test.labels})
print('train images total number:',mnist.train.num_examples)
print('test images total number:',mnist.test.num_examples)
print('\nAccuracy:',a)

# predict
r = random.randint(0,mnist.test.num_examples - 1) # 0-9999 ramdom int number
print('random:',r,'Label:',sess.run(tf.argmax(mnist.test.labels[r:r+1],1)))

print('Prediction:',sess.run(predict,feed_dict={X:mnist.test.images[r:r+1]}))

# matplotlib : imshow()
plt.imshow(mnist.test.images[r:r+1].reshape(28,28),\
           cmap='Greys',interpolation='nearest') # 흑백, 2차원 보간법
plt.show()


