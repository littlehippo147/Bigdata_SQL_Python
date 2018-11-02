Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def f(x):
    print(" x = ", x, ", id(x) = ", id(x))

    
>>> a = 10
b = 10
c = 20
SyntaxError: multiple statements found while compiling a single statement
>>> a = 10
>>> b = 10
>>> c = 20
>>> print(" a = ", a, ", id(a) = ", id(a))
 a =  10 , id(a) =  1479788816
>>> print(" b = ", b, ", id(b) = ", id(b))
 b =  10 , id(b) =  1479788816
>>> print(" c = ", c, ", id(c) = ", id(c))
 c =  20 , id(c) =  1479788976
>>> f(a)
 x =  10 , id(x) =  1479788816
>>> f(b)
 x =  10 , id(x) =  1479788816
>>> f(c)
 x =  20 , id(x) =  1479788976
>>> f(10)
 x =  10 , id(x) =  1479788816
>>> def ff(x):
    x = 500
    print(" x = ", x, ", id(x) = ", id(x))

    
>>> ff(55)
 x =  500 , id(x) =  35544720
>>> a = 55
>>> print(" a = ", a, ", id(a) = ", id(a))
 a =  55 , id(a) =  1479789536
>>> ff(a)
 x =  500 , id(x) =  35544720
>>> a = 500
>>> print(" a = ", a, ", id(a) = ", id(a))
 a =  500 , id(a) =  35544784
>>> f1 = lambda x : x*x
>>> f1(5)
25
>>> [for i in range(3): lambda i : i + 1]
SyntaxError: invalid syntax
>>> b = [i for i in range(2, 50, 2)]
>>> b
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> c = [lambda x : x*x for x in range(2, 10, 1)]
>>> c
[<function <listcomp>.<lambda> at 0x021E0660>, <function <listcomp>.<lambda> at 0x021E06A8>, <function <listcomp>.<lambda> at 0x021E06F0>, <function <listcomp>.<lambda> at 0x021E0738>, <function <listcomp>.<lambda> at 0x021E0780>, <function <listcomp>.<lambda> at 0x021E07C8>, <function <listcomp>.<lambda> at 0x021E0810>, <function <listcomp>.<lambda> at 0x021E0858>]
>>> 3 lambda x : x+2
SyntaxError: invalid syntax
>>> f4 = lambda x : x%2
>>> f4(10
       )
0
>>> f4(11)
1
>>> fillter(f4, range(1, 21))
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    fillter(f4, range(1, 21))
NameError: name 'fillter' is not defined
>>> filter(f4, range(1, 21))
<filter object at 0x02204390>
>>> print(filter(f4, range(1, 21)))
<filter object at 0x02204190>
>>> map(lambda x : x + 5, [1, 2, 3])
<map object at 0x02204190>
>>> print(map(lambda x : x + 5, [1, 2, 3]))
<map object at 0x02204290>
>>> d =map(lambda x : x + 5, [1, 2, 3])
>>> d
<map object at 0x02204130>
>>> list(map(lambda x : x + 5, [1, 2, 3]))
[6, 7, 8]
>>> list(filter(f4, range(1, 21)))
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
>>> # filter
>>> # map
>>> list(filter(f1, range(1, 5)))
[1, 2, 3, 4]
>>> list(filter(f1, range(0, 5)))
[1, 2, 3, 4]
>>> f(300)
 x =  300 , id(x) =  35544544
>>> f(300)
 x =  300 , id(x) =  35544368
>>> f(300)
 x =  300 , id(x) =  35544480
>>> f(100)
 x =  100 , id(x) =  1479790256
>>> f(100)
 x =  100 , id(x) =  1479790256
>>> f(256)
 x =  256 , id(x) =  1479792752
>>> f(256)
 x =  256 , id(x) =  1479792752
>>> f(257)
 x =  257 , id(x) =  35544240
>>> f(257)
 x =  257 , id(x) =  35544768
