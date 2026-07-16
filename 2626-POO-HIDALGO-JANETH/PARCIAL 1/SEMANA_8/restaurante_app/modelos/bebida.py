from modelos.producto import Producto

class Bebida(Producto):
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, tamano: str, tipo_envase: str):
        super().__init__(codigo, nombre, categoria, precio)
        self.tamano = tamano
        self.tipo_envase = tipo_envase

    def mostrar_informacion(self) -> str:
        base_info = super().mostrar_informacion()
        return f"{base_info} | Tamaño: {self.tamano} | Envase: {self.tipo_envase}"
