# Guía de Conceptos POO Implementados

## 🎯 Objetivo
Este documento explica cómo los conceptos de Programación Orientada a Objetos (POO) se han aplicado en el sistema de gestión de restaurante.

---

## 📦 1. CLASES Y OBJETOS

### Concepto
Una clase es un molde que define la estructura y comportamiento de los objetos. En nuestro sistema tenemos 3 clases principales.

### Implementación
```python
class Producto:
    """Representa un producto del restaurante"""

class Cliente:
    """Representa un cliente del restaurante"""

class Restaurante:
    """Gestiona el sistema del restaurante"""
```

### Ejemplo de uso
```python
producto = Producto("Hamburguesa", "Carne con verduras", 12.99, "Plato")
cliente = Cliente("Juan", "juan@email.com", "555-0101")
restaurante = Restaurante("El Sabor Gourmet", "Centro")
```

---

## 🔧 2. CONSTRUCTOR __init__()

### Concepto
El constructor es un método especial que se ejecuta cuando se crea una instancia de la clase. Se usa para inicializar los atributos.

### Implementación en Producto
```python
def __init__(self, nombre, descripcion, precio, categoria, disponible=True):
    self.nombre = nombre
    self.descripcion = descripcion
    self.precio = precio
    self.categoria = categoria
    self.disponible = disponible
```

### Ventajas
- Asegura que todo objeto tenga atributos válidos
- Inicializa valores por defecto (ej: disponible=True)
- Centraliza la lógica de creación

---

## 📋 3. ATRIBUTOS

### Tipos de Atributos

#### A) Atributos de Instancia
Únicos para cada objeto:
```python
# En Producto
self.nombre = nombre      # Cada producto tiene su nombre
self.precio = precio      # Cada producto tiene su precio
```

#### B) Atributos de Clase
Compartidos por todas las instancias:
```python
class Cliente:
    contador_clientes = 1000  # Compartido por todos los clientes
    
    def __init__(self, nombre, email, telefono):
        self.numero_cliente = Cliente.contador_clientes
        Cliente.contador_clientes += 1  # Incrementar para el siguiente
```

### Propósito
Los atributos almacenan datos que definen el estado de un objeto.

---

## ⚙️ 4. MÉTODOS

### Concepto
Son funciones definidas dentro de una clase que operan sobre los atributos.

### Tipos de Métodos

#### A) Métodos de Consulta (Getters)
Retornan información sin modificar el estado:
```python
def obtener_estado(self):
    """Retorna la disponibilidad del producto"""
    return "Disponible" if self.disponible else "No disponible"

def obtener_informacion_contacto(self):
    """Retorna datos de contacto del cliente"""
    return f"Email: {self.email} | Teléfono: {self.telefono}"
```

#### B) Métodos de Modificación (Setters)
Cambian el estado del objeto:
```python
def cambiar_disponibilidad(self, disponible):
    """Modifica la disponibilidad del producto"""
    self.disponible = disponible

def registrar_pedido(self):
    """Incrementa el contador de pedidos"""
    self.pedidos_realizados += 1
```

#### C) Métodos de Lógica de Negocio
Implementan reglas del dominio:
```python
def procesarPedido(self, numero_cliente, nombre_producto):
    """Procesa un pedido validando datos"""
    cliente = self.buscar_cliente_por_numero(numero_cliente)
    producto = self.buscar_producto_por_nombre(nombre_producto)
    
    if cliente is None:
        print("✗ Error: Cliente no encontrado.")
        return False
    
    if not producto.disponible:
        print("✗ Error: Producto no disponible.")
        return False
    
    cliente.registrar_pedido()
    return True
```

---

## 📝 5. MÉTODO ESPECIAL __str__()

### Concepto
Define cómo se representa el objeto como texto. Se llama automáticamente con `print()` o `str()`.

### Implementación en Producto
```python
def __str__(self):
    return (f"[{self.categoria}] {self.nombre}\n"
            f"  Descripción: {self.descripcion}\n"
            f"  Precio: ${self.precio:.2f}\n"
            f"  Estado: {self.obtener_estado()}")
```

### Resultado
```
[Plato] Hamburguesa Clásica
  Descripción: Carne molida con lechuga, tomate y queso
  Precio: $12.99
  Estado: Disponible
```

### Ventajas
- Mejora la legibilidad del programa
- Facilita debugging
- Hace el código más profesional

---

## 📚 6. ENCAPSULACIÓN

### Concepto
Agrupar datos (atributos) y métodos relacionados dentro de una clase, ocultando la complejidad interna.

### Ejemplo
```python
class Restaurante:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.productos = []      # Datos internos
        self.clientes = []       # Datos internos
    
    def agregar_producto(self, producto):
        """Interfaz pública para modificar datos internos"""
        self.productos.append(producto)
    
    def listar_productos(self):
        """Interfaz pública para acceder a datos internos"""
        return self.productos
```

### Beneficios
- **Seguridad**: Controla cómo se accede y modifica los datos
- **Mantenibilidad**: Cambios internos no afectan código externo
- **Validación**: Se pueden agregar validaciones en los métodos

---

## 🔗 7. IMPORTACIONES

