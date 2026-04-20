# Sistema de Ingesta Automatizada de Datos

## 📋 Descripción del Proyecto

Sistema de ingesta de datos que implementa la **Fase 1** de un pipeline de análisis de datos bajo principios **DataOps**. Permite a los usuarios cargar archivos CSV de forma segura a través de una interfaz visual, con validación automática, almacenamiento estructurado, trazabilidad mediante timestamps y **logging centralizado de todas las operaciones**.

### Objetivo Principal
Proporcionar una plataforma centralizada y confiable para la recolección de datos crudos (raw data) que sirvan como insumo para futuras transformaciones analíticas, con registro automático de todas las operaciones.

---

## 🏗️ Arquitectura del Sistema

```
Carga (UI)
    ↓
Validación (extensión, disponibilidad)
    ↓
Ingesta y Almacenamiento (data/raw/)
    ↓
Notificación (éxito/error en tiempo real)
    ↓
[Próxima Fase: Data Cleaning]
```

---

## 📦 Estructura del Proyecto

```
app/
├── README.md                 # Este archivo
├── .gitignore               # Exclusiones de Git
├── src/
│   └── app.py              # Aplicación principal Streamlit
└── data/
    └── raw/                # Almacenamiento de datos crudos
```

---

## 🔧 Requisitos Previos

