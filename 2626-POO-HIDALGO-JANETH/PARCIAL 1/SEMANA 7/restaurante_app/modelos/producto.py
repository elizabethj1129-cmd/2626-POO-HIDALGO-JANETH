"""
Módulo modelos.producto
Contiene la clase Producto implementada con constructor tradicional, propiedades y setters
"""
from typing import Any


class Producto:
    """Representa un producto del restaurante.

    Atributos:
        nombre (str): nombre del producto
        categoria (str): categoría del producto (ej. Bebida, Entrada, Plato)
        precio (float): precio del producto (debe ser > 0)
        disponible (bool): indica si está disponible
    """

    def __init__(self, nombre: str, categoria: str, precio: float, disponible: bool = True):
        # Usar los setters para aplicar validaciones
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible

    # nombre
    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        self._nombre = valor.strip()

    # categoria
    @property
    def categoria(self) -> str:
        return self._categoria

    @categoria.setter
    def categoria(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("La categoría del producto no puede estar vacía.")
        self._categoria = valor.strip()

    # precio
    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: Any) -> None:
        try:
            precio_val = float(valor)
        except Exception:
            raise ValueError("El precio debe ser un número válido.")
        if precio_val <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        self._precio = precio_val

    # disponible
    @property
    def disponible(self) -> bool:
        return self._disponible

    @disponible.setter
    def disponible(self, valor: Any) -> None:
        self._disponible = bool(valor)

    def mostrar_informacion(self) -> str:
        """Devuelve una representación legible del producto."""
        estado = "Sí" if self.disponible else "No"
        return f"Nombre: {self.nombre} | Categoría: {self.categoria} | Precio: ${self.precio:.2f} | Disponible: {estado}"

