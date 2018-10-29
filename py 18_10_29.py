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
>>> 
