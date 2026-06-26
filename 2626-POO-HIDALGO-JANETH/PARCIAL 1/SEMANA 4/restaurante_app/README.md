# Sistema de Gestión de Restaurante

## Descripción
Sistema básico de gestión de restaurante implementado en Python usando Programación Orientada a Objetos (POO). Demuestra la organización modular de un proyecto, separación de responsabilidades e importaciones entre archivos.

## Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── producto.py       # Clase que representa productos del restaurante
│   └── cliente.py        # Clase que representa clientes registrados
├── servicios/
│   └── restaurante.py    # Clase que gestiona el sistema del restaurante
└── main.py               # Punto de entrada del programa
```

## Componentes Principales

### 1. **Clase Producto** (modelos/producto.py)
Representa un artículo disponible en el restaurante (platos, bebidas, postres, etc.)

**Atributos:**
- `nombre`: Nombre del producto
- `descripcion`: Descripción breve
- `precio`: Precio en unidades monetarias
- `categoria`: Categoría (Plato, Bebida, Postre, Entrada)
- `disponible`: Estado de disponibilidad (booleano)

**Métodos principales:**
- `obtener_estado()`: Retorna si está disponible o no
- `cambiar_disponibilidad()`: Modifica la disponibilidad del producto
- `__str__()`: Representación textual del producto

---

### 2. **Clase Cliente** (modelos/cliente.py)
Representa un cliente registrado en el restaurante

**Atributos:**
- `numero_cliente`: ID único generado automáticamente
- `nombre`: Nombre del cliente
- `email`: Correo electrónico
- `telefono`: Número telefónico
- `pedidos_realizados`: Contador de pedidos del cliente

**Métodos principales:**
- `registrar_pedido()`: Incrementa el contador de pedidos
- `obtener_informacion_contacto()`: Retorna email y teléfono
- `__str__()`: Representación textual del cliente

**Característca especial:**
- Usa una variable de clase `contador_clientes` para generar IDs únicos y consecutivos

---

### 3. **Clase Restaurante** (servicios/restaurante.py)
Gestiona las operaciones principales del sistema

**Atributos:**
- `nombre`: Nombre del restaurante
- `ubicacion`: Ubicación del restaurante
- `productos`: Lista de productos disponibles
- `clientes`: Lista de clientes registrados

**Métodos principales:**
- `agregar_producto()`: Añade un producto al catálogo
- `agregar_cliente()`: Registra un nuevo cliente
- `listar_productos()`: Retorna los productos del restaurante
- `listar_clientes()`: Retorna los clientes registrados
- `buscar_producto_por_nombre()`: Busca un producto específico
- `buscar_cliente_por_numero()`: Busca un cliente por su ID
- `procesarPedido()`: Procesa un pedido validando cliente y producto
- `obtener_estadisticas()`: Retorna estadísticas del restaurante
- `__str__()`: Representación textual con estadísticas

---

### 4. **Módulo Principal** (main.py)
Punto de entrada que demuestra el funcionamiento del sistema:

1. **Creación del restaurante**: Instancia la clase Restaurante
2. **Agregación de productos**: Crea 6 productos de diferentes categorías
3. **Registro de clientes**: Registra 3 clientes en el sistema
4. **Listado de productos**: Muestra el catálogo disponible
5. **Procesamiento de pedidos**: Realiza transacciones de clientes
6. **Manejo de cambios**: Modifica disponibilidad de productos
7. **Visualización de datos**: Muestra clientes y estadísticas

---

## Características Implementadas

✅ **Constructores __init__()** en todas las clases principales  
✅ **Atributos pertinentes** según el contexto del restaurante  
✅ **Método especial __str__()** en Producto, Cliente y Restaurante  
✅ **Importaciones correctas** entre módulos  
✅ **Creación de objetos** desde main.py  
✅ **Gestión de datos** mediante métodos de búsqueda y agregar  
✅ **Validación** de datos en procesamiento de pedidos  
✅ **Generación de IDs únicos** mediante contador de clase  
✅ **Comentarios explicativos** en el código  
✅ **Salida organizada** en consola  

---

## Cómo Ejecutar

1. Navega hasta la carpeta del proyecto:
   ```bash
   cd restaurante_app
   ```

2. Ejecuta el programa:
   ```bash
   python main.py
   ```

3. El programa mostrará:
   - Información del restaurante
   - Productos registrados con precios
   - Clientes registrados
   - Procesamiento de pedidos
   - Estadísticas finales

---

## Ejemplo de Salida

```
SISTEMA DE GESTIÓN DE RESTAURANTE
============================================================

Restaurante creado: El Sabor Gourmet en Centro Comercial Downtown

--- AGREGANDO PRODUCTOS ---
✓ Producto 'Hamburguesa Clásica' agregado al restaurante.
...

--- LISTADO DE CLIENTES ---

Cliente #1000: Juan Pérez
  Contacto: Email: juan@email.com | Teléfono: 555-0101
  Pedidos realizados: 2
...
```

---

## Conceptos de POO Demostrados

1. **Encapsulación**: Cada clase organiza sus datos y métodos relacionados
2. **Modularización**: Separación en carpetas según responsabilidad
3. **Reutilización**: Las clases pueden usarse en diferentes contextos
4. **Abstracción**: Las clases representan conceptos del dominio (Producto, Cliente)
5. **Composición**: Restaurante contiene Productos y Clientes
6. **Variables de clase**: Contador compartido en Cliente para generar IDs únicos

---

## Posibles Extensiones

- Agregar clase Pedido para registrar detalles de compras
- Implementar cálculo de total de ventas
- Añadir persistencia de datos (archivos o bases de datos)
- Crear interfaz gráfica
- Implementar sistema de reservas
- Agregar valoraciones de clientes

