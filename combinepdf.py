#! python3
import PyPDF2
pdfreader1=PyPDF2.PdfFileReader(open('meetingminutes.pdf','rb'))
pdfreader2=PyPDF2.PdfFileReader(open('meetingminutes2.pdf','rb'))
pdfwriter=PyPDF2.PdfFileWriter()

for pagenum in range(pdfreader1.numPages):
	pageobj=pdfreader1.getPage(pagenum)
	pdfwriter.addPage(pageobj)
for pagenum in range(pdfreader2.numPages):
	pageobj=pdfreader2.getPage(pagenum)
	pdfwriter.addPage(pageobj)
pdfoutputfile=open('combinedpdffile.pdf','wb')
pdfwriter.write(pdfoutputfile)
pdfoutputfile.close()
