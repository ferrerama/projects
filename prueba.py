import openpyxl as px

book = px.load_workbook("C:/Users/mferrera/Desktop/ws/prueba.xlsx")
sheet = book["Hoja1"]
sheet["A1"] = 'Hola'

book.save('prueba.xlsx')

