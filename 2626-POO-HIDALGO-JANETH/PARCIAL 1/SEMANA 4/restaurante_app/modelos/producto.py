"""
Módulo Producto
Define la clase Producto que representa los platos, bebidas y otros artículos
disponibles en el restaurante.
"""


class Producto:
    """
    Representa un producto (plato, bebida, postre, etc.) del restaurante.

    Atributos:
        nombre (str): Nombre del producto
        descripcion (str): Descripción breve del producto
        precio (float): Precio del producto en unidades monetarias
        categoria (str): Categoría del producto (Plato, Bebida, Postre, etc.)
        disponible (bool): Indica si el producto está disponible para venta
    """

    def __init__(self, nombre, descripcion, precio, categoria, disponible=True):
        """
        Inicializa un nuevo producto del restaurante.

        Args:
            nombre (str): Nombre del producto
            descripcion (str): Descripción del producto
            precio (float): Precio del producto
            categoria (str): Categoría del producto
            disponible (bool): Estado de disponibilidad (por defecto True)
        """
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.categoria = categoria
        self.disponible = disponible

    def obtener_estado(self):
        """
        Retorna el estado de disponibilidad del producto.

        Returns:
            str: "Disponible" o "No disponible"
        """
        return "Disponible" if self.disponible else "No disponible"

    def cambiar_disponibilidad(self, disponible):
        """
        Cambia el estado de disponibilidad del producto.

        Args:
            disponible (bool): Nuevo estado de disponibilidad
        """
        self.disponible = disponible

    def __str__(self):
        """
        Representación en texto del producto.

        Returns:
            str: Información formateada del producto
        """
        return (f"[{self.categoria}] {self.nombre}\n"
                f"  Descripción: {self.descripcion}\n"
                f"  Precio: ${self.precio:.2f}\n"
                f"  Estado: {self.obtener_estado()}")

