# SEMANA 11: Fundamentos de Colecciones Aplicados a Relaciones, Ventas y Persistencia JSON

## Estudiante
**Nombre:** Janeth Hidalgo  
**Curso:** Programación Orientada a Objetos  
**Institución:** UEA

---

## Descripción General

Este proyecto corresponde a la **Semana 11** del curso de Programación Orientada a Objetos. Se trata de una evolución del sistema `restaurante_app` desarrollado en semanas anteriores, donde se incorporan las siguientes mejoras:

- **Persistencia completa JSON** de productos, usuarios y ventas.
- **Modelo de Venta** que relaciona usuarios con productos mediante colecciones.
- **Control de stock** para garantizar que no haya ventas sin inventario suficiente.
- **Operaciones de venta funcionales** que validan datos y actualizan múltiples colecciones.
- **Consultas por usuario** que demuestran filtrado y recorrido de colecciones.

El sistema mantiene una arquitectura modular clara, separando la lógica de negocio (Restaurante), la persistencia (ArchivoServicio) y los modelos de datos (Producto, Usuario, Venta).

---

## Estructura del Proyecto

```
restaurante_app/
├── datos/
│   ├── productos.json      # Persistencia de productos con stock
│   ├── usuarios.json       # Persistencia de usuarios
│   └── ventas.json         # Persistencia de ventas
├── modelos/
│   ├── __init__.py
│   ├── producto.py         # Clase Producto con atributo stock
│   ├── usuario.py          # Clase Usuario con método to_dict()
│   └── venta.py            # Clase Venta (nueva)
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py # Manejo de I/O para JSON
│   └── restaurante.py      # Lógica de negocio y colecciones
├── __init__.py
├── main.py                 # Punto de entrada con menú interactivo
└── README.md               # Este archivo
```

---

## Componentes Principales

### 1. **modelos/producto.py**

Clase que representa un producto del restaurante.

**Atributos:**
- `codigo`: identificador único (string)
- `nombre`: nombre del producto
- `categoria`: categoría a la que pertenece
- `precio`: precio unitario (float)
- `stock`: cantidad disponible (int, no negativo)

**Métodos destacados:**
- `vender(cantidad)`: disminuye el stock de forma segura
- `to_dict()`: convierte el objeto a diccionario para JSON

**Validaciones:**
- El stock nunca puede ser negativo
- El precio debe ser un número válido
- Los valores se validan en `__post_init__()`

### 2. **modelos/usuario.py**

Clase que representa un usuario registrado en el sistema.

**Atributos:**
- `identificacion`: identificador único
- `nombre`: nombre completo
- `correo`: correo electrónico

**Métodos:**
- `to_dict()`: convierte el objeto a diccionario para JSON

### 3. **modelos/venta.py** (Nueva)

Clase que representa la relación entre un usuario y un producto vendido.

**Atributos:**
- `usuario_id`: identificación del usuario que compra
- `producto_codigo`: código del producto vendido
- `cantidad`: cantidad vendida (positivo)
- `fecha`: fecha y hora de la venta (timestamp automático)

**Relación:**
```
Usuario + Producto → Venta
```

Una venta no es simplemente una resta de stock; es un objeto que conserva la referencia a ambas partes de la transacción.

### 4. **servicios/archivo_servicio.py**

Servicio responsable de la lectura y escritura de archivos JSON.

**Métodos:**
- `cargar_productos(path)`: carga productos desde JSON
- `guardar_productos(path, productos)`: persiste productos
- `cargar_usuarios(path)`: carga usuarios desde JSON
- `guardar_usuarios(path, usuarios)`: persiste usuarios
- `cargar_ventas(path)`: carga ventas desde JSON
- `guardar_ventas(path, ventas)`: persiste ventas

**Manejo de excepciones:**
- `FileNotFoundError`: inicia con colecciones vacías si el archivo no existe
- `JSONDecodeError`: notifica y continúa con colección vacía
- `PermissionError`: informa al usuario sobre permisos insuficientes

### 5. **servicios/restaurante.py**

Servicio central que administra todas las colecciones y reglas de negocio.

**Colecciones internas:**
- `_productos`: lista de Producto
- `_usuarios`: lista de Usuario
- `_ventas`: lista de Venta

