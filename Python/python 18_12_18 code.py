# python 18_12_18 MNIST softmax 
# mnist review
# mnist : 28 x 28 = 784 pixcell
# train image : 55000
# test image : 10000
# accuracy :

import tensorflow as tf
import numpy
from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt
import random 

tf.set_random_seed(777)

mnist = input_data.read_data_sets('Data/mnist/', one_hot = True)

learning_rate = 0.01
training_epoch = 15     # 1 epoch : tranning data를 한 번 다 학습한 것
batch_size = 100        # batch_size : 

X = tf.placeholder(tf.float32,shape=[None,784])
Y = tf.placeholder(tf.float32,shape=[None,10])

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
        cost_val, _ = sess.run([cost, train], feed_dict = {X : batch_xs, Y : batch_ys})
        avg_cost += cost_val / total_batch

    print('Epoch :', '%04d'%(epoch + 1), 'cost :', '{:9f}'.format(avg_cost))
    
# test 전체 예측    
predict = tf.argmax(hypothesis, 1)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predict, tf.argmax(Y, 1)), dtype = tf.float32))

a = sess.run(accuracy, feed_dict = {X : mnist.test.images, Y : mnist.test.labels})
print('accuracy :', a)

# 랜덤 1개 값 예측
r = random.randint(0, mnist.test.num_examples - 1)
print('random :', r, 'Label :', sess.run(tf.argmax(mnist.test.labels[r:r+1],1)))
print('Prediction :', sess.run(predict, feed_dict = {X : mnist.test.images[r:r+1]}))

# matplotlib : imshow()
plt.imshow(mnist.test.images[r:r+1].reshape(28, 28), cmap = 'Greys', interpolation = 'nearest') # 흑백 2차원 보간법
plt.show()


################################################
# python 18_12_18 cnn_basic
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

sess = tf.InteractiveSession()


image = np.array([[[[1],[2],[3]],
                   [[4],[5],[6]],
                   [[7],[8],[9]]]], dtype = np.float32)
print(image.shape) # (1, 3, 3, 1)
plt.imshow(image.reshape(3,3), cmap = 'Greys')
plt.show()
"""""""""""""""""""""""""""""""""""""""""""""""""""""""
# conv2d
# image: (1,3,3,1) , Filter : (2,2,1,1). stride : (1,1)
# number of images : 1, 3 * 3 image, color :1
# Padding : VALID
print("image:\n",image)
print(image.shape) # (1, 3, 3, 1)

weight = tf.constant([[[[1.]],[[1.]]],
                      [[[1.]],[[1.]]]])
print("weight.shape:",weight.shape)    # weigth.shape : (2,2,1,1)
# 2 * 2 image, color :1, filters : 1

conv2d = tf.nn.conv2d(image,weight,strides=[1,1,1,1], padding='VALID')
conv2d_img = conv2d.eval()
print('conv2d_img.shape:',conv2d_img.shape) # (1, 2, 2, 1)

# 시각화
conv2d_img = np.swapaxes(conv2d_img,0,3)
for i, one_image in enumerate(conv2d_img) :
    print(one_image.reshape(2,2))
    plt.subplot(1,2,i+1)
    plt.imshow(one_image.reshape(2,2), cmap='Greys')
plt.show()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# conv2d
# image: (1,3,3,1) , Filter : (2,2,1,1). stride : (1,1)
# number of images : 1, 3 * 3 image, color :1
# Padding : SAME
print("image:\n",image)
print(image.shape) # (1, 3, 3, 1)

weight = tf.constant([[[[1.]],[[1.]]],
                      [[[1.]],[[1.]]]])
print("weight.shape:",weight.shape)
# weigth.shape : (2,2,1,1)
# 2 * 2 image, color :1, filters : 1

conv2d = tf.nn.conv2d(image,weight,strides=[1,1,1,1], padding='SAME')
conv2d_img = conv2d.eval()
print('conv2d_img.shape:',conv2d_img.shape) # (1, 3, 3, 1)

# 시각화
conv2d_img = np.swapaxes(conv2d_img,0,3)
for i, one_image in enumerate(conv2d_img) :
    print(one_image.reshape(3,3))
    plt.subplot(1,2,i+1)
    plt.imshow(one_image.reshape(3,3), cmap='Greys')
