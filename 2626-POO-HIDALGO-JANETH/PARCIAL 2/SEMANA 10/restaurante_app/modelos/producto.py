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
    """

    codigo: str
    nombre: str
    categoria: str
    precio: float

    def __post_init__(self) -> None:
        self.codigo = str(self.codigo).strip()
        self.nombre = str(self.nombre).strip()
        self.categoria = str(self.categoria).strip()
        try:
            self.precio = float(self.precio)
        except (TypeError, ValueError):
            raise ValueError("El precio debe ser un número")

    def to_dict(self) -> dict:
        """Convertir el producto a un diccionario serializable a JSON."""
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
        }

    def __str__(self) -> str:
        return f"[{self.codigo}] {self.nombre} ({self.categoria}) - ${self.precio:.2f}"

