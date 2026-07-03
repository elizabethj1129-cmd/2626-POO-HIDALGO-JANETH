from modelos.producto import Producto

class Bebida(Producto):
    """Clase hija que representa una bebida del restaurante."""
    def __init__(self, nombre, precio, volumen_ml, disponibilidad=True):
        # Utilizar super() para inicializar atributos de la clase padre
        super().__init__(nombre, precio, disponibilidad)
        self.volumen_ml = volumen_ml

    def mostrar_informacion(self):
        """Sobrescribe el método de la clase padre para incluir volumen (Polimorfismo)."""
        estado = "Disponible" if self.disponibilidad else "No disponible"
        print(f"Bebida: {self.nombre} | Volumen: {self.volumen_ml} ml | Precio: ${self.obtener_precio():.2f} | Estado: {estado}")
