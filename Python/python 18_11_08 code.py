# pandas parsing and write

import pandas as pd

input_file = 'supplier_data.csv'
output_file = '1output.csv'

data_frame = pd.read_csv(input_file)

data_frame

data_frame.to_csv(output_file, index = False)


# 데이터 형태에 문제가 있는 경우 , <<
import csv

input_file2 = 'supplier_data2.csv'
output_file2 = '2output.csv'

with open(input_file2, 'r', newline = '') as csv_in_file:
    with open(output_file2, 'w', newline = '') as csv_out_file:
        filereader = csv.reader(csv_in_file, delimiter = ',')
        filewriter = csv.writer(csv_out_file, delimiter = ',')
        for row_list in filereader:
            filewriter.writerow(row_list)
            print(row_list)
        csv_out_file.close()

# 원래 방법 그대로 하기
with open(input_file2, 'r', newline = '') as filereader:
    header = filereader.readline()
    header = header.strip()
    header_list = header.split(', ')
    print(header_list)
    for row in filereader:
        row = row.strip()
        row_list = row.split(', ')
        print(row_list)


# 특정 행 필터링 하기

output_file3 = '3output.csv'

with open(input_file2, 'r', newline = '') as csv_in_file:
    with open(output_file3, 'w', newline = '') as csv_out_file:
        filereader = csv.reader(csv_in_file, delimiter = ',')
        filewriter = csv.writer(csv_out_file, delimiter = ',')
        header = next(filereader)
        print(header)
        filewriter.writerow(header)
        for row_list in filereader:
            supplier = str(row_list[0]).strip()
            cost = str(row_list[3]).strip('$').replace(',', '')
            if supplier == 'Supplier Z' or float(cost) > 600.0:
                filewriter.writerow(row_list)
                print(row_list)

# pandas로 쉽게 하기
pandas_output = 'pandas_output_file.csv'

df = pd.read_csv(input_file2)

df

df['Cost'] = df['Cost'].str.strip('$').str.replace(',', '').astype(float) # 이건 쉽진 않은데 ..?
df_codi = df[(df['Supplier Name'].str.contains('Z')) | (df['Cost'] > 600.0)]

df_codi.to_csv(pandas_output, index = False)


# 특정 집합의 값을 포함하는 행의 필터링
output_file4 = '4output.csv'

important_dates = ['1/20/14', '1/30/14']

with open(input_file2, 'r', newline = '') as csv_in_file:
    with open(output_file4, 'w', newline = '') as csv_out_file:
        filereader = csv.reader(csv_in_file, delimiter = ',')
        filewriter = csv.writer(csv_out_file, delimiter = ',')
        header = next(filereader)
        filewriter.writerow(header)
        for row_list in filereader:
            a_date = row_list[4]
            if a_date in important_dates:
                filewriter.writerow(row_list)

# pandas로

df2 = pd.read_csv(input_file2)
df2_set = df2[data_frame['Purchase Date'].isin(important_dates)]

df2_set.to_csv('pandas_output_file2.csv', index = False)