# python 18_11_19 code.py

# cost_gradient
import matplotlib.pyplot as plt

def gradient_descent(x, y, w):
    c = 0
    for i in range(len(x)):
        hx = w * x[i]
        loss = (hx - y[i]) * x[i]
        c += loss
    return c / len(x)

def cost(x, y, w):
    c = 0
    for i in range(len(x)):
        hx = w * x[i]
        loss = (hx - y[i]) ** 2 
        c += loss
    return c / len(x)

def not_used():
    x = [1, 2, 3]
    y = [5, 6, 7]
    print(cost(x, y, -1))
    print(cost(x, y, 0))
    print(cost(x, y, 1))
    print(cost(x, y, 2))
    print(cost(x, y, 3))
    
    for i in range(-30, 50):
        w = i / 10
        c = cost(x,y,w)
        print(w,c)
        plt.plot(w, c, 'ro')
    plt.show()

not_used()


# train
x = [1, 2, 3]
y = [5, 6, 7]

w, old = 10, 100
for i in range(100):
    c = cost(x, y, w)
    grad = gradient_descent(x, y, w)
    w = w - 0.1 * grad
    print(i, c, old, w, grad)
    if c >= old and abs(c-old) < 1.0e-15:
        break
    old = c
    
print('weight = ', w)

###############################################
# TENSORFLOW
import tensorflow as tf
 
# constant
hello = tf.constant("안녕 Hello,Tensorflow!")
print(hello)
sess = tf.Session()
result = sess.run(hello)
print(result)
print(result.decode())

node1 = tf.constant(3.0,tf.float32)
node2 = tf.constant(4.0)
node3 = tf.add(node1,node2)

print("node1:",node1)
print("node2:",node2)
print("node3:",node3)

sess = tf.Session()
# print("sess.run([node1,node2]):",sess.run([node1,node2]))
print("sess.run(node3):",sess.run(node3))

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = tf.add(a,b)

sess = tf.Session()
print(sess.run(adder_node,feed_dict={a:3, b:4.5}))
print(sess.run(adder_node,feed_dict={a:[1,3,5,7], b:[2,4,6,8]}))

a1 = tf.Variable(4.0,tf.float32)
b1 = tf.Variable(7.5,tf.float32)
adder_node2 = tf.add(a1,b1)
sess = tf.Session()
sess.run(tf.global_variables_initializer())
print(sess.run(adder_node2))


t0 = tf.constant(3)
print('t0:',t0)
t1 = tf.constant([1.,2.,3.])
print('t1:',t1)
t2 = tf.constant([[1.,2.,3.],[4.,5.,6.]])
print('t2:',t2)

t3 = tf.constant([[[1.,2.,3.]],[[7.,8.,9.]]])
print('t3:',t3)

sess = tf.Session()
print(sess.run(t0))
print(sess.run(t1))
print(sess.run(t2))
print(sess.run(t3))

sess.close()
