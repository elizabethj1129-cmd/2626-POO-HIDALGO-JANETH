# Servicio principal que gestiona productos y clientes del restaurante

from typing import List
from modelos import Producto, Cliente


class Restaurante:
    """
    Clase que administra los productos y clientes del restaurante.
    Ofrece métodos para agregar, listar y gestionar la información del restaurante.
    """
    
    def __init__(self, nombre: str, direccion: str):
        """
        Constructor de la clase Restaurante.
        
        Args:
            nombre: Nombre del restaurante (str)
            direccion: Ubicación del restaurante (str)
        """
        self.nombre = nombre
        self.direccion = direccion
        self.lista_productos: List[Producto] = []  # Lista de productos disponibles
        self.lista_clientes: List[Cliente] = []  # Lista de clientes registrados
        self.total_ventas = 0.0  # Total acumulado de ventas (float)
    
    def agregar_producto(self, producto: Producto) -> None:
        """
        Agrega un nuevo producto al inventario del restaurante.
        
        Args:
            producto: Objeto de tipo Producto a agregar (Producto)
        """
        self.lista_productos.append(producto)
        print(f"✓ Producto '{producto.nombre}' agregado exitosamente.")
    
    def agregar_cliente(self, cliente: Cliente) -> None:
        """
        Registra un nuevo cliente en el sistema del restaurante.
        
        Args:
            cliente: Objeto de tipo Cliente a registrar (Cliente)
        """
        self.lista_clientes.append(cliente)
        print(f"✓ Cliente '{cliente.nombre}' registrado exitosamente.")
    
    def listar_productos(self) -> None:
        """
        Muestra en consola todos los productos disponibles en el restaurante.
        """
        print("\n" + "="*60)
        print(f"PRODUCTOS DEL RESTAURANTE: {self.nombre}")
        print("="*60)
        
        if not self.lista_productos:
            print("No hay productos registrados.")
            return
        
        for indice, producto in enumerate(self.lista_productos, 1):
            print(f"\n[{indice}]")
            print(producto)
    
    def listar_clientes(self) -> None:
        """
        Muestra en consola todos los clientes registrados en el restaurante.
        """
        print("\n" + "="*60)
        print(f"CLIENTES DEL RESTAURANTE: {self.nombre}")
        print("="*60)
        
        if not self.lista_clientes:
            print("No hay clientes registrados.")
            return
        
        for indice, cliente in enumerate(self.lista_clientes, 1):
            print(f"\n[{indice}]")
            print(cliente)
    
    def procesar_venta(self, cliente: Cliente, producto: Producto, cantidad: int) -> bool:
        """
        Procesa la venta de un producto a un cliente.
        Actualiza el inventario, registra el pedido y acumula ventas.
        
        Args:
            cliente: Cliente que realiza la compra (Cliente)
            producto: Producto a vender (Producto)
            cantidad: Cantidad de unidades a vender (int)
        
        Returns:
            True si la venta fue exitosa, False en caso contrario (bool)
        """
        if not producto.disponible or producto.cantidad < cantidad:
            print(f"❌ No hay suficiente cantidad de {producto.nombre}")
            return False
        
        monto_venta = producto.precio * cantidad
        producto.actualizar_cantidad(cantidad)
        cliente.registrar_pedido(monto_venta)
        self.total_ventas += monto_venta
        
        print(f"✓ Venta realizada: {cantidad} x {producto.nombre} = ${monto_venta:.2f}")
        return True
    
    def obtener_resumen(self) -> None:
        """
        Muestra un resumen del estado actual del restaurante.
        Incluye cantidad de productos, cantidad de clientes y ventas totales.
        """
        print("\n" + "="*60)
        print("RESUMEN DEL RESTAURANTE")
        print("="*60)
        print(f"Nombre: {self.nombre}")
        print(f"Dirección: {self.direccion}")
        print(f"Productos disponibles: {len(self.lista_productos)}")
        print(f"Clientes registrados: {len(self.lista_clientes)}")
        print(f"Total de ventas: ${self.total_ventas:.2f}")
        print("="*60)

