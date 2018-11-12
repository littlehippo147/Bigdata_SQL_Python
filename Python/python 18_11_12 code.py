# 여러개의 파일 합치기!!
import csv
import glob         # 경로 탐색 모듈
import os
import sys


input_path = 'C:\\Users\\user\\Documents\\Python\\python project'  ## input file들의 경로

file_counter = 0
for input_file in glob.glob(os.path.join(input_path, 'sales_*')):
    row_counter = 1
    with open(input_file, 'r', newline='') as csv_in_file:
        filereader = csv.reader(csv_in_file)
        header = next(filereader)
        for row in filereader:
            row_counter += 1
        print('{0:s} :\t {1:d} rows \t {2:d} columns '.format(os.path.basename(input_file), row_counter, len(header)))
    file_counter += 1
print('Numbers of files : {:d}'.format(file_counter))

## 합쳐서 저장하기
out_file = "9output_file.csv"

first_file = True

for input_file in glob.glob(os.path.join(input_path, 'sales_*')):
    print(os.path.basename(input_file))
    with open(input_file, 'r', newline = '') as csv_in_file:
        with open(out_file, 'a', newline = '') as csv_out_file:
            filereader = csv.reader(csv_in_file)
            filewriter = csv.writer(csv_out_file)
            if first_file:
                for row in filereader:
                    filewriter.writerow(row)
                first_file = False
            else:
                header = next(filereader)
                for row in filereader:
                filewriter.writerow(row)

## pandas로 합치기!
import pandas as pd

output_file = "pandas_output_file9.csv"

all_files = glob.glob(os.path.join(input_path, 'sales_*'))
print(all_files)

all_df = []

for file in all_files:
    df = pd.read_csv(file, index_col = None)
    all_df.append(df)

df_conc = pd.concat(all_df, axis = 0, ignore_index = True)
df_conc.to_csv(output_file)

# 데이터 값의 통계내기

output_file = "10output.csv"

output_header_list = ['file_name', 'total_sales', 'average_sales']

csv_out_file = open(output_file, 'a', newline = '')
filewriter = csv.writer(csv_out_file)
filewriter.writerow(output_header_list)

for input_file in glob.glob(os.path.join(input_path, 'sales_*')):
    print(os.path.basename(input_file))
    with open(input_file, 'r', newline = '') as csv_in_file:
        filereader = csv.reader(csv_in_file)
        output_list = []
        output_list.append(os.path.basename(input_file))
        header = next(filereader)
        total_sales = 0.0
        num_of_sales = 0.0
        for row in filereader:
            sale_amount = row[3]
            total_sales += float(sale_amount.strip('$').replace(',', ''))
            num_of_sales += 1
        average_sales = '{0:.2f}'.format(total_sales / num_of_sales)
        output_list.append(total_sales)
        output_list.append(average_sales)
        filewriter.writerow(output_list)
csv_out_file.close()

## 항목 늘려서 시도
output_file = "11output.csv"

output_header_list = ['file_name', 'total_sales', 'average_sales', 'Customer_ID', 'total_ID']


csv_out_file = open(output_file, 'a', newline = '')
filewriter = csv.writer(csv_out_file)
filewriter.writerow(output_header_list)

for input_file in glob.glob(os.path.join(input_path, 'sales_*')):
    print(os.path.basename(input_file))
    with open(input_file, 'r', newline = '') as csv_in_file:
        filereader = csv.reader(csv_in_file)
        output_list = []
        output_list.append(os.path.basename(input_file))
        header = next(filereader)
        total_sales = 0.0
        total_ID = 0.0
        num_of_sales = 0.0
        for row in filereader:
            sale_amount = row[3]
            Customer_ID = row[0]
            total_sales += float(sale_amount.strip('$').replace(',', ''))
            total_ID = float(Customer_ID.strip())
            num_of_sales += 1
        average_sales = '{0:.2f}'.format(total_sales / num_of_sales)
        output_list.append(total_sales)
        output_list.append(average_sales)
        output_list.append(Customer_ID)
        output_list.append(total_ID)
        filewriter.writerow(output_list)
csv_out_file.close()

## pandas
output_file = "pandas_output_file10.csv"

all_files = glob.glob(os.path.join(input_path, 'sales_*'))

all_df2 = []

for input_file in all_files:
    df2 = pd.read_csv(input_file, index_col = None)

    total_sales = pd.DataFrame([float(str(value).strip('$').replace(',', '')) for value in df2.loc[ : , 'Sale Amount']]).sum()
    average_sales = pd.DataFrame([float(str(value).strip('$').replace(',', '')) for value in df2.loc[ : , 'Sale Amount']]).mean()

    data = {'file_name' : os.path.basename(input_file),
            'total_sales' : total_sales,
            'average_sales' : average_sales}

    all_df2.append(pd.DataFrame(data, columns = ['file_name', 'total_sales', 'average_sales']))

df2_conc = pd.concat(all_df2, axis = 0, ignore_index = True)
df2_conc.to_csv(output_file, index = False)

output_file = "pandas_output_file11.csv"

all_files = glob.glob(os.path.join(input_path, 'sales_*'))

all_df3 = []

for input_file in all_files:
    df3 = pd.read_csv(input_file, index_col = None)

    total_sales = pd.DataFrame([float(str(value).strip('$').replace(',', '')) for value in df2.loc[ : , 'Sale Amount']]).sum()
    average_sales = pd.DataFrame([float(str(value).strip('$').replace(',', '')) for value in df2.loc[ : , 'Sale Amount']]).mean()

    data = {'file_name' : os.path.basename(input_file),
            'total_sales' : total_sales,
            'average_sales' : average_sales}

    all_df2.append(pd.DataFrame(data, columns = ['file_name', 'total_sales', 'average_sales']))

df2_conc = pd.concat(all_df2, axis = 0, ignore_index = True)
df2_conc.to_csv(output_file, index = False)

# 엑셀 파일 불러오기
from xlrd import open_workbook

input_file = 'sales_2013.xlsx'

workbook = open_workbook(input_file)
print('Number of worksheets:', workbook.nsheets)
for worksheet in workbook.sheets():
    print("Worksheet name:", worksheet.name, "\tRows:", worksheet.nrows, "\tColumns:", worksheet.ncols)
