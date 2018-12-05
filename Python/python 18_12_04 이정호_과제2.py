# 이정호_과제2 / Spider 개발환경

import numpy as np
import tensorflow as tf
import os
from sklearn.model_selection import train_test_split as tts
from sklearn.preprocessing import LabelEncoder

os.getcwd()
os.chdir('C:\\Users\\user\\Documents\\python project')

tf.set_random_seed(777)

#######################
learning_rate = 0.01
training_epoch = 30
batch_size = 20
#######################

# 데이터 불러오기
xy = np.array(np.loadtxt('balance-scale.csv', delimiter = ',', dtype = np.str))

# train, test 7:3으로 분리
x_train, x_test, y_train, y_test = tts(xy[:, 1:], xy[:, 0], test_size = 0.3)

# Label Encoding, One-hot Encoding 통해 Y 값 처리
le = LabelEncoder()
le.fit(np.unique(y_train))

# Label : 'B' = 0, 'L' = 1, 'R' = 2
y_train = le.transform(y_train)
y_test = le.transform(y_test)

nclass = 3

y_train = tf.reshape(tf.one_hot(y_train, 3), [-1, nclass])


# X, Y placeholder 생성
X = tf.placeholder(tf.float32, shape = [None, 4])
Y = tf.placeholder(tf.float32, shape = [None, nclass])

# Layer 및 가중치 초깃값 생성
## Layer1
W1 = tf.get_variable("W1",shape=[4, 10], initializer = tf.contrib.layers.xavier_initializer())
b1 = tf.Variable(tf.random_normal([10]),name='b1')
L1 = tf.nn.relu(tf.matmul(X,W1) + b1)

## Layer2
W2 = tf.get_variable("W2", shape=[10, 10], initializer=tf.contrib.layers.xavier_initializer())
b2 = tf.Variable(tf.random_normal([10]),name='b2')
L2 = tf.nn.relu(tf.matmul(L1,W2) + b2)

## Layer3
W3 = tf.get_variable("W3", shape=[10, 10], initializer=tf.contrib.layers.xavier_initializer())
b3 = tf.Variable(tf.random_normal([10]),name='b3')
L3 = tf.nn.relu(tf.matmul(L2,W3) + b3)

## Layer4
W4 = tf.get_variable("W4", shape=[10, 10], initializer=tf.contrib.layers.xavier_initializer())
b4 = tf.Variable(tf.random_normal([10]),name='b4')
L4 = tf.nn.relu(tf.matmul(L3,W4) + b4)

## Output Layer
W5 = tf.get_variable("W5", shape=[10, nclass], initializer=tf.contrib.layers.xavier_initializer())
b5 = tf.Variable(tf.random_normal([nclass]),name='b5')

model = tf.matmul(L4,W5) + b5
hypothesis = tf.nn.softmax(model)

# Cost function
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=Y, logits=model))

# Adam optimizer
optimizer = tf.train.AdamOptimizer(learning_rate = learning_rate)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

# one-hot encoding 된 y값 체크
y_train = sess.run(y_train)

# 학습 시작
for step in range(20000):
    sess.run(train, feed_dict = {X : x_train, Y : y_train})
    if step % 1000 == 0:
        print(step, sess.run(cost, feed_dict = {X : x_train, Y : y_train}))
        
        
predict = sess.run(tf.argmax(hypothesis, 1), feed_dict = {X : x_test})

accuracy = tf.reduce_mean(tf.cast(tf.equal(predict, y_test), dtype=tf.float32))

print('predict :', predict, '\n', 'y Truevalue :', y_test, '\n', 'accuracy :', sess.run(accuracy))        

