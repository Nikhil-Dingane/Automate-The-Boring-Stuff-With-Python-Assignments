#! python3
import ezsheets
ss=ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')
sheet=ss[0];
for i in range(2,sheet.rowCount):
	row=sheet.getRow(i)
	if int(row[0]) * int(row[1]) != int(row[2]):
		print("There is wrong calculation on the row : "+str(i))
		break;
