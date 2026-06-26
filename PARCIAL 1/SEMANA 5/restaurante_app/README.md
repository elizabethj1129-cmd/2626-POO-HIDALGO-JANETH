# Sistema de Gestión de Restaurante - Semana 5

## 📋 Descripción del Proyecto

Este proyecto demuestra la aplicación de conceptos fundamentales de Programación Orientada a Objetos (POO) en Python, incluyendo:

- **Identificadores descriptivos**: Nombres claros para clases, variables y métodos
- **Convenciones de nombres**: PascalCase para clases, snake_case para métodos y atributos
- **Tipos de datos básicos**: str, int, float, bool
- **Tipos de datos compuestos**: Listas para almacenar objetos
- **Estructuración modular**: Organización en carpetas y módulos
- **Importaciones correctas**: Entre módulos y paquetes

## 📁 Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py          # Importaciones de modelos
│   ├── producto.py          # Clase Producto
│   └── cliente.py           # Clase Cliente
├── servicios/
│   ├── __init__.py          # Importaciones de servicios
│   └── restaurante.py       # Clase Restaurante (servicio principal)
└── main.py                  # Punto de entrada del programa
```

## 🎯 Entidades Principales

### 1. Clase `Producto` (modelos/producto.py)

Representa un artículo disponible en el restaurante.

**Atributos:**
- `nombre`: str - Identificador del producto
- `precio`: float - Valor monetario
- `cantidad`: int - Unidades disponibles en inventario
- `descripcion`: str - Detalles del producto
- `disponible`: bool - Estado de disponibilidad

**Métodos:**
- `__init__()`: Constructor de la clase
- `__str__()`: Representación del producto como texto
- `actualizar_cantidad()`: Reduce el inventario al realizar una venta
- `obtener_información()`: Retorna un diccionario con los datos del producto

### 2. Clase `Cliente` (modelos/cliente.py)

Representa una persona registrada en el sistema del restaurante.

**Atributos:**
- `nombre`: str - Nombre completo del cliente
- `email`: str - Correo electrónico
- `telefono`: str - Número de teléfono
- `cliente_frecuente`: bool - Indica si es cliente habitual
- `numero_pedidos`: int - Contador de transacciones realizadas
- `historial_pedidos`: list - Lista de montos de pedidos

**Métodos:**
- `__init__()`: Constructor de la clase
- `__str__()`: Representación del cliente como texto
- `registrar_pedido()`: Registra una nueva compra del cliente
- `obtener_información()`: Retorna un diccionario con los datos del cliente

### 3. Clase `Restaurante` (servicios/restaurante.py)

Administra la lógica de negocio del restaurante.

**Atributos:**
- `nombre`: str - Nombre del restaurante
- `direccion`: str - Ubicación
- `lista_productos`: List[Producto] - Inventario de productos
- `lista_clientes`: List[Cliente] - Registro de clientes
- `total_ventas`: float - Acumulado de ingresos

**Métodos:**
- `__init__()`: Constructor que inicializa el restaurante
- `agregar_producto()`: Añade un producto al inventario
- `agregar_cliente()`: Registra un nuevo cliente
- `listar_productos()`: Muestra todos los productos en consola
- `listar_clientes()`: Muestra todos los clientes registrados
- `procesar_venta()`: Ejecuta una transacción de venta
- `obtener_resumen()`: Muestra un resumen del estado del restaurante

## 🚀 Cómo Ejecutar el Programa

1. Abre una terminal en la carpeta `restaurante_app`
2. Ejecuta el comando:
   ```bash
   python main.py
   ```

3. El programa mostrará:
   - Lista de productos agregados al inventario
   - Lista de clientes registrados
   - Simulación de transacciones de venta
   - Información actualizada después de las ventas
   - Resumen final del estado del restaurante

## 📊 Ejemplo de Salida

El programa demuestra:
- Creación de 4 productos con diferentes características
- Registro de 3 clientes en el sistema
- Procesamiento de 5 transacciones de venta
- Actualización dinámica de inventario y registros de clientes
- Cálculo de ventas totales

## ✅ Requisitos Cumplidos

- ✔️ Estructura modular con carpetas y módulos
- ✔️ Dos clases en modelos (Producto, Cliente)
- ✔️ Una clase en servicios (Restaurante)
- ✔️ Constructores `__init__()` en todas las clases
- ✔️ Identificadores descriptivos en todo el código
- ✔️ Convenciones PascalCase y snake_case
- ✔️ Tipos de datos básicos: str, int, float, bool
- ✔️ Listas como tipos de datos compuestos
- ✔️ Anotaciones de tipo en atributos
- ✔️ Método especial `__str__()` en modelos
- ✔️ Importaciones correctas entre módulos
- ✔️ Creación de múltiples objetos de cada modelo
- ✔️ Gestión de objetos en listas
- ✔️ Mostración de información organizada en consola
- ✔️ Comentarios explicativos en el código

## 📝 Notas Importantes

- El código NO es una copia del ejemplo de biblioteca docente
- Se utilizan conceptos de POO de forma consistente
- Las responsabilidades están bien separadas entre clases
- El programa es modular, extensible y mantenible
- Se sigue la filosofía de código limpio y legible

## 👨‍💼 Autor

Actividad desarrollada para la Semana 5 - Programación Orientada a Objetos

