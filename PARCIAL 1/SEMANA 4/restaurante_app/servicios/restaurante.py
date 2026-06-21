"""
Módulo Restaurante
Define la clase Restaurante que gestiona los productos y clientes del sistema.
"""

from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """
    Clase que gestiona las operaciones principales del restaurante.

    Atributos:
        nombre (str): Nombre del restaurante
        ubicacion (str): Ubicación del restaurante
        productos (list): Lista de productos disponibles
        clientes (list): Lista de clientes registrados
    """

    def __init__(self, nombre, ubicacion):
        """
        Inicializa un nuevo restaurante.

        Args:
            nombre (str): Nombre del restaurante
            ubicacion (str): Ubicación del restaurante
        """
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.productos = []
        self.clientes = []

    def agregar_producto(self, producto):
        """
        Agrega un producto al catálogo del restaurante.

        Args:
            producto (Producto): Instancia de la clase Producto a agregar
        """
        self.productos.append(producto)
        print(f"[OK] Producto '{producto.nombre}' agregado al restaurante.")

    def agregar_cliente(self, cliente):
        """
        Registra un nuevo cliente en el sistema del restaurante.

        Args:
            cliente (Cliente): Instancia de la clase Cliente a agregar
        """
        self.clientes.append(cliente)
        print(f"[OK] Cliente '{cliente.nombre}' registrado en el sistema.")

    def listar_productos(self, solo_disponibles=False):
        """
        Lista los productos del restaurante.

        Args:
            solo_disponibles (bool): Si es True, solo muestra productos disponibles

        Returns:
            list: Lista de productos filtrados según el criterio
        """
        if solo_disponibles:
            productos_filtrados = [p for p in self.productos if p.disponible]
        else:
            productos_filtrados = self.productos

        return productos_filtrados

    def listar_clientes(self):
        """
        Retorna la lista de clientes registrados.

        Returns:
            list: Lista de clientes del restaurante
        """
        return self.clientes

    def buscar_producto_por_nombre(self, nombre):
        """
        Busca un producto por nombre.

        Args:
            nombre (str): Nombre del producto a buscar

        Returns:
            Producto: El producto encontrado o None si no existe
        """
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None

    def buscar_cliente_por_numero(self, numero_cliente):
        """
        Busca un cliente por su número de identificación.

        Args:
            numero_cliente (int): Número del cliente a buscar

        Returns:
            Cliente: El cliente encontrado o None si no existe
        """
        for cliente in self.clientes:
            if cliente.numero_cliente == numero_cliente:
                return cliente
        return None

    def procesarPedido(self, numero_cliente, nombre_producto):
        """
        Procesa un pedido de un cliente para un producto.

        Args:
            numero_cliente (int): Número del cliente
            nombre_producto (str): Nombre del producto

        Returns:
            bool: True si el pedido se procesó exitosamente
        """
        cliente = self.buscar_cliente_por_numero(numero_cliente)
        producto = self.buscar_producto_por_nombre(nombre_producto)

        if cliente is None:
            print(f"[ERROR] Cliente #{numero_cliente} no encontrado.")
            return False

        if producto is None:
            print(f"[ERROR] Producto '{nombre_producto}' no encontrado.")
            return False

        if not producto.disponible:
            print(f"[ERROR] Producto '{nombre_producto}' no está disponible.")
            return False

        cliente.registrar_pedido()
        print(f"[OK] Pedido procesado: {cliente.nombre} ordenó {nombre_producto} (${producto.precio:.2f})")
        return True

    def obtener_estadisticas(self):
        """
        Obtiene estadísticas generales del restaurante.

        Returns:
            dict: Diccionario con estadísticas del restaurante
        """
        productos_disponibles = sum(1 for p in self.productos if p.disponible)
        total_pedidos = sum(c.pedidos_realizados for c in self.clientes)

        return {
            'total_productos': len(self.productos),
            'productos_disponibles': productos_disponibles,
            'total_clientes': len(self.clientes),
            'total_pedidos': total_pedidos
        }

    def __str__(self):
        """
        Representación en texto del restaurante.

        Returns:
            str: Información del restaurante
        """
        stats = self.obtener_estadisticas()
        return (f"=== {self.nombre} ===\n"
                f"Ubicación: {self.ubicacion}\n"
                f"Productos registrados: {stats['total_productos']} "
                f"({stats['productos_disponibles']} disponibles)\n"
                f"Clientes registrados: {stats['total_clientes']}\n"
                f"Pedidos totales procesados: {stats['total_pedidos']}")




