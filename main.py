from PyPDF2 import PdfReader, PdfWriter

#Source PDF
pdf_file_path = 'unknown file name.pdf'
file_base_name = pdf_file_path.replace('.pdf', '')

pdf = PdfReader(pdf_file_path)

# Pages to be extracted
# Remember to start your counting from 0
pagesNumber= [16, 36] 


pdfWriter = PdfWriter()

for page_num in pagesNumber:
	pdfWriter.add_page(pdf.pages[page_num])

with open('{0}_subset.pdf'.format(file_base_name), 'wb') as f:
	pdfWriter.write(f)
	f.close()
	