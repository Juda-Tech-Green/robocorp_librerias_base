from RPA.Excel.Application import Application
from time import sleep
class ExcelGuiKeywords:
    def __init__(self):
        self.excel_app = Application()
    
    def abrir_excel_visible(self, ruta_archivo):
        self.excel_app.open_application(visible=True)

        self.excel_app.open_workbook(ruta_archivo)
    
    def add_hoja_con_gui(self, nombre_nueva_hoja):
        
        self.excel_app.add_new_sheet(nombre_nueva_hoja, create_workbook=False)

        self.excel_app.save_excel()
        sleep(3)
        #self.excel_app.quit_application()
    
    def activar_hoja(self, nombre_hoja):
        self.excel_app.set_active_worksheet(sheetname=nombre_hoja)

    def escribir_en_celda(self, fila, columna, valor):
        self.excel_app.write_to_cells(row=fila, column=columna, value=valor)
        sleep(2)
    
    def leer_de_celda(self, fila, columna):
        dato = self.excel_app.read_from_cells(row=fila, column=columna)
        sleep(5)
        return dato


    def guardar_y_salir(self):
        self.excel_app.save_excel()
        self.excel_app.close_document()
        self.excel_app.quit_application()