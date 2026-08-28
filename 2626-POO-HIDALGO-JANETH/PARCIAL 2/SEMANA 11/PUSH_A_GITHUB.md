# 🚀 INSTRUCCIONES PARA PUSH A GITHUB

## ✅ Commit Local Completado

El commit local ha sido realizado exitosamente con:
- **27 archivos** agregados
- **4515 líneas** de código/documentación
- **Commit:** "Semana 11: Sistema de ventas con persistencia JSON"

---

## 📋 PASOS PARA HACER PUSH A GITHUB

### Opción 1: Crear Repositorio Nuevo en GitHub (Recomendado)

#### PASO 1: Crear repositorio en GitHub.com
1. Ir a https://github.com/new
2. Llenar los datos:
   - **Repository name:** `restaurante-app-semana11`
   - **Description:** "Sistema de restaurante con operaciones de venta y persistencia JSON"
   - **Public:** ✓ (marcar para que sea público)
   - **Add .gitignore:** No es necesario (ya lo tenemos)
   - **Add a license:** Opcional

3. Hacer clic en "Create repository"

#### PASO 2: Agregar remoto y hacer push
```bash
# Desde PowerShell en la carpeta SEMANA 11:

# Cambiar rama principal a "main" (estándar en GitHub)
git branch -M main

# Agregar el repositorio remoto (reemplaza USUARIO con tu usuario de GitHub)
git remote add origin https://github.com/USUARIO/restaurante-app-semana11.git

# Hacer push del código al repositorio remoto
git push -u origin main
```

---

### Opción 2: Si Ya Tienes un Repositorio

```bash
git remote add origin https://github.com/USUARIO/restaurante-app-semana11.git
git branch -M main
git push -u origin main
```

---

## 🔐 Autenticación en GitHub

### Si es la Primera Vez:

GitHub puede pedir autenticación. Hay dos formas:

#### A) Token de Acceso Personal (Recomendado)
1. Ir a https://github.com/settings/tokens
2. Generar nuevo token (classic)
3. Seleccionar permisos: `repo`, `user`
4. Copiar el token
5. Cuando pida contraseña, pegar el token

#### B) SSH (Más Seguro)
```bash
# Generar clave SSH (si no la tienes)
ssh-keygen -t ed25519 -C "tu_email@example.com"

# Agregar la clave a GitHub:
# Ir a https://github.com/settings/keys
# Pegar el contenido de ~/.ssh/id_ed25519.pub

# Usar URL SSH en lugar de HTTPS:
git remote add origin git@github.com:USUARIO/restaurante-app-semana11.git
```

---

## ✅ VERIFICAR QUE TODO ESTÉ LISTO

Antes de hacer push, verifica:

```bash
# Ver estado del repositorio
git status

# Ver logs (commits)
git log

# Ver remoto configurado
git remote -v

# Mostrar rama actual
git branch
```

---

## 📊 RESUMEN DEL PUSH

Después de hacer push, tu repositorio en GitHub tendrá:

```
✓ 27 archivos
✓ Código Python (1000+ líneas)
✓ Documentación (7 archivos)
✓ Tests automatizados
✓ Scripts de utilidad
✓ .gitignore configurado
✓ Historial de commits
```

---

## 🎯 COMANDO RÁPIDO (COPIAR Y PEGAR)

```bash
cd "C:\Users\Herobook\UEA\2626-POO-HIDALGO-JANETH\PARCIAL 2\SEMANA 11"

# Cambiar rama a main
git branch -M main

# Agregar remoto (cambia USUARIO por tu usuario de GitHub)
git remote add origin https://github.com/USUARIO/restaurante-app-semana11.git

# Hacer push
git push -u origin main
```

---

## 🔗 RESULTADO FINAL

Después de completar, tu repositorio estará en:
```
https://github.com/USUARIO/restaurante-app-semana11
```

---

## ❓ SOLUCIÓN DE PROBLEMAS

### Error: "fatal: remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/USUARIO/restaurante-app-semana11.git
```

### Error: "Authentication failed"
Asegúrate de:
- Usar token de acceso o SSH correctamente
- Tener permisos en GitHub
- Repositorio creado en GitHub.com

### Cambiar remoto después
```bash
git remote set-url origin https://github.com/USUARIO/nuevo-repositorio.git
```

---

## 📝 NOTAS FINALES

- El repositorio es **público** (requerimiento de entrega)
- Contiene **todo el código** necesario
- Incluye **documentación profesional**
- Está **listo para revisión**
- Puede ser **compartido como enlace**

---

**¡Listo! Después de hacer push, compartir el enlace del repositorio con los profesores.**

Enlace para compartir:
```
https://github.com/USUARIO/restaurante-app-semana11
```

---

Realizado: 26 de agosto de 2026

