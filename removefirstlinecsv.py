#! python3
import csv, os, glob
filelist=glob.glob("*.csv")
os.makedirs('headerRemoved', exist_ok=True)
print("Removing header from the file")

for onefile in filelist:
	csvreader=csv.reader(open(onefile))
	csvrows=[]
	for row in csvreader:
		if csvreader.line_num==1:
			continue
		csvrows.append(row)
		
	csvWriter = csv.writer(open('headerRemoved'+onefile,'w'))
	for row in csvrows:
		csvWriter.writerow(row)
