from modelos.producto import Producto

class Platillo(Producto):
    """Clase hija que representa un platillo o comida del restaurante."""
    def __init__(self, nombre, precio, calorias, disponibilidad=True):
        # Utilizar super() para inicializar atributos de la clase padre
        super().__init__(nombre, precio, disponibilidad)
        self.calorias = calorias

    def mostrar_informacion(self):
        """Sobrescribe el método de la clase padre para incluir calorías (Polimorfismo)."""
        estado = "Disponible" if self.disponibilidad else "No disponible"
        print(f"Platillo: {self.nombre} | Calorías: {self.calorias} kcal | Precio: ${self.obtener_precio():.2f} | Estado: {estado}")
