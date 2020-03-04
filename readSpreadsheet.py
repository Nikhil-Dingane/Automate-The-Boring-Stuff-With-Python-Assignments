#! python3
import ezsheets
ss=ezsheets.Spreadsheet('1cm-WAf6qGr3bCYr38mzUquO39x_mgzDtPzbZv8QRQ-E')
sheet=ss[0];
emails=sheet.getColumn(4)
print('Emails are :')
for i in range(1,len(emails)):
	print(emails[i])
