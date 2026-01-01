#   Leer pdf
#   pip install pypdf2
import PyPDF2

pdf_file_obj = open("/home/ed/otrapracticamas/Ejercicio-Video-84/book.pdf", "rb")

pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
#print(pdf_reader.documentInfo)
print(pdf_reader.getNumPages())
page_obj=pdf_reader.getPage(0)
text=page_obj.extract_text()
print(text)