# 🤖 Robocorp RPA Framework - Módulos Prácticos

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![Robocorp](https://img.shields.io/badge/RPA-Robocorp-black?logo=robotframework&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Educational-orange)

Este repositorio contiene una colección de scripts y módulos desarrollados como ejercicio académico para explorar las capacidades de la librería **RPA Framework** y la orquestación con **Robocorp**.

El proyecto demuestra la implementación de flujos de trabajo automatizados que interactúan con diversas aplicaciones de escritorio, servicios web, APIs y manipulación de archivos, siguiendo las mejores prácticas de modularización en Python.

## 🚀 Funcionalidades y Librerías Implementadas

El proyecto está estructurado en módulos reutilizables (`KeywordLibrary`), cada uno enfocado en una tecnología específica:

| Librería RPA / Módulo | Descripción del Ejercicio |
| :--- | :--- |
| **RPA.Excel.Files** | Lectura y escritura de hojas de cálculo sin interfaz gráfica (modo headless). |
| **RPA.Excel.Application** | Automatización de Excel interactuando directamente con la aplicación de escritorio. |
| **RPA.PDF** | Manipulación de PDFs: unión de archivos, extracción de texto y recorte de imágenes. |
| **RPA.Email.ImapSmtp** | Envío de correos (texto y HTML con imágenes inline) y descarga de adjuntos mediante protocolos IMAP/SMTP. |
| **RPA.HTTP & JSON** | Consumo de APIs REST (GET, POST, PUT, DELETE). Ejemplo práctico con **PokeAPI**. |
| **RPA.Browser.Selenium** | Automatización web para traducir subtítulos (`.srt`) usando Google Translate, respetando los tiempos de sincronización. |
| **RPA.Archive** | Compresión y descompresión de archivos (ZIP) con filtrado recursivo por extensiones. |
| **RPA.Word.Application** | Creación, edición y lectura de documentos `.docx` utilizando la automatización COM de Windows. |
| **RPA.Dialogs** | Creación de interfaces gráficas interactivas para solicitar input al usuario antes de la ejecución. |

## 🛠️ Estructura del Proyecto

```text
├── KeywordLibrary/          # Módulos con la lógica encapsulada
│   ├── api_manager.py       # Gestión de peticiones HTTP
│   ├── archive.py           # Gestión de compresión ZIP
│   ├── browser.py           # Traductor de subtítulos con Selenium
│   ├── email.py             # Cliente de correo
│   ├── excel.py             # Manejo de datos Excel
│   ├── pdf.py               # Herramientas PDF
│   └── word.py              # Automatización de MS Word
├── DataSets/                # Archivos de entrada para pruebas (.xlsx, .srt, .pdf)
├── output/                  # Carpeta generada con los resultados de la automatización
├── tasks.py                 # Punto de entrada principal (Main) que orquesta los robots
├── conda.yaml               # Definición del entorno y dependencias
└── robot.yaml               # Configuración de ejecución de Robocorp