>>> list(filter(lambda x : x > 2, range(0, 5)))
[3, 4]
>>> list(filter(lambda x : x % 2 == 0, range(0, 5)))
[0, 2, 4]
>>> (filter(lambda x : x % 2 == 0, range(0, 5)))
<filter object at 0x02204B10>
>>> (filter(lambda x : x % 2 == 0, range(0, 5)))
<filter object at 0x02204190>
>>> (filter(lambda x : x % 2 == 0, range(0, 5)))
<filter object at 0x02204B70>
>>> map(lambda x : x * 5 + 2, range(0, 10))
<map object at 0x02204650>
>>> list(map(lambda x : x * 5 + 2, range(0, 10)))
[2, 7, 12, 17, 22, 27, 32, 37, 42, 47]
>>> list(map(lambda x : x * 5 + 2, [2, 3, 5, 7]))
[12, 17, 27, 37]
>>> list(map(lambda x : x * 5 + 2, (2, 3, 5, 7)))
[12, 17, 27, 37]
>>> list(map(lambda x, y : x * y, {2 : 3, 5 : 7}))
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    list(map(lambda x, y : x * y, {2 : 3, 5 : 7}))
TypeError: <lambda>() missing 1 required positional argument: 'y'
>>> list(map(lambda x, y : x * y, {2 : 3, 5 : 7}.item()))
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    list(map(lambda x, y : x * y, {2 : 3, 5 : 7}.item()))
AttributeError: 'dict' object has no attribute 'item'
>>> list(map(lambda x, y : x * y, {2 : 3, 5 : 7}.items()))
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    list(map(lambda x, y : x * y, {2 : 3, 5 : 7}.items()))
TypeError: <lambda>() missing 1 required positional argument: 'y'
>>> a + 50
550
>>> a.__add__(50)
550
>>> a.__eq__(5)
False
>>> 
>>> a.__sub__(50)
450
>>> dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> a.__mul(2)__
SyntaxError: invalid syntax
>>> a.__mul__(2)
1000
>>> k = [1, 2, 3]
>>> t = (2, 4, 6)
>>> dir(t)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> class Smart(object):
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
        
SyntaxError: expected an indented block
>>> # Smart class 정의
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

>>> s1 = Smart("Galaxy s8", "GOLD", 900000)

 Smart __init__ 
>>> s2 = Smart("Iphone 8", "BLACK", 950000)
 Smart __init__ 
>>> s1
<__main__.Smart object at 0x02204F50>
>>> s1.Disp()
모델 :  Galaxy s8 색상 :  GOLD 가격 :  900000 원
>>> s2.Disp()
모델 :  Iphone 8 색상 :  BLACK 가격 :  950000 원
>>> class point():
	'''
	'''

>>> x = point()
>>> d
<map object at 0x02204130>
>>> x
<__main__.point object at 0x02204B70>
>>> x = (1,2)
>>> x
(1, 2)
>>> type(x)
<class 'tuple'>
>>> x = point()
>>> x.x = 3
>>> x.y = 5
>>> x
<__main__.point object at 0x02204B70>
>>> print(x)
<__main__.point object at 0x02204B70>
>>> class point():
	def print(self):
		print("({},{})".format(x.x, x.y))

>>> x = point()
>>> x.x = 3
>>> x.y = 4
>>> print(x)
<__main__.point object at 0x02204670>
>>> 
class point():
	def pprint(self):
		print("({},{})".format(x.x, x.y))

	
>>> x = point()
>>> x.x = 3
>>> x.y = 4
>>> pprint(x)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    pprint(x)
NameError: name 'pprint' is not defined
>>> x.print()
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    x.print()
AttributeError: 'point' object has no attribute 'print'
>>> x.pprint()
(3,4)
>>> class point():
	def pprint(self):
		print("({},{})".format(x.x, x.y))

		
>>> x = point()
>>> x.x = 3
>>> x.y = 4
>>> x.pprint()
(3,4)
>>> 
>>> # 함수에서 생성한 객체는 함수가 끝나면 사라짐.
>>> def f():
    ss = Smart("hoho", "white", 950)

    
>>> ㄹ()
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    ㄹ()
NameError: name 'ᄅ' is not defined
>>> f()
 Smart __init__ 
 Smart __del__ 
>>> ## Smart class의 object가 생성됐다가 함수가 끝나면서 다시 사라짐
>>> ## garbage collector가 memory를 자동으로 회수해준다
>>> def f():
	global ss
	ss = Smart("hoho", "white", 950)

	
>>> f()
 Smart __init__ 
>>> ss.Disp()
모델 :  hoho 색상 :  white 가격 :  950 원
>>> s1.self
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    s1.self
AttributeError: 'Smart' object has no attribute 'self'
>>> s1.self()
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    s1.self()
AttributeError: 'Smart' object has no attribute 'self'
>>> s1.selfDisp()
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    s1.selfDisp()
AttributeError: 'Smart' object has no attribute 'selfDisp'
>>> s1
<__main__.Smart object at 0x02204F50>
>>> id(s1)
35671888
>>> hex(id(s1))
'0x2204f50'
>>> x = point(3,4)
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    x = point(3,4)
TypeError: point() takes no arguments
>>> class point():
	po = []
	def __init__(self, *point):
		for i in point:
			po.append(i)

			
