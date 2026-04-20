"""
Script de demostración del Sistema de Logging
Muestra cómo se registran las operaciones en los archivos de log
"""

import sys
import os

# Agregar src al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from logger import (
    log_operación,
    log_inicio_ingesta,
    log_validacion,
    log_ingesta_exitosa,
    log_error_ingesta,
    obtener_log_file,
    obtener_error_log_file
)

print("=" * 80)
print("DEMOSTRACIÓN DEL SISTEMA DE LOGGING")
print("=" * 80)
print()

# Simular operaciones
print("📝 Registrando operaciones de prueba...")
print()

log_operación("Sistema iniciado", "Versión 1.0.0")
log_inicio_ingesta("datos_prueba.csv", 2048)
log_validacion("datos_prueba.csv", True)
log_ingesta_exitosa(
    "datos_prueba.csv",
    "datos_prueba_20260420_143025.csv",
    "data/raw/datos_prueba_20260420_143025.csv",
    100
)

log_operación("Prueba completada", "Sin errores")

print()
print("=" * 80)
print("ARCHIVOS DE LOG GENERADOS")
print("=" * 80)
print()
print(f"📄 Log general:  {obtener_log_file()}")
print(f"❌ Log errores:  {obtener_error_log_file()}")
print()
print("Abre estos archivos para ver los registros detallados.")
print()
