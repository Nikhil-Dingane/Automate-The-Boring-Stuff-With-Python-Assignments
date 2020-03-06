#! python3
import PyPDF2, glob, os
pdflist=glob.glob("*.pdf")
pdflist.sort()
pdfwriter=PyPDF2.PdfFileWriter()
for filename in pdflist:
	pdffilereader=PyPDF2.PdfFileReader(filename)
	for i in range(1,pdffilereader.numPages):
		pdfwriter.addPage(pdffilereader.getPage(i))
pdfwriter.write(open('combinedminutes.pdf','wb'))
