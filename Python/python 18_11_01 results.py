Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ~555
-556
>>> ~2
-3
>>> 2 ** 8
256
>>> 2 ** 16
65536
>>> 2 ** 32
4294967296
>>> 2 ** 64
18446744073709551616
>>> ~2150000000
-2150000001
>>> ~21500000000
-21500000001
>>> ~900000000000000000000
-900000000000000000001
>>> def aha():
    print(" 안녕 aha 함수야! ")

def ace():
    print(" 불주먹 ace ")

def good():
    print(" 잘했어요 ")

SyntaxError: invalid syntax
>>> def aha():
    print(" 안녕 aha 함수야! ")

>>> def ace():
    print(" 불주먹 ace ")

    
>>> def good():
    print(" 잘했어요 ")

    
>>> aha()
 안녕 aha 함수야! 
>>> ace()
 불주먹 ace 
>>> good()
 잘했어요 
>>> a = aha()
 안녕 aha 함수야! 
>>> a
>>> def better():
    print(" 이건 100을 주는 함수다 ")
    return 100

>>> better()
 이건 100을 주는 함수다 
100
>>> a = better()
 이건 100을 주는 함수다 
>>> a
100
>>> def xandy(x, y):
    print("x 는 {}, y 는 {}".format(x, y))

    
>>> xandy(2,3)
x 는 2, y 는 3
>>> def xandyandz(x, y, z):
    return (x+y+z)

>>> xandyandz(1,2,3)
6
>>> xandy('아이스베어', '팬팬')
x 는 아이스베어, y 는 팬팬
>>> xandyandz('아이스베어', 3, '도라에몽')
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    xandyandz('아이스베어', 3, '도라에몽')
  File "<pyshell#30>", line 2, in xandyandz
    return (x+y+z)
TypeError: can only concatenate str (not "int") to str
>>> for i in range(3):
	print("www.naver.com/", i, "/toto/")

www.naver.com/ 0 /toto/
www.naver.com/ 1 /toto/
www.naver.com/ 2 /toto/
>>> def Sum(num1, num2):
    return num1 + num2

>>> Sum(5, 6)
11
>>> def Sq(n1, n2):
    num = 1
    for i in range(n2)
        num *= n1
    return num

SyntaxError: invalid syntax
>>> def Sq(n1, n2):
    num = 1
    for i in range(n2):
        num *= n1
    return num

>>> Sq(2, 4)
16
>>> a = Sum(5,5)
>>> a
10
>>> b = Sq(2, 64)
>>> b
18446744073709551616
>>> def Calc(n1, n2, op):
    if op == '+':
        print(n1, "+", n2, "=", n1 + n2)
    elif op == '-':
        print(n1, "-", n2, "=", n1 - n2)
    elif op == '*':
        print(n1, "*", n2, "=", n1 * n2)
    elif op == '/':
        print(n1, "/", n2, "=", round(n1 / n2, 2))
    else:
        print("사칙연산만 가능합시다")

        
>>> Calc(2, 3, '+')
2 + 3 = 5
>>> Calc(2, 3, '-')
2 - 3 = -1
>>> Calc(2, 3, '*')
2 * 3 = 6
>>> Calc(2, 3, '/')
2 / 3 = 0.67
>>> 
def call(name):
    print("내 이름은", name, "입니다.")

    
>>> call('짱구')
내 이름은 짱구 입니다.
>>> def xyz(x, y, z):
    return x, y, z

