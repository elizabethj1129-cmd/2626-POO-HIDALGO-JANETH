# CHECKLIST DE VERIFICACIÓN - SEMANA 13

Completa las siguientes verificaciones antes de entregar:

## ✓ Estructura del Proyecto

### Carpetas Principales
- [x] restaurante_app/ existe
- [x] restaurante_app/datos/ existe
- [x] restaurante_app/modelos/ existe
- [x] restaurante_app/servicios/ existe
- [x] restaurante_app/ui/ existe

### Archivos de Datos
- [x] restaurante_app/datos/productos.json existe
- [x] restaurante_app/datos/usuarios.json existe
- [x] productos.json contiene productos válidos
- [x] usuarios.json contiene usuarios válidos

### Archivos de Modelos
- [x] restaurante_app/modelos/__init__.py existe
- [x] restaurante_app/modelos/producto.py existe
- [x] restaurante_app/modelos/usuario.py existe
- [x] Producto es una dataclass
- [x] Usuario es una dataclass
- [x] Ambos tienen método to_dict()

### Archivos de Servicios
- [x] restaurante_app/servicios/__init__.py existe
- [x] restaurante_app/servicios/archivo_servicio.py existe
- [x] restaurante_app/servicios/restaurante_servicio.py existe
- [x] ArchivoServicio carga desde JSON
- [x] ArchivoServicio guarda en JSON
- [x] RestauranteServicio usa ArchivoServicio

### Archivos de UI
- [x] restaurante_app/ui/__init__.py existe
- [x] restaurante_app/ui/login_view.py existe
- [x] restaurante_app/ui/main_view.py existe
- [x] LoginView usa Tkinter
- [x] MainView usa Tkinter

### Archivo Principal
- [x] restaurante_app/main.py existe
- [x] main.py tiene RestauranteApp class
- [x] main.py tiene función main()

### Documentación
- [x] README.md existe en SEMANA 13
- [x] README.md describe la estructura
- [x] README.md describe el flujo
- [x] README.md tiene instrucciones de ejecución

## ✓ Funcionalidad

### Servicios
- [x] RestauranteServicio carga productos correctamente
- [x] RestauranteServicio carga usuarios correctamente
- [x] validar_acceso() funciona con credenciales válidas
- [x] validar_acceso() rechaza credenciales inválidas
- [x] buscar_producto() encuentra productos
- [x] buscar_usuario() encuentra usuarios
- [x] listar_productos() retorna lista
- [x] listar_usuarios() retorna lista

### Interfaz de Login
- [x] LoginView se muestra al iniciar
- [x] Campos de entrada de usuario y contraseña
- [x] Botón de ingreso funciona
- [x] Campos vacíos muestran error
- [x] Credenciales inválidas muestran error
- [x] Credenciales válidas aceptan login
- [x] Enter en contraseña envía formulario

### Interfaz Principal
- [x] MainView se muestra después de login válido
- [x] Muestra nombre del usuario autenticado
- [x] Botón Productos funciona
- [x] Botón Usuarios funciona
- [x] Botón Ventas está deshabilitado (pendiente)
- [x] Botón Cerrar sesión funciona
- [x] Cerrar sesión regresa a LoginView
- [x] La información se actualiza correctamente

### Datos
- [x] Los productos se muestran desde JSON
- [x] Los usuarios se muestran desde JSON
- [x] La información no se lee directamente en vistas
- [x] RestauranteServicio es intermediario

### Arquitectura
- [x] Una sola ventana Tkinter (Tk())
- [x] Un solo mainloop()
- [x] Cambio de vistas dentro de la misma ventana
- [x] Separación entre modelos, servicios y vistas
- [x] Imports relativos en módulos
- [x] Manejo correcto de rutas

## ✓ Ejecución

### Pruebas Básicas
Ejecuta estos comandos en PowerShell:

```powershell
# Paso 1: Navegar a SEMANA 13
cd C:\Users\Herobook\UEA\2626-POO-HIDALGO-JANETH\PARCIAL 2\SEMANA 13

# Paso 2: Verificar estructura
python verificar_estructura.py
# Debería mostrar: ✓ ESTRUCTURA VERIFICADA

# Paso 3: Probar servicios
python test_servicios.py
# Debería mostrar todos los ✓

# Paso 4: Ejecutar aplicación
python -m restaurante_app.main
# Debería abrir ventana de login
```

### Checklist de Ejecución
- [ ] verificar_estructura.py pasa sin errores
- [ ] test_servicios.py muestra todos los ✓
- [ ] La aplicación abre sin errores
- [ ] Se muestra LoginView
- [ ] Los campos de entrada funcionan
- [ ] Puedo ingresar usuario 12345 con contraseña 1234
- [ ] Login exitoso muestra MainView
- [ ] Productos muestran los 6 productos del JSON
- [ ] Usuarios muestran los 3 usuarios del JSON
- [ ] Cerrar sesión regresa a LoginView en la misma ventana

## ✓ Código

### Calidad
- [ ] Sin errores de sintaxis
- [ ] Sin errores de importación
- [ ] Nombres descriptivos en variables y funciones
- [ ] Docstrings en clases y métodos
- [ ] Manejo de excepciones donde es necesario

### Responsabilidades
- [ ] Modelos: representan entidades
- [ ] Servicios: lógica de negocio
- [ ] Vistas: interfaz gráfica
- [ ] ArchivoServicio: lectura/escritura JSON
- [ ] main.py: orquestación y punto de entrada

## ✓ Documentación

- [ ] README.md describe el propósito
- [ ] README.md describe la estructura
- [ ] README.md describe el flujo
- [ ] README.md tiene instrucciones de ejecución
- [ ] README.md lista credenciales de prueba
- [ ] INSTRUCCIONES_EJECUCION.md existe
- [ ] RESUMEN_EJECUTIVO.md existe

## ✓ Credenciales de Prueba

Para login, usar:

```
Usuario: 12345
Contraseña: 1234

Usuario: 67890
Contraseña: 5678

Usuario: 11111
Contraseña: 9999
```

Todas estas credenciales están en usuarios.json

## ✓ Datos de Ejemplo

### Productos (6 items)
- P001: Hamburguesa Clásica - $8.50
- P002: Pizza Margarita - $12.00
- P003: Ensalada César - $7.50
- P004: Pasta Carbonara - $10.50
- P005: Jugo Natural - $3.50
- P006: Postre de Chocolate - $5.00

### Usuarios (3 items)
- 12345: Juan Pérez
- 67890: María García
- 11111: Carlos López

---

## Resumen Final

**Estado General**: ✓ Completo

Si todos los items están marcados como ✓, el proyecto está listo para:
1. Demostración
2. Evaluación
3. Publicación en GitHub
4. Entrega final

**Nota**: Los archivos de prueba (test_servicios.py, verificar_estructura.py) pueden ser incluidos en el repositorio de GitHub como referencias de verificación, aunque no son obligatorios en la entrega.

---

Última actualización: Semana 13

