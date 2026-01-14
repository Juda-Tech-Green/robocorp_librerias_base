from RPA.Archive import Archive
import os 

class ArchiveKeyWords:
    def __init__(self):
        self.lib = Archive()       
    
    def comprimir_carpeta(self,
                          ruta_carpeta,
                          nombre_zip="salida.zip",
                          extension=None,
                          excluir=False):
        """
        - excluir: Si es True, guarda todo MENOS esa extensión. 
                   Si es False, guarda SOLO esa extensión.
        """
        patron = f"*{extension}" if extension else "*"
        
        if excluir and extension:
            self.lib.archive_folder_with_zip(
                folder=ruta_carpeta,
                archive_name=nombre_zip,
                recursive=True,
                exclude=patron
            )
        else:
            self.lib.archive_folder_with_zip(
                folder=ruta_carpeta,
                archive_name=nombre_zip,
                recursive=True,
                include=patron)
            
        return os.path.abspath(nombre_zip)