>>> x = point(1,2,3)
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    x = point(1,2,3)
  File "<pyshell#149>", line 5, in __init__
    po.append(i)
NameError: name 'po' is not defined
>>> class point():

	def __init__(self, *point):
		po = []
		for i in point:
			po.append(i)

			
>>> x = point(1,2,3)
>>> x
<__main__.point object at 0x022217D0>
>>> print(x)
<__main__.point object at 0x022217D0>
>>> list(x)
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    list(x)
TypeError: 'point' object is not iterable
>>> del point()
SyntaxError: can't delete function call
>>> del point
>>> x= ponint()
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    x= ponint()
NameError: name 'ponint' is not defined
>>> x = point()
Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    x = point()
NameError: name 'point' is not defined
>>> ss
<__main__.Smart object at 0x02221610>
>>> ss.del()
SyntaxError: invalid syntax
>>> ss.del
SyntaxError: invalid syntax
>>> ss.__del__()
 Smart __del__ 
>>> dir(Smart)
['Disp', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'cnt']
>>> dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> ss
<__main__.Smart object at 0x02221610>
>>> ss.Disp()
모델 :  hoho 색상 :  white 가격 :  950 원
>>> ss.__del__()
 Smart __del__ 
>>> x = point()
Traceback (most recent call last):
  File "<pyshell#170>", line 1, in <module>
    x = point()
NameError: name 'point' is not defined
>>> class Mt:
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

        
>>> def Hoho():
    print(" Hoho function ")

    
>>> m1 = Mt("설악산", 3500)
 Mt init 
>>> m2 = Mt("지랄산", 1915)
 Mt init 
>>> m1.Disp()
설악산  ==>  3500 M
>>> m2.Disp()
지랄산  ==>  1915 M
>>> m1.Haha()
 Haha method 
>>> Hoho()
 Hoho function 
>>> m1.mount
'설악산'
>>> m1.mount()
Traceback (most recent call last):
  File "<pyshell#182>", line 1, in <module>
    m1.mount()
TypeError: 'str' object is not callable
>>> class Mt:
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

        
>>> m1 = Mt("설악산", 3500)
 Mt init 
 Mt del 
>>> m2 = Mt("지랄산", 1915)
 Mt init 
 Mt del 
>>> m1
<__main__.Mt object at 0x02221CF0>
>>> m2
<__main__.Mt object at 0x02221D10>
>>> m1.__str__()
' 설악산 ==> 3500M '
>>> m1.mount()
Traceback (most recent call last):
  File "<pyshell#190>", line 1, in <module>
    m1.mount()
TypeError: 'str' object is not callable
>>> m1.mount
'설악산'
>>> class Mt:
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

        
>>> print(m1)
 설악산 ==> 3500M 
>>> m1.setmount(1708)
Traceback (most recent call last):
  File "<pyshell#195>", line 1, in <module>
    m1.setmount(1708)
AttributeError: 'Mt' object has no attribute 'setmount'
>>> m1.setalt(1708)
Traceback (most recent call last):
  File "<pyshell#196>", line 1, in <module>
    m1.setalt(1708)
AttributeError: 'Mt' object has no attribute 'setalt'
>>> m1 = Mt("설악산", 3500)
 Mt init 
 Mt del 
>>> m2 = Mt("지랄산", 1915)
 Mt init 
 Mt del 
>>> m1.setalt(1708)
>>> m2.setmount("지리산")
>>> print(m2)
 지리산 ==> 1915M 
>>> class Mt:
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

    def __eq__(self, other):
        if self.alt == other.alt & self.mount == other.mount:
            return True
        else:
            return False

>>> 
>>> m1.__eq__(m2)
NotImplemented
>>> m1 = Mt("설악산", 3500)
 Mt init 
 Mt del 
>>> m2 = Mt("지랄산", 1915)
 Mt init 
 Mt del 
>>> m1.__eq__(m2)
Traceback (most recent call last):
  File "<pyshell#207>", line 1, in <module>
    m1.__eq__(m2)
  File "<pyshell#202>", line 26, in __eq__
    if self.alt == other.alt & self.mount == other.mount:
TypeError: unsupported operand type(s) for &: 'int' and 'str'
>>> class Mt:
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

    def __eq__(self, other):
        if self.alt == other.alt and self.mount == other.mount:
            return True
        else:
            return False

        
>>> m1 = Mt("설악산", 3500)
 Mt init 
>>> m2 = Mt("지랄산", 1915)
 Mt init 
