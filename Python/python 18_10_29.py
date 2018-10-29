Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hello World!")
Hello World!
>>> x = 5
>>> x
5
>>> x+5
10
>>> 10 + 5
15
>>> 10 -5
5
>>> 10 / 3
3.3333333333333335
>>> 10 * 5
50
>>> 10 //3
3
>>> 10 % 3
1
>>> 10/3
3.3333333333333335
>>> a = input("정수 입력 : ")
정수 입력 : 300
>>> a
'300'
>>> print(a)
300
>>> k = 'korea'
>>> num = 1000
>>> k
'korea'
>>> num
1000
>>> name = input(" 이름은 : ")
 이름은 : 이정호
>>> name
'이정호'
>>> print(name)
이정호
>>> type(name)
<class 'str'>
>>> def where:
	
SyntaxError: invalid syntax
>>> def were():
	dong = input(" 무슨동에 사세요 : ")
	beon = input(" 몇 번 타고 오세요 : ")
	print(dong)
	print('에서')
	print(beon)
	print('타고 옵니다.')

>>> were
<function were at 0x02201A98>
>>> were()
 무슨동에 사세요 : 성수동
 몇 번 타고 오세요 : 50
성수동
에서
50
타고 옵니다.
>>> def were():
	dong = input(" 무슨동에 사세요 : ")
	beon = input(" 몇 번 타고 오세요 : ")
	print(dong, '에서 ', beon, '번 타고 옵니다.')

>>> def where():
	dong = input(" 무슨동에 사세요 : ")
	beon = input(" 몇 번 타고 오세요 : ")
	print(dong, '에서 ', beon, '번 타고 옵니다.')

>>> where()
 무슨동에 사세요 : 성수동
 몇 번 타고 오세요 : 50
성수동 에서  50 번 타고 옵니다.
>>> def where():
	dong = input(" 무슨동에 사세요 : ")
	beon = input(" 몇 번 타고 오세요 : ")
	print(dong + '에서 ', beon + '번 타고 옵니다.')

>>> where()
 무슨동에 사세요 : 성수동
 몇 번 타고 오세요 : 50
성수동에서  50번 타고 옵니다.
>>> def where():
	dong = input(" 무슨동에 사세요 : ")
	beon = input(" 몇 번 타고 오세요 : ")
	print(dong + '에서', beon + '번 타고 옵니다.')

>>> where()
 무슨동에 사세요 : 성수동
 몇 번 타고 오세요 : 50