### Concepto
Permite reutilizar código de otros archivos/módulos en el proyecto.

### Estructura de carpetas
```
restaurante_app/
├── modelos/
│   ├── producto.py
│   └── cliente.py
├── servicios/
│   └── restaurante.py
└── main.py
```

### Importación en restaurante.py
```python
from modelos.producto import Producto
from modelos.cliente import Cliente
```

### Importación en main.py
```python
from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante
```

### Ventajas
- **Reutilización**: Código utilizable desde múltiples archivos
- **Organización**: Cada módulo tiene una responsabilidad
- **Mantenibilidad**: Cambios centralizados en un lugar

---

## 🏗️ 8. COMPOSICIÓN

### Concepto
Una clase está compuesta por instancias de otras clases (relación "tiene-un").

### Ejemplo
```python
class Restaurante:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.productos = []    # Lista de Productos
        self.clientes = []     # Lista de Clientes

# Uso
restaurante = Restaurante("El Sabor Gourmet", "Centro")
producto = Producto("Hamburguesa", ..., 12.99, "Plato")
cliente = Cliente("Juan", "juan@email.com", "555-0101")

restaurante.agregar_producto(producto)  # Composición
restaurante.agregar_cliente(cliente)    # Composición
```

### Relaciones
```
Restaurante ----→ Productos
    ↓
    └─→ Clientes
```

---

## 🔍 9. BÚSQUEDA Y VALIDACIÓN

### Concepto
Métodos que localizan objetos y validan información antes de realizar operaciones.

### Implementación
```python
def buscar_producto_por_nombre(self, nombre):
    """Busca un producto específico por nombre"""
    for producto in self.productos:
        if producto.nombre.lower() == nombre.lower():
            return producto
    return None

def procesarPedido(self, numero_cliente, nombre_producto):
    """Valida antes de procesar"""
    cliente = self.buscar_cliente_por_numero(numero_cliente)
    if cliente is None:
        print(f"✗ Error: Cliente #{numero_cliente} no encontrado.")
        return False
    
    producto = self.buscar_producto_por_nombre(nombre_producto)
    if producto is None:
        print(f"✗ Error: Producto '{nombre_producto}' no encontrado.")
        return False
    
    if not producto.disponible:
        print(f"✗ Error: Producto no disponible.")
        return False
    
    # Si todo es válido, procesar
    cliente.registrar_pedido()
    return True
```

---

## 📊 10. ESTADÍSTICAS Y AGREGACIÓN

### Concepto
Recorrer colecciones de objetos para extraer información resumida.

### Implementación
```python
def obtener_estadisticas(self):
    """Calcula y retorna estadísticas del restaurante"""
    productos_disponibles = sum(1 for p in self.productos if p.disponible)
    total_pedidos = sum(c.pedidos_realizados for c in self.clientes)
    
    return {
        'total_productos': len(self.productos),
        'productos_disponibles': productos_disponibles,
        'total_clientes': len(self.clientes),
        'total_pedidos': total_pedidos
    }
```

### Técnicas
- **Comprensiones de lista**: `sum(1 for p in self.productos if p.disponible)`
- **Agregaciones**: Sumar, contar, promediar valores
- **Filtrado**: Aplicar condiciones en colecciones

---

## 🎓 RESUMEN DE CONCEPTOS

| Concepto | Propósito | Ejemplo |
|----------|----------|---------|
| **Clase** | Definir estructura | `class Producto` |
| **Atributo** | Almacenar datos | `self.precio = 12.99` |
| **Método** | Implementar comportamiento | `obtener_estado()` |
| **__init__()** | Inicializar objetos | Constructor del producto |
| **__str__()** | Representar como texto | Mostrar en consola |
| **Encapsulación** | Organizar y proteger datos | Métodos públicos de acceso |
| **Composición** | Relaciones entre clases | Restaurante contiene Productos |
| **Importación** | Reutilizar código | `from modelos.producto import Producto` |

---

## 💡 DECISIONES DE DISEÑO

### ¿Por qué esta estructura?

1. **Separación de carpetas**
   - `modelos/`: Clases que representan entidades del dominio
   - `servicios/`: Lógica de negocio y gestión del sistema

2. **Dos clases en modelos**
   - Producto y Cliente representan entidades independientes
   - Cada una tiene responsabilidades bien definidas

3. **Una clase en servicios**
   - Restaurante actúa como intermediario entre objetos
   - Implementa la lógica de negocio del sistema

4. **Contador de clientes**
   - Atributo de clase `contador_clientes` para IDs únicos
   - Evita duplicados sin necesidad de base de datos

5. **Validaciones en procesarPedido**
   - Comprueba existencia y disponibilidad antes de procesar
   - Retorna falso/verdadero indicando éxito

---

## 🚀 CÓMO EXTENDER EL SISTEMA

### Posibilidades futuras
1. Agregar clase `Pedido` para registrar compras
2. Implementar persistencia en archivo o base de datos
3. Agregar valoraciones y reseñas de clientes
4. Crear sistema de reservas
5. Calcular ingresos totales
6. Implementar descuentos por volumen
7. Agregar interfaz gráfica con Tkinter