>>> m1.__eq__(m2)
False
>>> m1 == m2
False
>>> m1 is m2
False
>>> class Mt:
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
        self.alt += other.alt
        self.mount += other.mount

>>> 
>>> m1 = Mt("설악산", 3500)
 Mt init 
 Mt del 
>>> m1 = Mt("설악산", 1708)
 Mt init 
 Mt del 

>>> m2 = Mt("지리산", 1915)
 Mt init 
 Mt del 
>>> m1 + m2
>>> print(m1 + m2)
None
>>> class Mt:
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
        self.alt += other.alt
        self.mount += other.mount
        return self

>>> m1 = Mt("설악산", 1708)
 Mt init 
 Mt del 
>>> m1 = Mt("설악산", 1708)
 Mt init 
 Mt del 
>>> m1 + m2
<__main__.Mt object at 0x02221BF0>
>>> print(m1 + m2)
 설악산지리산지리산 ==> 5538M 
>>> class Mt:
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
        a = Mt()
        a.alt = self.alt + other.alt
        a.mount = self.mount + other.mount
        return a

>>> m1 = Mt("설악산", 1708)
 Mt init 
>>> m2 = Mt("지리산", 1915)
 Mt init 
 Mt del 
>>> print(m1 + m2)
 Mt del 
 Mt del 
 Mt del 
Traceback (most recent call last):
  File "<pyshell#232>", line 1, in <module>
    print(m1 + m2)
  File "<pyshell#229>", line 33, in __add__
    a = Mt()
TypeError: __init__() missing 2 required positional arguments: 'm' and 'a'
>>> class Mt:
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

>>> m1 = Mt("설악산", 1708)
 Mt init 
>>> m2 = Mt("지리산", 1915)
 Mt init 
>>> print(m1 + m2)
 Mt init 
 설악산지리산 ==> 3623M 
 Mt del 
>>> print(m1 + m2)
 Mt init 
 설악산지리산 ==> 3623M 
 Mt del 
>>> class Mt:
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

        
>>> 
>>> m1 = Mt("설악산", 1708)
 Mt init 
 Mt del 
>>> m2 = Mt("지리산", 1915)
 Mt init 
 Mt del 
>>> m1 + 6
 Mt del 
<__main__.Mt object at 0x02221410>
>>> m1
<__main__.Mt object at 0x02221410>
>>> print(m1)
 설악산 ==> 1714M 
>>> class Date(object):
    def __init__(self, y, m, d):
        self.y = y
        self.m = m
        self.d = d
        print(" Date init ")

    def __del__(self):
        print(" Date del ")

    def __str__(self):
        return "{}/{}/{}".format(y, m, d)

>>> d1 = Date(1999, 3, 24)
 Date init 
>>> d2 = Date(201, 10, 15)
 Date init 
>>> print(d1)
 Mt del 
 Mt del 
Traceback (most recent call last):
  File "<pyshell#250>", line 1, in <module>
    print(d1)
  File "<pyshell#247>", line 12, in __str__
    return "{}/{}/{}".format(y, m, d)
NameError: name 'y' is not defined
>>> d1.y
1999
>>> print(d2)
Traceback (most recent call last):
  File "<pyshell#252>", line 1, in <module>
    print(d2)
  File "<pyshell#247>", line 12, in __str__
    return "{}/{}/{}".format(y, m, d)
NameError: name 'y' is not defined
>>> class Date(object):
    def __init__(self, y, m, d):
        self.y = y
        self.m = m
        self.d = d
        print(" Date init ")

    def __del__(self):
        print(" Date del ")

    def __str__(self):
        return "{}/{}/{}".format(y, m, d)
d1 = Date(1999, 3, 24)
SyntaxError: invalid syntax
>>> class Date(object):
    def __init__(self, y, m, d):
        self.y = y
        self.m = m
        self.d = d
        print(" Date init ")

    def __del__(self):
        print(" Date del ")

    def __str__(self):
        return "{}/{}/{}".format(y, m, d)

>>> d1 = Date(1999, 3, 24)
 Date init 
 Date del 
>>> d2 = Date(201, 10, 15)
 Date init 
>>> d1
<__main__.Date object at 0x022216B0>
>>> print(d1)
 Date del 
Traceback (most recent call last):
  File "<pyshell#259>", line 1, in <module>
    print(d1)
  File "<pyshell#255>", line 12, in __str__
    return "{}/{}/{}".format(y, m, d)
NameError: name 'y' is not defined
>>> class Date(object):
    def __init__(self, y, m, d):
        self.y = y
        self.m = m
        self.d = d
        print(" Date init ")

    def __del__(self):
        print(" Date del ")

    def __str__(self):
        return "{}/{}/{}".format(self.y, self.m, self.d)

