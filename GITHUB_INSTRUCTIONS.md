# 🌐 Instrucciones para GitHub

## Requisitos Previos

- Tener una cuenta en [GitHub](https://github.com)
- Tener instalado [Git](https://git-scm.com/downloads)
- Credenciales de GitHub configuradas

---

## 📤 Pasos para Publicar en GitHub

### 1. **Crear repositorio en GitHub (Opción A - GUI)**

1. Ir a [github.com/new](https://github.com/new)
2. Completar:
   - **Repository name:** `sistema-ingesta-datos` (o el nombre deseado)
   - **Description:** `Sistema de Ingesta Automatizada de Datos - Fase 1`
   - **Visibility:** `Public` (o `Private` si prefieres)
   - **NO marques:** "Initialize this repository with..."
3. Click en **Create repository**
4. Copiar la URL del repositorio (HTTPS o SSH)

### 2. **Conectar repositorio local a GitHub**

En PowerShell, en la carpeta del proyecto:

```powershell
cd c:\Users\SSDD\Desktop\app

# Opción A: HTTPS (recomendado para principiantes)
git remote add origin https://github.com/TU_USUARIO/sistema-ingesta-datos.git

# Opción B: SSH (si tienes configuradas claves SSH)
git remote add origin git@github.com:TU_USUARIO/sistema-ingesta-datos.git

# Verificar conexión
git remote -v
```

### 3. **Renombrar rama principal (si es necesario)**

```powershell
# Git modern usa 'main' como por defecto, nosotros tenemos 'master'
git branch -M main
```

### 4. **Enviar código a GitHub**

```powershell
# Primera vez: push con -u (establece tracking)
git push -u origin main

# Posteriores: solo
git push
```

### 5. **Verificar en GitHub**

1. Ir a tu repositorio en GitHub
2. Deberías ver todos los archivos del proyecto
3. El README.md se mostrará automáticamente

---

## 📝 Flujo de Commits Futuro

Después de hacer cambios locales:

```powershell
# Ver estado
git status

# Agregar cambios
git add .
# O específicos con:
git add archivo.py

# Hacer commit
git commit -m "Descripción clara del cambio"

# Enviar a GitHub
git push
```

### Ejemplos de buenos mensajes de commit:

```
git commit -m "feat: agregar validación de tamaño de archivo"
git commit -m "fix: corregir conteo de registros en CSV"
git commit -m "docs: actualizar README con instrucciones de logging"
git commit -m "refactor: mejorar estructura del logger"
```

---

## 🔐 Autenticación GitHub (Si solicita contraseña)

**Nota:** GitHub no permite autenticación por contraseña en 2024+

### Opción 1: Token Personal (Recomendado)

1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token
3. Scopes: Marcar `repo` y `workflow`
4. Copiar el token
5. Cuando Git solicite contraseña, usar el token

### Opción 2: SSH Keys

1. Generar clave: `ssh-keygen -t ed25519 -C "tu_email@ejemplo.com"`
2. Copiar contenido de `~/.ssh/id_ed25519.pub`
3. GitHub → Settings → SSH and GPG keys → New SSH key
4. Usar URL SSH en `git remote`

---

## 📊 Estructura que verás en GitHub

```
sistema-ingesta-datos/
├── README.md
├── GITHUB_INSTRUCTIONS.md
├── .gitignore
├── src/
│   ├── app.py
│   └── logger.py
├── data/
│   └── raw/
│       └── .gitkeep
└── logs/
    └── .gitkeep
```

---

## ✨ Extras: Mejorar tu GitHub

### Agregar badge al README

```markdown
[![Código en GitHub](https://img.shields.io/badge/GitHub-sistema--ingesta--datos-blue?logo=github)](https://github.com/TU_USUARIO/sistema-ingesta-datos)
```

### Crear etiqueta (tag) para versión

```powershell
git tag -a v1.0.0 -m "Versión 1.0.0 - Fase 1 completa"
git push origin v1.0.0
```

### Ver historial de commits

```powershell
git log --oneline
git log --graph --all --decorate
```

---

## 🆘 Troubleshooting

### Error: "remote origin already exists"
```powershell
git remote remove origin
git remote add origin https://github.com/TU_USUARIO/sistema-ingesta-datos.git
```

### Error: "fatal: not a git repository"
```powershell
# Asegúrate de estar en c:\Users\SSDD\Desktop\app
cd c:\Users\SSDD\Desktop\app
```

### Cambiar URL del repositorio remoto
```powershell
git remote set-url origin https://github.com/TU_USUARIO/NUEVO_NOMBRE.git
```

---

**¡Listo!** Tu proyecto está en control de versiones y publicable en GitHub. 🚀
