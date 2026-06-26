# Clase que representa un cliente registrado en el restaurante

class Cliente:
    """
    Clase que define un cliente del restaurante.
    Almacena información personal y datos sobre sus interacciones.
    """
    
    def __init__(self, nombre: str, email: str, telefono: str, cliente_frecuente: bool = False):
        """
        Constructor de la clase Cliente.
        
        Args:
            nombre: Nombre completo del cliente (str)
            email: Correo electrónico del cliente (str)
            telefono: Número de teléfono del cliente (str)
            cliente_frecuente: Indica si es cliente frecuente (bool)
        """
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.cliente_frecuente = cliente_frecuente
        self.numero_pedidos = 0  # Contador de pedidos realizados (int)
        self.historial_pedidos = []  # Lista de pedidos realizados (list)
    
    def __str__(self) -> str:
        """
        Método especial que representa el cliente como texto.
        Permite visualizar la información del cliente de forma clara.
        """
        tipo_cliente = "Frecuente" if self.cliente_frecuente else "Regular"
        return (f"Cliente: {self.nombre}\n"
                f"  Email: {self.email}\n"
                f"  Teléfono: {self.telefono}\n"
                f"  Tipo: {tipo_cliente}\n"
                f"  Pedidos realizados: {self.numero_pedidos}")
    
    def registrar_pedido(self, monto_pedido: float) -> None:
        """
        Método que registra un nuevo pedido del cliente.
        Incrementa el contador de pedidos e historial.
        
        Args:
            monto_pedido: Monto total del pedido (float)
        """
        self.numero_pedidos += 1
        self.historial_pedidos.append(monto_pedido)
        
        # Si el cliente llega a 5 pedidos, se marca como frecuente
        if self.numero_pedidos >= 5 and not self.cliente_frecuente:
            self.cliente_frecuente = True
            print(f"¡{self.nombre} ahora es cliente frecuente!")
    
    def obtener_información(self) -> dict:
        """
        Retorna un diccionario con la información del cliente.
        
        Returns:
            Diccionario con los atributos del cliente (dict)
        """
        return {
            "nombre": self.nombre,
            "email": self.email,
            "telefono": self.telefono,
            "cliente_frecuente": self.cliente_frecuente,
            "numero_pedidos": self.numero_pedidos
        }

