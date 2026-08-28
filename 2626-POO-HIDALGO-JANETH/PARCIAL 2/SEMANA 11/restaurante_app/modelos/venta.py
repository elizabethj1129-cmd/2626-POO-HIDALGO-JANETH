from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Venta:
    """Representa una venta realizada en el restaurante.

    Atributos:
        usuario_id: identificación del usuario que realiza la compra
        producto_codigo: código del producto vendido
        cantidad: cantidad vendida
        fecha: fecha y hora de la venta (se registra automáticamente)
    """

    usuario_id: str
    producto_codigo: str
    cantidad: int
    fecha: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def __post_init__(self) -> None:
        self.usuario_id = str(self.usuario_id).strip()
        self.producto_codigo = str(self.producto_codigo).strip()
        try:
            self.cantidad = int(self.cantidad)
            if self.cantidad <= 0:
                raise ValueError("La cantidad debe ser mayor que cero")
        except (TypeError, ValueError) as e:
            raise ValueError(f"La cantidad debe ser un número entero positivo: {e}")

    def to_dict(self) -> dict:
        """Convertir la venta a un diccionario serializable a JSON."""
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad,
            "fecha": self.fecha,
        }

    def __str__(self) -> str:
        return f"Venta: Usuario {self.usuario_id} | Producto {self.producto_codigo} | Cantidad: {self.cantidad} | Fecha: {self.fecha}"

