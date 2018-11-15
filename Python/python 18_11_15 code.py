# 2018-11-15
import csv
import MySQLdb
import sqlite3
import sys
import pandas
from datetime import datetime, date
import os
os.getcwd()
os.chdir('C:\\Users\\user\\Documents\\python project')

input_file = 'supplier_data.csv'

con = MySQLdb.connect(host='localhost', port=3306, db='hippo_db', user='root', passwd='1234')
c = con.cursor()

file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader)
for row in file_reader:
	data = []
	for column_index in range(len(header)):
		if column_index < 4:
			data.append(str(row[column_index]).lstrip('$')\
			.replace(',', '').strip())
		else:
			a_date = datetime.date(datetime.strptime(\
			str(row[column_index]), '%m/%d/%y'))
			# %Y: year is 2016; %y: year is 15
			a_date = a_date.strftime('%Y-%m-%d')
			data.append(a_date)
	print(data)
	c.execute("INSERT INTO Suppliers VALUES (%s, %s, %s, %s, %s);", data)

con.commit()
print("")

# Query the Suppliers table
c.execute("SELECT * FROM Suppliers;")
rows = c.fetchall()
for row in rows:
	row_list_output = []
	for column_index in range(len(row)):
		row_list_output.append(str(row[column_index]))
	print(row_list_output)


# 테이블 검색 및 결과물 csv 파일로 출력
output_file = "12output.csv"
f = open(output_file, 'w', newline = '')
filewriter = csv.writer(f, delimiter = ',')
header = ['supplier name', 'invoice number', 'part number', 'cost', 'purchase date']
filewriter.writerow(header)

c.execute("SELECT * FROM Suppliers WHERE cost > 700.0;")
rows = c.fetchall()
for row in rows:
    filewriter.writerow(row)
f.close()


# 데이터 변경하기 
c.execute("""update suppliers set supplier_name = 'KPC004'; """)
con.commit()

##########################################
# ip 별로 서버 생성 및 데이터 옮겨와서 변경하기
import csv
import MySQLdb
import sys


con=MySQLdb.connect(host='10.1.44.104',port=3306,db='my_suppliers',user='kpc2',passwd='1234')
c=con.cursor()

c.execute("""UPDATE Suppliers SET Supplier_Name = 'kpc003';""")

c.execute("SELECT * FROM Suppliers")
rows = c.fetchall()

con2=MySQLdb.connect(host='10.1.44.103',port=3306,db='my_suppliers',user='kpc2',passwd='1234')
c2=con2.cursor()


for row in rows:
    c2.execute("""INSERT INTO Suppliers VALUES (%s, %s, %s, %s, %s);""", row)

con2.commit()

