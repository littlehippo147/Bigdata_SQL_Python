# python 18_11_20.py

# Linear Regression
## using tensorflow : 텐서플로
import tensorflow as tf

## 난수 seed number 설정
tf.set_random_seed(777)

# train data : X and Y data
x_train = [1,2,3]   # 원인, 입력값
y_train = [1,2,3]   # 결과, 우리가 원하는 답, 출력값
# y_train = [4,7,10]

# hypothesis : H(X) = WX + B
## tf.random_normal([1]) : 난수 생성
## tf.random_normal([2, 1, 3]) : [ ] 차원
W = tf.Variable(tf.random_normal([1]),name='weight')    
b = tf.Variable(tf.random_normal([1]),name='bias')


hypothesis = x_train*W + b # 가설

# cost function & gradient descent : W와 b를 찾아내는 것이 목적
## cost function : 비용함수
### tf.square() : 제곱, tf.reduce_mean() : 합의 평균
cost =  tf.reduce_mean(tf.square(hypothesis - y_train)) 

## gradient descent
### 학습률 0.01로 gradient descent optimizer 객체 생성
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)

###  optimizer.minimize() : 해당 값을 최소화 하는 방향으로 W, b 값을 찾는 method
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer()) # session내 기존 변수 초기화

# trainnig
for step in range(10001):
    sess.run(train)     # optimizer.minimize를 실행해 cost가 최소가 되는 방향으로 진행
    if step % 20 == 0 : # 학습과정을 모니터링하기 위해 구현
        print(step,sess.run(cost),sess.run(W),sess.run(b))

# predict : 예측, x=5, x=11
predict = 5*W + b
print('x=5, H(x):',sess.run(predict))
predict = 11*W + b
print('x=11, H(x):',sess.run(predict))


## 데이터 추가시 정확도 향상 기대
x_train2 = [1,2,3,4]
y_train2 = [1,2,3,4]

W2 = tf.Variable(tf.random_normal([1]),name='weight')
b2 = tf.Variable(tf.random_normal([1]),name='bias')

hypothesis2 = x_train2 * W2 + b2

cost2 =  tf.reduce_mean(tf.square(hypothesis2 - y_train2))

optimizer2 = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train2 = optimizer.minimize(cost2)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(10001):
    sess.run(train2)
    if step % 20 == 0 :
        print(step,sess.run(cost2),sess.run(W2),sess.run(b2))

predict = 5 * W2 + b2
print('x=5, H(x):',sess.run(predict))
predict = 11 * W2 + b2
print('x=11, H(x):',sess.run(predict))


# Linear Regression placeholder
## 학습 데이터를 place holder로 지정
X = tf.placeholder(tf.float32, shape = [None]) 
y = tf.placeholder(tf.float32, shape = [None])

W3 = tf.Variable(tf.random_normal([1]),name='weight')    
b3 = tf.Variable(tf.random_normal([1]),name='bias')

hypothesis3 = X * W3 + b3

cost3 =  tf.reduce_mean(tf.square(hypothesis3 - y))

optimizer3 = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train3 = optimizer.minimize(cost3)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(10001):
    sess.run(train3, feed_dict= {X:[1, 3, 4, 5, 7], y:[3, 7, 9, 11, 15]})
    if step % 100 == 0 :
        print(step,sess.run(cost3, feed_dict= {X:[1, 3, 4, 5, 7], y:[3, 7, 9, 11, 15]}),sess.run(W3),sess.run(b3))

predict = 5 * W3 + b3
print('x=5, H(x):',sess.run(predict))
predict = 11 * W3 + b3
print('x=11, H(x):',sess.run(predict))
print('x=[2, 6, 8], H(x):',sess.run(hypothesis3, feed_dict = {X:[2, 6, 8]}))


# placeholder lab
# 문제 1 : 다음 공식을 placeholder 버전으로 구현해보세요/
## H(x) = 3 * x + 5
## sess.run(op, feed_dict = {x:[2,7]})
## a + b : tf.add(a, b)
## a - b : tf.sub(a, b)
## a * b : tf.multiply(a, b)
## a / b : tf.divide(a, b)

x = tf.placeholder(tf.float32) 
op = tf.add(tf.multiply(x, 3), 5)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
print(sess.run(op, feed_dict = {x:[2, 7]}))


# 문제 2 : placeholder를 사용하여 구구단을 출력하는 프로그램을 구현해보세요.
## left, right 두개의 변수를 구현.
## 근데 이거 왜 꼭 이걸로 해야됨?

left = tf.placeholder(tf.int32)
right = tf.placeholder(tf.int32)

res = tf.multiply(left, right)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for j in range(2, 10):
    print('--', j, '단 --')
    for i in range(1,10):
        print(j, '*', i, '=', sess.run(res, feed_dict = {left : j, right : i}))
    

# 데이터를 파일로 부터 읽어들이기
import numpy as np
import matplotlib.pyplot as plt

# unpack = True는 array로 묶인 데이터를 리스트로 풀어줌
data = np.loadtxt('cars.csv', unpack = True, delimiter = ',', skiprows = 1)
data2 = np.loadtxt('cars.csv', unpack = False, delimiter = ',', skiprows = 1)
print(data)
print(data2)

x = data[0]
y = data[1]

W4 = tf.Variable(tf.random_normal([1]), name='weight')
b4 = tf.Variable(tf.random_normal([1]), name='bias')

hypothesis4 = x * W4 + b4

cost4 =  tf.reduce_mean(tf.square(hypothesis4 - y))

optimizer4 = tf.train.GradientDescentOptimizer(learning_rate=0.001)
train4 = optimizer4.minimize(cost4)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(40001):
    sess.run(train4)
    if step % 100 == 0 :
        print(step,sess.run(cost4),sess.run(W4),sess.run(b4))


## placeholder
x = data[0]
y = data[1]

X = tf.placeholder(tf.float32, shape = [None])
Y = tf.placeholder(tf.float32, shape = [None])

W5 = tf.Variable(tf.random_normal([1]), name='weight')
b5 = tf.Variable(tf.random_normal([1]), name='bias')

hypothesis5 = X * W5 + b5

cost5 =  tf.reduce_mean(tf.square(hypothesis5 - Y))

optimizer5 = tf.train.GradientDescentOptimizer(learning_rate=0.001)
train5 = optimizer4.minimize(cost5)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(40001):
    sess.run(train5, feed_dict = {X:x, Y:y})
    if step % 100 == 0 :
        print(step,sess.run(cost5, feed_dict = {X:x, Y:y}),sess.run(W5),sess.run(b5))

## 결과 값 저장
w_val = sess.run(W5)
b_val = sess.run(b5)
        
## predict 
print(sess.run(hypothesis5, feed_dict = {X:[30, 50]}))
print(sess.run(hypothesis5, feed_dict = {X:[14, 16, 17, 20]}))

# 시각화 :matplotlib 사용
def prediction(x, W, b):
    return W*x + b


plt.plot(x, y, 'ro')
plt.plot((0, 25), (0, prediction(25, w_val, b_val)))
plt.plot((0,25), (prediction(0, w_val, b_val), prediction(25, w_val, b_val)))
