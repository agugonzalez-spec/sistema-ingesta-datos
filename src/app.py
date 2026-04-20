"""
Sistema de Ingesta Automatizada de Datos - Fase 1
Módulo principal de la aplicación Streamlit para carga y almacenamiento de datos.

Autor: Data Engineering Team
Fecha: 2026-04-20
"""

import streamlit as st
import os
import shutil
from datetime import datetime
from logger import (
    log_inicio_ingesta,
    log_validacion,
    log_ingesta_exitosa,
    log_error_ingesta,
    log_operación,
    obtener_ruta_logs
)


# ============================================================================
# CONFIGURACIÓN INICIAL DE STREAMLIT
# ============================================================================

st.set_page_config(
    page_title="Sistema de Ingesta de Datos",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("📊 Sistema de Ingesta Automatizada de Datos")
st.markdown("**Fase 1:** Carga, Validación y Almacenamiento de Datos Crudos")
st.markdown("---")


# ============================================================================
# CONFIGURACIÓN DE RUTAS
# ============================================================================

# Definir rutas base (relativas al directorio de ejecución)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DATA_DIR = os.path.join(BASE_DIR, "data", "raw")


# ============================================================================
# FUNCIÓN: Crear estructura de directorios
# ============================================================================

def crear_estructura_directorios():
    """
    Crea la estructura de directorios necesaria si no existe.
    
    Garantiza que el directorio `data/raw/` esté disponible para
    almacenar los archivos crudos ingestionados.
    """
    try:
        if not os.path.exists(RAW_DATA_DIR):
            os.makedirs(RAW_DATA_DIR, exist_ok=True)
            return True
    except Exception as e:
        st.error(f"❌ Error al crear estructura de directorios: {str(e)}")
        return False
    return True


# ============================================================================
# FUNCIÓN: Validar archivo cargado
# ============================================================================

def validar_archivo(archivo_cargado):
    """
    Valida que el archivo cargado sea del tipo permitido.
    
    Parámetros:
        archivo_cargado: Objeto UploadedFile de Streamlit
    
    Retorna:
        bool: True si el archivo es válido, False en caso contrario
    """
    # Extensiones permitidas
    extensiones_permitidas = {".csv"}
    
    # Obtener extensión del archivo
    nombre_archivo = archivo_cargado.name
    _, extension = os.path.splitext(nombre_archivo)
    
    if extension.lower() not in extensiones_permitidas:
        motivo = f"Extensión no permitida: {extension}"
        log_validacion(nombre_archivo, False, motivo)
        st.error(f"❌ Formato de archivo no permitido: {extension}")
        st.info(f"✅ Extensiones permitidas: {', '.join(extensiones_permitidas)}")
        return False
    
    log_validacion(nombre_archivo, True)
    return True


# ============================================================================
# FUNCIÓN: Generar nombre único con timestamp
# ============================================================================

def generar_nombre_archivo_unico(nombre_original):
    """
    Genera un nombre único para el archivo agregando timestamp.
    
    Esto garantiza:
    - Trazabilidad: saber cuándo se ingirió cada archivo
    - Evitar sobreescrituras: archivos con mismo nombre no se pierden
    
    Parámetros:
        nombre_original: Nombre del archivo original
    
    Retorna:
        str: Nombre modificado con timestamp (ej: data_20260420_143025.csv)
    """
    nombre_sin_extension, extension = os.path.splitext(nombre_original)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_unico = f"{nombre_sin_extension}_{timestamp}{extension}"
    
    return nombre_unico


# ============================================================================
# FUNCIÓN: Guardar archivo en data/raw/
# ============================================================================

def guardar_archivo(archivo_cargado, nombre_archivo_unico):
    """
    Guarda el archivo cargado en la ruta estandarizada data/raw/.
    
    Implementa manejo de excepciones para evitar fallos abruptos
    de la aplicación e incluye conteo de registros.
    
    Parámetros:
        archivo_cargado: Objeto UploadedFile de Streamlit
        nombre_archivo_unico: Nombre único generado con timestamp
    
    Retorna:
        tuple: (bool, str, int) - (éxito, ruta_guardada_o_error, num_registros)
    """
    try:
        # Construir ruta completa del destino
        ruta_destino = os.path.join(RAW_DATA_DIR, nombre_archivo_unico)
        
        # Guardar archivo y contar registros
        contenido = archivo_cargado.getbuffer()
        with open(ruta_destino, "wb") as f:
            f.write(contenido)
        
        # Contar número de registros (líneas) en el CSV
        # Decodificar el contenido para contar líneas
        contenido_texto = contenido.tobytes().decode('utf-8')
        num_registros = len(contenido_texto.strip().split('\n')) - 1  # -1 para excluir header
        
        return True, ruta_destino, num_registros
    
    except PermissionError as e:
        log_error_ingesta(archivo_cargado.name, "PermissionError", str(e))
        return False, "❌ Permiso denegado al escribir el archivo", 0
    except IOError as e:
        log_error_ingesta(archivo_cargado.name, "IOError", str(e))
        return False, f"❌ Error de entrada/salida: {str(e)}", 0
    except Exception as e:
        log_error_ingesta(archivo_cargado.name, type(e).__name__, str(e))
        return False, f"❌ Error inesperado al guardar: {str(e)}", 0


# ============================================================================
# FLUJO PRINCIPAL DE LA APLICACIÓN
# ============================================================================

# Crear estructura de directorios al iniciar
crear_estructura_directorios()
log_operación("Sistema iniciado", f"Directorio de logs: {obtener_ruta_logs()}")

# Sección 1: Información del usuario
st.sidebar.markdown("### 📝 Información")
st.sidebar.markdown("""
Este sistema permite cargar archivos CSV que serán:
- ✅ Validados
- 📦 Almacenados en `data/raw/`
- 🔐 Identificados con timestamp para trazabilidad
- 📝 Todos los eventos quedan registrados en logs/
""")

st.sidebar.markdown("---")
st.sidebar.markdown(f"**Ruta de almacenamiento:** `{RAW_DATA_DIR}`")
st.sidebar.markdown(f"**Ruta de logs:** `{obtener_ruta_logs()}`")

# Sección 2: Componente de carga de archivo
st.markdown("### 📤 Cargar Dataset")
archivo_cargado = st.file_uploader(
    "Selecciona un archivo CSV para ingestar",
    type="csv",
    key="file_uploader"
)

# Sección 3: Procesar archivo si se cargó
if archivo_cargado is not None:
    st.markdown("---")
    st.markdown("### ⚙️ Procesando...")
    
    # Registrar inicio de ingesta
    log_inicio_ingesta(archivo_cargado.name, archivo_cargado.size)
    
    # Paso 1: Validar archivo
    if validar_archivo(archivo_cargado):
        
        # Paso 2: Generar nombre único con timestamp
        nombre_unico = generar_nombre_archivo_unico(archivo_cargado.name)
        
        # Paso 3: Guardar archivo
        exito, resultado, num_registros = guardar_archivo(archivo_cargado, nombre_unico)
        
        # Notificar resultado al usuario
        if exito:
            # Registrar éxito
            log_ingesta_exitosa(
                archivo_cargado.name,
                nombre_unico,
                resultado,
                num_registros
            )
            
            st.success(f"✅ **Archivo ingestionado exitosamente**")
            st.markdown(f"""
            **Detalles de la ingesta:**
            - 📄 Nombre original: `{archivo_cargado.name}`
            - 🏷️ Nombre único: `{nombre_unico}`
            - 📦 Tamaño: `{archivo_cargado.size} bytes`
            - 📊 Registros procesados: `{num_registros}`
            - 📍 Ubicación: `{resultado}`
            - ⏰ Timestamp: `{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}`
            """)
            
            # Información para la próxima fase
            st.info("""
            ℹ️ **Próxima Fase (Data Cleaning):**
            Este archivo ahora está disponible en `data/raw/` para ser procesado
            en la etapa de limpieza y transformación de datos.
            """)
        else:
            st.error(resultado)

# Pie de página con información de la versión
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; font-size: 12px;'>
    Sistema de Ingesta Automatizada v1.0 | Fase 1 | 2026
</div>
""", unsafe_allow_html=True)
