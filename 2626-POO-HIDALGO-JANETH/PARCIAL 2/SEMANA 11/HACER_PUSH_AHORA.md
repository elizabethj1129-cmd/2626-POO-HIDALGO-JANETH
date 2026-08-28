# 🚀 PUSH A GITHUB - INSTRUCCIONES FINALES

## Tu repositorio local está 100% listo

**5 commits** con **33 archivos** esperando ser enviados a GitHub.

---

## 📋 OPCIÓN 1: Script Automático (Recomendado)

Abre PowerShell en la carpeta del proyecto y ejecuta:

```powershell
cd "C:\Users\Herobook\UEA\2626-POO-HIDALGO-JANETH\PARCIAL 2\SEMANA 11"
powershell -ExecutionPolicy Bypass -File push.ps1
```

**El script te pedirá:**
1. Tu usuario de GitHub
2. Nombre del repositorio (default: restaurante-app-semana11)
3. Tu contraseña/token

**¡Listo!**

---

## 📋 OPCIÓN 2: Comandos Manuales (Si prefieres)

```powershell
# 1. Ir a la carpeta
cd "C:\Users\Herobook\UEA\2626-POO-HIDALGO-JANETH\PARCIAL 2\SEMANA 11"

# 2. Agregar remoto (reemplaza TU_USUARIO)
git remote add origin https://github.com/TU_USUARIO/restaurante-app-semana11.git

# 3. Hacer push
git push -u origin main
```

---

## ⚠️ ANTES DE HACER PUSH

✓ Crear repositorio en https://github.com/new
  - Nombre: `restaurante-app-semana11`
  - Descripción: "Sistema de restaurante con ventas y persistencia JSON"
  - Público: ✓ (marcar)
  - Click: "Create repository"

✓ Tener listo:
  - Tu usuario de GitHub
  - Token de acceso personal (https://github.com/settings/tokens)
    - O tu contraseña

---

## 🔐 Autenticación

GitHub puede pedir:
- **Usuario:** Tu usuario de GitHub
- **Contraseña:** 
  - Si tienes 2FA: usar token de acceso personal
  - Si no: tu contraseña de GitHub

**Crear token (si lo necesitas):**
1. Ir a https://github.com/settings/tokens
2. Click "Generate new token"
3. Seleccionar permisos: `repo`
4. Copiar el token
5. Usarlo como "contraseña"

---

## ✅ Verificación

Después del push, deberías ver:

```
Enumerating objects...
Compressing objects...
Writing objects...
Updating references...
* [new branch] main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

Y tu repositorio estará en:
```
https://github.com/TU_USUARIO/restaurante-app-semana11
```

---

## 🎯 Pasos Finales

1. ✓ Crear repositorio en GitHub
2. ✓ Ejecutar script push.ps1 (o comandos manuales)
3. ✓ Compartir enlace con profesores
4. ✓ ¡Entrega completada!

---

**¡Listo para hacer push!**

