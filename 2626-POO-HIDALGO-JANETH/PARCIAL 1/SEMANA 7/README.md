# Restaurante App - Semana 7

Autor: Nombre del Estudiante (reemplazar con su nombre completo)

Descripción breve
------------------
Proyecto didáctico que implementa las nociones de constructores, decoradores (@property y @setter), @dataclass y arquitectura modular por capas. Permite registrar, listar y buscar productos y clientes mediante un menú interactivo por consola.

Estructura del proyecto
----------------------
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py

Uso del constructor en Producto
------------------------------
La clase `Producto` utiliza un constructor tradicional `__init__` que recibe `nombre`, `categoria`, `precio` y `disponible`. Los atributos son controlados mediante `@property` y `@setter` para aplicar validaciones (nombre y categoría no vacíos, precio > 0).

Uso de @dataclass en Cliente
---------------------------
La clase `Cliente` está implementada con `@dataclass` y contiene `id_cliente`, `nombre` y `correo`.

Menú interactivo
-----------------
Ejecute `python main.py` desde la carpeta `restaurante_app`. El menú permite:
- Registrar producto
- Listar productos
- Buscar producto
- Registrar cliente
- Listar clientes
- Buscar cliente por ID

Reflexión
----------
Crear objetos a partir de datos ingresados por el usuario muestra cómo los constructores y las validaciones protegen la integridad de los objetos, y cómo una clase de servicio puede administrar estas instancias para ofrecer operaciones de consulta y listado.

