from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Producto:
    """Representa un producto del restaurante.

    Atributos:
        codigo: identificador único del producto
        nombre: nombre del producto
        categoria: categoría a la que pertenece
        precio: precio unitario
        stock: cantidad disponible del producto
    """

    codigo: str
    nombre: str
    categoria: str
    precio: float
    stock: int = 0

    def __post_init__(self) -> None:
        self.codigo = str(self.codigo).strip()
        self.nombre = str(self.nombre).strip()
        self.categoria = str(self.categoria).strip()
        try:
            self.precio = float(self.precio)
        except (TypeError, ValueError):
            raise ValueError("El precio debe ser un número")
        try:
            self.stock = int(self.stock)
            if self.stock < 0:
                raise ValueError("El stock no puede ser negativo")
        except (TypeError, ValueError) as e:
            raise ValueError(f"El stock debe ser un número no negativo: {e}")

    def vender(self, cantidad: int) -> None:
        """Disminuye el stock del producto.

        Args:
            cantidad: cantidad a disminuir

        Raises:
            ValueError: si la cantidad es inválida o supera el stock disponible
        """
        try:
            cantidad = int(cantidad)
        except (TypeError, ValueError):
            raise ValueError("La cantidad debe ser un número entero")

        if cantidad <= 0:
            raise ValueError("La cantidad a vender debe ser mayor que cero")

        if self.stock < cantidad:
            raise ValueError(f"Stock insuficiente. Disponible: {self.stock}, Solicitado: {cantidad}")

        self.stock -= cantidad

    def to_dict(self) -> dict:
        """Convertir el producto a un diccionario serializable a JSON."""
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock,
        }

    def __str__(self) -> str:
        return f"[{self.codigo}] {self.nombre} ({self.categoria}) - ${self.precio:.2f} | Stock: {self.stock}"

