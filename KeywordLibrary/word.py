from RPA.Word.Application import Application
from time import sleep
import os, re

class WordKeyWords:
    def __init__(self):
        self.word = Application()

    def leer_todo_el_texto(self, ruta_archivo, palabra_objetivo):
        
        self.word.open_application(visible=False, display_alerts=False)

        self.word.open_file(ruta_archivo)

        text = self.word.get_all_texts()

        count = text.lower().count(palabra_objetivo.lower())

        sleep(3)

        self.word.quit_application()
        print(count)
        return text, count
    
    def reemplazar_texto(self,
                         ruta_archivo,
                         src_str,
                         dest_str,
                         ruta_destino, numero_de_veces):
        self.word.open_application(visible=True, display_alerts=False)

        self.word.open_file(ruta_archivo)

        for i in range(numero_de_veces):
            self.word.replace_text(
                find=src_str,
                replace=dest_str
            )

        self.word.save_document_as(ruta_destino)

        

        sleep(3)

        self.word.quit_application()

        return ruta_destino
    
    def convertir_word_a_pdf(
            self,
            ruta_archivo,
            ruta_salida_pdf,
            texto_introducir="Converted By Robot" ):
        
        self.word.open_application(visible=False, display_alerts=False)

        self.word.open_file(ruta_archivo)

        if texto_introducir:
            self.word.write_text(texto_introducir)

        self.word.export_to_pdf(ruta_salida_pdf)

        self.word.quit_application()