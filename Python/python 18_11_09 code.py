# 패턴/정규표현식

import pandas as pd

input_file2 = 'supplier_data2.csv'
output_file = 'pandas_output_file3.csv'

df3 = pd.read_csv(input_file2)

df3_pat = df3.ix[df3['Invoice Number'].str.startswith("001-"), :] # startswith() 앞에서부터 해당 문자열 포함시 True

df3_pat.to_csv(output_file, index = False)

output_file2 = 'pandas_output_file4.csv'

df4 = pd.read_csv(input_file2)

df4_pat = df4.ix[df4['Purchase Date'].str.endswith("-03-14"), :] # endswith() 뒤에서부터 해당 문자열 포함시 True

df4_pat.to_csv(output_file2, index = False)

# 열 인덱스로 선택하기
## with open 문 이용
import csv

output_file5 = '5output.csv'

my_columns = [0, 3]

with open(input_file2, 'r', newline = '') as csv_in_file:
    with open(output_file5, 'w', newline = '') as csv_out_file:
        filereader = csv.reader(csv_in_file, delimiter = ',')
        filewriter = csv.writer(csv_out_file, delimiter = ',')
        for row_list in filereader:
            row_list_output = []
            for idx in my_columns:
                row_list_output.append(row_list[idx])
            filewriter.writerow(row_list_output)


## pandas 이용

output_file = 'pandas_output_file5.csv'

df5 = pd.read_csv(input_file2)

df5_colidx = df5.iloc[ : , [0, 3]] # 인덱스 그대로 사용

df5_colidx.to_csv(output_file, index = False)

## 열 이름으로 찾기
output_file6 = '6output.csv'

my_columns = ['Invoice Number', 'Purchase Date']
my_columns_inx = []

with open(input_file2, 'r', newline = '') as csv_in_file:   # 이게 훨씬 불편한데 왜 쓰는거야야
    with open(output_file6, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file, delimiter = ',')
        filewriter = csv.writer(csv_out_file, delimiter = ',')
        header = next(filereader)
        for index_value in range(len(header)):
            if header[index_value] in my_columns:
                my_columns_inx.append(index_value)
        filewriter.writerow(my_columns)
        for row_list in filereader:
            row_list_output = []
            for index_value in my_columns_inx:
                row_list_output.append(row_list[index_value])
            filewriter.writerow(row_list_output)

## pandas 이용

output_file = 'pandas_output_file6.csv'

df6 = pd.read_csv(input_file2, header = True)

my_columns = ['Invoice Number', 'Purchase Date']


df6_colname = df5.loc[ : , my_columns] # 인덱스 그대로 사용
df6_colname.to_csv(output_file, index = False)

# 더러운 데이터의 처리
## with open 이용
input_file3 = 'supplier_data3.csv'
output_file = '7output.csv'

row_counter = 0

with open(input_file3, 'r', newline = '') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file, delimiter = ',')
        filewriter = csv.writer(csv_out_file, delimiter = ',')

        for row in filereader:
            if row_counter >= 3 and row_counter <= 15:
                filewriter.writerow([value.strip() for value in row])
            row_counter += 1

## pandas  drop method 이용
output_file = 'pandas_output_file7.csv'

df7 = pd.read_csv(input_file3, header = None)

df7 = df7.drop([0, 1, 2, 16, 17, 18])
df7.columns = df7.iloc[0]

df7 = df7.reindex(df7.index.drop([3]))
df7.to_csv(output_file, index = False)

# 헤더 추가하기
## with open
input_file = 'supplier_data_nohead.csv'
output_file = '8output.csv'

header_list = ['Supplier Name', 'Invoice Number', 'Part Number', 'Coast', 'Purchase Date']

with open(input_file, 'r', newline = '') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file, delimiter = ',')
        filewriter = csv.writer(csv_out_file, delimiter = ',')
        filewriter.writerow(header_list)
        for row in filereader:
            filewriter.writerow(row)


## pandas 이용
output_file = 'pandas_output_file8.csv'

df8 = pd.read_csv(input_file, header = None, names = header_list) # names로 열 이름 리스트 지정

df8.to_csv(output_file, index = False)


# 여러개의 파일 합치기!!
import csv
import glob         # 경로 탐색 모듈
import os
import sys


input_path = 'C:\\Users\\user\\Documents\\Python\\python project'  ## input file들의 경로

file_counter = 0
for input_file in glob.glob(os.path.join(input_path, 'sales_*')):
