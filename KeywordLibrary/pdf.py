from RPA.PDF import PDF
from RPA.Browser.Selenium import Selenium
from time import sleep
import os, re


class PDFKeywords:
    def __init__(self):
        self.pdf = PDF()
        self.browser = Selenium()
    
    def extraer_paginas_con_imagenes(self, ruta_pdf, palabra_clave,carpeta_destino="output"):
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)
        
        self.pdf.open_pdf(ruta_pdf)

        try:
            pdf_info = self.pdf.get_pdf_info()
            total_paginas = self.pdf.get_number_of_pages()
            print(f"Info: {pdf_info}")
            print(f"Páginas totales: {total_paginas}")

            texto_completo = self.pdf.get_text_from_pdf()

            for pagina in texto_completo.keys():
                text = texto_completo[pagina]

                patron=fr"{re.escape(palabra_clave)}\s+\d+:"

                resultado = re.search(patron, text)

                if resultado:
                    print(f"Página {pagina} contiene imágenes. Guardando...")

                    destino = os.path.join(carpeta_destino, f"page_{pagina}.pdf")

                    self.pdf.extract_pages_from_pdf(
                        source_path=ruta_pdf,
                        output_path=destino,
                        pages=str(pagina)
                    )

                    print(f"Página {pagina} guardada en: {destino}")
        finally:
            self.pdf.close_pdf()

    def guardar_url_como_imagen_en_pdf(self,
                                       url,
                                       ruta_salida,
                                       plantilla_html):
        
        html_preparado = plantilla_html.replace("URL_TO_UPDATE", url)

        self.browser.open_available_browser(url)

        try:
            sleep(5)
            self.pdf.html_to_pdf(html_preparado, ruta_salida)
            
            ruta_screenshot = "temp_captura.png"
            self.browser.capture_page_screenshot(ruta_screenshot)

            self.pdf.add_watermark_image_to_pdf(
                image_path=ruta_screenshot,
                source_path=ruta_salida,
                output_path=ruta_salida
            )

        finally:
            self.browser.close_all_browsers()

            if os.path.exists("temp_captura.png"):
                os.remove("temp_captura.png")
