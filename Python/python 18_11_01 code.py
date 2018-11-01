# 함수 정의하기

def aha():
    print(" 안녕 aha 함수야! ")

def ace():
    print(" 불주먹 ace ")

def good():
    print(" 잘했어요 ")

def better():
    print(" 이건 100을 주는 함수다 ")
    return 100

aha()
ace()
good()
better()

a = aha()
a = better()

def xandy(x, y):
    print("x 는 {}, y 는 {}".format(x, y))

def xandyandz(x, y, z):
    return (x+y+z)

xandy(2,3)
xandyandz(1,2,3)

# 문자도 숫자도 가능하지만 함수에 따라 형을 맞춰주어야함.
xandy('아이스베어', '팬팬')
xandyandz('아이스베어', 3, '도라에몽')

def Sum(num1, num2):
    return num1 + num2

Sum(5, 6)
a = Sum(5, 5)
a

def Sq(n1, n2):
    num = 1
    for i in range(n2):
        num *= n1
    return num

Sq(2, 4)

b = Sq(2, 64)
b

def Calc(n1, n2, op):
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

Calc(2, 3, '+')
Calc(2, 3, '-')
Calc(2, 3, '*')
Calc(2, 3, '/')


def call(name):
    print("내 이름은", name, "입니다.")

def xyz(x, y, z):
    return x, y, z

# return 값의 형태에 따라 타입이 결정된다.
c = xyz(2, 3, 5)
type(c)

def Plus(x,y):
    return x + y

def Minus(x,y):
    return x - y

def Multi(x,y):
    return x * y

def Divi(x,y):
    return round(x / y, 2)

def calcul():
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

def calcul2():
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

def Display():
    while True:
        x = input(" 이  름 > ")
        y = int(input(" 횟  수 > "))
        
        if y == 0:
            print("그가 나의 이름을 불러주었다면, 나는 그에게로 가 꽃이 되었을텐데.")
            break

        for i in range(y):
            print("{}, 너는 나에게로 와 꽃{}이(가) 되었다.".format(x, i + 1))
        return

Display()
        

def Add(x):
    return x + x

def Add2(x, y):
    return x + y

def add3(x, y, z):
    return x+ y+ z

# 가변인자 : 길이를 알 수 없는 인자를 받을 때 사용.
def Add5(*x):
    for i in x:
        print(i, end= ' ')

def Add6(x, *y):
    print("x ==> ", x)
    for i in y:
        print(i, end= ' ')

# 사전인자 : 길이를 알 수 없는 keyword 인자를 받을 때 사용
def Add7(**x):
    for key, value in x.items():
        print(key, " ==> ", value)


# sum 함수 바꾸기
def sum2(*args):
    s = 0
    for i in args:
        s += i
    return s

sum2(2, 3, 5)
sum([2, 3, 5])

# 최솟값, 최댓값 구하기
## 최솟값
def min2(*args):
    res = args[0]
    for i in args:
        if i < res:
            res = i
    return res

def min3(*a):
    res = a[0]
    for i in range(len(a)-1):
        if res > a[i+1]:
            res = a[i+1]
    return res

# 리스트 인자도 받을 수 있도록 수정
def min4(a1, *a2):
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

## 최댓값
def max2(*args):
    res = args[0]
    for i in args:
        if i > res:
            res = i
    return res

def max3(*a):
    res = a[0]
    for i in range(len(a)-1):
        if res < a[i+1]:
            res = a[i+1]
    return res

# 리스트 인자도 받을 수 있도록 수정
def max4(a1, *a2):
    if type(a1) == type([]):
        res = a1[0]
        for i in range(len(a1)-1):
            if res < a1[i+1]:
                res = a1[i+1]
        return res
    else:
        res = a1
        for i in a2:
            if res < i:
                res = i
        return res

## 내장 함수에도 발생하는 문제 : 단일 값을 넣으면 오류 남

# 지역변수, 전역변수

def f():
    f1 = 100
    print("f1 = ", f1)

f()
f1 # 에러 (함수 안에서만 정의되었기 때문)

g1 = 100
def g():
    g1 = 50
    print("g1 = ", g1)

g()
g1 # 함수 내부에서는 값이 수정돼도, 함수 안에서만 영향. 밖으로 나오면 그대로

def gg():
    global g1
    g1 = 50
    print("g1 = ", g1)

gg()
g1 # 값이 바뀜. global로 전역변수 선언을 했기 때문

# lambda 표현식
# 는 내일 함

# 다시 지역변수 전역변수

g = 600
cnt = 0

def f():
    a= 100

a

def f2(x):
    g = x
    print(g, "지역변수 입니다")

def Call():
    global cnt
    print(" Call ")
    cnt += 1
    print(" cnt ==> ", cnt)

Call()
cnt


