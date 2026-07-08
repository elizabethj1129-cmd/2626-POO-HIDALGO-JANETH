"""Módulo servicios.restaurante
Contiene la clase Restaurante que administra productos y clientes.
"""
from typing import List, Optional
from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """Servicio que administra listas de productos y clientes."""

    def __init__(self) -> None:
        self._productos: List[Producto] = []
        self._clientes: List[Cliente] = []

    # Métodos para productos
    def registrar_producto(self, producto: Producto) -> None:
        """Registra un producto en la lista."""
        self._productos.append(producto)

    def listar_productos(self) -> List[Producto]:
        """Devuelve la lista de productos registrados."""
        return list(self._productos)

    def buscar_producto_por_nombre(self, nombre: str) -> List[Producto]:
        """Busca productos cuyo nombre contiene la cadena (case-insensitive)."""
        nombre = nombre.strip().lower()
        return [p for p in self._productos if nombre in p.nombre.lower()]

    # Métodos para clientes
    def registrar_cliente(self, cliente: Cliente) -> None:
        """Registra un cliente en la lista."""
        self._clientes.append(cliente)

    def listar_clientes(self) -> List[Cliente]:
        """Devuelve la lista de clientes registrados."""
        return list(self._clientes)

    def buscar_cliente_por_id(self, id_cliente: int) -> Optional[Cliente]:
        """Busca un cliente por su identificador, devuelve None si no existe."""
        for c in self._clientes:
            if c.id_cliente == id_cliente:
                return c
        return None

