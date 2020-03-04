#!python3
import ezsheets, sys
print('Enter the full path of file to convert:')
filename=input()
try:
	ss=ezsheets.upload(filename)
	print(str(ss.title)+" was successfully uplodaded")
except:
	print('Invalid file!!!')
	#sys.exit()
print("Choose the option")
print("1. Excel")
print("2. ODS")
print("3. CSV")
print("4. TSV")
print("5. PDF")
print("6. HTML")
print("7. exit")
choice=input()

if int(choice)==1:
	ss.downloadAsExcel()
elif int(choice)==2:
	ss.downloadAsODS()
elif int(choice)==3:
	ss.downloadAsCSV()
elif int(choice)==4:
	ss.downloadAsTSV()
elif int(choice)==5:
	ss.downloadAsPDF()
elif int(choice)==6:
	ss.downloadAsHTML()
elif int(choice)==7:
	sys.exit()
else:
	print('Invalid choice')
