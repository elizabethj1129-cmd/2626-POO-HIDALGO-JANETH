# ESTRUCTURA FINAL DEL PROYECTO - SEMANA 13

## Árbol de Directorios Completo

```
SEMANA 13/
│
├── restaurante_app/                  # Paquete principal
│   │
│   ├── __init__.py                  # Inicializador del paquete
│   ├── main.py                      # Punto de entrada principal
│   │
│   ├── datos/                       # Directorio de datos
│   │   ├── productos.json          # Datos de productos
│   │   └── usuarios.json           # Datos de usuarios
│   │
│   ├── modelos/                     # Directorio de modelos de datos
│   │   ├── __init__.py
│   │   ├── producto.py             # Clase Producto
│   │   └── usuario.py              # Clase Usuario
│   │
│   ├── servicios/                   # Directorio de servicios
│   │   ├── __init__.py
│   │   ├── archivo_servicio.py     # Servicio de I/O JSON
│   │   └── restaurante_servicio.py # Servicio de lógica
│   │
│   ├── ui/                          # Directorio de vistas gráficas
│   │   ├── __init__.py
│   │   ├── login_view.py           # Vista de autenticación
│   │   └── main_view.py            # Vista principal
│   │
│   └── __pycache__/                 # Cache de Python (generado)
│
├── test_servicios.py                # Script de prueba de servicios
├── verificar_estructura.py          # Script de verificación
│
├── README.md                        # Documentación principal
├── INSTRUCCIONES_EJECUCION.md      # Instrucciones para ejecutar
├── RESUMEN_EJECUTIVO.md            # Resumen del proyecto
└── CHECKLIST_VERIFICACION.md       # Lista de verificación
```

## Descripción de cada componente

### 📦 restaurante_app/ (Paquete Principal)
La raíz del proyecto que contiene toda la lógica de la aplicación.

### 📄 restaurante_app/main.py
**Responsabilidad**: Punto de entrada de la aplicación
- Crea la ventana principal de Tkinter
- Inicializa los servicios
- Gestiona el flujo entre vistas (LoginView → MainView)
- Mantiene un único Tk() y un solo mainloop()

```python
# Estructura simplificada
class RestauranteApp:
    __init__(root: Tk)
    _mostrar_login()
    _en_login_exitoso()
    _en_logout()
    ejecutar()
```

### 📊 restaurante_app/datos/
**Responsabilidad**: Almacenamiento de datos locales

#### productos.json
```json
[
  {"codigo": "P001", "nombre": "...", "categoria": "...", "precio": 8.50, "stock": 20},
  ...
]
```

#### usuarios.json
```json
[
  {"identificacion": "12345", "nombre": "...", "correo": "...", "contraseña": "..."},
  ...
]
```

### 🏗️ restaurante_app/modelos/
**Responsabilidad**: Definición de estructuras de datos

#### producto.py
```python
@dataclass
class Producto:
    codigo: str
    nombre: str
    categoria: str
    precio: float
    stock: int
    
    def __post_init__(): ...
    def to_dict(): ...
    def __str__(): ...
```

#### usuario.py
```python
@dataclass
class Usuario:
    identificacion: str
    nombre: str
    correo: str
    contraseña: str
    
    def __post_init__(): ...
    def to_dict(): ...
    def __str__(): ...
```

### ⚙️ restaurante_app/servicios/
**Responsabilidad**: Lógica de negocio y persistencia

#### archivo_servicio.py
```python
class ArchivoServicio:
    @staticmethod
    def cargar_productos(path: Path) -> List[Dict]
    @staticmethod
    def guardar_productos(path: Path, productos: List[Dict])
    @staticmethod
    def cargar_usuarios(path: Path) -> List[Dict]
    @staticmethod
    def guardar_usuarios(path: Path, usuarios: List[Dict])
```

#### restaurante_servicio.py
```python
class RestauranteServicio:
    __init__(datos_dir: Path = None)
    
    # Validación de acceso
    validar_acceso(identificacion: str, contraseña: str) -> bool
    
    # Búsqueda
    buscar_usuario(identificacion: str) -> Optional[Usuario]
    buscar_producto(codigo: str) -> Optional[Producto]
    
    # Listados
    listar_usuarios() -> List[Usuario]
    listar_productos() -> List[Producto]
    
    # Utilidades
    obtener_cantidad_producto(codigo: str) -> int
```

### 🎨 restaurante_app/ui/
**Responsabilidad**: Interfaz gráfica con Tkinter

