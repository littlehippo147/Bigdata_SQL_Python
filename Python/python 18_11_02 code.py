def f(x):
    print(" x = ", x, ", id(x) = ", id(x))

a = 10
b = 10
c = 20

print(" a = ", a, ", id(a) = ", id(a))

print(" b = ", b, ", id(b) = ", id(b))

print(" c = ", c, ", id(c) = ", id(c))

def ff(x):
    x = 500
    print(" x = ", x, ", id(x) = ", id(x))

a = 55

print(" a = ", a, ", id(a) = ", id(a))

f1 = lambda x : x*x

b = [i for i in range(2, 50, 2)]

f4 = lambda x : x%2

filter(f4, range(1, 21))
list(filter(f1, range(1, 5)))
list(filter(f1, range(0, 5)))  

# filter는 조건에 맞는 값을 뽑아내는 함수, list로 풀어주어야 출력
list(filter(lambda x : x > 2, range(0, 5)))
list(filter(lambda x : x % 2 == 0, range(0, 5)))

# map은 R에서 apply 함수와 비슷. 각 값에 함수 취하여 결과 뽑아냄
map(lambda x : x * 5 + 2, range(0, 10))
list(map(lambda x : x * 5 + 2, range(0, 10)))
list(map(lambda x : x * 5 + 2, [2, 3, 5, 7]))
list(map(lambda x : x * 5 + 2, (2, 3, 5, 7)))
## 두 번째 인자가 list여도 tuple이어도 상관 없음. 결과는 list로 출력할 수 있음


# __add__
a + 50
a.__add__(50)

## 연산자 명령어 __( )__ 던더 매직 메소드
+  add
== eq
!= nq
>  gt
>= ge
<  lt
<= le

# Smart class 정의
class Smart(object):
    '''
     휴대폰의 모델, 색상, 가격을 알려주는 class
    '''
    cnt = 0
    # Smart class의 속성 설정
    def __init__(self, model, color, price):
        self.model = model
        self.color = color
        self.price = price
        print(" Smart __init__ ")

    # 제거
    def __del__(self):
        print(" Smart __del__ ")


    # method 정의
    def Disp(self):
        print("모델 : ", self.model, "색상 : ",
              self.color, "가격 : ", self.price, "원")

s1 = Smart("Galaxy s8", "GOLD", 900000)
s2 = Smart("Iphone 8", "BLACK", 950000)

# 함수에서 생성한 객체는 함수가 끝나면 사라짐.
def f():
    ss = Smart("hoho", "white", 950)

## garbage collector가 memory를 자동으로 회수해준다

class Mt:
    def __init__(self, m, a):
        self.mount = m
        self.alt = a
        print(" Mt init ")

    def __del__(self):
        print(" Mt del ")

    def Disp(self):
        print(self.mount, " ==> ", self.alt, "M")

    def Haha(self):
        print(" Haha method ")

def Hoho():
    print(" Hoho function ")

m1 = Mt("설악산", 3500)
m2 = Mt("지랄산", 1915)
m1.Disp()
m2.Disp()

class Mt:
    def __init__(self, m, a):
        self.mount = m
        self.alt = a
        print(" Mt init ")

    def __str__(self):
        return " {} ==> {}M ".format(self.mount, self.alt)
               
    def __del__(self):
        print(" Mt del ")

    def Disp(self):
        print(self.mount, " ==> ", self.alt, "M")

    def Haha(self):
        print(" Haha method ")

    def setmount(self, m):
        self.mount = m

    def setalt(self, a):
        self.alt = a
        
    # method 재정의
    def __eq__(self, other):
        if self.alt == other.alt and self.mount == other.mount:
            return True
        else:
            return False

    def __add__(self, other):
        return Mt(self.mount + other.mount, self.alt + other.alt)

    def __add__(self, a):
        self.alt += a
        return self
        

m1 = Mt("설악산", 1708)
m2 = Mt("지리산", 1915)


# date class 만들기

class Date(object):
    def __init__(self, y, m, d):
        self.y = y
        self.m = m
        self.d = d
        print(" Date init ")

    def __del__(self):
        print(" Date del ")

    def __str__(self):
        return "{}/{}/{}".format(self.y, self.m, self.d)


d1 = Date(1999, 3, 24)
d2 = Date(2001, 10, 15)
print(d1)
print(d2)

# 상속

class Man(Date):
    def __init__(self, n, y, m, d):
        Date.__init__(self, y, m, d)
        self.name = n
        self.age = 2018 - y + 1
        print(" Man init ")

    def __del__(self):
        print(" Man del ")

    def __str__(self):
        return "{} {} {} {} {}".format(self.name, self.age, self.y, self.m, self.d)

man = Man("이정호", 1993, 12, 22)
print(man)

class Man(Date):
    def __init__(self, n, y, m, d):
        super().__init__(y, m, d)
        self.name = n
        self.age = 2018 - y + 1
        print(" Man init ")

    def __del__(self):
        print(" Man del ")

    def __str__(self):
        return "{} {} {} {} {}".format(self.name, self.age, self.y, self.m, self.d)
