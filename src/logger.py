"""
Módulo de Logging para el Sistema de Ingesta Automatizada de Datos

Este módulo configura y proporciona funcionalidades de logging centralizadas
para registrar todas las operaciones del pipeline de ingesta.

Autor: Data Engineering Team
Fecha: 2026-04-20
"""

import logging
import os
from datetime import datetime


# ============================================================================
# CONFIGURACIÓN DE RUTAS DE LOGS
# ============================================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGS_DIR = os.path.join(BASE_DIR, "logs")

# Crear directorio de logs si no existe
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR, exist_ok=True)

# Rutas de archivos de log
LOG_FILE = os.path.join(LOGS_DIR, f"ingestion_{datetime.now().strftime('%Y%m%d')}.log")
ERROR_LOG_FILE = os.path.join(LOGS_DIR, f"ingestion_errors_{datetime.now().strftime('%Y%m%d')}.log")


# ============================================================================
# CONFIGURACIÓN DEL LOGGER
# ============================================================================

def configurar_logger():
    """
    Configura el logger principal del sistema con manejo de archivos.
    
    Retorna:
        logging.Logger: Logger configurado
    """
    logger = logging.getLogger("IngestionSystem")
    
    # Evitar duplicar handlers si ya existe
    if logger.handlers:
        return logger
    
    # Nivel de logging
    logger.setLevel(logging.DEBUG)
    
    # Formato de logs
    formato = logging.Formatter(
        '%(asctime)s | %(levelname)-8s | %(funcName)-20s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Handler para archivo general
    file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formato)
    logger.addHandler(file_handler)
    
    # Handler para archivo de errores
    error_handler = logging.FileHandler(ERROR_LOG_FILE, encoding='utf-8')
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formato)
    logger.addHandler(error_handler)
    
    return logger


# ============================================================================
# INSTANCIA GLOBAL DEL LOGGER
# ============================================================================

logger = configurar_logger()


# ============================================================================
# FUNCIONES DE LOGGING ESPECÍFICAS
# ============================================================================

def log_inicio_ingesta(nombre_archivo, tamaño):
    """
    Registra el inicio del proceso de ingesta.
    
    Parámetros:
        nombre_archivo: Nombre del archivo a ingestar
        tamaño: Tamaño del archivo en bytes
    """
    mensaje = f"INICIO INGESTA | Archivo: {nombre_archivo} | Tamaño: {tamaño} bytes"
    logger.info(mensaje)


def log_validacion(nombre_archivo, resultado, motivo=""):
    """
    Registra el resultado de la validación de archivo.
    
    Parámetros:
        nombre_archivo: Nombre del archivo validado
        resultado: True si validó correctamente, False si no
        motivo: Razón si la validación falló
    """
    if resultado:
        logger.info(f"VALIDACIÓN OK | Archivo: {nombre_archivo}")
    else:
        logger.warning(f"VALIDACIÓN FALLIDA | Archivo: {nombre_archivo} | Motivo: {motivo}")


def log_ingesta_exitosa(nombre_archivo, nombre_unico, ruta_destino, num_registros):
    """
    Registra una ingesta exitosa con detalles completos.
    
    Parámetros:
        nombre_archivo: Nombre original del archivo
        nombre_unico: Nombre único generado con timestamp
        ruta_destino: Ruta completa donde se guardó
        num_registros: Cantidad de registros procesados
    """
    mensaje = (
        f"INGESTA EXITOSA | Original: {nombre_archivo} | "
        f"Almacenado: {nombre_unico} | Registros: {num_registros} | "
        f"Ruta: {ruta_destino}"
    )
    logger.info(mensaje)


def log_error_ingesta(nombre_archivo, error_tipo, error_mensaje):
    """
    Registra un error durante la ingesta.
    
    Parámetros:
        nombre_archivo: Nombre del archivo que causó error
        error_tipo: Tipo de error (PermissionError, IOError, etc.)
        error_mensaje: Mensaje de error
    """
    mensaje = (
        f"ERROR INGESTA | Archivo: {nombre_archivo} | "
        f"Tipo: {error_tipo} | Detalle: {error_mensaje}"
    )
    logger.error(mensaje)


def log_operación(descripcion, detalles=""):
    """
    Registra una operación genérica del sistema.
    
    Parámetros:
        descripcion: Descripción de la operación
        detalles: Detalles adicionales opcionales
    """
    mensaje = f"OPERACIÓN | {descripcion}"
    if detalles:
        mensaje += f" | {detalles}"
    logger.info(mensaje)


# ============================================================================
# INFORMACIÓN DE LOGS
# ============================================================================

def obtener_ruta_logs():
    """Retorna la ruta del directorio de logs."""
    return LOGS_DIR


def obtener_log_file():
    """Retorna la ruta del archivo de log principal actual."""
    return LOG_FILE


def obtener_error_log_file():
    """Retorna la ruta del archivo de log de errores actual."""
    return ERROR_LOG_FILE
