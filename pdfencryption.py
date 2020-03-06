#! python3
import PyPDF2
pdfreader=PyPDF2.PdfFileReader(open('meetingminutes.pdf','rb'))
pdfwriter=PyPDF2.PdfFileWriter()
for i in range(0,pdfreader.numPages):
	pdfwriter.addPage(pdfreader.getPage(i))
pdfwriter.encrypt('nick')
pdfwriter.write(open('encrypted.pdf','wb'))
