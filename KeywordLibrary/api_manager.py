from RPA.HTTP import HTTP
from RPA.JSON import JSON

class APIKeywords:
    def __init__(self):
        self.http = HTTP()
        self.json = JSON()
   
    def ejecutar_get(self,url,endpoint):
        full_url = f"{url}{endpoint}"

        response = self.http.http_get(full_url)
        

        print(response.status_code)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error en API: Código {response.status_code}")
        
    
    def ejecutar_post(self, url, endpoint, datos_json):
        full_url = f"{url}{endpoint}"
        

    def extraer_dato(self, objeto_json, expresion_json):
        valor = self.json.get_value_from_json(objeto_json, expresion_json)
        return valor