성수동에서 50번 타고 옵니다.
>>> def plus():
	first = input(" 첫 번째 수 : ")
	second = input(" 두 번째 수 : ")
	print('출력>>', first, '+', second, '=", int(first) + int(second))
	      
SyntaxError: EOL while scanning string literal
>>> def plus():
	first = input(" 첫 번째 수 : ")
	second = input(" 두 번째 수 : ")
	print('출력>>', first, '+', second, '=', int(first) + int(second))

>>> plus()
	      
 첫 번째 수 : 40
 두 번째 수 : 50
출력>> 40 + 50 = 90
>>> def plus():
	first = input(" 첫 번째 수 : ")
	second = input(" 두 번째 수 : ")
	print(first, '+', second, '=', int(first) + int(second))

>>> plus()
	      
 첫 번째 수 : 40
 두 번째 수 : 50
40 + 50 = 90
>>> def plus2():
	first = int(input(" 첫 번째 수 : "))
	second = int(input(" 두 번째 수 : "))
	print(first, '+', second, '=', first + second)

>>> plus2()
	      
 첫 번째 수 : 30
 두 번째 수 : 60
30 + 60 = 90
>>> f = open("c:\dd\aa.txt")
	      
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    f = open("c:\dd\aa.txt")
OSError: [Errno 22] Invalid argument: 'c:\\dd\x07a.txt'
>>> f = open("c:\\dd\\aa.txt")
	      
>>> r = f.read()
	      
>>> print(r)
	      
경 기도 파주시
복 수동 리어카
궁 둥이 맴매
>>> f.close
	      
<built-in method close of _io.TextIOWrapper object at 0x021C4330>
>>> f.close()
	      
>>> f1 = open("c:\\dd\\name.txt", 'w')
	      
>>> f1.write('류현진\n")
	     
SyntaxError: EOL while scanning string literal
>>> f1.write('류현진\n')
	     
4
>>> f1.write('추신수\n')
	     
4
>>> f1.write('박병호\n')
	     
4
>>> f1.close()
	     
>>> type(20)
	     
<class 'int'>
>>> type(2.0)
	     
<class 'float'>
>>> type('aaa')
	     
<class 'str'>
>>> type("Boss")
	     
<class 'str'>
>>> 30
	     
30
>>> 20.45
	     
20.45
>>> "한국"
	     
'한국'
>>> a = False
	     
>>> a
	     
False
>>> type(a)
	     
<class 'bool'>
>>> b = [1,2,3]
	     
>>> type(b)
	     
<class 'list'>
>>> c = 1,2,3
	     
>>> type(c)
	     
<class 'tuple'>
>>> d = {1,2,3}
	     
>>> type(d)
	     
<class 'set'>
>>> e = {[1,2,3], (1,2,3), {1,2,3}}
	     
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    e = {[1,2,3], (1,2,3), {1,2,3}}
TypeError: unhashable type: 'list'
>>> e = [[1,2,3], (1,2,3), {1,2,3}]
	     
>>> e
	     
[[1, 2, 3], (1, 2, 3), {1, 2, 3}]
>>> type(e)
	     
<class 'list'>
>>> 
	     
>>> def where2():
	dong = input(" 무슨동에 사세요 : ")
	beon = input(" 몇 번 타고 오세요 : ")
	print("%c에서 %d번 타고 옵니다." % (dong, beon))

>>> where2
	     
<function where2 at 0x022272B8>
>>> where2()
	     
 무슨동에 사세요 : 휘경동
 몇 번 타고 오세요 : 272
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    where2()
  File "<pyshell#89>", line 4, in where2
    print("%c에서 %d번 타고 옵니다." % (dong, beon))
TypeError: %c requires int or char
>>> def where2():
	dong = input(" 무슨동에 사세요 : ")
	beon = input(" 몇 번 타고 오세요 : ")
	print("%c에서 %s번 타고 옵니다." % (dong, beon))

>>> where2()
	     
 무슨동에 사세요 : 휘경동
 몇 번 타고 오세요 : 272
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    where2()
  File "<pyshell#95>", line 4, in where2
    print("%c에서 %s번 타고 옵니다." % (dong, beon))
TypeError: %c requires int or char
>>> def where2():
	dong = input(" 무슨동에 사세요 : ")
	beon = input(" 몇 번 타고 오세요 : ")
	print("%s에서 %d번 타고 옵니다." % (dong, beon))

>>> where2()
	     
 무슨동에 사세요 : 휘경동
 몇 번 타고 오세요 : 272
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    where2()
  File "<pyshell#98>", line 4, in where2
    print("%s에서 %d번 타고 옵니다." % (dong, beon))
TypeError: %d format: a number is required, not str
>>> def where2():
	dong = input(" 무슨동에 사세요 : ")
	beon = input(" 몇 번 타고 오세요 : ")
	print("%s에서 %s번 타고 옵니다." % (dong, beon))

>>> where2()
	     
 무슨동에 사세요 : 휘경동
 몇 번 타고 오세요 : 272
휘경동에서 272번 타고 옵니다.
>>> t1 = bool(False)
	     
>>> print(t1)
	     
False
>>> t2 = bool(True)
	     
>>> t2
	     
True
>>> 2 * 10
	     
20
>>> 2 ** 10
	     
1024
>>> print("돌아이" *3)
	     
돌아이돌아이돌아이
>>> print("오바마" + 10)
	     
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    print("오바마" + 10)
TypeError: can only concatenate str (not "int") to str
>>> x = 30
	     
>>> y = 2/3
	     
>>> y = 2.3
	     
>>> z = "Korea"
	     
>>> print(x,y,z)
	     
30 2.3 Korea
>>> print("x = %d, y = %f, z = %s
	  
SyntaxError: EOL while scanning string literal
>>> print("x = %d, y = %f, z = %s" % (x, y, z))
	  
x = 30, y = 2.300000, z = Korea
>>> print("x = %5d, y = %5f, z = %5s" % (x, y, z))
	  
x =    30, y = 2.300000, z = Korea
>>> print("x = %-5d, y = %-5f, z = %-5s" % (x, y, z))
	  
x = 30   , y = 2.300000, z = Korea
>>> print("x =", x, "y =", y)
	  
x = 30 y = 2.3
>>> print("{} {} {}".format(x, y, z))
	  
30 2.3 Korea
>>> print("{0}, {1}, {2}".format(x, y, z))
	  
30, 2.3, Korea
>>> print("{2} {0} {2}".format(x, y, z))
	  
Korea 30 Korea
>>> a = input("입력 : ")
	  
입력 : Korea
>>> a
	  
'Korea'
>>> type(a)
	  
<class 'str'>
>>> b = int(input("정수입력 : "))
	  
정수입력 : 50
>>> b
	  
50
>>> type(b)
	  
<class 'int'>
>>> bb = "Boss"
	  
>>> type(bb)
	  
<class 'str'>
>>> bb = 20
	  
>>> type(bb)
	  
<class 'int'>
>>> bb = 4.7
	  
>>> type(bb)
	  
<class 'float'>
>>> a=100
	  
>>> b=200
	  
>>> c=100
	  
>>> id(a)
	  
1853607600
>>> id(b)
	  
1853609200
>>> id(c)
	  
1853607600
>>> a1 = 10
	  
>>> a2 = 20
	  
>>> 1a = 5
	  
SyntaxError: invalid syntax
>>> $t = 10
	  
SyntaxError: invalid syntax
>>> _a = 50
	  
>>> a_ = 60
	  
>>> 한글 = "변수"
	  
>>> print(한글)
	  
변수
>>> #a = 5
	  
>>> #은 주석. 프로그램에 영향 X
	  
>>> a.df
	  
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    a.df
AttributeError: 'int' object has no attribute 'df'
>>> print("[x = %5d] [y = %5f] [z = %5s]" % (x, y, z))
	  
[x =    30] [y = 2.300000] [z = Korea]
>>> print("{} {} {}".format(x, y, z))
	  
30 2.3 Korea
>>> print("[{:10}] [{:10}] [{:10}]".format(x, y, z))
	  
[        30] [       2.3] [Korea     ]
>>> print("[{0:10}] [{1:10}] [{2:10}]".format(x, y, z))
	  
[        30] [       2.3] [Korea     ]
>>> print("[{2:10}] [{0:10}] [{1:10}]".format(x, y, z))
	  
[Korea     ] [        30] [       2.3]
>>> print("[{2:<10}] [{0:1<0}] [{1:<10}]".format(x, y, z))
	  
[Korea     ] [30] [2.3       ]
>>> print("[{2:<10}] [{0:<10}] [{1:<10}]".format(x, y, z))
	  
[Korea     ] [30        ] [2.3       ]
>>> print("[{2:>10}] [{0:>10}] [{1:>10}]".format(x, y, z))
	  
[     Korea] [        30] [       2.3]
>>> print("[{2:^10}] [{0:^10}] [{1:^10}]".format(x, y, z))
	  
[  Korea   ] [    30    ] [   2.3    ]
>>> print("[{:.2f}] [{:10.2f}] [{:.1f}]".format(2.345, 2.345, 2.3456789))
	  
[2.35] [      2.35] [2.3]
>>> print(" python linux oracle mysql ")
	  
 python linux oracle mysql 
>>> print(" python \n linux \n oracle \n mysql ")
	  
 python 
 linux 
 oracle 
 mysql 
>>> print(" python \t linux \t oracle \t mysql ")
	  
 python 	 linux 	 oracle 	 mysql 
>>> print(" python linux \n oracle \a mysql ")
	  
 python linux 
 oracle  mysql 
>>> print(" python linux \\n oracle mysql ")
	  
 python linux \n oracle mysql 
>>> f = open("c:\\dd\\a3.txt", 'w')
	  
>>> f.write("이 정호의 이름은 \n 정 호다. \n 호 랑이 기운이 솟아난다.
	    
SyntaxError: EOL while scanning string literal
>>> f.write("이 정호의 이름은 \n 정 호다. \n 호 랑이 기운이 솟아난다.")
	    
34
>>> f.close()
	    
>>> f
	    
<_io.TextIOWrapper name='c:\\dd\\a3.txt' mode='w' encoding='cp949'>
>>> print(f)
	    
<_io.TextIOWrapper name='c:\\dd\\a3.txt' mode='w' encoding='cp949'>
>>> f = open("c:\\dd\\a3.txt", 'r')
	    
>>> f.read()
	    
'이 정호의 이름은 \n 정 호다. \n 호 랑이 기운이 솟아난다.'
>>> f = open("c:\\dd\\a3.txt", 'r')
	    
>>> f.read()
	    
'이 정호의 이름은 \n정 호다. \n호 랑이 기운이 솟아난다.'
>>> print(f)
	    
<_io.TextIOWrapper name='c:\\dd\\a3.txt' mode='r' encoding='cp949'>
>>> print(f.read())
	    

>>> f.read()
	    
''
>>> f = open("c:\\dd\\a3.txt", 'r')
	    
>>> print(f.read())
	    
이 정호의 이름은 
정 호다. 
호 랑이 기운이 솟아난다.
>>> f = open("c:\\dd\\b3.txt", 'w')
	    
>>> f.read()
	    
Traceback (most recent call last):
  File "<pyshell#184>", line 1, in <module>
    f.read()
io.UnsupportedOperation: not readable
>>> f = open("c:\\dd\\b3.txt", 'a')
	    
>>> f.write("파이썬")
	    
3
>>> f.read()
	    
Traceback (most recent call last):
  File "<pyshell#187>", line 1, in <module>
    f.read()
io.UnsupportedOperation: not readable
>>> f.close()
	    
>>> f = open("c:\\dd\\b3.txt", 'w')
	    
>>> f.write("재미있는 파이썬 공부")
	    
11
>>> f.close
	    
<built-in method close of _io.TextIOWrapper object at 0x021C4430>
>>> f.close()
	    
>>> f = open("c:\\dd\\b3.txt", 'a')
	    
>>> f.write("즐거운 파이썬 공부")
	    
10
>>> f.close()
	    
>>> f = open("c:\\dd\\b3.txt", 'a')
	    
>>> f.write("\n행복한 파이썬 공부")
	    
11
>>> f.close()
	    
>>> print("{}, {}, {}".format(x, y, z))
	    
30, 2.3, Korea
>>> bool(3>2)
	    
True
>>> bool('korea')
	    
True
>>> bool(-9)
	    
True
>>> bool([])
	    
False
>>> bool(0)
	    
False
>>> bool({})
	    
False
>>> a == 'a'
	    
False
>>> 5 != 2
	    
True
>>> 5 <> 5
	    
SyntaxError: invalid syntax
>>> a = 40
	    
>>> b = 3.14
	    
>>> c= "coke"
	    
>>> a.bit_length()
	    
6
>>> c.bit_length()
	    
Traceback (most recent call last):
  File "<pyshell#213>", line 1, in <module>
    c.bit_length()
AttributeError: 'str' object has no attribute 'bit_length'
>>> c.count()
	    
Traceback (most recent call last):
  File "<pyshell#214>", line 1, in <module>
    c.count()
TypeError: count() takes at least 1 argument (0 given)
>>> c.count
	    
<built-in method count of str object at 0x0222B800>
>>> c.count('c')
	    
1
>>> k = 'koreakoreakbs'
	    
>>> k.count('k')
	    
3
>>> min(1, 9, 5, 7, 6)
	    
1
>>> max(3, 4, 2, 5, 10)
	    
10
>>> sum(2, 5, 3, 6)
	    
Traceback (most recent call last):
  File "<pyshell#221>", line 1, in <module>
    sum(2, 5, 3, 6)
TypeError: sum expected at most 2 arguments, got 4
>>> a = [3, 4, 5, 2, 3]
	    
>>> sum(a)
	    
17
>>> dir()
	    
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', '__warningregistry__', '_a', 'a', 'a1', 'a2', 'a_', 'b', 'bb', 'c', 'd', 'e', 'f', 'f1', 'k', 'name', 'num', 'plus', 'plus2', 'r', 't1', 't2', 'were', 'where', 'where2', 'x', 'y', 'z', '한글']
>>> h = 'house'
	    
>>> p = 'peace'
	    
>>> r = 'rpw'
	    
>>> r = 'row'
	    
>>> dir()
	    
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', '__warningregistry__', '_a', 'a', 'a1', 'a2', 'a_', 'b', 'bb', 'c', 'd', 'e', 'f', 'f1', 'h', 'k', 'name', 'num', 'p', 'plus', 'plus2', 'r', 't1', 't2', 'were', 'where', 'where2', 'x', 'y', 'z', '한글']
>>> del r
	    
>>> del p
	    
>>> del h
	    
>>> dir()
	    
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', '__warningregistry__', '_a', 'a', 'a1', 'a2', 'a_', 'b', 'bb', 'c', 'd', 'e', 'f', 'f1', 'k', 'name', 'num', 'plus', 'plus2', 't1', 't2', 'were', 'where', 'where2', 'x', 'y', 'z', '한글']
>>> dir(__builtins__)
	    
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
>>> bin(100)
	    
'0b1100100'
>>> hex(100)
	    
'0x64'
>>> oct(100)
	    
'0o144'
>>> pow(2,5)
	    
32
>>> improt math
	    
SyntaxError: invalid syntax
>>> import math
	    
>>> pi
	    
Traceback (most recent call last):
  File "<pyshell#241>", line 1, in <module>
    pi
NameError: name 'pi' is not defined
>>> math.pi
	    
3.141592653589793
>>> import math as m
	    
>>> m.pi
	    
3.141592653589793
>>> m.cos(5)
	    
0.28366218546322625
>>> m.tan(90)
	    
-1.995200412208242
>>> m.e
	    
2.718281828459045
>>> m.log(m.e)
	    
1.0
>>> m.log(4,2)
	    
2.0
>>> log10(100)
	    
Traceback (most recent call last):
  File "<pyshell#250>", line 1, in <module>
    log10(100)
NameError: name 'log10' is not defined
>>> m.log10(100)
	    
2.0
>>> m.factorial(5)
	    
120
>>> import math as
	    
SyntaxError: invalid syntax
>>> asd
	    
Traceback (most recent call last):
  File "<pyshell#254>", line 1, in <module>
    asd
NameError: name 'asd' is not defined
>>> k = 0.05
	    
>>> print("%f" %(k))
	    
0.050000
>>> print("%20f" %(k))
	    
            0.050000
>>> print("%.2f" %(k))
	    
0.05
>>> print("%.15f" %(k))
	    
0.050000000000000
>>> a = 3+ 4j
	    
>>> b = 5 + 2j
	    
>>> a
	    
(3+4j)
>>> type(a)
	    
<class 'complex'>
>>> a.real
	    
3.0
>>> a.imag
	    
4.0
>>> a.conjugate()
	    
(3-4j)
>>> a+b
	    
(8+6j)
>>> a-b
	    
(-2+2j)
>>> a*b
	    
(7+26j)
>>> a/b
	    
(0.793103448275862+0.48275862068965514j)
>>> k = korea
	    
Traceback (most recent call last):
  File "<pyshell#271>", line 1, in <module>
    k = korea
NameError: name 'korea' is not defined
>>> k = 'korea'
	    
>>> k[0]
	    
'k'
>>> k[-1]
	    
'a'
>>> k.find('r')
	    
2
>>> k.find('g')
	    
-1
>>> k2 = k * 3
	    
>>> k2
	    
'koreakoreakorea'
>>> k2.count('or')
	    
3
>>> k2.startswitch('R')
	    
Traceback (most recent call last):
  File "<pyshell#280>", line 1, in <module>
    k2.startswitch('R')
AttributeError: 'str' object has no attribute 'startswitch'
>>> k2.startswitch('e')
	    
Traceback (most recent call last):
  File "<pyshell#281>", line 1, in <module>
    k2.startswitch('e')
AttributeError: 'str' object has no attribute 'startswitch'
>>> k2.startswitch('k')
	    
Traceback (most recent call last):
  File "<pyshell#282>", line 1, in <module>
    k2.startswitch('k')
AttributeError: 'str' object has no attribute 'startswitch'
>>> k2.upper()
	    
'KOREAKOREAKOREA'
>>> k3 = k2.upper()
	    
>>> k3.lower()
	    
'koreakoreakorea'
>>> len(k2)
	    
15
>>> len(k)
	    
5
>>> s = ' seoul '
	    
>>> len(s)
	    
7
>>> s.strip()
	    
'seoul'
>>> s.rstrip()
	    
' seoul'
>>> s.lastrip()
	    
Traceback (most recent call last):
  File "<pyshell#292>", line 1, in <module>
    s.lastrip()
AttributeError: 'str' object has no attribute 'lastrip'
>>> s.lstrip()
	    
'seoul '
>>> 'T'.isalpha()
	    
True
>>> '0'.isalpha()
	    
False
>>> '5'.isnumeric()
	    
True
>>> 'a'.isalnum()
	    
True
>>> '6'.isalnum()
	    
True
>>> '%'.isalnum()
	    
False
>>> for i in range(100):
	    SUM = SUM + 1.7

Traceback (most recent call last):
  File "<pyshell#302>", line 2, in <module>
    SUM = SUM + 1.7
NameError: name 'SUM' is not defined
>>> SUM = 0.0
	    
>>> for i in range(100):
	    SUM = SUM + 1.7

>>> SUM
	    
169.99999999999986
>>> s
	    
' seoul '
>>> s = s.strip()
	    
>>> s
	    
'seoul'
>>> s.replace('eou', 'a')
	    
'sal'
>>> s
	    
'seoul'
>>> s2 = s.split()
	    
>>> s2
	    
['seoul']
>>> len(s2)
	    
1
>>> s3 = "seoul,jeonju,jeju"
	    
>>> s4 = s3.split(',')
	    
>>> s4
	    
['seoul', 'jeonju', 'jeju']
>>> print("aa" "bb" "cc")
	    
aabbcc
>>> print("aa" "bb" "cc", sep=)
	    
SyntaxError: invalid syntax
>>> print("aa" "bb" "cc", sep=' ')
	    
aabbcc
>>> print("aa" "bb" "cc", sep=' ', end = '\n')
	    
aabbcc
>>> a = 'aa'
	    
>>> b = 'bb'
	    
>>> c = 'cc'
	    
>>> print(a,b,c)
	    
aa bb cc
>>> print(a,b,c end = '\t')
	    
SyntaxError: invalid syntax
>>> print("aa", end = '\t')
	    
aa	
>>> print("bb", end = '\n')
	    
bb
>>> abs(-1)
	    
1
>>> print(a,b,c, sep = ' ')
	    
aa bb cc
>>> a= [2, 3, 4, 0]
	    
>>> all(a)
	    
False
>>> any(a)
	    
True
>>> a = 50
	    
>>> a+5
	    
55
>>> a.__add__(5)
	    
55
>>> a
	    
50
>>> chr(65)
	    
'A'
>>> chr(66)
	    
'B'
>>> chr(48)
	    
'0'
>>> ord('A')
	    
65
>>> ord('d')
	    
100
>>> dir(a)
	    
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> '\uac00'
	    
'가'
>>> ord('히라가나 마')
	    
Traceback (most recent call last):
  File "<pyshell#345>", line 1, in <module>
    ord('히라가나 마')
TypeError: ord() expected a character, but string of length 6 found
>>> chr(55203)
	    
'힣'
>>> '\ud7a3'
	    
'힣'
>>> 
