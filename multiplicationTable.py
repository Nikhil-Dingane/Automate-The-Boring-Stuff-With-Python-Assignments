#! python3
import openpyxl
import sys

wb=openpyxl.Workbook()
sheet=wb.active
sheet.title='multtable'

no = int(sys.argv[1])

for i in range(1,11):
	for j in range(1,no+1):
		sheet.cell(i,j).value= i * j
wb.save('multi_table.xlsx')
