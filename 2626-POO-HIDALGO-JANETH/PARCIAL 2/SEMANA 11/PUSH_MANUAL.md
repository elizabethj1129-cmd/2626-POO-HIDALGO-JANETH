# PASO A PASO: PUSH A GITHUB

## ✅ TU REPOSITORIO LOCAL ESTÁ LISTO

Tienes 3 commits con 30 archivos listos para compartir.

---

## 🚀 SIGUE ESTOS PASOS:

### PASO 1: Ir a GitHub y crear un nuevo repositorio

1. Abre: https://github.com/new
2. Completa:
   - Repository name: `restaurante-app-semana11`
   - Description: "Sistema de restaurante con ventas y persistencia JSON"
   - Public: ✓ (marcar)
3. Clic en "Create repository"

---

### PASO 2: Ejecuta estos comandos en PowerShell

Copia y pega uno por uno:

```powershell
# Ir a la carpeta del proyecto
cd "C:\Users\Herobook\UEA\2626-POO-HIDALGO-JANETH\PARCIAL 2\SEMANA 11"

# Cambiar rama de master a main
git branch -M main

# Agregar tu repositorio remoto (cambia TU_USUARIO por tu usuario de GitHub)
git remote add origin https://github.com/TU_USUARIO/restaurante-app-semana11.git

# Hacer push
git push -u origin main
```

---

### PASO 3: Cuando pida contraseña/token

- **Usuario:** Tu usuario de GitHub
- **Contraseña:** Usa un token de acceso personal
  - Crear en: https://github.com/settings/tokens
  - Permisos: `repo`

---

### PASO 4: ¡Verifica!

Tu repositorio estará en:
```
https://github.com/TU_USUARIO/restaurante-app-semana11
```

Comparte este enlace con tus profesores.

---

## 💡 EJEMPLO COMPLETO

Si tu usuario de GitHub es `janed`:

```powershell
cd "C:\Users\Herobook\UEA\2626-POO-HIDALGO-JANETH\PARCIAL 2\SEMANA 11"
git branch -M main
git remote add origin https://github.com/janed/restaurante-app-semana11.git
git push -u origin main
```

---

**¡Eso es todo! El proyecto estará en GitHub.**

