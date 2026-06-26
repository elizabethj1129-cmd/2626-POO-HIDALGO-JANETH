# Clase que representa un producto disponible en el restaurante

class Producto:
    """
    Clase que define un producto del restaurante.
    Almacena información como nombre, precio, disponibilidad y cantidad.
    """

    def __init__(self, nombre: str, precio: float, cantidad: int, descripcion: str, disponible: bool = True):
        """
        Constructor de la clase Producto.

        Args:
            nombre: Identificador del producto (str)
            precio: Valor monetario del producto (float)
            cantidad: Cantidad disponible en inventario (int)
            descripcion: Detalles sobre el producto (str)
            disponible: Indica si el producto está disponible (bool)
        """
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.descripcion = descripcion
        self.disponible = disponible

    def __str__(self) -> str:
        """
        Método especial que representa el producto como texto.
        Permite visualizar la información del producto de forma clara.
        """
        estado = "Disponible" if self.disponible else "No disponible"
        return (f"Producto: {self.nombre}\n"
                f"  Precio: ${self.precio:.2f}\n"
                f"  Cantidad: {self.cantidad} unidades\n"
                f"  Descripción: {self.descripcion}\n"
                f"  Estado: {estado}")

    def actualizar_cantidad(self, cantidad_vendida: int) -> None:
        """
        Método que reduce la cantidad disponible del producto.

        Args:
            cantidad_vendida: Número de unidades vendidas (int)
        """
        if cantidad_vendida <= self.cantidad:
            self.cantidad -= cantidad_vendida
        else:
            print(f"No hay suficiente cantidad de {self.nombre}")

    def obtener_información(self) -> dict:
        """
        Retorna un diccionario con la información del producto.

        Returns:
            Diccionario con los atributos del producto (dict)
        """
        return {
            "nombre": self.nombre,
            "precio": self.precio,
            "cantidad": self.cantidad,
            "descripcion": self.descripcion,
            "disponible": self.disponible
        }

