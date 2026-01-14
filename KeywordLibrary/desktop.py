from RPA.Desktop import Desktop



from time import sleep

class DesktopKeywords:
    def __init__(self):
        self.desktop = Desktop()
    


    def abrir_app_y_clic_en_imagen(self, 
                                   texto_busqueda, 
                                   imagen_objetivo):
        self.desktop.press_keys('cmd')
        sleep(1)

        self.desktop.type_text(texto_busqueda)
        
        locator =f"image:{imagen_objetivo}"
        self.desktop.wait_for_element(locator, timeout=10)

        self.desktop.click(locator)
        sleep(3)
        
    def buscar_imagen_y_dar_clic(self,
                                 imagen_objetivo):
        locator =f"image:{imagen_objetivo}"
        reference = self.desktop.wait_for_element(locator, timeout=10)
        self.desktop.click(locator)
        return reference 

    def navegar_acciones_positivas(self):
        acciones_verdes = self.desktop.find_elements("alias:GreenStock")

        print(f"Se encontraron: {len(acciones_verdes)}")

        for accion in acciones_verdes:
            self.desktop.click(accion, action="click")
            sleep(2)
        

    def recopilar_info_desde_busqueda(self,reference):
        

        referencia = reference

        region_datos = self.desktop.move_region(referencia, left=0, top=500)

        region_ajustada = self.desktop.resize_region(region_datos, 0, 0, 800, 400)

        texto_recopilado = self.desktop.read_text(region_ajustada)
        print(texto_recopilado)

        return texto_recopilado
    
    def capturar_area_especifica(self, elemento_referencia, nombre_archivo="captura_robot.png"):
        nueva_region = self.desktop.move_region(elemento_referencia, left=0, top=0)
        region_final = self.desktop.resize_region(nueva_region, 0, 0, 500, 500)

        
        
