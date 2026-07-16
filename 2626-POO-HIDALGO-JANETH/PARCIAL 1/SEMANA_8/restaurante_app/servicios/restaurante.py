from modelos.producto import Producto
from modelos.cliente import Cliente
from typing import List

class Restaurante:
    def __init__(self):
        self.productos: List[Producto] = []
        self.clientes: List[Cliente] = []

    def registrar_producto(self, producto: Producto) -> bool:
        for p in self.productos:
            if p.codigo == producto.codigo:
                print(f"Error: Ya existe un producto con el código {producto.codigo}.")
                return False
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' registrado con éxito.")
        return True

    def registrar_cliente(self, cliente: Cliente) -> bool:
        for c in self.clientes:
            if c.identificacion == cliente.identificacion:
                print(f"Error: Ya existe un cliente con la identificación {cliente.identificacion}.")
                return False
        self.clientes.append(cliente)
        print(f"Cliente '{cliente.nombre}' registrado con éxito.")
        return True

    def listar_productos(self) -> None:
        print("\n--- Lista de Productos y Bebidas ---")
        if not self.productos:
            print("No hay productos registrados.")
        else:
            for producto in self.productos:
                print(producto.mostrar_informacion())

    def listar_clientes(self) -> None:
        print("\n--- Lista de Clientes ---")
        if not self.clientes:
            print("No hay clientes registrados.")
        else:
            for cliente in self.clientes:
                print(cliente.mostrar_informacion())
