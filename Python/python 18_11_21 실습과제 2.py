# python 18_11_21 code.py

# 실습과제 2
import csv
import MySQLdb
import sys

# KPC004의 서버 접속, database에 접근하여 cars_pred04 data 저장
con=MySQLdb.connect(host='10.1.42.61',port=3306,db='cars_pred04',user='KPC001',passwd='1234')
c=con.cursor()

c.execute("select * from cars_pred04;")
rows = c.fetchall()

speed = []
dist = []

for row in rows:
    speed.append(row[0])
    dist.append(row[1])

# 텐서플로 학습하기
tf.set_random_seed(777)

X = tf.placeholder(tf.float32, shape = [None])
Y = tf.placeholder(tf.float32, shape = [None])

W = tf.Variable(tf.random_normal([1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

hypothesis = X * W + b

cost =  tf.reduce_mean(tf.square(hypothesis - Y))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(30000):
    sess.run(train, feed_dict = {X:speed, Y:dist})
    if step % 100 == 0 :
        print(step,sess.run(cost, feed_dict = {X:speed, Y:dist}),sess.run(W),sess.run(b))
        
cost_min, W_pred, b_pred = sess.run([cost, W, b]) # 결정된 cost, W, b 값


# cars_predict 예측하기
## 예측할 데이터 불러와서 예측한 결과값 합치기
input_file = 'cars_predict.csv'
output_file = 'cars_predict_pred.csv'
data = pd.read_csv(input_file, header = None)    # 예측할 데이터

data[1] = sess.run(hypothesis, feed_dict = {X:data[0]})

data.columns = ['speed', 'dist']

data.to_csv(output_file, header = True, index = False)

# 예측한 결과값 DB에 저장
con2=MySQLdb.connect(host='localhost',port=3306,db='cars_predDB',user='KPC001',passwd='1234')
c2=con2.cursor()

c2.execute("use cars_predDB;")

create_table = """create table if not exists cars_pred004_pred
(speed float,
 dist float);"""

c2.execute(create_table)

for idx in range(len(data)):
    c2.execute("INSERT INTO cars_pred004_pred VALUES (%s, %s);", data.loc[idx])

con2.commit()
