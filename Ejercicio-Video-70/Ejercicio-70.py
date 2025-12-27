#   Crear excel
# pip install openpyxl
import openpyxl

excel_book = openpyxl.Workbook()
sheet = excel_book.active

data = [
    ("Name", "Age", "Company"),
    ("Johin", 21, "La vieja Tuerta"),
    ("Miguel", 17, "Coca-Colas"),
    ("Cintia", 19, "Toyota"),
    ("Romina", 18, "Los vuelas"),
]

for index, row in enumerate(data):
    sheet[f"A{index+1}"] = row[0]
    sheet[f"B{index+1}"] = row[1]
    sheet[f"C{index+1}"] = row[2]

excel_book.save("mi_excel.xlsx")
