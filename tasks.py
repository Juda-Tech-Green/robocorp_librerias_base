from robocorp.tasks import task
from KeywordLibrary.excel import ExcelKeywords
from KeywordLibrary.excel_app import ExcelGuiKeywords
from KeywordLibrary.desktop import DesktopKeywords
from KeywordLibrary.file_system import FileSystemKeywords
from KeywordLibrary.pdf import PDFKeywords
from KeywordLibrary.email import EmailKeywords
from KeywordLibrary.api_manager import APIKeywords
from KeywordLibrary.browser import SubtitleTranslator
from KeywordLibrary.archive import ArchiveKeyWords
from KeywordLibrary.word import WordKeyWords
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv()


@task
def mi_primer_robot():

    """ ==================== EXCEL SIN GUI
    
    ex = ExcelKeywords()
    ruta = "DataSets/sampledatainsurance.xlsx"
    
    # 1. Leer los datos
    policy_data = ex.abrir_y_leer_datos(ruta, "PolicyData")
    
    # 2. Ver dimensiones 
    dimensiones = ex.obtener_dimensiones(policy_data)
    
    print(f"Filas: {dimensiones[0]}, Columnas: {dimensiones[1]}")
    
    # 3. Obtener la primera fila (índice 0)
    primera_fila = ex.obtener_fila(policy_data, 0)
    print(f"Datos de la primera fila: {primera_fila}")
    # 4. Iterar en 
    for i in range (10):
        print(f"Datos de la fila {i}: \n {ex.obtener_fila(policy_data, i)}")

    # 5. Crear nuevo archivo excel
    nombre_archivo_nuevo = "DataSets/new_wbook_2.xlsx"
    ex.crear_excel_nuevo(nombre_archivo_nuevo)
    
    resultados = ex.iterar_hojas_del_libro(ruta)
    """

    """==================== EXCEL CON GUI
    nombre_archivo = "SampleXLSFile.xlsx"
    nueva_hoja= "CareServices"
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta = os.path.join(root_path, "introduction","DataSets", nombre_archivo)

    gui_ex = ExcelGuiKeywords()
    gui_ex.abrir_excel_visible(ruta)
    
    gui_ex.add_hoja_con_gui(ruta_archivo=ruta, nombre_nueva_hoja=nueva_hoja)
    print(f"¡Hoja '{nueva_hoja}' agregada correctamente!")
    
    gui_ex.activar_hoja(nueva_hoja)

    valor = gui_ex.leer_de_celda(fila=1, columna=3)
    print(f"El robot lee: {valor}")
    
    gui_ex.escribir_en_celda(1,1,"TestData1")
    gui_ex.escribir_en_celda(1,2,"TestData2")
    
    gui_ex.guardar_y_salir()
    """

    """==================== DESKTOP APPLICATIONS
    desk = DesktopKeywords()
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    img_objetivo1 = os.path.join(root_path, "introduction","Images", "Money.png")
    img_objetivo2 = os.path.join(root_path, "introduction","Images", "Stock.JPG")

    desk.abrir_app_y_clic_en_imagen(
        texto_busqueda="Money",
        imagen_objetivo=img_objetivo1
    )
    sleep(5)
    reference = desk.buscar_imagen_y_dar_clic(img_objetivo2)
    #desk.navegar_acciones_positivas()
    #info = desk.recopilar_info_desde_busqueda(reference)
    desk.capturar_area_especifica(reference, "evidencia.png")
    """

    """==================== SYSTEM FILES OPERATIONS
    fs_tool = FileSystemKeywords()
    directorio_base = "./../introduction"
    tipo_buscado = ".yaml"
    archivo_log = "registro_archivos.txt"

    fs_tool.buscar_archivos_en_directorios(directorio_base, tipo_buscado, archivo_log)
    """

    """==================== PDF & CREATE PDF FROM HTML TEMPLATES
    pdf_tool= PDFKeywords()

    #archivo_a_leer = "./DataSets/DOCUMENTO INTEGRADO SISTEMAS DE CONTROL AMBIENTAL.pdf"
    #archivo_a_leer = "./DataSets/stfdoc.pdf"
    
    pdf_tool.extraer_paginas_con_imagenes(
        ruta_pdf= archivo_a_leer,
        palabra_clave="Figure",
        carpeta_destino="pdf_outputs")
    
    mi_plantilla = "<h1>Reporte de Captura</h1><p>Evidencia de la URL: URL_TO_UPDATE</p>"
    
    pdf_tool.guardar_url_como_imagen_en_pdf(
        url="https://robocorp.com/portal",
        ruta_salida="evidencia_web.pdf",
        plantilla_html=mi_plantilla
    )
    """
    
    """==================== GMAIL 
    GMAIL_USER = os.getenv("GMAIL_USER")
    GMAIL_APP_PASS= os.getenv("GMAIL_APP_PASSWORD")


    email_tool = EmailKeywords(GMAIL_USER,GMAIL_APP_PASSWORD)

    destinatarios = ["david.mesa3@udea.edu.co","david.mesa2629@gmail.com"]
    adjuntos = ["./DataSets/DOCUMENTO INTEGRADO SISTEMAS DE CONTROL AMBIENTAL.pdf","./DataSets/stfdoc.pdf"]
    
    
    email_tool.enviar_email_de_texto(
        recipient_email=destinatarios,
        mail_subject="Test Reporte automatizado",
        mail_body="Hola, este es un email con el framework robocorp con adjuntos",
        mail_attachments=adjuntos
    )
    
    email_tool.guardar_adjunto_donde_sujeto_contiene(
        "PYTORCH",
        "email_managment"
    )
    
    cuerpo_html = f"""
    #    <html>
    #        <body>
    #            <h1>Hola, aquí está la evidencia</h1>
    #            <p>Se tomó esta captura:</p>
    #            <img src="{"Money.png"}" alt="Captura de pantalla" style="border: 1px solid #ccc;">
    #            <p>Saludos cordiales,<br>Tu Robot de confianza.</p>
    #        </body>
    #    </html>
    """
    email_tool.enviar_html_email_con_imagen(
        recipient_email=destinatarios,
        mail_subject="Reporte HTML con imagen",
        mail_body=cuerpo_html,
        image_file_path="./Images/Money.png"

    )
    """

    """==================== API y JSON
    api_tool = APIKeywords()
    base_url = "https://pokeapi.co/api/v2/pokemon/"
    endpoint_pokemon = "30"

    datos_pokemon = api_tool.ejecutar_get(base_url, endpoint_pokemon)

    nombre = api_tool.extraer_dato(datos_pokemon, "$.name")
    experiencia = api_tool.extraer_dato(datos_pokemon, "$.base_experience")
    primera_habilidad = api_tool.extraer_dato(datos_pokemon, "$.abilities[0].ability.name")

    print(f"--- DATOS DE {nombre.upper()} ---")
    print(f"Experiencia base: {experiencia}")
    print(f"Habilidad principal: {primera_habilidad}")
    """

    """==================== BROWSER SRT TRANSLATOR
    movie_translator_tool = SubtitleTranslator()
    archivo_traducido = movie_translator_tool.procesar_srt(
        ruta_archivo="./DataSets/subtitulos.srt",
        idioma_origen="en",
        idioma_destino="es"
    )

    print(f"Archivo generado en: {archivo_traducido}")
    """
    

    """==================== ARCHIVE
    archivador = ArchiveKeyWords()

    archivador.comprimir_carpeta(
        ruta_carpeta="./DataSets/Images",
        nombre_zip="solo_pngs.zip",
        extension=".png",
        excluir=False
    )
    """

    """====================WORD

    word_tool = WordKeyWords()


    texto, veces = word_tool.leer_todo_el_texto(
        ruta_archivo="./DataSets/sample_word.docx",
        palabra_objetivo="document")
    #print(texto)

    salida = word_tool.reemplazar_texto(
        ruta_archivo="./DataSets/sample_word.docx",
        src_str="document",
        dest_str="HALABALUZA",
        ruta_destino="./DataSets/word_changed.docx",
        numero_de_veces=veces
    )
    sleep(5)

    word_tool.convertir_word_a_pdf(
        ruta_archivo="./DataSets/word_changed.docx",
        ruta_salida_pdf="./DataSets/sample_pdf_new.pdf",
    )
    """


    