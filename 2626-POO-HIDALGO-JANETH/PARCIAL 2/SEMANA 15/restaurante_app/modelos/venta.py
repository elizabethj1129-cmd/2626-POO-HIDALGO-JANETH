from typing import Dict, Any
from datetime import datetime
import uuid

class Venta:
    """Modelo que representa una venta en el restaurante.

    Almacena la relación entre un usuario que realiza la compra
    y el producto adquirido, junto con la cantidad y el total.
    """

    def __init__(
        self,
        usuario_identificacion: str,
        producto_codigo: str,
        cantidad: int = 1,
        total: float = 0.0,
        id_venta: str = None,
        fecha: str = None,
    ):
        """Inicializar una nueva venta.

        Args:
            usuario_identificacion: identificación del usuario comprador
            producto_codigo: código del producto vendido
            cantidad: cantidad vendida
            total: total de la venta
            id_venta: identificador único de la venta (opcional)
            fecha: fecha de la venta en formato ISO (opcional)
        """
        self.id_venta = id_venta if id_venta else str(uuid.uuid4())
        self.usuario_identificacion = usuario_identificacion
        self.producto_codigo = producto_codigo
        self.cantidad = cantidad
        self.total = total
        self.fecha = fecha if fecha else datetime.now().isoformat()

    def to_dict(self) -> Dict[str, Any]:
        """Convertir la venta a un diccionario para serialización JSON.

        Returns:
            Diccionario con los datos de la venta
        """
        return {
            "id_venta": self.id_venta,
            "usuario_identificacion": self.usuario_identificacion,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad,
            "total": self.total,
            "fecha": self.fecha,
        }
