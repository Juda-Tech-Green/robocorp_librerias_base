from RPA.Browser.Selenium import Selenium
from RPA.FileSystem import FileSystem
from time import sleep
import re,os

class SubtitleTranslator:
    def __init__(self):
        self.browser = Selenium()
        self.fs = FileSystem()
        self.url_base = "https://translate.google.com/?sl={sl}&tl={tl}&op=translate"

    def abrir_traductor(self, idioma_origen, idioma_destino):
        url = self.url_base.format(sl=idioma_origen,tl=idioma_destino)
        self.browser.open_available_browser(url)

        try:
            self.browser.click_button_when_visible("//button[contains(.,'Aceptar')]")
        except:
            pass
    
    def traducir_texto(self, texto):
        if not texto.strip():
            return ""
    
        input_xpath='//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/div/c-wiz/span/span/div/textarea'
        output_xpath = '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz/div/div[6]/div/div[1]'
        
        self.browser.wait_until_element_is_visible(input_xpath)
        self.browser.clear_element_text(input_xpath)
        self.browser.input_text(input_xpath, texto)
        sleep(1.3)

        try:
            
            traduccion = self.browser.get_text(output_xpath)
            return traduccion
        except:
            return texto

    def procesar_srt(self, ruta_archivo, idioma_origen, idioma_destino):
        if not os.path.exists(ruta_archivo):
            raise FileNotFoundError("Archivo no encontrado")
    
        with open(ruta_archivo, "r", encoding="utf-8") as f:
            lineas = f.readlines()

        self.abrir_traductor(idioma_origen,idioma_destino)

        resultado = []
        bloque_texto = []

        for linea in  lineas:
            linea_strip = linea.strip()

             # Línea vacía
            if linea_strip == "":
                if bloque_texto:
                    texto_original = " ".join(bloque_texto)
                    texto_traducido = self.traducir_texto(texto_original)
                    sleep(2)
                    resultado.append(texto_traducido + "\n")
                    bloque_texto = []
                resultado.append("\n")
                continue

            if linea_strip.isdigit() or "-->" in linea_strip:
                resultado.append(linea)
                continue

            bloque_texto.append(linea_strip)

        if bloque_texto:
            texto_original = " ".join(bloque_texto)
            texto_traducido = self.traducir_texto(texto_original)
            sleep(2)
            resultado.append(texto_traducido + "\n")

        
        base, ext = os.path.splitext(ruta_archivo)
        ruta_salida = f"{base}_{idioma_destino}{ext}"

        with open(ruta_salida, "w", encoding="utf-8") as f:
            f.writelines(resultado)

        return ruta_salida