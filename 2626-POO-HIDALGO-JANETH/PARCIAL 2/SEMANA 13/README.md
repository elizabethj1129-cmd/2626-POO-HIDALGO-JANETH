# Restaurante App - Semana 13

## Propósito

Esta aplicación es una versión inicial de un sistema de gestión de restaurante con interfaz gráfica. Implementa autenticación de usuarios y permite consultar productos y usuarios registrados a través de una interfaz visual usando Tkinter.

Esta base estructural sigue el patrón del proyecto docente (Biblioteca App) adaptándolo al dominio del restaurante, manteniendo una separación clara entre modelos, servicios, datos y vistas gráficas.

## Estructura del Proyecto

```
restaurante_app/
├── datos/
│   ├── productos.json          # Datos de productos
│   └── usuarios.json           # Datos de usuarios
├── modelos/
│   ├── __init__.py
│   ├── producto.py             # Clase Producto
│   └── usuario.py              # Clase Usuario
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py     # Servicio de I/O para JSON
│   └── restaurante_servicio.py # Servicio de lógica de negocio
├── ui/
│   ├── __init__.py
│   ├── login_view.py           # Vista de autenticación
│   └── main_view.py            # Vista principal
├── main.py                      # Punto de entrada
└── README.md                    # Este archivo
```

## Responsabilidades de cada componente

### Modelos (`modelos/`)

- **Producto**: Representa un producto del restaurante con atributos de código, nombre, categoría, precio y stock.
- **Usuario**: Representa un usuario del sistema con identificación, nombre, correo y contraseña para acceso.

### Servicios (`servicios/`)

- **ArchivoServicio**: Responsable de leer y escribir archivos JSON. Carga y guarda productos y usuarios de forma persistente.
- **RestauranteServicio**: Capa de lógica de negocio. Convierte datos JSON en objetos, valida acceso de usuarios y proporciona operaciones para consultar productos y usuarios.

### Vistas (`ui/`)

- **LoginView**: Interfaz de autenticación. Permite ingresar identificación y contraseña con validación en tiempo real.
- **MainView**: Interfaz principal después del login. Muestra opciones para consultar productos, usuarios y otras funcionalidades (algunas pendientes).

### Punto de Entrada (`main.py`)

- **RestauranteApp**: Crea la ventana principal de Tkinter, inicializa los servicios y gestiona el flujo entre vistas.
- Mantiene una única instancia de `Tk()` y un solo `mainloop()`.
- Realiza el cambio entre LoginView y MainView dentro de la misma ventana.

## Flujo de la Aplicación

```
┌─────────────────────────────────────────────┐
│  Inicio: main.py crea RestauranteApp        │
│  - Inicializa Tk()                          │
│  - Carga servicios con datos JSON           │
│  - Prepara RestauranteServicio             │
└─────────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────┐
│  LoginView                                  │
│  - Muestra campos de identificación         │
│  - Muestra campo de contraseña              │
└─────────────────────────────────────────────┘
                     ↓
        ┌───────────────────────┐
        │  Validación de datos  │
        └───────────────────────┘
                     ↓
        ┌─────────────────────────────────┐
        │  RestauranteServicio validar    │
        │  _acceso(identificacion, pass)  │
        └─────────────────────────────────┘
                     ↓
   ┌─────────────────────┬─────────────────────┐
   │  Válido             │  Inválido           │
   ↓                     ↓
MainView              LoginView (error visual)
│                     
├── Productos (botón)
│   └── Muestra lista de productos con detalles
│
├── Usuarios (botón)
│   └── Muestra lista de usuarios registrados
│
├── Ventas (botón - deshabilitado)
│   └── Mensaje de funcionalidad pendiente
│
└── Cerrar sesión (botón)
    └── Regresa a LoginView en la misma ventana
```

## Datos de Prueba

### Usuarios disponibles para login

| Identificación | Contraseña | Nombre         |
|---|---|---|
| 12345          | 1234       | Juan Pérez     |
| 67890          | 5678       | María García   |
| 11111          | 9999       | Carlos López   |

### Productos disponibles

Se cargan 6 productos de ejemplo en diferentes categorías (Platos Principales, Ensaladas, Pastas, Bebidas, Postres).

## Cómo ejecutar

### Requisitos previos

- Python 3.8 o superior
- Tkinter (generalmente incluido con Python)

### Pasos para ejecutar

**Opción 1: Usando run.py (RECOMENDADO)**

```powershell
# 1. Navega a la carpeta SEMANA 13
cd C:\Users\Herobook\UEA\2626-POO-HIDALGO-JANETH\PARCIAL 2\SEMANA 13

# 2. Ejecuta el script
python run.py
```

**Opción 2: En Windows - Doble click**

Simplemente haz doble click en el archivo `ejecutar.bat` en la carpeta SEMANA 13.

**Opción 3: Con módulo Python**

```powershell
cd C:\Users\Herobook\UEA\2626-POO-HIDALGO-JANETH\PARCIAL 2\SEMANA 13
python -m restaurante_app.main
```

**Opción 4: Con PowerShell**

```powershell
cd C:\Users\Herobook\UEA\2626-POO-HIDALGO-JANETH\PARCIAL 2\SEMANA 13
.\ejecutar.ps1
```

## Verificación de Funcionamiento

- [ ] La aplicación inicia sin errores
- [ ] Se muestra primero la pantalla de acceso
- [ ] Los campos permiten ingresar usuario y contraseña
- [ ] Campos vacíos producen mensaje de error
- [ ] Credenciales incorrectas producen mensaje de error
- [ ] Credenciales válidas muestran la interfaz principal
- [ ] El botón "Productos" muestra los productos desde JSON
- [ ] El botón "Usuarios" muestra los usuarios desde JSON
- [ ] Las vistas usan RestauranteServicio (no leen JSON directamente)
- [ ] El botón "Cerrar sesión" regresa a login en la misma ventana
- [ ] No hay errores de importación o rutas

## Notas Importantes

- Esta es una base estructural simplificada. Las funcionalidades completas del restaurante (ventas, reportes, etc.) se integrarán progresivamente en semanas posteriores.
- La validación de acceso es pedagógica. En un sistema real, las contraseñas estarían hasheadas y habría validaciones de seguridad adicionales.
- La interfaz gráfica es básica pero funcional. En futuras versiones se pueden mejorar aspectos visuales y agregar más opciones.
- Los datos se cargan desde archivos JSON. La persistencia de cambios requerirá implementación adicional en futuras semanas.

## Adaptaciones del Proyecto Docente

Comparado con Biblioteca App (proyecto de referencia):

| Biblioteca App | Restaurante App |
|---|---|
| Libros | Productos |
| Autores | Categorías |
| BibliotecaServicio | RestauranteServicio |
| LoginView (igual) | LoginView (adaptada al contexto) |
| MainView (igual estructura) | MainView (muestra productos y usuarios) |

La estructura, patrones y principios son los mismos; solo cambian las entidades y el contexto del dominio.

## Archivos de Entrada

- `productos.json`: Lista de productos del restaurante en formato JSON
- `usuarios.json`: Lista de usuarios registrados con credenciales en formato JSON

## Próximos Pasos (Futuras Semanas)

- Implementar funcionalidad de Ventas gráficamente
- Agregar opciones de CRUD (Crear, Leer, Actualizar, Eliminar)
- Incorporar más entidades del restaurante
- Mejorar diseño visual de la interfaz
- Agregar persistencia de cambios
- Implementar reportes y consultas más avanzadas

---

**Autor**: Estudiante de POO  
**Fecha de Creación**: Semana 13  
**Estado**: Base estructural completada y funcional

