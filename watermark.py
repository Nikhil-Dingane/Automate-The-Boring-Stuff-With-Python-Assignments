#! python3
import PyPDF2
pdfreader=PyPDF2.PdfFileReader('meetingminutes.pdf','rb')
pdfwatermarkreader=PyPDF2.PdfFileReader('watermark.pdf','rb')
firstpage=pdfreader.getPage(0)
firstpage.mergePage(pdfwatermarkreader.getPage(0))
pdfwriter=PyPDF2.PdfFileWriter()
pdfwriter.addPage(firstpage)
for pagenum in range(1,pdfreader.numPages):
	pdfwriter.addPage(pdfreader.getPage(pagenum))
outputfile=open('watermarkedfile.pdf','wb')

pdfwriter.write(outputfile)

