class Restaurante:
    """Clase de servicio que administra los productos del restaurante."""
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []  # Lista para almacenar los productos

    def agregar_producto(self, producto):
        """Agrega un producto a la lista del restaurante."""
        self.productos.append(producto)

    def mostrar_menu(self):
        """Recorre la lista de productos y muestra su información (Demuestra Polimorfismo)."""
        print(f"\n{'='*40}")
        print(f"      MENÚ DE {self.nombre.upper()}")
        print(f"{'='*40}")
        
        for producto in self.productos:
            # Polimorfismo en acción: cada objeto (Platillo o Bebida) 
            # ejecuta su propia versión del método mostrar_informacion().
            producto.mostrar_informacion()
            
        print(f"{'='*40}\n")
