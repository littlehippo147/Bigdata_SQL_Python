Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = input(" 이름 :
		 
SyntaxError: EOL while scanning string literal
>>> name = input(" 이름 : ")
		 
 이름 : 이정호
>>> year = int(input(" 생년 : "))
		 
 생년 : 1993
>>> age = 2018 - year - 1
		 
>>> print(name, "님은 ", age, "살")
		 
이정호 님은  24 살
>>> print("{}님은 {}살".format(name, age))
		 
이정호님은 24살
>>> age = 2018 - year + 1
		 
>>> print("{}님은 {}살".format(name, age))
		 
이정호님은 26살
>>> print("%s님은 %d살" % (name, age))
		 
이정호님은 26살
>>> for nation in '대한민국', '일본', '중국':
		 print(nation, end = ' ')

대한민국 일본 중국 
>>> for i in range(1,10)
		 
SyntaxError: invalid syntax
>>> for i in range(1,10):
		 print("{} * {} = {}".format(5, i, 5*i))

5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
>>> def gugu():
	dan = int(input(" 몇 단 : "))
	for i in range(1,10):
		 print("{} * {} = {}".format(dan, i, dan * i))

>>> gugu()
		 
 몇 단 : 
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    gugu()
  File "<pyshell#24>", line 2, in gugu
    dan = int(input(" 몇 단 : "))
ValueError: invalid literal for int() with base 10: ''
>>> gugu()
		 
 몇 단 : 4
4 * 1 = 4
4 * 2 = 8
4 * 3 = 12
4 * 4 = 16
4 * 5 = 20
4 * 6 = 24
4 * 7 = 28
4 * 8 = 32
4 * 9 = 36
>>> while True: # while문과 for문을 이용한 구구단
		 dan = int(input("몇 단 : "))
		 if dan == 0: # while문 루프 탈출을 위한 조건문
			 print("종료")
			 break
		 if dan < 2 or dan > 9:
			 print("범위를 벗어났습니다.")
			 continue
		 for i in range(1, 10):
			 print("{} X {} = {}".format(dan, i, dan * i))

몇 단 : 1
범위를 벗어났습니다.
몇 단 : 11
범위를 벗어났습니다.
몇 단 : 5
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
몇 단 : 3
3 X 1 = 3
3 X 2 = 6
3 X 3 = 9
3 X 4 = 12
3 X 5 = 15
3 X 6 = 18
3 X 7 = 21
3 X 8 = 24
3 X 9 = 27
몇 단 : 4
4 X 1 = 4
4 X 2 = 8
4 X 3 = 12
4 X 4 = 16
4 X 5 = 20
4 X 6 = 24
4 X 7 = 28
4 X 8 = 32
4 X 9 = 36
몇 단 : 0
종료
>>> def gugu2()
	while True: # while문과 for문을 이용한 구구단
		dan = int(input("몇 단 : "))
		if dan == 0: # while문 루프 탈출을 위한 조건문
			print("종료")
			break
		if dan < 2 or dan > 9:
			print("범위를 벗어났습니다.")
			continue
		for i in range(1, 10):
			print("{} X {} = {}".format(dan, i, dan * i))
		 
SyntaxError: invalid syntax
>>> def gugu2():
	while True: # while문과 for문을 이용한 구구단
		dan = int(input("몇 단 : "))
		if dan == 0: # while문 루프 탈출을 위한 조건문
			print("종료")
			break
		if dan < 2 or dan > 9:
			print("범위를 벗어났습니다.")
			continue
		for i in range(1, 10):
			print("{} X {} = {}".format(dan, i, dan * i))

>>> gugu2()
		 
몇 단 : 2
2 X 1 = 2
2 X 2 = 4
2 X 3 = 6
2 X 4 = 8
2 X 5 = 10
2 X 6 = 12
2 X 7 = 14
2 X 8 = 16
2 X 9 = 18
몇 단 : 3
3 X 1 = 3
3 X 2 = 6
3 X 3 = 9
3 X 4 = 12
3 X 5 = 15
3 X 6 = 18
3 X 7 = 21
3 X 8 = 24
3 X 9 = 27
몇 단 : 0
종료
>>> for j in range(3): # 구구단 3번만 출력하기
	dan = int(input("몇 단 : "))

	
몇 단 : 2
몇 단 : 1
몇 단 : 2
>>> for j in range(3): # 구구단 3번만 출력하기
	dan = int(input("몇 단 : "))

		
몇 단 : 0
몇 단 : 0
몇 단 : 0
>>> for j in range(3): # 구구단 3번만 출력하기
	dan = int(input("몇 단 : "))
	for i in (1, 10)
		 
SyntaxError: invalid syntax
>>> for j in range(3): # 구구단 3번만 출력하기
	dan = int(input("몇 단 : "))
	for i in (1, 10):
		 print("{} * {} = {}".format(dan, i, dan * i))

몇 단 : 4
4 * 1 = 4
4 * 10 = 40
몇 단 : 5
5 * 1 = 5
5 * 10 = 50
몇 단 : 6
6 * 1 = 6
6 * 10 = 60
>>> for j in range(3): # 구구단 3번만 출력하기
	dan = int(input("몇 단 : "))
	for i in range(1, 10):
		 print("{} * {} = {}".format(dan, i, dan * i))

	
몇 단 : 4
4 * 1 = 4
4 * 2 = 8
4 * 3 = 12
4 * 4 = 16
4 * 5 = 20
4 * 6 = 24
4 * 7 = 28
4 * 8 = 32
4 * 9 = 36
몇 단 : 5
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
몇 단 : 6
6 * 1 = 6
6 * 2 = 12
6 * 3 = 18
6 * 4 = 24
6 * 5 = 30
6 * 6 = 36
6 * 7 = 42
6 * 8 = 48
6 * 9 = 54
>>> for i in range(2, 10):
		print(" *** ", i, " 단 ***")
		for j in range(1, 10):
			print("{} * {} = {}".format(i, j, i * j)
		print() # 공백 한 줄
			      
SyntaxError: invalid syntax
>>> for i in range(2, 10):
		print(" *** ", i, " 단 ***")
		for j in range(1, 10):
			print("{} * {} = {}".format(i, j, i * j))
			
		print() # 공백 한 줄

 ***  2  단 ***
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18

 ***  3  단 ***
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18
3 * 7 = 21
3 * 8 = 24
3 * 9 = 27

 ***  4  단 ***
4 * 1 = 4
4 * 2 = 8
4 * 3 = 12
4 * 4 = 16
4 * 5 = 20
4 * 6 = 24
4 * 7 = 28
4 * 8 = 32
4 * 9 = 36

 ***  5  단 ***
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45

 ***  6  단 ***
6 * 1 = 6
6 * 2 = 12
6 * 3 = 18
6 * 4 = 24
6 * 5 = 30
6 * 6 = 36
6 * 7 = 42
6 * 8 = 48
6 * 9 = 54

 ***  7  단 ***
7 * 1 = 7
7 * 2 = 14
7 * 3 = 21
7 * 4 = 28
7 * 5 = 35
7 * 6 = 42
7 * 7 = 49
7 * 8 = 56
7 * 9 = 63

 ***  8  단 ***
8 * 1 = 8
8 * 2 = 16
8 * 3 = 24
8 * 4 = 32
8 * 5 = 40
8 * 6 = 48
8 * 7 = 56
8 * 8 = 64
8 * 9 = 72

 ***  9  단 ***
9 * 1 = 9
9 * 2 = 18
9 * 3 = 27
9 * 4 = 36
9 * 5 = 45
9 * 6 = 54
9 * 7 = 63
9 * 8 = 72
9 * 9 = 81

>>> Sum = 0
			      
>>> for i in range(1, 11):
	Sum = Sum + i
	print("i ==> {}, Sum = {}".format(i, Sum))

i ==> 1, Sum = 1
i ==> 2, Sum = 3
i ==> 3, Sum = 6
i ==> 4, Sum = 10
i ==> 5, Sum = 15
i ==> 6, Sum = 21
i ==> 7, Sum = 28
i ==> 8, Sum = 36
i ==> 9, Sum = 45
i ==> 10, Sum = 55
>>> for i in range(1, 11):
	Sum += i
	print("i ==> {}, Sum = {}".format(i, Sum))

i ==> 1, Sum = 56
i ==> 2, Sum = 58
i ==> 3, Sum = 61
i ==> 4, Sum = 65
i ==> 5, Sum = 70
i ==> 6, Sum = 76
i ==> 7, Sum = 83
i ==> 8, Sum = 91
i ==> 9, Sum = 100
i ==> 10, Sum = 110
>>> Sum = 0
			      
>>> for i in range(1, 11):
	Sum += i # Sum = Sum + i 와 같은 표현
	print("i ==> {}, Sum = {}".format(i, Sum))

i ==> 1, Sum = 1
i ==> 2, Sum = 3
i ==> 3, Sum = 6
i ==> 4, Sum = 10
i ==> 5, Sum = 15
i ==> 6, Sum = 21
i ==> 7, Sum = 28
i ==> 8, Sum = 36
i ==> 9, Sum = 45
i ==> 10, Sum = 55
>>> for i in range(1, 11):
	Sum += i # Sum = Sum + i 와 같은 표현
	print("i ==> {:4d}, Sum = {:4d}".format(i, Sum))

i ==>    1, Sum =   56
i ==>    2, Sum =   58
i ==>    3, Sum =   61
i ==>    4, Sum =   65
i ==>    5, Sum =   70
i ==>    6, Sum =   76
i ==>    7, Sum =   83
i ==>    8, Sum =   91
i ==>    9, Sum =  100
i ==>   10, Sum =  110
>>> for i in range(1, 101):
	Sum += i # Sum = Sum + i 와 같은 표현
	print("i ==> {:4d}, Sum = {:4d}".format(i, Sum))
	# :4d 4칸 확보 우측 정렬

i ==>    1, Sum =  111
i ==>    2, Sum =  113
i ==>    3, Sum =  116
i ==>    4, Sum =  120
i ==>    5, Sum =  125
i ==>    6, Sum =  131
i ==>    7, Sum =  138
i ==>    8, Sum =  146
i ==>    9, Sum =  155
i ==>   10, Sum =  165
i ==>   11, Sum =  176
i ==>   12, Sum =  188
i ==>   13, Sum =  201
i ==>   14, Sum =  215
i ==>   15, Sum =  230
i ==>   16, Sum =  246
i ==>   17, Sum =  263
i ==>   18, Sum =  281
i ==>   19, Sum =  300
i ==>   20, Sum =  320
i ==>   21, Sum =  341
i ==>   22, Sum =  363
i ==>   23, Sum =  386
i ==>   24, Sum =  410
i ==>   25, Sum =  435
i ==>   26, Sum =  461
i ==>   27, Sum =  488
i ==>   28, Sum =  516
i ==>   29, Sum =  545
i ==>   30, Sum =  575
i ==>   31, Sum =  606
i ==>   32, Sum =  638
i ==>   33, Sum =  671
i ==>   34, Sum =  705
i ==>   35, Sum =  740
i ==>   36, Sum =  776
i ==>   37, Sum =  813
i ==>   38, Sum =  851
i ==>   39, Sum =  890
i ==>   40, Sum =  930
i ==>   41, Sum =  971
i ==>   42, Sum = 1013
i ==>   43, Sum = 1056
i ==>   44, Sum = 1100
i ==>   45, Sum = 1145
i ==>   46, Sum = 1191
i ==>   47, Sum = 1238
i ==>   48, Sum = 1286
i ==>   49, Sum = 1335
i ==>   50, Sum = 1385
i ==>   51, Sum = 1436
i ==>   52, Sum = 1488
i ==>   53, Sum = 1541
i ==>   54, Sum = 1595
i ==>   55, Sum = 1650
i ==>   56, Sum = 1706
i ==>   57, Sum = 1763
i ==>   58, Sum = 1821
i ==>   59, Sum = 1880
i ==>   60, Sum = 1940
i ==>   61, Sum = 2001
i ==>   62, Sum = 2063
i ==>   63, Sum = 2126
i ==>   64, Sum = 2190
i ==>   65, Sum = 2255
i ==>   66, Sum = 2321
i ==>   67, Sum = 2388
i ==>   68, Sum = 2456
i ==>   69, Sum = 2525
i ==>   70, Sum = 2595
i ==>   71, Sum = 2666
i ==>   72, Sum = 2738
i ==>   73, Sum = 2811
i ==>   74, Sum = 2885
i ==>   75, Sum = 2960
i ==>   76, Sum = 3036
i ==>   77, Sum = 3113
i ==>   78, Sum = 3191
i ==>   79, Sum = 3270
i ==>   80, Sum = 3350
i ==>   81, Sum = 3431
i ==>   82, Sum = 3513
i ==>   83, Sum = 3596
i ==>   84, Sum = 3680
i ==>   85, Sum = 3765
i ==>   86, Sum = 3851
i ==>   87, Sum = 3938
i ==>   88, Sum = 4026
i ==>   89, Sum = 4115
i ==>   90, Sum = 4205
i ==>   91, Sum = 4296
i ==>   92, Sum = 4388
i ==>   93, Sum = 4481
i ==>   94, Sum = 4575
i ==>   95, Sum = 4670
i ==>   96, Sum = 4766
i ==>   97, Sum = 4863
i ==>   98, Sum = 4961
i ==>   99, Sum = 5060
i ==>  100, Sum = 5160
>>> Sum = 0
			      
>>> for i in range(1, 101):
	Sum += i # Sum = Sum + i 와 같은 표현
	print("i ==> {:4d}, Sum = {:4d}".format(i, Sum))
	# :4d 4칸 확보 우측 정렬

i ==>    1, Sum =    1
i ==>    2, Sum =    3
i ==>    3, Sum =    6
i ==>    4, Sum =   10
i ==>    5, Sum =   15
i ==>    6, Sum =   21
i ==>    7, Sum =   28
i ==>    8, Sum =   36
i ==>    9, Sum =   45
i ==>   10, Sum =   55
i ==>   11, Sum =   66
i ==>   12, Sum =   78
i ==>   13, Sum =   91
i ==>   14, Sum =  105
i ==>   15, Sum =  120
i ==>   16, Sum =  136
i ==>   17, Sum =  153
i ==>   18, Sum =  171
i ==>   19, Sum =  190
i ==>   20, Sum =  210
i ==>   21, Sum =  231
i ==>   22, Sum =  253
i ==>   23, Sum =  276
i ==>   24, Sum =  300
i ==>   25, Sum =  325
i ==>   26, Sum =  351
i ==>   27, Sum =  378
i ==>   28, Sum =  406
i ==>   29, Sum =  435
i ==>   30, Sum =  465
i ==>   31, Sum =  496
i ==>   32, Sum =  528
i ==>   33, Sum =  561
i ==>   34, Sum =  595
i ==>   35, Sum =  630
i ==>   36, Sum =  666
i ==>   37, Sum =  703
i ==>   38, Sum =  741
i ==>   39, Sum =  780
i ==>   40, Sum =  820
i ==>   41, Sum =  861
i ==>   42, Sum =  903
i ==>   43, Sum =  946
i ==>   44, Sum =  990
i ==>   45, Sum = 1035
i ==>   46, Sum = 1081
i ==>   47, Sum = 1128
i ==>   48, Sum = 1176
i ==>   49, Sum = 1225
i ==>   50, Sum = 1275
i ==>   51, Sum = 1326
i ==>   52, Sum = 1378
i ==>   53, Sum = 1431
i ==>   54, Sum = 1485
i ==>   55, Sum = 1540
i ==>   56, Sum = 1596
i ==>   57, Sum = 1653
i ==>   58, Sum = 1711
i ==>   59, Sum = 1770
i ==>   60, Sum = 1830
i ==>   61, Sum = 1891
i ==>   62, Sum = 1953
i ==>   63, Sum = 2016
i ==>   64, Sum = 2080
i ==>   65, Sum = 2145
i ==>   66, Sum = 2211
i ==>   67, Sum = 2278
i ==>   68, Sum = 2346
i ==>   69, Sum = 2415
i ==>   70, Sum = 2485
i ==>   71, Sum = 2556
i ==>   72, Sum = 2628
i ==>   73, Sum = 2701
i ==>   74, Sum = 2775
i ==>   75, Sum = 2850
i ==>   76, Sum = 2926
i ==>   77, Sum = 3003
i ==>   78, Sum = 3081
i ==>   79, Sum = 3160
i ==>   80, Sum = 3240
i ==>   81, Sum = 3321
i ==>   82, Sum = 3403
i ==>   83, Sum = 3486
i ==>   84, Sum = 3570
i ==>   85, Sum = 3655
i ==>   86, Sum = 3741
i ==>   87, Sum = 3828
i ==>   88, Sum = 3916
i ==>   89, Sum = 4005
i ==>   90, Sum = 4095
i ==>   91, Sum = 4186
i ==>   92, Sum = 4278
i ==>   93, Sum = 4371
i ==>   94, Sum = 4465
i ==>   95, Sum = 4560
i ==>   96, Sum = 4656
i ==>   97, Sum = 4753
i ==>   98, Sum = 4851
i ==>   99, Sum = 4950
i ==>  100, Sum = 5050
>>> def cum_sum():
	csum = 0
	start = int(input("시작 > "))
	end = int(input("끝 > "))
	for i in range(start, end + 1):
		csum += i 
	print(csum)

>>> cum_sum()
			      
시작 > 5
끝 > 10
45
>>> def cum_sum():
	csum = 0
	start = int(input("시작 > "))
	end = int(input("끝 > "))
	if start >= end:
		for i in range(start, end + 1):
			csum += i
	if start < end:
		for i in range(end, start + 1):
			csum += i
	print(csum)

>>> cum_sum()
			      
시작 > 10
끝 > 5
0
>>> def cum_sum():
	csum = 0
	start = int(input("시작 > "))
	end = int(input("끝 > "))
	if start <= end:
		for i in range(start, end + 1):
			csum += i
	if start > end:
		for i in range(end, start + 1):
			csum += i
	print(csum)

>>> cum_sum()
			      
시작 > 10
끝 > 5
45
>>> rang(5,1)
			      
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    rang(5,1)
NameError: name 'rang' is not defined
>>> range(5,1)
			      
range(5, 1)
>>> for i in range(5,1):
	print(i)

>>> for i in range(5,1,-1):
	print(i)

5
4
3
2
>>> 
def cum_sum2():
	while True:
		if start < 0 or end < 0:
			      break
		csum = 0
		start = int(input("시작 > "))
		end = int(input("끝 > "))
		if start <= end:
			for i in range(start, end + 1):
				csum += i
		if start > end:
			for i in range(end, start + 1):
				csum += i
		print(csum)

>>> cum_sum2()
			      
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    cum_sum2()
  File "<pyshell#102>", line 4, in cum_sum2
    if start < 0 or end < 0:
UnboundLocalError: local variable 'start' referenced before assignment
>>> def cum_sum2():
	while True:
		csum = 0
		start = int(input("시작 > "))
		end = int(input("끝 > "))
		if start < 0 or end < 0:
			      break
		if start <= end:
			for i in range(start, end + 1):
				csum += i
		if start > end:
			for i in range(end, start + 1):
				csum += i
		print(csum)

>>> cum_sum2()
			      
시작 > 2
끝 > 5
14
시작 > 1
끝 > 10
55
시작 > 10
끝 > 1
55
시작 > 5
끝 > -5
>>> for i in range(10):
			      if i == 3:
				      continue
			      print(" i ==> {} ".format(i))

 i ==> 0 
 i ==> 1 
 i ==> 2 
 i ==> 4 
 i ==> 5 
 i ==> 6 
 i ==> 7 
 i ==> 8 
 i ==> 9 
>>> # continue 는 skip
			      
>>> while i <= 10:
			      Sum += i
			      i += 1
			      print("i ==> {} Sum ==> {}".format(i. Sum))

Traceback (most recent call last):
  File "<pyshell#117>", line 4, in <module>
    print("i ==> {} Sum ==> {}".format(i. Sum))
AttributeError: 'int' object has no attribute 'Sum'
>>> Sum = 0
			      
>>> i = 0
			      
>>> while i <= 10:
			      Sum += i
			      i += 1
			      print("i ==> {} Sum ==> {}".format(i, Sum))

i ==> 1 Sum ==> 0
i ==> 2 Sum ==> 1
i ==> 3 Sum ==> 3
i ==> 4 Sum ==> 6
i ==> 5 Sum ==> 10
i ==> 6 Sum ==> 15
i ==> 7 Sum ==> 21
i ==> 8 Sum ==> 28
i ==> 9 Sum ==> 36
i ==> 10 Sum ==> 45
i ==> 11 Sum ==> 55
>>> while True:
	name = input(" 이름 : ")
	if name == "이정호":
		print(" {} 님 반갑습니다.".format(name))
		break

 이름 : 이종호
 이름 : 이중호
 이름 : 이장호
 이름 : 이강호
 이름 : 이정호
 이정호 님 반갑습니다.
>>> import random as rd
			      
>>> rd.random()
			      
0.732318817940642
>>> rd.random(1,10)
			      
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    rd.random(1,10)
TypeError: random() takes no arguments (2 given)
>>> rd.random(10)
			      
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    rd.random(10)
TypeError: random() takes no arguments (1 given)
>>> rd.random()
			      
0.9717020958324559
>>> rd.randint(1, 100)
			      
80
>>> rd.randint(1, 100)
			      
7
>>> rd.randint(1, 100)
			      
46
>>> rd.randint(1, 100)
			      
33
>>> 
			      
>>> 
			      
>>> rd.randint(1, 100)
			      
84
>>> rd.randint(1, 100)
			      
85
>>> rd.randint(1, 100)
			      
77
>>> def pick_num():
	import random as rd

	random_number = rd.randinit(1,100)
	cnt = 0

	while True:		      
		pick = int(input("1 ~ 100 중에 고르세요"))
		cnt += 1
		if pick == random_number:
			print("{}번 만에 맞추셨습니다!".format(cnt))
			break

		if pick > random_number:
			print("{} 보다는 작습니다!".format(pick))
		if pick
			      
SyntaxError: invalid syntax
>>> def pick_num():
	import random as rd

	random_number = rd.randinit(1,100)
	cnt = 0

	while True:
		pick = int(input("1 ~ 100 중에 고르세요"))
		cnt += 1
		if pick == random_number:
			print("{}번 만에 맞추셨습니다!".format(cnt))
			break

		elif pick > random_number:
			print("{} 보다는 작습니다!".format(pick))

		else:
			print("{} 보다는 큰 것 같습니다!".format(pick))

>>> pick_num()
			      
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    pick_num()
  File "<pyshell#160>", line 4, in pick_num
    random_number = rd.randinit(1,100)
AttributeError: module 'random' has no attribute 'randinit'
>>> def pick_num():
	import random as rd

	random_number = rd.randint(1,100)
	cnt = 0

	while True:
		pick = int(input("1 ~ 100 중에 고르세요"))
		cnt += 1
		if pick == random_number:
			print("{}번 만에 맞추셨습니다!".format(cnt))
			break

		elif pick > random_number:
			print("{} 보다는 작습니다!".format(pick))

		else:
			print("{} 보다는 큰 것 같습니다!".format(pick))

>>> pick_num()
			      
1 ~ 100 중에 고르세요1
1 보다는 큰 것 같습니다!
1 ~ 100 중에 고르세요5
5 보다는 큰 것 같습니다!
1 ~ 100 중에 고르세요50
50 보다는 큰 것 같습니다!
1 ~ 100 중에 고르세요75
75 보다는 작습니다!
1 ~ 100 중에 고르세요66
66 보다는 작습니다!
1 ~ 100 중에 고르세요60
60 보다는 큰 것 같습니다!
1 ~ 100 중에 고르세요63
63 보다는 큰 것 같습니다!
1 ~ 100 중에 고르세요64
8번 만에 맞추셨습니다!
>>> def pick_num():
	import random as rd

	random_number = rd.randint(1,100)
	cnt = 0
	print("1 ~ 100 중에 고르세요!")
	
	while True:
		pick = int(input("Pick > "))
		cnt += 1
		if pick == random_number:
			print("{}번 만에 맞추셨습니다!".format(cnt))
			break

		elif pick > random_number:
			print("{} 보다는 작습니다!".format(pick))

		else:
			print("{} 보다는 큰 것 같습니다!".format(pick))

>>> pick_num()
			      
1 ~ 100 중에 고르세요!
Pick > 50
50 보다는 작습니다!
Pick > 25
25 보다는 작습니다!
Pick > 13
13 보다는 작습니다!
Pick > 6
6 보다는 작습니다!
Pick > 3
3 보다는 작습니다!
Pick > 2
2 보다는 작습니다!
Pick > 1
7번 만에 맞추셨습니다!
>>> score = int(input("점수 입력 > "))
			      
점수 입력 > 60
>>> if score >= 90:
			print(score, "점 ===> 수")
elif score >= 80:
			print(score, "점 ===> 우")
elif score >= 70:
			print(score, "점 ===> 미")
elif score >= 60:
			print(score, "점 ===> 양")
else:
			print(score, "점 ===> 가")

60 점 ===> 양
>>> while True:
	score = int(input("점수 입력 > "))
	if score = -1:
				break
	
	if score >= 90:
				print(score, "점 ===> 수")
	elif score >= 80:
				print(score, "점 ===> 우")
	elif score >= 70:
				print(score, "점 ===> 미")
	elif score >= 60:
				print(score, "점 ===> 양")
	else:
				print(score, "점 ===> 노오오오력을 해야지")
			      
SyntaxError: invalid syntax
>>> while True:
	score = int(input("점수 입력 > "))
	if score == -1:
				break

	if score >= 90:
				print(score, "점 ===> 수")
	elif score >= 80:
				print(score, "점 ===> 우")
	elif score >= 70:
				print(score, "점 ===> 미")
	elif score >= 60:
				print(score, "점 ===> 양")
	else:
				print(score, "점 ===> 노오오오력을 해야지")

점수 입력 > 50
50 점 ===> 노오오오력을 해야지
점수 입력 > 60
60 점 ===> 양
점수 입력 > 75
75 점 ===> 미
점수 입력 > 88
88 점 ===> 우
점수 입력 > 92
92 점 ===> 수
점수 입력 > -1
>>> 
while True:
	score = int(input("점수 입력 > "))
	if score > 100 or score < -1:
			print("제대로 된 점수를 입력해주세요.")
			continue
	if score == -1:
			break

	if score >= 90:
			print(score, "점 ===> 수")
	elif score >= 80:
			print(score, "점 ===> 우")
	elif score >= 70:
			print(score, "점 ===> 미")
	elif score >= 60:
			print(score, "점 ===> 양")
	else:
			print(score, "점 ===> 노오오오력을 해야지")

점수 입력 > 121
제대로 된 점수를 입력해주세요.
점수 입력 > -2
제대로 된 점수를 입력해주세요.
점수 입력 > 100
100 점 ===> 수
점수 입력 > 90
90 점 ===> 수
점수 입력 > 88
88 점 ===> 우
점수 입력 > 75
75 점 ===> 미
점수 입력 > 61
61 점 ===> 양
점수 입력 > 55
55 점 ===> 노오오오력을 해야지
점수 입력 > 30
30 점 ===> 노오오오력을 해야지
점수 입력 > 1
1 점 ===> 노오오오력을 해야지
점수 입력 > 0
0 점 ===> 노오오오력을 해야지
점수 입력 > -1
>>> a = []
			      
>>> with open("c:\\dd\\ss.txt", 'r') as f:
	for i in range(10):
		a.append(f.readline().split())

>>> a
			      
[['이순신', '85', '80', '90'], ['강감찬', '75', '80', '95'], ['한석봉', '99', '99', '99'], ['황진이', '35', '45', '20'], ['안중근', '90', '85', '90'], ['박문수', '95', '95', '95'], ['임꺽정', '15', '35', '45'], ['김정호', '90', '95', '80'], ['정몽주', '90', '90', '95'], ['이정호', '50', '45', '60']]
>>> a.ix[:,1:4]
			      
Traceback (most recent call last):
  File "<pyshell#187>", line 1, in <module>
    a.ix[:,1:4]
AttributeError: 'list' object has no attribute 'ix'
>>> a[:, :]
			      
Traceback (most recent call last):
  File "<pyshell#188>", line 1, in <module>
    a[:, :]
TypeError: list indices must be integers or slices, not tuple
>>> for i in range(len(a)):
	for j in range(1,4):
		a[i][j] = int(a[i][j])
	a[i].append(sum(a[i][1:4])
	a[i].append(a[i][4] / 3)
		    
SyntaxError: invalid syntax
>>> for i in range(len(a)):
	for j in range(1,3):
		a[i][j] = int(a[i][j])
	a[i].append(sum(a[i][1:4])
	a[i].append(a[i][4] / 3)
		    
SyntaxError: invalid syntax
>>> for i in range(len(a)):
	for j in range(1,3):
		a[i][j] = int(a[i][j])

>>> a = []
		    
>>> with open("c:\\dd\\ss.txt", 'r') as f:
	for i in range(10):
		a.append(f.readline().split())

>>> a
		    
[['이순신', '85', '80', '90'], ['강감찬', '75', '80', '95'], ['한석봉', '99', '99', '99'], ['황진이', '35', '45', '20'], ['안중근', '90', '85', '90'], ['박문수', '95', '95', '95'], ['임꺽정', '15', '35', '45'], ['김정호', '90', '95', '80'], ['정몽주', '90', '90', '95'], ['이정호', '50', '45', '60']]
>>> for i in range(len(a)):
	for j in range(1,3):
		a[i][j] = int(a[i][j])
	a[i].append(sum(a[i][1:4]))
	a[i].append(a[i][4] / 3)

Traceback (most recent call last):
  File "<pyshell#204>", line 4, in <module>
    a[i].append(sum(a[i][1:4]))
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> for i in range(len(a)):
	for j in range(1,4):
		a[i][j] = int(a[i][j])
	a[i].append(sum(a[i][1:4]))
	a[i].append(a[i][4] / 3)

>>> a
		    
[['이순신', 85, 80, 90, 255, 85.0], ['강감찬', 75, 80, 95, 250, 83.33333333333333], ['한석봉', 99, 99, 99, 297, 99.0], ['황진이', 35, 45, 20, 100, 33.333333333333336], ['안중근', 90, 85, 90, 265, 88.33333333333333], ['박문수', 95, 95, 95, 285, 95.0], ['임꺽정', 15, 35, 45, 95, 31.666666666666668], ['김정호', 90, 95, 80, 265, 88.33333333333333], ['정몽주', 90, 90, 95, 275, 91.66666666666667], ['이정호', 50, 45, 60, 155, 51.666666666666664]]
>>> a = []
		    
>>> with open("c:\\dd\\ss.txt", 'r') as f:
	for i in range(10):
		a.append(f.readline().split())

>>> for i in range(len(a)):
	for j in range(1,4):
		a[i][j] = int(a[i][j])
	a[i].append(sum(a[i][1:4]))
	a[i].append(round((a[i][4] / 3), 2))

>>> a
		    
[['이순신', 85, 80, 90, 255, 85.0], ['강감찬', 75, 80, 95, 250, 83.33], ['한석봉', 99, 99, 99, 297, 99.0], ['황진이', 35, 45, 20, 100, 33.33], ['안중근', 90, 85, 90, 265, 88.33], ['박문수', 95, 95, 95, 285, 95.0], ['임꺽정', 15, 35, 45, 95, 31.67], ['김정호', 90, 95, 80, 265, 88.33], ['정몽주', 90, 90, 95, 275, 91.67], ['이정호', 50, 45, 60, 155, 51.67]]
>>> avg
		    
Traceback (most recent call last):
  File "<pyshell#214>", line 1, in <module>
    avg
NameError: name 'avg' is not defined
>>> for i in range(len(a)):
	print(" {} {} {} [
	      
SyntaxError: EOL while scanning string literal
>>> for i in range(len(a)):
	print(" {} {} {} {} {:3d} {:.2f}".format(a[i][0], a[i][1], a[i][2], a[i][3], a[i][4], a[i][5]))

 이순신 85 80 90 255 85.00
 강감찬 75 80 95 250 83.33
 한석봉 99 99 99 297 99.00
 황진이 35 45 20 100 33.33
 안중근 90 85 90 265 88.33
 박문수 95 95 95 285 95.00
 임꺽정 15 35 45  95 31.67
 김정호 90 95 80 265 88.33
 정몽주 90 90 95 275 91.67
 이정호 50 45 60 155 51.67
>>> korT = 0
	      
>>> engT = 0
	      
>>> matT = 0
	      
>>> for i in len(a):
	korT += a[i][1]
	engT += a[i][2]
	matT += a[i][3]

Traceback (most recent call last):
  File "<pyshell#226>", line 1, in <module>
    for i in len(a):
TypeError: 'int' object is not iterable
>>> for i in range(len(a)):
	korT += a[i][1]
	engT += a[i][2]
	matT += a[i][3]

>>> korA = korT / len(a)
	      
>>> engA = engT / len(a)
	      
>>> matA = matT / len(a)
	      
>>> everyT = korT + engT + matT
	      
>>> everyA = everyT / (3 * len(a))
	      
>>> print(" ******************* 성 적 표 ******************* ")
	      
 ******************* 성 적 표 ******************* 
>>> print(" ******************* 성 적 표 ******************* "):
	      
SyntaxError: invalid syntax
>>> print(" ******************* 성 적 표 ******************* ")
	      
 ******************* 성 적 표 ******************* 
>>> print(" **************** 성 적 표 **************** ")
print(" ****************************************** ")
print("  이 름   국어   영어   수학   총점   평균  ")
print(" ****************************************** ")

for i in range(len(a)):
	print(" {} {:5d} {:5d} {:5d} {:5d} {:7.2f} "
              .format(a[i][0], a[i][1], a[i][2], a[i][3], a[i][4], a[i][5]))

print(" ***************************************** ")
print(" 총평균 {:5.1f} {:5.1f} {:5.1f} {:5.1f} {:7.1f} "
      .format(korA, engA, matA, everyT, everyA))
	      
SyntaxError: multiple statements found while compiling a single statement
>>> 
=============== RESTART: C:/Users/user/Documents/Python/aa.py ===============
 **************** 성 적 표 **************** 
 ****************************************** 
  이 름   국어   영어   수학   총점   평균  
 ****************************************** 
Traceback (most recent call last):
  File "C:/Users/user/Documents/Python/aa.py", line 6, in <module>
    for i in range(len(a)):
NameError: name 'a' is not defined
>>> 
=============== RESTART: C:/Users/user/Documents/Python/aa.py ===============
 **************** 성 적 표 **************** 
 ****************************************** 
  이 름   국어   영어   수학   총점   평균  
 ****************************************** 
 이순신    85    80    90   255   85.00 
 강감찬    75    80    95   250   83.33 
 한석봉    99    99    99   297   99.00 
 황진이    35    45    20   100   33.33 
 안중근    90    85    90   265   88.33 
 박문수    95    95    95   285   95.00 
 임꺽정    15    35    45    95   31.67 
 김정호    90    95    80   265   88.33 
 정몽주    90    90    95   275   91.67 
 이정호    50    45    60   155   51.67 
 ***************************************** 
 총평균  72.4  74.9  76.9 2242.0    74.7 
>>> 
=============== RESTART: C:/Users/user/Documents/Python/aa.py ===============
 *************** 성 적 표 ************** 
 *************************************** 
  이 름  국어  영어  수학  총점  평균  
 *************************************** 
 이순신    85    80    90   255   85.00 
 강감찬    75    80    95   250   83.33 
 한석봉    99    99    99   297   99.00 
 황진이    35    45    20   100   33.33 
 안중근    90    85    90   265   88.33 
 박문수    95    95    95   285   95.00 
 임꺽정    15    35    45    95   31.67 
 김정호    90    95    80   265   88.33 
 정몽주    90    90    95   275   91.67 
 이정호    50    45    60   155   51.67 
 ************************************** 
 총평균  72.4  74.9  76.9 2242.0    74.7 
>>> 
=============== RESTART: C:/Users/user/Documents/Python/aa.py ===============
 *************** 성 적 표 ************** 
 *************************************** 
  이 름  국어  영어  수학  총점    평균  
 *************************************** 
 이순신    85    80    90   255   85.00 
 강감찬    75    80    95   250   83.33 
 한석봉    99    99    99   297   99.00 
 황진이    35    45    20   100   33.33 
 안중근    90    85    90   265   88.33 
 박문수    95    95    95   285   95.00 
 임꺽정    15    35    45    95   31.67 
 김정호    90    95    80   265   88.33 
 정몽주    90    90    95   275   91.67 
 이정호    50    45    60   155   51.67 
 ************************************** 
 총평균  72.4  74.9  76.9 2242.0    74.7 
>>> 
=============== RESTART: C:/Users/user/Documents/Python/aa.py ===============
 *************** 성 적 표 ************** 
 *************************************** 
  이 름  국어  영어  수학  총점    평균  
 *************************************** 
 이순신    85    80    90   255   85.00 
 강감찬    75    80    95   250   83.33 
 한석봉    99    99    99   297   99.00 
 황진이    35    45    20   100   33.33 
 안중근    90    85    90   265   88.33 
 박문수    95    95    95   285   95.00 
 임꺽정    15    35    45    95   31.67 
 김정호    90    95    80   265   88.33 
 정몽주    90    90    95   275   91.67 
 이정호    50    45    60   155   51.67 
 ************************************** 
 총평균  72.4  74.9  76.9 2242.0  74.7 
>>> 
=============== RESTART: C:/Users/user/Documents/Python/aa.py ===============
 *************** 성 적 표 ************** 
 *************************************** 
  이 름  국어  영어  수학  총점    평균  
 *************************************** 
 이순신    85    80    90   255   85.00 
 강감찬    75    80    95   250   83.33 
 한석봉    99    99    99   297   99.00 
 황진이    35    45    20   100   33.33 
 안중근    90    85    90   265   88.33 
 박문수    95    95    95   285   95.00 
 임꺽정    15    35    45    95   31.67 
 김정호    90    95    80   265   88.33 
 정몽주    90    90    95   275   91.67 
 이정호    50    45    60   155   51.67 
 ************************************** 
 총평균  72.4  74.9  76.9 2242.0 74.73 
>>> 
=============== RESTART: C:/Users/user/Documents/Python/aa.py ===============
 *************** 성 적 표 ************** 
 *************************************** 
  이 름  국어  영어  수학  총점    평균  
 *************************************** 
 이순신    85    80    90   255   85.00 
 강감찬    75    80    95   250   83.33 
 한석봉    99    99    99   297   99.00 
 황진이    35    45    20   100   33.33 
 안중근    90    85    90   265   88.33 
 박문수    95    95    95   285   95.00 
 임꺽정    15    35    45    95   31.67 
 김정호    90    95    80   265   88.33 
 정몽주    90    90    95   275   91.67 
 이정호    50    45    60   155   51.67 
 ************************************** 
Traceback (most recent call last):
  File "C:/Users/user/Documents/Python/aa.py", line 41, in <module>
    .format(korA, engA, matA, everyT, everyA))
ValueError: Format specifier missing precision
>>> 
=============== RESTART: C:/Users/user/Documents/Python/aa.py ===============
 *************** 성 적 표 ************** 
 *************************************** 
  이 름  국어  영어  수학  총점    평균  
 *************************************** 
 이순신    85    80    90   255   85.00 
 강감찬    75    80    95   250   83.33 
 한석봉    99    99    99   297   99.00 
 황진이    35    45    20   100   33.33 
 안중근    90    85    90   265   88.33 
 박문수    95    95    95   285   95.00 
 임꺽정    15    35    45    95   31.67 
 김정호    90    95    80   265   88.33 
 정몽주    90    90    95   275   91.67 
 이정호    50    45    60   155   51.67 
 ************************************** 
 총평균  72.4  74.9  76.9  2242 74.73 
>>> 
=============== RESTART: C:/Users/user/Documents/Python/aa.py ===============
 *************** 성 적 표 ************** 
 *************************************** 
  이 름  국어  영어  수학  총점    평균  
 *************************************** 
 이순신    85    80    90   255   85.00 
 강감찬    75    80    95   250   83.33 
 한석봉    99    99    99   297   99.00 
 황진이    35    45    20   100   33.33 
 안중근    90    85    90   265   88.33 
 박문수    95    95    95   285   95.00 
 임꺽정    15    35    45    95   31.67 
 김정호    90    95    80   265   88.33 
 정몽주    90    90    95   275   91.67 
 이정호    50    45    60   155   51.67 
 ************************************** 
 총평균  72.4  74.9  76.9  2242   74.73 
>>> ~0
		    
-1
>>> ~~0
		    
0
>>> 2 << 5
		    
64
>>> 2 >> 5
		    
0
>>> 3 >>2
		    
0
>>> "ace" + 3
		    
Traceback (most recent call last):
  File "<pyshell#243>", line 1, in <module>
    "ace" + 3
TypeError: can only concatenate str (not "int") to str
>>> 'ace' + 3
		    
Traceback (most recent call last):
  File "<pyshell#244>", line 1, in <module>
    'ace' + 3
TypeError: can only concatenate str (not "int") to str
>>> 0|0
		    
0
>>> 0|1
		    
1
>>> 1|0
		    
1
>>> 1|1
		    
1
>>> 0 ^ 0
		    
0
>>> 0 ^ 1
		    
1
>>> 1 ^ 0
		    
1
>>> 1 ^ 1
		    
0
>>> bin(3)
		    
'0b11'
>>> bin(2)
		    
'0b10'
>>> 2|3
		    
3
>>> 2&3
		    
2
>>> 2 ^ 3
		    
1
>>> 2 ^ 4
		    
6
>>> 2 ^ 5
		    
7
>>> 3 ^ 4
		    
7
>>> 2 ^ 3
		    
1
>>> 1 ^ 2
		    
3
>>> 4 ^ 5
		    
1
>>> 10 | 11
		    
11
>>> 10 & 11
		    
10
>>> 10 ^| 11
		    
SyntaxError: invalid syntax
>>> 10 ^ 11
		    
1
>>> bin(10)
		    
'0b1010'
>>> bin(11)
		    
'0b1011'
>>> 10101
		    
10101
>>> 3 ^ 15
		    
12
>>> <<2
		    
SyntaxError: invalid syntax
>>> 2 << 2
		    
8
>>> 2 <<
		    
SyntaxError: invalid syntax
>>> 2<< 3
		    
16
>>> 2 >> 2
		    
0
>>> 2 >>10
		    
0
>>> 10 >> 10
		    
0
>>> 10 >> 2
		    
2
>>> ~1
		    
-2
>>> ~2
		    
-3
>>> ~3
		    
-4
>>> 10 & 3
		    
2
>>> 10 ^ 3
		    
9
>>> 2^3
		    
1
>>> 3 << 3
		    
24
>>> 64 >> 2
		    
16
>>> -1>>5
		    
-1
>>> -10>>3
		    
-2
>>> -10>>4
		    
-1
>>> ~300
		    
-301
>>> ~299
		    
-300
>>> 0~
		    
SyntaxError: invalid syntax
>>> ~0
		    
-1
>>> ~1
		    
-2
>>> ~2
		    
-3
>>> ~-1
		    
0
>>> ~128
		    
-129
>>> ~127
		    
-128
>>> ~300
		    
-301
>>> 
