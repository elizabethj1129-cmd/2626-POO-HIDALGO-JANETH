# Instrucciones de Uso - restaurante_app Semana 11

## Prerrequisitos

- Python 3.7 o superior
- Sistema operativo: Windows, macOS o Linux
- Sin dependencias externas adicionales

## Estructura del Proyecto

```
SEMANA 11/
├── restaurante_app/
│   ├── __init__.py
│   ├── main.py                    # Punto de entrada principal
│   ├── datos/
│   │   ├── productos.json         # Persistencia de productos
│   │   ├── usuarios.json          # Persistencia de usuarios
│   │   └── ventas.json            # Persistencia de ventas
│   ├── modelos/
│   │   ├── __init__.py
│   │   ├── producto.py            # Clase Producto
│   │   ├── usuario.py             # Clase Usuario
│   │   └── venta.py               # Clase Venta
│   └── servicios/
│       ├── __init__.py
│       ├── archivo_servicio.py    # Servicio de persistencia JSON
│       └── restaurante.py         # Servicio de lógica de negocio
├── test_restaurante.py            # Pruebas automatizadas (opcional)
├── README.md                       # Documentación del proyecto
├── .gitignore                      # Configuración para Git
└── INSTRUCCIONES.md               # Este archivo
```

## Ejecución del Programa

### En Windows (PowerShell o CMD)

```powershell
cd "C:\Ruta\A\SEMANA 11"
python restaurante_app/main.py
```

O directamente desde el directorio raíz del proyecto:

```powershell
python restaurante_app\main.py
```

### En macOS / Linux

```bash
cd /ruta/a/SEMANA\ 11
python restaurante_app/main.py
```

O con Python 3 específicamente:

```bash
python3 restaurante_app/main.py
```

## Ejecución de Pruebas (Opcional)

Para ejecutar las pruebas automatizadas:

```bash
python test_restaurante.py
```

Esto ejecutará una serie de tests que verifican:
- Creación y validación de productos
- Creación y validación de usuarios
- Creación y validación de ventas
- Operaciones del servicio Restaurante
- Verificación de archivos JSON

## Flujo de Uso del Programa

### 1. Inicio del Programa

Al ejecutar, se carga:
- Todos los productos desde `datos/productos.json`
- Todos los usuarios desde `datos/usuarios.json`
- Todas las ventas desde `datos/ventas.json`

Si los archivos no existen, se inicia con listas vacías.

### 2. Menú Principal

```
========================================
        SISTEMA DE RESTAURANTE
========================================
PRODUCTOS:
  1. Registrar producto
  2. Buscar producto
  3. Actualizar producto
  4. Eliminar producto
  5. Listar productos
----------------------------------------
USUARIOS:
  6. Registrar usuario
  7. Listar usuarios
----------------------------------------
CONSULTAS:
  8. Mostrar categorías
----------------------------------------
VENTAS:
  9. Vender producto
  10. Consultar ventas de un usuario
----------------------------------------
  11. Salir
========================================
```

### 3. Operaciones Disponibles

#### Productos

**1. Registrar producto**
- Solicita: Código, Nombre, Categoría, Precio, Stock
- Valida: Código único, valores numéricos válidos
- Guarda: productos.json

**2. Buscar producto**
- Solicita: Código a buscar
- Muestra: Información completa del producto

**3. Actualizar producto**
- Solicita: Código del producto a actualizar
- Permite: Cambiar nombre, categoría, precio, stock (opcionalmente)
- Guarda: productos.json

**4. Eliminar producto**
- Solicita: Código del producto
- Elimina: Producto de la colección
- Guarda: productos.json

**5. Listar productos**
- Muestra: Todos los productos con sus detalles

#### Usuarios

**6. Registrar usuario**
- Solicita: Identificación, Nombre, Correo
- Valida: Identificación única
- Guarda: usuarios.json

**7. Listar usuarios**
- Muestra: Todos los usuarios registrados

#### Consultas

**8. Mostrar categorías**
- Muestra: Lista de categorías únicas en orden alfabético

#### Ventas (Nuevas en Semana 11)

**9. Vender producto**
- Proceso:
  1. Solicita identificación del usuario
  2. Solicita código del producto
  3. Solicita cantidad a vender
  4. Valida: Usuario existe, Producto existe, Cantidad > 0, Stock suficiente
  5. Si válido: Crea Venta, disminuye stock, guarda cambios
  6. Si inválido: Muestra error específico, no modifica datos

**10. Consultar ventas de un usuario**
- Solicita: Identificación del usuario
- Muestra: Todas las ventas del usuario con:
  - Nombre del producto y código
  - Cantidad vendida
  - Precio unitario y subtotal
  - Fecha de la venta
  - Total de artículos vendidos