**Operaciones principales:**

#### Productos
- `registrar_producto(producto)`: añade un nuevo producto
- `buscar_producto(codigo)`: busca por código
- `actualizar_producto(codigo, ...)`: actualiza atributos
- `eliminar_producto(codigo)`: elimina un producto
- `listar_productos()`: retorna todos los productos

#### Usuarios
- `registrar_usuario(usuario)`: registra un nuevo usuario
- `buscar_usuario(identificacion)`: busca por identificación
- `listar_usuarios()`: retorna todos los usuarios

#### Ventas (Nuevas)
- `vender_producto(codigo_producto, identificacion_usuario, cantidad)`: 
  - Valida usuario y producto existentes
  - Valida cantidad > 0
  - Valida stock suficiente
  - Crea objeto Venta
  - Disminuye stock del producto
  - Guarda cambios en JSON
  - Retorna True/False

- `obtener_ventas_usuario(identificacion_usuario)`: 
  - Filtra ventas por usuario
  - Demuestra recorrido y comparación de colecciones

- `listar_ventas()`: retorna todas las ventas

### 6. **main.py**

Punto de entrada que proporciona un menú interactivo con las siguientes opciones:

```
PRODUCTOS:
  1. Registrar producto (con stock inicial)
  2. Buscar producto
  3. Actualizar producto (incluye stock)
  4. Eliminar producto
  5. Listar productos

USUARIOS:
  6. Registrar usuario
  7. Listar usuarios

CONSULTAS:
  8. Mostrar categorías

VENTAS:
  9. Vender producto (nueva opción)
  10. Consultar ventas de un usuario (nueva opción)

  11. Salir
```

---

## Persistencia de Datos

### Formato JSON

Cada entidad se serializa a su correspondiente archivo JSON.

**productos.json:**
```json
[
  {
    "codigo": "P001",
    "nombre": "Hamburguesa",
    "categoria": "Comida Rápida",
    "precio": 12.50,
    "stock": 8
  }
]
```

**usuarios.json:**
```json
[
  {
    "identificacion": "1234567890",
    "nombre": "Juan García",
    "correo": "juan@example.com"
  }
]
```

**ventas.json:**
```json
[
  {
    "usuario_id": "1234567890",
    "producto_codigo": "P001",
    "cantidad": 2,
    "fecha": "2026-08-26 15:30:45"
  }
]
```

### Ciclo de Vida de Datos

1. **Inicio:** Restaurante carga productos, usuarios y ventas desde JSON
2. **Operación:** Se modifica una colección
3. **Persistencia:** Se actualiza el archivo JSON correspondiente
4. **Cierre:** Al salir, los datos quedan guardados

### Operaciones que Generan Persistencia

- Registrar/Actualizar/Eliminar producto → **productos.json**
- Registrar usuario → **usuarios.json**
- Realizar venta → **ventas.json** + **productos.json** (stock)

---

## Operación de Venta: Flujo Completo

```
1. Usuario selecciona opción "Vender producto"
       ↓
2. Sistema solicita:
   - Identificación del usuario
   - Código del producto
   - Cantidad a vender
       ↓
3. Sistema valida:
   - Usuario existe
   - Producto existe
   - Cantidad > 0
   - Stock ≥ cantidad solicitada
       ↓
4. Si todo es válido:
   - Crea Venta(usuario_id, producto_codigo, cantidad)
   - Agrega Venta a colección _ventas
   - Disminuye stock del producto
   - Guarda ventas.json
   - Guarda productos.json (con nuevo stock)
   - Muestra confirmación
       ↓
5. Si hay error:
   - Muestra mensaje de error específico
   - No modifica datos
   - No genera archivo JSON
```

---

## Manejo de Excepciones

El sistema implementa manejo específico de excepciones para:

| Excepción | Situación | Acción |
|-----------|-----------|--------|
| `FileNotFoundError` | Archivo JSON no existe en primer inicio | Inicia con colección vacía |
| `JSONDecodeError` | Archivo JSON con contenido inválido | Informa al usuario y continúa |
| `PermissionError` | Permisos insuficientes para leer/escribir | Notifica y continúa si es posible |
| `KeyError` | Falta una clave esperada en registro JSON | Omite el registro y continúa |
| `ValueError` | Validación fallida en modelo o entrada | Muestra mensaje descriptivo |