>>> xyz(2, 3, 5)
(2, 3, 5)
>>> c = xyz(2, 3, 5)
>>> 
>>> c
(2, 3, 5)
>>> type(c)
<class 'tuple'>
>>> def calcul():
    while True:
        print(" ** 간단 계산기 ** ")
        num1 = int(input(" 첫번째 수 : ")
        if num1 == -999 :
            print(" 프로그램 종료 ")
            break
        op = input(" [ +, - , *, / ] : ")
        num2 = int(input(" 두번째 수 : "))

        if op == '+':
            res = Plus(num1, num2)
        elif op == '-':
            res = Minus(num1, num2)
        elif op == '*':
            res = Multi(num1, num2)
        elif op == '/':
            res = Divi(num1, num2)
        else:
            print(' {}연산자 없음'.format(op))
            continue

        print(' 결과 : {} {} {} = {}'.format(num1, op, num2, res))
		   
SyntaxError: invalid syntax
>>> def calcul():
    while True:
        print(" ** 간단 계산기 ** ")
        num1 = int(input(" 첫번째 수 : ")
        if num1 == -999:
            print(" 프로그램 종료 ")
            break
        op = input(" [ +, - , *, / ] : ")
        num2 = int(input(" 두번째 수 : "))

        if op == '+':
            res = Plus(num1, num2)
        elif op == '-':
            res = Minus(num1, num2)
        elif op == '*':
            res = Multi(num1, num2)
        elif op == '/':
            res = Divi(num1, num2)
        else:
            print(' {}연산자 없음'.format(op))
            continue

        print(' 결과 : {} {} {} = {}'.format(num1, op, num2, res))
		   
SyntaxError: invalid syntax
>>> 
		   
>>> def calcul():
    while True:
        print(" ** 간단 계산기 ** ")
        num1 = int(input(" 첫번째 수 : "))
        if num1 == -999:
            print(" 프로그램 종료 ")
            break
        op = input(" [ +, - , *, / ] : ")
        num2 = int(input(" 두번째 수 : "))

        if op == '+':
            res = Plus(num1, num2)
        elif op == '-':
            res = Minus(num1, num2)
        elif op == '*':
            res = Multi(num1, num2)
        elif op == '/':
            res = Divi(num1, num2)
        else:
            print(' {}연산자 없음'.format(op))
            continue

        print(' 결과 : {} {} {} = {}'.format(num1, op, num2, res))

		   
>>> calcul()
		   
 ** 간단 계산기 ** 
 첫번째 수 : 2
 [ +, - , *, / ] : 5
 두번째 수 : 5
 5연산자 없음
 ** 간단 계산기 ** 
 첫번째 수 : 2
 [ +, - , *, / ] : +
 두번째 수 : 3
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    calcul()
  File "<pyshell#69>", line 12, in calcul
    res = Plus(num1, num2)
NameError: name 'Plus' is not defined
>>> def Plus(x,y):
    return x + y

		   
>>> def Minus(x,y):
    return x - y

		   
>>> def Multi(x,y):
    return x * y

		   
>>> def Divi(x,y):
    return round(x / y)

		   
>>> calcul()
		   
 ** 간단 계산기 ** 
 첫번째 수 : 5
 [ +, - , *, / ] : +
 두번째 수 : 3
 결과 : 5 + 3 = 8
 ** 간단 계산기 ** 
 첫번째 수 : 5
 [ +, - , *, / ] : -
 두번째 수 : 18
 결과 : 5 - 18 = -13
 ** 간단 계산기 ** 
 첫번째 수 : 3
 [ +, - , *, / ] : *
 두번째 수 : 2
 결과 : 3 * 2 = 6
 ** 간단 계산기 ** 
 첫번째 수 : 6
 [ +, - , *, / ] : /
 두번째 수 : 4
 결과 : 6 / 4 = 2
 ** 간단 계산기 ** 
 첫번째 수 : -999
 프로그램 종료 
>>> def Divi(x,y):
    return round(x / y, 2)

		   
>>> calcul()
		   
 ** 간단 계산기 ** 
 첫번째 수 : 4
 [ +, - , *, / ] : /
 두번째 수 : 2
 결과 : 4 / 2 = 2.0
 ** 간단 계산기 ** 
 첫번째 수 : 6
 [ +, - , *, / ] : /
 두번째 수 : 4
 결과 : 6 / 4 = 1.5
 ** 간단 계산기 ** 
 첫번째 수 : -999
 프로그램 종료 
>>> def calcul2():
    while True:
        print(" ** 간단 계산기 ** ")
        num1 = int(input(" 첫번째 수 : "))
        if num1 == -999:
            print(" 프로그램 종료 ")
            break
        op = input(" [ +, - , *, / ] : ")
        num2 = int(input(" 두번째 수 : "))

        if op == '+':
            res = num1 + num2
        elif op == '-':
            res = num1 - num2
        elif op == '*':
            res = num1 * num2
        elif op == '/':
            res = round(num / num2, 2)
        else:
            print(' {}연산자 없음'.format(op))
            continue

        print(' 결과 : {} {} {} = {}'.format(num1, op, num2, res))

>>> calcul2()
		   
 ** 간단 계산기 ** 
 첫번째 수 : 5
 [ +, - , *, / ] : *
 두번째 수 : 3
 결과 : 5 * 3 = 15
 ** 간단 계산기 ** 
 첫번째 수 : -999
 프로그램 종료 
>>> def Display():
    while True:
        x = input(" 이  름 > ")
        y = int(input(" 횟  수 > ")
        
        if y == 0:
            print("그가 나의 이름을 불러주었다면, 나는 그에게로 가 꽃이 되었을텐데.")
            break

        for i in range(y):
            print("{}, 너는 나에게로 와 꽃이 되었다.".format(x))
        return
		
SyntaxError: invalid syntax
>>> def Display():
    while True:
        x = input(" 이  름 > ")
        y = int(input(" 횟  수 > "))
        
        if y == 0:
            print("그가 나의 이름을 불러주었다면, 나는 그에게로 가 꽃이 되었을텐데.")
            break

        for i in range(y):
            print("{}, 너는 나에게로 와 꽃이 되었다.".format(x))
        return

		
>>> Display()
		
 이  름 > 이정호
 횟  수 > 2
이정호, 너는 나에게로 와 꽃이 되었다.
이정호, 너는 나에게로 와 꽃이 되었다.
>>> def Display():
    while True:
        x = input(" 이  름 > ")
        y = int(input(" 횟  수 > "))
        
        if y == 0:
            print("그가 나의 이름을 불러주었다면, 나는 그에게로 가 꽃이 되었을텐데.")
            break

        for i in range(y):
            print("{}, 너는 나에게로 와 꽃{}이(가) 되었다.".format(x, y))
        return

>>> Display()
		
 이  름 > 이정호
 횟  수 > 5
이정호, 너는 나에게로 와 꽃5이(가) 되었다.
이정호, 너는 나에게로 와 꽃5이(가) 되었다.
이정호, 너는 나에게로 와 꽃5이(가) 되었다.
이정호, 너는 나에게로 와 꽃5이(가) 되었다.
이정호, 너는 나에게로 와 꽃5이(가) 되었다.
>>> def Display():
    while True:
        x = input(" 이  름 > ")
        y = int(input(" 횟  수 > "))
        
        if y == 0:
            print("그가 나의 이름을 불러주었다면, 나는 그에게로 가 꽃이 되었을텐데.")
            break

        for i in range(y):
            print("{}, 너는 나에게로 와 꽃{}이(가) 되었다.".format(x, i))
        return

		
>>> Display()
		
 이  름 > 
 횟  수 > 
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    Display()
  File "<pyshell#94>", line 4, in Display
    y = int(input(" 횟  수 > "))
ValueError: invalid literal for int() with base 10: ''
>>> Display()
		
 이  름 > 이정호
 횟  수 > 3
이정호, 너는 나에게로 와 꽃0이(가) 되었다.
이정호, 너는 나에게로 와 꽃1이(가) 되었다.
이정호, 너는 나에게로 와 꽃2이(가) 되었다.
>>> def Display():
    while True:
        x = input(" 이  름 > ")
        y = int(input(" 횟  수 > "))
        
        if y == 0:
            print("그가 나의 이름을 불러주었다면, 나는 그에게로 가 꽃이 되었을텐데.")
            break

        for i in range(y):
            print("{}, 너는 나에게로 와 꽃{}이(가) 되었다.".format(x, i + 1))
        return

		
>>> Display()
		
 이  름 > 이정호
 횟  수 > 3
이정호, 너는 나에게로 와 꽃1이(가) 되었다.
이정호, 너는 나에게로 와 꽃2이(가) 되었다.
이정호, 너는 나에게로 와 꽃3이(가) 되었다.
>>> 
Display()
		
 이  름 > 이정호
 횟  수 > 0
그가 나의 이름을 불러주었다면, 나는 그에게로 가 꽃이 되었을텐데.
>>> 
def Add(x):
    return x + x

		
>>> print(Add(x))
		
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    print(Add(x))
NameError: name 'x' is not defined
>>> print(Add(2))
		
4
>>> def Add2(x, y):
    returrn x + y
		
SyntaxError: invalid syntax
>>> 
		
>>> def Add2(x, y):
    return x + y

		
>>> Add2(2,3)
		
5
>>> def add3(x, y, z):
    return x+ y+ z

		
>>> add3(5, 2 ,3)
		
10
>>> def Add5(*x):
    for i im x:
        print(i, end= ' ')
		
SyntaxError: invalid syntax
>>> 
		
>>> def Add5(*x):
    for i in x:
        print(i, end= ' ')

		
>>> Add5(5)
		
5 
>>> Add5(2,5)
		
2 5 
>>> def Add6(x, *y):
    print("a ==> ", a)
    for i in x:
        print(i, end= ' ')

>>> 
		
>>> Add6(3, 3,4,5)
		
a ==>  10
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    Add6(3, 3,4,5)
  File "<pyshell#119>", line 3, in Add6
    for i in x:
TypeError: 'int' object is not iterable
>>> def Add6(x, *y):
    print("x ==> ", x)
    for i in y:
        print(i, end= ' ')

		
>>> Add6(3, 4, 5, 6)
		
x ==>  3
4 5 6 
>>> def Add7(**x):
    for key, value in x.items():
        print(ket, " ==> ", value)

		
>>> def Add7(**x):
    for key, value in x.items():
        print(key, " ==> ", value)

>>> 
		
>>> Add7(age = 30, name = "민지호", job = "셰프")
		
age  ==>  30
name  ==>  민지호
job  ==>  셰프
>>> def sum2(*args):
    s = 0
    for i in args:
        s += i
    return s

		
>>> sum2(2, 3, 5)
		
10
>>> sum([2, 3, 5])
		
10
>>> def min2(*args):
    res = args[1]
    for i in args:
        if i < res:
            res = i
        else:
            continue
    return res

		
>>> min2(3, 4, 1, 2, 8, 9)
		
1
>>> def max2(*args):
    res = args[1]
    for i in args:
        if i > res:
            res = i
        else:
            continue
    return res

		
>>> max2(2, 5, 20, 3, 15, 78, 60)
		
78
>>> max(1,2,3)
		
3
>>> max()
		
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    max()
TypeError: max expected 1 arguments, got 0
>>> help(max())
		
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    help(max())
TypeError: max expected 1 arguments, got 0
>>> max2([2, 3, 5])
		
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    max2([2, 3, 5])
  File "<pyshell#138>", line 2, in max2
    res = args[1]
IndexError: tuple index out of range
>>> max2(2)
		
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    max2(2)
  File "<pyshell#138>", line 2, in max2
    res = args[1]
IndexError: tuple index out of range
>>> max2(2,3)
		
3
>>> res = 2
		
>>> for i in 2:
	if 2 > res:
		res = i

Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    for i in 2:
TypeError: 'int' object is not iterable
>>> for i in 2:
	if i > res:
		res = i

		
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    for i in 2:
TypeError: 'int' object is not iterable
>>> max(2)
		
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    max(2)
TypeError: 'int' object is not iterable
>>> max2(2)
		
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    max2(2)
  File "<pyshell#138>", line 2, in max2
    res = args[1]
IndexError: tuple index out of range
>>> def min2(*args):
    res = args[0]
    for i in args:
        if i < res:
            res = i
        else:
            continue
    return res

		
>>> min2(3, 4, 1, 2, 8, 9)
		
1
>>> def min3(*a):
    res = a[0]
    for i in range(len(a)-1):
        if res > a[i+1]:
            res = a[i+1]
    return res

		
>>> min3(3, 4, 5, 2, 1)
		
1
>>> min2([2, 5, 3, 1])
		
[2, 5, 3, 1]
>>> def min4(a1, *a2):
    res = a1[0]
    if type(a1) == type([]):
        for i in range(len(a1)-1):
            if res > a1[i+1]:
                res = a1[i+1]
        return res
    else:
        for i in a2:
            if res > i
                res = i
        return res
		
SyntaxError: invalid syntax
>>> def min4(a1, *a2):
    res = a1[0]
    if type(a1) == type([]):
        for i in range(len(a1)-1):
            if res > a1[i+1]:
                res = a1[i+1]
        return res
    else:
        for i in a2:
            if res > i:
                res = i
        return res

		
>>> min4([2, 5, 1, 3])
		
1
>>> min4(2, 5, 1, 3)
		
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    min4(2, 5, 1, 3)
  File "<pyshell#164>", line 2, in min4
    res = a1[0]
TypeError: 'int' object is not subscriptable
>>> def min4(a1, *a2):
    if type(a1) == type([]):
        res = a1[0]
        for i in range(len(a1)-1):
            if res > a1[i+1]:
                res = a1[i+1]
        return res
    else:
        res = a1
        for i in a2:
            if res > i:
                res = i
        return res

		
>>> min4([2, 5, 1, 3])
		
1
>>> min4(2, 5, 1, 3)
		
1
>>> min4(2, 5, 1, 3, 0, -5, 25)
		
-5
>>> min4([2, 5, 1, 3, -4, -3])
		
-4
>>> type([1,2,3]) == 'list'
		
False
>>> type([1,2,3])
		
<class 'list'>
>>> min([2, 1, 5, 4])
		
1
>>> min([2, 1, 5, 4], 7)
		
Traceback (most recent call last):
  File "<pyshell#176>", line 1, in <module>
    min([2, 1, 5, 4], 7)
TypeError: '<' not supported between instances of 'int' and 'list'
>>> min4([2, 1, 5, 4], 7)
		
1
>>> min4([2, 1, 5, 4], 7, -2)
		
1
>>> def f():
    f1 = 100
    print("f1 = ", f1)

		
>>> f()
		
f1 =  100
>>> f1
		
Traceback (most recent call last):
  File "<pyshell#182>", line 1, in <module>
    f1
NameError: name 'f1' is not defined
>>> def g():
    g1 = 50
    print("g1 = ", g1)

		
>>> g()
		
g1 =  50
>>> g1
		
Traceback (most recent call last):
  File "<pyshell#186>", line 1, in <module>
    g1
NameError: name 'g1' is not defined
>>> g1 = 100
		
>>> g()
		
g1 =  50
>>> g1
		
100
>>> def gg():
    global g1 = 50
    print("g1 = ", g1)
		
SyntaxError: invalid syntax
>>> def gg():
    global g1
    g1 = 50
    print("g1 = ", g1)

		
>>> g1
		
100
>>> gg()
		
g1 =  50
>>> g1
		
50
>>> for i in range(5):
	a = i

		
>>> a
		
4
>>> g = 600
cnt = 0
		
SyntaxError: multiple statements found while compiling a single statement
>>> g = 600
		
>>> cnt = 0
		
>>> def f():
    a= 100

		
>>> a
		
4
>>> def f2():
    t = x
    print(t, "지역변수 입니다")

		
>>> f2(5)
		
Traceback (most recent call last):
  File "<pyshell#208>", line 1, in <module>
    f2(5)
TypeError: f2() takes 0 positional arguments but 1 was given
>>> def f2(x):
    t = x
    print(t, "지역변수 입니다")

		
>>> f2(5)
		
5 지역변수 입니다
>>> def Call():
    global cnt
    print(" Call ")
    cnt += 1
    print(" cnt ==> ", cnt)

		
>>> cnt
		
0
>>> Call()
		
 Call 
 cnt ==>  1
>>> cnt
		
1
>>> Call()
		
 Call 
 cnt ==>  2
>>> cnt
		
2
>>> def f2(x):
    g = x
    print(g, "지역변수 입니다")

		
>>> f2(5)
		
5 지역변수 입니다
>>> g
		
600
>>> global a
		
>>> def f():
    a= 100

		
>>> a
		
4
>>> 
