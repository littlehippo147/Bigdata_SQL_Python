# dict
d = { 1:[1, 2, 3, 4, 5], 2 : [6, 7, 8, 9, 10]}
type(d)
print(d)
for _ in d.keys():
    for __ in d[_]:
        print(_, __)

d.items()
d.keys()
d.values()

# 루프 : for, while 반복문
a = [1, 2, 3, 4, 5, 6, 7 ,8 ,9, 10]
for i in range(0,10):
    print(a[i], end = ' ')

for i in a:              ## 결과는 같지만 더 쉽게하기
    print(i, end = ' ')

for i in range(1, 11, 2):
    print(i)

# 문제 : 0부터 99까지 정수를 한 줄에 10개씩 출력해보세요
## 내 풀이
for i in range(0, 10):
    for j in range(0, 10):
        print(10 * i + j, end = ' ')
    print()

## 강사님 풀이
for i in range(100):
    print(i, end = ' ')
    if i % 10 == 9:
        print()


# function : 함수, 함수의 목적 : 재사용, 모듈화화
def add(a, b):
    c = a + b
    return c

print(add(10,20))

# 유형 1 : 반환값이 없고 매개변수(인자)가 없는 경우
def f_1():
    print('f_1 is called!!')
f_1()

# 유형 2 : 반환값이 없고 매개변수(인자)가 있는 경우
def f_2(a,b):
    print('f_2', a, b, a + b)
f_2(12,34)
f_2('hello', 'kpc')

def f_22(a1,a2, a3 = ' aaa'):       # default argument(기본 인자)
    print('f_22', a1, a2, a3)
f_22('hello', 'kpc')
f_22('hello', 'kpc', 'good-bye')

# 유형 3 : 반환값이 있고 매개변수 없는 경우
def f_3():
    print('f_3 is called')
    return 78
f_3()
print(f_3())

# 유형 4 : 반환값이 있고 매개변수 있는 경우우
def f_4(a, b):
    c = a + b
    print('f_4', a, b, c)
    return c
print(f_4(5, 7))
print(f_4('hello', 'kpc'))

# 문제 : 2개의 정수에 대해 큰 수, 작은 수의 순서로 반환하는 함수를 구현하세요
def order(a, b):
    print(max(a,b), min(a,b))
    return max(a,b), min(a,b)
order(3,5)

def order2(a,b):
    if a < b:
        a, b = b, a
    return a, b
order2(3, 5)
order2(5, 3)

## CSV 파일 불러오기
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

print(input_file)
print(output_file)

input_file = 'supplier_data.csv'
output_file = '1output.csv'

with open(input_file, 'r', newline = '') as filereader:
    a = filereader.readline()
    b = filereader.readline()
    c = filereader.readline()

with open(input_file, 'r', newline = '') as filereader:
    header = filereader.readline()
    header = header.strip()             ## strip() : 양 끝의 공백 또는 개행문자 제거
    header_list = header.split(',')
    print(header_list)
    with open(output_file, 'w', newline = '') as filewriter:
        filewriter.write(header)
        filewriter.close()
    pass

header
header_list

with open(input_file, 'r', newline = '') as filereader:
    header = filereader.readline()
    header = header.strip()
    header_list = header.split(',')
    print(header_list)
    for row in filereader:
        row = row.strip()
        row_list = row.split(',')
        print(row_list)

# CSV 파일
import pandas as pd

df = pd.read_csv('supplier_data.csv')
df