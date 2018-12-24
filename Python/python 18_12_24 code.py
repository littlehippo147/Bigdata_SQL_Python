# 18_12_21 review 

# tf.train.Saver()

import os
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import random
import matplotlib.pyplot as plt

tf.set_random_seed(777)

mnist = input_data.read_data_sets('Data/mnist/',one_hot=True)

learning_rate = 0.01
training_epoch = 11
batch_size = 100

CHECK_POINT_DIR = './saver/mnist2'

X = tf.placeholder(tf.float32,shape=[None,784]) # 28*28 픽셀
Y = tf.placeholder(tf.float32,shape=[None,10])

# (?,784) * (784,10 ) = (?,10)
W = tf.Variable(tf.random_normal([784,10]),name='weight')
b = tf.Variable(tf.random_normal([10]),name='bias')

logits = tf.matmul(X,W) + b
hypothesis = tf.nn.softmax(logits)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits( \
    logits=logits,labels=Y))

# optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate)
train = optimizer.minimize(cost)

# 이어서 학습하기 위한 old epoch 값
last_epoch = tf.Variable(0,name='last_epoch')

sess = tf.Session()
sess.run(tf.global_variables_initializer())

# Restore & Saver
saver = tf.train.Saver()

# Restore
checkpoint = tf.train.get_checkpoint_state(CHECK_POINT_DIR)
if checkpoint and checkpoint.model_checkpoint_path:
    try:
        saver.restore(sess,checkpoint.model_checkpoint_path)
        print("Successfully loaded:",checkpoint.model_checkpoint_path)
    except:
        print("Error on loading old network weights")
else:
    print("Could not find old network weights")

start_from = sess.run(last_epoch)

print("Starting learning from:",start_from)

# start training
for epoch in range(start_from,training_epoch): # 이어서 학습
    avg_cost = 0
    # 550 = 55000/100
    total_batch = int(mnist.train.num_examples/batch_size)
    for i in range(total_batch):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        cost_value,_ = sess.run([cost,train],feed_dict={X:batch_xs,Y:batch_ys})
        avg_cost += cost_value/total_batch
    print('Epoch:','%04d'%(epoch + 1) ,'cost:','{:9f}'.format(avg_cost))

    # Saver
    print("Saving network:")
    sess.run(last_epoch.assign(epoch + 1))
    if not os.path.exists(CHECK_POINT_DIR): # 저장 디렉토리가 없으면 새로 생성
        os.makedirs(CHECK_POINT_DIR)
    saver.save(sess, CHECK_POINT_DIR + "/model", global_step=epoch)

print('Learnig Finished!!')

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


######################
# hello_rnn
# hi hello --> ihello

import tensorflow as tf
import numpy as np

idx2char = ['h', 'i', 'e', 'l', 'o'] # (1,6)

x_data = [[0, 1, 0, 2, 3, 3]] # 'hihell' o는 입력이 아님 출력데이터
x_one_hot = [[[1, 0, 0, 0, 0],
              [0, 1, 0, 0, 0],
              [1, 0, 0, 0, 0],
              [0, 0, 1, 0, 0],
              [0, 0, 0, 1, 0],
              [0, 0, 0, 1, 0]]] # (1, 6, 5)


y_data = [[1, 0, 2, 3, 3, 4]] # 'ihello' 예측, (1,6)

num_classes = 5

input_dim = 5       # input data(x_data)의 one_hot size
hidden_size = 5     # output from the LSTM, one_hot size
batch_size = 1      # input data의 sentence 갯수
sequence_length = 6 # 'ihello' : 6

learning_rate = 0.1

# 입력변수 : X, Y
X = tf.placeholder(tf.float32, shape = [None, sequence_length, input_size])
Y = tf.placeholder(tf.float32, shape = [None, sequence_length])

# LSTM cell, RNN
cell = tf.contrib.rnn.BasicLSTMCell(num_units = hidden_size, state_is_tuple = True)
initial_state = cell.zero_state(batch_size, tf.float32)
outputs, _states = tf.nn.dynamic_rnn(cell, X, initial_state = initial_state, dtype = tf.float32) 


