#   Encriptar pdf con contraseña
from PyPDF2 import PdfWriter, PdfReader
import getpass

pdf_writer = PdfWriter()
pdf_reader = PdfReader("/home/ed/otrapracticamas/Ejercicio-Video-85/document.pdf")

for page_num in range(len(pdf_reader.pages)):
    pdf_writer.add_page(pdf_reader.pages[page_num])

password = getpass.getpass(prompt="Ingrese el password:")
print(password)
pdf_writer.encrypt(password)
with open("document-protected.pdf", "wb") as file:
    pdf_writer.write(file)
