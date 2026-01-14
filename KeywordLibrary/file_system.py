from RPA.FileSystem import FileSystem

class FileSystemKeywords:
    def __init__(self):
        self.fs = FileSystem()

    def buscar_archivos_en_directorios(self, directorio, tipo_extension, log_file):
        print(f"Buscando en: {directorio}")

        files = self.fs.list_files_in_directory(directorio)

        for file in files:
            print(file)
            extension=self.fs.get_file_extension(file.path)
            if extension.lower() == tipo_extension.lower():
                self.guardar_detalles_archivos(file, log_file)
            else:
                pass
        
        child_directories = self.fs.list_directories_in_directory(directorio)

        for child_dir in child_directories:
            self.buscar_archivos_en_directorios(child_dir, tipo_extension, log_file)
    
    def guardar_detalles_archivos(self, file, log_file):
        if not self.fs.does_file_exist(log_file):
            self.fs.create_file(log_file)
            
        texto_a_guardar = f"Archivo: {file.name} | Ruta: {file.path}\n"
        self.fs.append_to_file(log_file, texto_a_guardar)