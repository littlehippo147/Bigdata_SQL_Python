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
 