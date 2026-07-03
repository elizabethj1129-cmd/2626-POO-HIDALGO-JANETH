class Producto:
    """Clase padre que representa un producto general del restaurante."""
    def __init__(self, nombre, precio, disponibilidad=True):
        self.nombre = nombre
        self.__precio = precio  # Atributo encapsulado
        self.disponibilidad = disponibilidad

    def obtener_precio(self):
        """Método de acceso (getter) para el precio encapsulado."""
        return self.__precio

    def cambiar_precio(self, nuevo_precio):
        """Método de modificación (setter) con validación para el precio."""
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print(f"Error: El precio no puede ser negativo ni cero (Valor ingresado: {nuevo_precio}).")

    def mostrar_informacion(self):
        """Muestra la información general del producto."""
        estado = "Disponible" if self.disponibilidad else "No disponible"
        print(f"Producto: {self.nombre} | Precio: ${self.__precio:.2f} | Estado: {estado}")
