# GUÍA RÁPIDA - RESTAURANTE APP SEMANA 13

## ⚡ INICIO RÁPIDO

### 1. Abrir PowerShell en la carpeta SEMANA 13
```powershell
cd C:\Users\Herobook\UEA\2626-POO-HIDALGO-JANETH\PARCIAL 2\SEMANA 13
```

### 2. Ejecutar la aplicación
```powershell
python -m restaurante_app.main
```

### 3. Hacer login
- Usuario: `12345`
- Contraseña: `1234`

### 4. Explorar
- Click en **Productos**: Ver 6 productos
- Click en **Usuarios**: Ver 3 usuarios
- Click en **Cerrar sesión**: Volver a login

---

## 📖 DOCUMENTOS DISPONIBLES

| Archivo | Para qué |
|---------|----------|
| **README.md** | Entender la estructura y el proyecto |
| **INSTRUCCIONES_EJECUCION.md** | Pasos detallados para ejecutar |
| **RESUMEN_EJECUTIVO.md** | Visión general del proyecto |
| **CHECKLIST_VERIFICACION.md** | Verificar que todo funciona |
| **ESTRUCTURA_DETALLADA.md** | Entender el código |
| **HOJA_ENTREGA.md** | Resumen de lo entregado |

---

## 🧪 VERIFICAR QUE FUNCIONA

### Prueba 1: Estructura
```powershell
python verificar_estructura.py
```
Debe mostrar: ✓ ESTRUCTURA VERIFICADA

### Prueba 2: Servicios
```powershell
python test_servicios.py
```
Debe mostrar: Todos los ✓

### Prueba 3: Aplicación
```powershell
python -m restaurante_app.main
```
Debe abrir ventana de login

---

## 🔑 CREDENCIALES (3 usuarios)

```
12345 / 1234     → Juan Pérez
67890 / 5678     → María García
11111 / 9999     → Carlos López
```

---

## 🏗️ ESTRUCTURA (en una línea)

```
restaurante_app/ → (main.py) datos/ modelos/ servicios/ ui/
```

---

## 💾 DATOS

**6 Productos** (productos.json):
1. Hamburguesa Clásica - $8.50
2. Pizza Margarita - $12.00
3. Ensalada César - $7.50
4. Pasta Carbonara - $10.50
5. Jugo Natural - $3.50
6. Postre de Chocolate - $5.00

**3 Usuarios** (usuarios.json):
1. Juan Pérez (12345)
2. María García (67890)
3. Carlos López (11111)

---

## 🎯 FLUJO SIMPLE

```
Inicio → Login → (valida) → Menú Principal
                    ↓
                  (error)
                    ↑
           Vuelve a pedir
```

---

## 📂 COMPONENTES CLAVE

| Componente | Archivo | Función |
|---|---|---|
| Entrada | main.py | Inicia la app |
| Autenticación | login_view.py | Pantalla de login |
| Interfaz | main_view.py | Menú principal |
| Datos | productos.json, usuarios.json | Información |
| Lógica | restaurante_servicio.py | Procesa datos |
| Lectura | archivo_servicio.py | Lee JSON |

---

## 🚀 EJECUTAR EN 3 PASOS

**Opción A - Más simple (Recomendado):**
```powershell
# 1. Ir a la carpeta
cd C:\Users\Herobook\UEA\2626-POO-HIDALGO-JANETH\PARCIAL 2\SEMANA 13

# 2. Ejecutar
python run.py

# 3. Ingresar
Usuario: 12345
Contraseña: 1234
```

**Opción B - En Windows (Doble click):**
- Abre la carpeta SEMANA 13
- Haz doble click en `ejecutar.bat`

**Opción C - Con módulo Python:**
```powershell
cd C:\Users\Herobook\UEA\2626-POO-HIDALGO-JANETH\PARCIAL 2\SEMANA 13
python -m restaurante_app.main
```

---

## ❓ PROBLEMAS COMUNES

| Problema | Solución |
|----------|----------|
| "ModuleNotFoundError" | Estar en carpeta SEMANA 13 |
| "No module named 'tkinter'" | Python no incluye Tkinter |
| La interfaz no abre | Ejecutar desde PowerShell |

---

## 📋 LO QUE ESTÁ LISTO

- ✅ Login funcional
- ✅ Ver productos
- ✅ Ver usuarios
- ✅ Cerrar sesión
- ✅ Datos precargados
- ✅ Documentación completa
- ✅ Pruebas incluidas

---

## ⏭️ PRÓXIMAS SEMANAS

En futuras semanas se agregarán:
- Ventas completas
- Agregar/editar/eliminar productos
- Reportes
- Más funcionalidades

---

**Estado**: ✅ Listo para usar
**Última actualización**: Semana 13

