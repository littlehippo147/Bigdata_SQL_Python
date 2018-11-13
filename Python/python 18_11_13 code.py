# 단일 워크시트 처리
## with open 읽기 쓰기
from xlrd import open_workbook
from xlwt import Workbook

input_file = 'sales_2013.xlsx'
output_file = 'output.xls'

output_WB = Workbook()
output_WS = output_WB.add_sheet('jan_2013_output')

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    for row_index in range(worksheet.nrows):
        for column_index in range(worksheet.ncols):
            output_WS.write(row_index, column_index, worksheet.cell_value(row_index, column_index))

output_WB.save(output_file)

# 날짜 형식 할당
import sys
from datetime import date
from xlrd import xldate_as_tuple

output_file = '2output.xls'

output_WB = Workbook()
output_WS = output_WB.add_sheet('jan_2013_output')

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    for row_index in range(worksheet.nrows):
        row_list_output = []
        for column_index in range(worksheet.ncols):
            if worksheet.cell_type(row_index, column_index) == 3:
                date_cell = xldate_as_tuple(worksheet.cell_value(row_index, column_index), workbook.datemode)
                date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                row_list_output.append(date_cell)
                output_WS.write(row_index, column_index, date_cell)
            else:
                non_date_cell = worksheet.cell_value(row_index, column_index)
                row_list_output.append(non_date_cell)
                output_WS.write(row_index, column_index, non_date_cell)

output_WB.save(output_file)

## pandas로 쉽게 하기
import pandas as pd

output_file2 = 'pandas_output1.xls'

df = pd.read_excel(input_file, sheetname = 'january_2013')

writer = pd.ExcelWriter(output_file2)
df.to_excel(writer, sheet_name = 'january_13_output', index = False)
writer.save()

## 여러 시트 한번에 처리
input_sheet_name = ['january_2013', 'february_2013', 'march_2013']
output_sheet_name = ['jan_13_output', 'feb_13_output', 'mar_13_output']

# mystr = (input_sheet_name[0])[0:3] + '_13_output'       # output_sheet_name 일정한 형식으로 만들기

output_file2 = 'pandas_output2.xls'

writer = pd.ExcelWriter(output_file2)
for index in range(len(input_sheet_name)):
    df2 = pd.read_excel(input_file, sheet_name = input_sheet_name[index])
    df2.to_excel(writer, sheet_name = output_sheet_name[index], index = False)

writer.save()


# numpy / matplotlib
import numpy as np
import matplotlib.pyplot as plt

# 직선 그래프
x = np.arange(0, 6, 1)  # array 만들기
x2 = np.arange(0, 6, 0.1)
y = 2 * x + 1

plt.plot(x, y)
plt.show()

def draw_linear_graph(a, b):
    x = np.arange(0, 6, 0.1)
    y = a * x + b
    plt.plot(x, y)
    plt.show()

draw_linear_graph(3, 5)

y2 = np.sin(x2)
plt.plot(x2, y2)
plt.show()


# sine 그래프
def draw_sine_graph():
    x = np.arange(0, 6, 0.1)
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()

draw_sine_graph()

# cos 그래프
def draw_cos_graph():
    x = np.arange(0, 6, 0.1)
    y = np.cos(x)
    plt.plot(x, y)
    plt.show()

draw_cos_graph()

# legend 추가
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, label = 'sin')
plt.plot(x, y2, label = 'cos')
plt.legend()
plt.show()

# line type, title
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, label = 'sin')
plt.plot(x, y2, linestyle = '--', label = 'cos')
plt.xlabel("x")
plt.ylabel("y")
plt.title("sin과 cos")
plt.legend()
plt.show()

## 한글 font 설정하기!
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

font_name = font_manager.FontProperties(fname = "c:\Windows\Fonts\malgun.ttf").get_name()
rc('font', family = font_name)

## image 다루기
def draw_image():
    from matplotlib.image import imread

    img = imread("가을.jpg")

    plt.imshow(img)
    plt.show()

draw_image()

## bar plot 그리기
plt.style.use('ggplot')

customers = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO']
customers_index = range(len(customers))
sale_amounts = [127, 90, 201, 111, 232]

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.bar(customers_index, sale_amounts, align='center', color='darkblue')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
plt.xticks(customers_index, customers, rotation=0, fontsize='small')

plt.xlabel('Customer Name')
plt.ylabel('Sale Amount')
plt.title('Sale Amount per Customer')

plt.savefig('bar_plot.png', dpi=400, bbox_inches='tight')
plt.show()

## histogram 예
plt.style.use('ggplot')

mu1, mu2, sigma = 100, 130, 15
x1 = mu1 + sigma*np.random.randn(10000)
x2 = mu2 + sigma*np.random.randn(10000)

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
n, bins, patches = ax1.hist(x1, bins=50, normed=False, color='darkgreen')
n, bins, patches = ax1.hist(x2, bins=50, normed=False, color='orange', alpha=0.5)
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')

plt.xlabel('Bins')
plt.ylabel('Number of Values in Bin')
fig.suptitle('Histograms', fontsize=14, fontweight='bold')
ax1.set_title('Two Frequency Distributions')

plt.savefig('histogram.png', dpi=400, bbox_inches='tight')
plt.show()

