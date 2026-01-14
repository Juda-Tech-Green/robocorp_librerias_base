from RPA.Excel.Files import Files
from RPA.Tables import Tables

class ExcelKeywords:
    def __init__(self):
        self.excel = Files()
        self.tables = Tables()

    
    def abrir_y_leer_datos(self, ruta ,hoja):
        """Abre un libro y devuelve los datos como tabla"""
        self.excel.open_workbook(ruta)
        datos = self.excel.read_worksheet_as_table(name=hoja, header=True)
        self.excel.close_workbook()
        return datos
    
    def obtener_dimensiones(self, tabla):
        return self.tables.get_table_dimensions(tabla)
    
    def obtener_fila(self, tabla, numero_fila):
        return self.tables.get_table_row(tabla, numero_fila)
    
    def crear_excel_nuevo(self, nombre_archivo):
        self.excel.create_workbook(nombre_archivo)
        self.excel.append_rows_to_worksheet(["ID", "Producto", "Precio"])
        for i in range(1,11):
            linea = {"ID":i, "Estado":"Pendiente"}
            self.excel.append_rows_to_worksheet(linea)
        self.excel.save_workbook(nombre_archivo)
    
    def iterar_hojas_del_libro(self, ruta_archivo):
        self.excel.open_workbook(ruta_archivo)

        nombres_hojas = self.excel.list_worksheets()

        resumen = []

        for nombre in nombres_hojas:
            datos_hoja = self.excel.read_worksheet(nombre)
            num_filas= len(datos_hoja)

            resumen.append({"hoja": nombre,
                            "filas": num_filas})
            print(f"La hoja '{nombre}' contiene {num_filas} filas.")
        self.excel.close_workbook()
        return resumen