**Principio:** No se utiliza `except: pass` ni capturas genéricas para ocultar errores.

---

## Validaciones Implementadas

### Producto
- Código único (no se permite duplicados)
- Stock ≥ 0 (nunca negativo)
- Precio > 0
- Campos requeridos no vacíos

### Usuario
- Identificación única
- Campos requeridos no vacíos

### Venta
- Usuario debe existir
- Producto debe existir
- Cantidad > 0
- Stock suficiente

---

## Uso del Sistema

### Requisitos
- Python 3.7 o superior
- Sin dependencias externas

### Ejecución

Desde la raíz del proyecto:

```bash
python restaurante_app/main.py
```

O en sistemas Windows:

```cmd
python restaurante_app\main.py
```

### Ejemplo de Sesión Completa

```
1. Registrar producto: "P001", "Hamburguesa", "Comida Rápida", 12.50, 10
2. Registrar usuario: "1234567890", "Juan García", "juan@example.com"
3. Vender producto: usuario "1234567890", producto "P001", cantidad 2
   - Stock de P001: 10 → 8
   - Venta registrada en ventas.json
4. Consultar ventas de usuario "1234567890"
   - Muestra todas las compras del usuario
5. Cerrar programa
6. Ejecutar nuevamente
   - Productos, usuarios y ventas se recuperan automáticamente
```

---

## Pruebas Realizadas

### Test 1: Registro Inicial
✓ Registrar producto con stock  
✓ Registrar usuario  
✓ Archivos JSON creados en directorio datos/

### Test 2: Venta Válida
✓ Vender con stock suficiente  
✓ Stock disminuye correctamente  
✓ ventas.json registra operación  
✓ productos.json actualiza stock

### Test 3: Venta Rechazada
✓ Rechaza venta sin usuario válido  
✓ Rechaza venta sin producto válido  
✓ Rechaza cantidad ≤ 0  
✓ Rechaza stock insuficiente  
✓ No modifica datos al rechazar

### Test 4: Persistencia
✓ Datos se guardan al cerrar  
✓ Datos se recuperan al iniciar  
✓ Múltiples sesiones conservan información

### Test 5: Consultas
✓ Filtrado de ventas por usuario  
✓ Información de producto en consulta  
✓ Manejo de usuario sin ventas

---

## Mejoras Respecto a Semana 10

| Mejora | Detalles |
|--------|----------|
| **Stock en Producto** | Atributo `stock` con validación y método `vender()` |
| **Persistencia de Usuarios** | usuarios.json se carga y guarda |
| **Modelo Venta** | Nueva clase que relaciona usuario-producto |
| **Operación de Venta** | Valida y registra transacciones |
| **Persistencia de Ventas** | ventas.json con historial de operaciones |
| **Consultas por Usuario** | Filtrado de colecciones de ventas |
| **Menú Expandido** | Opciones 9 y 10 para ventas |

---

## Limitaciones Conocidas (Por Diseño)

- No se implementan carrito de compras (fuera de alcance)
- No se calcula IVA ni descuentos
- No se manejan múltiples métodos de pago
- No se implementan proveedores
- No se utiliza base de datos (JSON únicamente)
- No hay interfaz gráfica

---

## Estructura de Archivos JSON en disco

```
SEMANA 11/
├── restaurante_app/
│   ├── datos/
│   │   ├── productos.json  (actualizado en cada operación de producto)
│   │   ├── usuarios.json   (actualizado en cada registro de usuario)
│   │   └── ventas.json     (actualizado en cada venta)
│   ├── modelos/
│   ├── servicios/
│   ├── main.py
│   └── __init__.py
└── README.md
```

---

## Conclusiones

Este proyecto demuestra:
- Uso efectivo de colecciones para almacenar relaciones entre objetos
- Persistencia de datos mediante JSON
- Validación de operaciones de negocio
- Manejo apropiado de excepciones
- Arquitectura modular y mantenible
- Separación de responsabilidades entre capas

El sistema está listo para producción en el contexto educativo y puede extenderse fácilmente con nuevas funcionalidades respetando la estructura existente.

---

## Autor
**Janeth Hidalgo**  
Semana 11 - Programación Orientada a Objetos