>>> d1 = Date(1999, 3, 24)
 Date init 
>>> d2 = Date(201, 10, 15)
 Date init 
 Date del 
>>> print(d1)
1999/3/24
>>> print(d2)
201/10/15

>>> d2 = Date(2001, 10, 15)
 Date init 
 Date del 
>>> print(d2)
2001/10/15
>>> class Date(object):
    def __init__(self, y, m, d):
        self.y = y
        self.m = m
        self.d = d
        print(" Date init ")

    def __del__(self):
        print(" Date del ")

    def __str__(self):
        print("{}/{}/{}".format(y, m, d))

        
>>> d1 = Date(1999, 3, 24)
 Date init 
 Date del 
>>> d1
<__main__.Date object at 0x02221270>
>>> print(d1)
 Date del 
Traceback (most recent call last):
  File "<pyshell#272>", line 1, in <module>
    print(d1)
  File "<pyshell#269>", line 12, in __str__
    print("{}/{}/{}".format(y, m, d))
NameError: name 'y' is not defined
>>> class Date(object):
    def __init__(self, y, m, d):
        self.y = y
        self.m = m
        self.d = d
        print(" Date init ")

    def __del__(self):
        print(" Date del ")

    def __str__(self):
        print("{}/{}/{}".format(self.y, self.m, self.d))

        
>>> d1 = Date(1999, 3, 24)
 Date init 
>>> d1
<__main__.Date object at 0x02221210>
>>> print(d1)
1999/3/24
 Date del 
Traceback (most recent call last):
  File "<pyshell#277>", line 1, in <module>
    print(d1)
TypeError: __str__ returned non-string (type NoneType)
>>> ## 이건 안됨 ㅇㅇ print는 값을 보여주기만 할 뿐, 실체가 없다
>>> class Man(Date):
    def __init__(self, n, y, m, d):
        Date.__init__(self, y, m, d)
        self.name = n
        self.age = 2018 - y + 1
        print(" Man init ")

    def __del__(self):
        print(" Man del ")

    def __str__(self):
        return "{} {} {} {} {}".format(self.name, self.age, self.y, self.m, self.d)

    
>>> man = Man("이정호", 1993, 12, 22)
 Date init 
 Man init 
>>> print(man)
이정호 26 1993 12 22
>>> class Man(Date):
    def __init__(self, n, y, m, d):
        super()(self, y, m, d)
        self.name = n
        self.age = 2018 - y + 1
        print(" Man init ")

    def __del__(self):
        print(" Man del ")

    def __str__(self):
        return "{} {} {} {} {}".format(self.name, self.age, self.y, self.m, self.d)


>>> 
>>> man = Man("이정호", 1993, 12, 22)
Traceback (most recent call last):
  File "<pyshell#284>", line 1, in <module>
    man = Man("이정호", 1993, 12, 22)
  File "<pyshell#282>", line 3, in __init__
    super()(self, y, m, d)
TypeError: 'super' object is not callable
>>> class Man(Date):
    def __init__(self, n, y, m, d):
        super()(y, m, d)
        self.name = n
        self.age = 2018 - y + 1
        print(" Man init ")

    def __del__(self):
        print(" Man del ")

    def __str__(self):
        return "{} {} {} {} {}".format(self.name, self.age, self.y, self.m, self.d)

>>> man = Man("이정호", 1993, 12, 22)
 Man del 
Traceback (most recent call last):
  File "<pyshell#287>", line 1, in <module>
    man = Man("이정호", 1993, 12, 22)
  File "<pyshell#286>", line 3, in __init__
    super()(y, m, d)
TypeError: 'super' object is not callable
>>> class Man(Date):
    def __init__(self, n, y, m, d):
        super()__init__(y, m, d)
        self.name = n
        self.age = 2018 - y + 1
        print(" Man init ")

    def __del__(self):
        print(" Man del ")

    def __str__(self):
        return "{} {} {} {} {}".format(self.name, self.age, self.y, self.m, self.d)
SyntaxError: invalid syntax
>>> 
>>> class Man(Date):
    def __init__(self, n, y, m, d):
        super().__init__(y, m, d)
        self.name = n
        self.age = 2018 - y + 1
        print(" Man init ")

    def __del__(self):
        print(" Man del ")

    def __str__(self):
        return "{} {} {} {} {}".format(self.name, self.age, self.y, self.m, self.d)

>>> man = Man("이정호", 1993, 12, 22)
 Date init 
 Man init 
 Man del 
>>> 