#### login_view.py
```python
class LoginView:
    __init__(parent: Tk, servicio: RestauranteServicio, on_login_success: Callable)
    
    crear_interfaz() -> None  # Crea la interfaz visual
    _intentar_login() -> None # Maneja el evento de login
```

**Elementos visuales**:
- Título: "RESTAURANTE APP"
- Subtítulo: "Ingrese sus credenciales"
- Campo de Identificación
- Campo de Contraseña (ocultado)
- Label de error
- Botón de Ingreso
- Soporte para Enter en contraseña

#### main_view.py
```python
class MainView:
    __init__(parent: Tk, servicio: RestauranteServicio, 
             usuario_identificacion: str, on_logout: Callable)
    
    crear_interfaz() -> None      # Crea la interfaz visual
    _mostrar_productos() -> None  # Muestra lista de productos
    _mostrar_usuarios() -> None   # Muestra lista de usuarios
    _mostrar_pendiente() -> None  # Mensaje de funcionalidad pendiente
    _cerrar_sesion() -> None      # Cierra la sesión
```

**Elementos visuales**:
- Encabezado con título e info del usuario
- Botón: Productos (📦)
- Botón: Usuarios (👥)
- Botón: Ventas (💳) - Deshabilitado
- Botón: Cerrar sesión (🚪)
- Área de información scrolleable

### 🧪 Scripts de Prueba y Verificación

#### test_servicios.py
```
Prueba:
1. Carga de productos
2. Carga de usuarios
3. Validación de acceso
4. Búsqueda de productos
5. Búsqueda de usuarios
```

#### verificar_estructura.py
```
Verifica:
- Existencia de todos los archivos requeridos
- Estructura de directorios completa
- Archivos JSON presentes
```

## Flujo de Datos

```
main.py (RestauranteApp)
    │
    ├─→ Lee restaurante_app.datos/productos.json
    │       │
    │       ↓ ArchivoServicio.cargar_productos()
    │       │
    │       ↓ RestauranteServicio._cargar_datos()
    │       │
    │       ↓ Convierte a objetos Producto
    │       │
    │       ↓ Almacena en RestauranteServicio.productos
    │
    └─→ Lee restaurante_app.datos/usuarios.json
            │
            ↓ ArchivoServicio.cargar_usuarios()
            │
            ↓ RestauranteServicio._cargar_datos()
            │
            ↓ Convierte a objetos Usuario
            │
            ↓ Almacena en RestauranteServicio.usuarios
```

## Flujo de Interfaz

```
main.py
  │
  ├─→ Crea: LoginView(parent, servicio, on_login_success)
  │     │
  │     └─→ Muestra: campos usuario/contraseña + botón ingreso
  │           │
  │           └─→ Usuario ingresa datos
  │               │
  │               └─→ Valida: servicio.validar_acceso()
  │                   │
  │                   ├─→ Válido: llama on_login_success(usuario_id)
  │                   │   │
  │                   │   └─→ Crea: MainView(parent, servicio, usuario_id, on_logout)
  │                   │       │
  │                   │       └─→ Muestra: opciones (Productos, Usuarios, etc.)
  │                   │           │
  │                   │           ├─→ Click Productos → servicios.listar_productos()
  │                   │           ├─→ Click Usuarios → servicios.listar_usuarios()
  │                   │           └─→ Click Cerrar sesión → on_logout()
  │                   │               │
  │                   │               └─→ Regresa a LoginView
  │                   │
  │                   └─→ Inválido: Muestra error, mantiene LoginView
  │
  └─→ Ejecuta: root.mainloop()
```

## Responsabilidades por Archivo

| Archivo | Responsabilidad |
|---------|---|
| main.py | Orquestación, ciclo de vida de la aplicación |
| producto.py | Representar producto |
| usuario.py | Representar usuario |
| archivo_servicio.py | Leer/escribir archivos JSON |
| restaurante_servicio.py | Lógica de negocio, validaciones |
| login_view.py | Interfaz de autenticación |
| main_view.py | Interfaz principal post-login |
| productos.json | Datos de productos |
| usuarios.json | Datos de usuarios |

## Características de Implementación

✓ Arquitectura en capas
✓ Separación de responsabilidades
✓ Patrones de diseño (Observer mediante callbacks)
✓ Manejo de excepciones
✓ Documentación en docstrings
✓ Type hints en funciones
✓ Validación de datos
✓ Manejo de rutas relativas
✓ Una única ventana Tkinter
✓ Un único mainloop()

---

Última actualización: Semana 13
Estado: Completado ✓