plt.show()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# conv2d  3 filters : (2,2,1,3)
# image: (1,3,3,1)   ==>  ouput : (1,3,3,3)
weight = tf.constant([[[[1.,10.,-1.]],[[1.,10.,-1.]]],
                      [[[1.,10.,-1.]],[[1.,10.,-1.]]]])
print("weight.shape:",weight.shape)
# weigth.shape : (2,2,1,3)
# 2 * 2 image, color :1, filters : 3

conv2d = tf.nn.conv2d(image,weight,strides=[1,1,1,1], padding='SAME')
conv2d_img = conv2d.eval()
print('conv2d_img.shape:',conv2d_img.shape) # (1, 3, 3, 3)

# 시각화
conv2d_img = np.swapaxes(conv2d_img,0,3)
for i, one_image in enumerate(conv2d_img) :
    print(one_image.reshape(3,3))
    plt.subplot(1,3,i+1)
    plt.imshow(one_image.reshape(3,3), cmap='Greys')
plt.show()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# max pooling (1, 2, 2, 1) --> (1, 1, 1, 1)
# padding : VALID
image = np.array([[[[4],[3]],
                   [[2],[1]]]], dtype=np.float32)
print(image.shape) # (1, 2, 2, 1)

pool = tf.nn.max_pool(image,ksize=[1,2,2,1],
                      strides=[1,1,1,1],padding='VALID')
print(pool.shape) # (1, 1, 1, 1)
print(pool.eval()) # [[[[4.]]]]

""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# max pooling  (1, 2, 2, 1) --> (1, 2, 2, 1)
# padding : SAME
image = np.array([[[[4],[3]],
                   [[2],[1]]]], dtype=np.float32)
print(image.shape) # (1, 2, 2, 1)

pool = tf.nn.max_pool(image,ksize=[1,2,2,1],
                      strides=[1,1,1,1],padding='SAME')
print(pool.shape) # (1, 2, 2, 1)
print(pool.eval())
# [[[[4.]
#    [3.]]
#   [[2.]
#    [1.]]]]

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""

# MNIST image loading
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
# Check out https://www.tensorflow.org/get_started/mnist/beginners for
# more information about the mnist dataset

img = mnist.train.images[0].reshape(28,28)
plt.imshow(img, cmap='Greys')
plt.show()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# MNIST Convolution layer
sess = tf.InteractiveSession()

img = img.reshape(-1,28,28,1)
print("img.shape", img.shape)  # img.shape (1, 28, 28, 1)

W1 = tf.Variable(tf.random_normal([3, 3, 1, 5], stddev=0.01)) # 3*3,  color:1 ,filters:5

# Output size : (N-F)/stride + 1
#     (29 - 3)/2 + 1 = 13 + 1 = 14  ,  ==> (1, 14, 14, 5)
conv2d = tf.nn.conv2d(img, W1, strides=[1, 2, 2, 1], padding='SAME')

print(conv2d) # (1, 14, 14, 5)
sess.run(tf.global_variables_initializer())
conv2d_img = conv2d.eval()
conv2d_img = np.swapaxes(conv2d_img, 0, 3)
for i, one_img in enumerate(conv2d_img):
    plt.subplot(1,5,i+1), plt.imshow(one_img.reshape(14,14), cmap='Greys')

plt.show()


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# MNIST Max pooling
# conv2d : (1, 14, 14, 5)
# Output size : (N-F)/stride + 1
#     (14 - 2)/2 + 1 = 6 + 1 = 7 ,  ==> (1, 7, 7, 5)
pool = tf.nn.max_pool(conv2d, ksize=[1, 2, 2, 1], strides=[
                        1, 2, 2, 1], padding='SAME')
print(pool) # shape=(1, 7, 7, 5)

sess.run(tf.global_variables_initializer())
pool_img = pool.eval()

pool_img = np.swapaxes(pool_img, 0, 3)
for i, one_img in enumerate(pool_img):
    plt.subplot(1,5,i+1), plt.imshow(one_img.reshape(7, 7), cmap='Greys')

plt.show()