#### Salida

**11. Salir**
- Cierra el programa
- Todos los datos permanecen guardados en JSON

## Ejemplo de Sesión Completa

```
Seleccione una opción: 6
Identificación: 1234567890
Nombre: Juan García
Correo: juan@example.com
Usuario registrado correctamente.

Seleccione una opción: 1
Código del producto: P001
Nombre: Hamburguesa
Categoría: Comida Rápida
Precio: 12.50
Stock disponible: 20
Producto registrado correctamente.

Seleccione una opción: 9
--- Realizar una venta ---
Identificación del usuario: 1234567890
Código del producto: P001
Cantidad a vender: 3
Venta registrada exitosamente: Venta: Usuario 1234567890 | Producto P001 | Cantidad: 3 | Fecha: 2026-08-26 15:30:45

Seleccione una opción: 10
--- Consultar ventas de un usuario ---
Identificación del usuario: 1234567890

Ventas del usuario: Juan García (1234567890)
======================================================================
  Producto: Hamburguesa (P001)
  Cantidad: 3
  Precio unitario: $12.50
  Subtotal: $37.50
  Fecha: 2026-08-26 15:30:45
----------------------------------------------------------------------
Total de artículos vendidos: 3

Seleccione una opción: 11
Saliendo...
```

## Validaciones y Restricciones

### Productos
- Código debe ser único
- Stock no puede ser negativo
- Precio debe ser numérico positivo
- No se permiten campos vacíos

### Usuarios
- Identificación debe ser única
- No se permiten campos vacíos

### Ventas
- Usuario debe existir en el sistema
- Producto debe existir en el sistema
- Cantidad debe ser mayor que cero
- Stock disponible debe ser ≥ cantidad solicitada
- No se permite vender si alguna validación falla

## Manejo de Errores

El programa maneja los siguientes errores:

- **FileNotFoundError**: Inicia con colecciones vacías si los archivos JSON no existen
- **JSONDecodeError**: Informa al usuario y continúa con colecciones vacías
- **PermissionError**: Notifica sobre permisos insuficientes
- **ValueError**: Valida campos de entrada
- **KeyError**: Omite registros con claves faltantes

## Persistencia de Datos

### Cuándo se guardan los datos

| Operación | Archivos guardados |
|-----------|-------------------|
| Registrar producto | `productos.json` |
| Actualizar producto | `productos.json` |
| Eliminar producto | `productos.json` |
| Registrar usuario | `usuarios.json` |
| Realizar venta | `ventas.json` + `productos.json` (nuevo stock) |

### Recuperación de datos

Al iniciar el programa:
1. Se cargan todos los productos desde `productos.json`
2. Se cargan todos los usuarios desde `usuarios.json`
3. Se cargan todas las ventas desde `ventas.json`
4. Se reconstruyen como objetos del sistema

## Solución de Problemas

### El programa no inicia
- Verifica que tengas Python 3.7+ instalado
- Comprueba que estés en el directorio correcto
- Intenta: `python --version`

### Permiso denegado al guardar
- Verifica los permisos del directorio `datos/`
- En Windows: Click derecho → Propiedades → Seguridad
- En Linux/Mac: `chmod 755 restaurante_app/datos`

### Archivos JSON corruptos
- El programa inicia con listas vacías si detecta JSON inválido
- Puedes eliminar los archivos `.json` y volver a empezar
- Los archivos se recrearán automáticamente

### Módulos no encontrados
- Verifica que estés ejecutando desde la carpeta correcta
- Comprueba que los archivos `__init__.py` existan en cada carpeta
- Intenta: `python -m restaurante_app.main`

## Archivos de Configuración

### .gitignore
Contiene patrones de archivos que Git debe ignorar:
- Directorios `__pycache__/`
- Archivos compilados `.pyc`
- Directorios virtuales de Python
- Archivos del IDE

### datos/
**Importante**: Los archivos JSON en `datos/` contienen información persistente y DEBEN ser incluidos en el repositorio.

## Notas para Desarrolladores

- Todos los modelos implementan `to_dict()` para serialización JSON
- El servicio Restaurante maneja validaciones de negocio
- ArchivoServicio abstrae operaciones de I/O
- main.py no modifica directamente las colecciones internas
- Se utilizan type hints en todo el código

## Contacto y Soporte

Para más información, consulta:
- README.md - Documentación completa del proyecto
- Docstrings en el código - Información de métodos y clases
- test_restaurante.py - Ejemplos de uso de las clases

---

**Última actualización:** 2026-08-26  
**Versión:** 1.0 - Semana 11  
**Estado:** Listo para producción educativa

