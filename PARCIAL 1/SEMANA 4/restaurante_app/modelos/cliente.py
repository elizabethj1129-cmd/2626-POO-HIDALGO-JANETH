"""
Módulo Cliente
Define la clase Cliente que representa a los clientes del restaurante.
"""


class Cliente:
    """
    Representa un cliente del restaurante.

    Atributos:
        numero_cliente (int): Identificador único del cliente
        nombre (str): Nombre completo del cliente
        email (str): Correo electrónico del cliente
        telefono (str): Número telefónico del cliente
        pedidos_realizados (int): Cantidad de pedidos realizados por el cliente
    """

    contador_clientes = 1000  # Contador para generar IDs únicos

    def __init__(self, nombre, email, telefono):
        """
        Inicializa un nuevo cliente del restaurante.

        Args:
            nombre (str): Nombre del cliente
            email (str): Email del cliente
            telefono (str): Teléfono del cliente
        """
        self.numero_cliente = Cliente.contador_clientes
        Cliente.contador_clientes += 1
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.pedidos_realizados = 0

    def registrar_pedido(self):
        """
        Registra un nuevo pedido realizado por el cliente.
        """
        self.pedidos_realizados += 1

    def obtener_informacion_contacto(self):
        """
        Retorna la información de contacto del cliente.

        Returns:
            str: Información de contacto formateada
        """
        return f"Email: {self.email} | Teléfono: {self.telefono}"

    def __str__(self):
        """
        Representación en texto del cliente.

        Returns:
            str: Información formateada del cliente
        """
        return (f"Cliente #{self.numero_cliente}: {self.nombre}\n"
                f"  Contacto: {self.obtener_informacion_contacto()}\n"
                f"  Pedidos realizados: {self.pedidos_realizados}")