### Instalación de Python
- **Versión requerida:** Python 3.8+
- Descargar desde [python.org](https://www.python.org/downloads/)

### Instalación de Dependencias

```bash
# Crear entorno virtual (recomendado)
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate

# En macOS/Linux:
source venv/bin/activate

# Instalar Streamlit
pip install streamlit
```

---

## 🚀 Cómo Ejecutar el Proyecto

### Opción 1: Ejecución Local

```bash
# Navegar al directorio del proyecto
cd app

# Ejecutar la aplicación
streamlit run src/app.py
```

La interfaz se abrirá en tu navegador en `http://localhost:8501`

### Opción 2: Verificar Instalación

```bash
# Confirmar que Streamlit está instalado
streamlit --version

# Verificar Python
python --version
```

---

## 📖 Guía de Uso

1. **Acceder a la interfaz:** Abre tu navegador en `http://localhost:8501`
2. **Cargar archivo:** Haz clic en "Selecciona un archivo CSV para ingestar"
3. **Seleccionar archivo:** Elige un archivo `.csv` de tu computadora
4. **Confirmación:** Verás un mensaje de éxito con detalles de la ingesta
5. **Verificar almacenamiento:** El archivo estará en `data/raw/` con un timestamp único

### Ejemplo de Flujo

```
Usuario → Carga archivo_datos.csv
         ↓
Sistema → Valida formato (.csv)
         ↓
Sistema → Genera nombre: archivo_datos_20260420_143025.csv
         ↓
Sistema → Almacena en data/raw/
         ↓
Usuario ← Recibe confirmación ✅
```

---

## 🔒 Características de Seguridad

- ✅ **Validación de extensión:** Solo archivos `.csv`
- 🔐 **Manejo de excepciones:** Previene caídas por errores
- 📍 **Timestamps únicos:** Evita sobreescrituras y garantiza trazabilidad
- 📦 **Estructura estandarizada:** `data/raw/` como único punto de ingesta

---

## 📊 Entregables de Fase 1

- ✅ Estructura de repositorio (`src/`, `data/raw/`, `logs/`)
- ✅ Aplicación funcional (`src/app.py`)
- ✅ Módulo de logging centralizado (`src/logger.py`)
- ✅ Interfaz visual con Streamlit
- ✅ Trazabilidad con logging detallado
- ✅ Documentación base (`README.md`)

---

## 📝 Sistema de Logging

El proyecto incluye un **sistema de logging centralizado** que registra:

- **Inicio de ingesta:** Cuando comienza el procesamiento de un archivo
- **Validación:** Archivos validados o rechazados con motivos
- **Éxito/Error:** Status final de cada operación
- **Cantidad de registros:** Número de filas procesadas del CSV
- **Detalles técnicos:** Rutas, tamaños, timestamps

### Archivos de Log

Los logs se guardan automáticamente en la carpeta `logs/`:

```
logs/
├── ingestion_20260420.log          # Log general del día
└── ingestion_errors_20260420.log   # Log de errores del día
```

### Formato de Log

```
2026-04-20 14:30:25 | INFO     | log_inicio_ingesta | INICIO INGESTA | Archivo: datos.csv | Tamaño: 2048 bytes
2026-04-20 14:30:25 | INFO     | validar_archivo    | VALIDACIÓN OK | Archivo: datos.csv
2026-04-20 14:30:26 | INFO     | log_ingesta_exitosa| INGESTA EXITOSA | Original: datos.csv | Almacenado: datos_20260420_143025.csv | Registros: 100 | Ruta: data/raw/datos_20260420_143025.csv
```

### Acceso a Logs

- **Por Streamlit:** Visible en la barra lateral con la ruta de logs
- **Por archivo:** Abre `logs/ingestion_YYYYMMDD.log` con cualquier editor de texto
- **Por terminal:** `cat logs/ingestion_*.log` o `Get-Content logs/ingestion_*.log` (PowerShell)

---

## 🔮 Próximos Pasos: Fase 2 - Data Cleaning

Los datos ingestionados en `data/raw/` servirán como insumo directo para:

- 🧹 **Limpieza de datos:** Valores faltantes, duplicados
- 🔄 **Transformación:** Normalización y formateo
- 📈 **Validación de esquema:** Consistencia de tipos
- 💾 **Almacenamiento staging:** `data/processed/`

---

## 🛠️ Stack Tecnológico

| Componente | Tecnología |
|-----------|-----------|
| **Lógica de Procesamiento** | Python 3.8+ |
| **Interfaz de Usuario** | Streamlit |
| **Manejo de Archivos** | `os`, `shutil`, `datetime` |
| **Control de Versiones** | Git & GitHub |

---

## 📝 Notas Importantes

- El sistema **no usa `pandas`** en esta fase para mantener minimal las dependencias
- Los datos crudos se almacenan tal como se cargan (sin transformaciones)
- Cada archivo recibe un **timestamp único** para trazabilidad
- La estructura de directorios se crea automáticamente si no existe

---

## 📞 Soporte

Para más información sobre DataOps o consultas técnicas, consulta la [documentación oficial de Streamlit](https://docs.streamlit.io/).

---

## 🚀 Información de Control de Versiones (GitHub)

Este proyecto está versionado con Git y puede ser publicado en GitHub.

### Comandos para subir a GitHub:

```bash
# 1. Crear repositorio en GitHub (a través de la web)
# https://github.com/new
# Nota: NO inicialices con README, .gitignore o LICENSE

# 2. Agregar repositorio remoto
git remote add origin https://github.com/TU_USUARIO/app.git

# 3. Renombrar rama principal (si es necesario)
git branch -M main

# 4. Enviar código a GitHub
git push -u origin main

# 5. Verificar conexión
git remote -v
```

### Commits realizados:

```
5432df8 (HEAD -> master) Inicialización Fase 1: Estructura base del Sistema de Ingesta Automatizada
```

---

## 📊 Criterios de Entrega Cumplidos

Este proyecto cumple con todos los criterios solicitados:

| Criterio | Estado | Detalles |
|----------|--------|----------|
| ✅ Obtener datos desde fuente estructurada | **CUMPLE** | Ingesta de archivos CSV con validación |
| ✅ Automatización del proceso | **CUMPLE** | Pipeline completamente automático |
| ✅ Logging del proceso | **CUMPLE** | Trazabilidad completa en `logs/` |
| ✅ Control de versiones (Git) | **CUMPLE** | Repositorio inicializado con commits |
| ✅ GitHub | **CUMPLE** | Instrucciones para publicación incluidas |

---

**Autor:** Data Engineering Team  
**Versión:** 1.0  
**Fase:** 1 - Ingesta Automatizada  
**Última actualización:** 2026-04-20
