"""
Clase Mascota - Programa de Programación Orientada a Objetos
Esta clase implementa la abstracción de una mascota con sus atributos y métodos.
"""


class Mascota:
    """
    Clase que representa una mascota.

    Atributos:
        nombre (str): El nombre de la mascota
        especie (str): La especie de la mascota (perro, gato, pájaro, etc.)
        edad (int): La edad de la mascota en años
    """

    def __init__(self, nombre, especie, edad):
        """
        Constructor de la clase Mascota.

        Args:
            nombre (str): El nombre de la mascota
            especie (str): La especie de la mascota
            edad (int): La edad de la mascota
        """
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self):
        """
        Método que muestra la información completa de la mascota.
        Imprime el nombre, especie y edad de la mascota.
        """
        print(f"=== Información de la Mascota ===")
        print(f"Nombre: {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad: {self.edad} años")
        print()

    def hacer_sonido(self):
        """
        Método que emite el sonido característico de la mascota.
        El sonido depende de la especie de la mascota.
        """
        sonidos = {
            "perro": "¡Guau guau!",
            "gato": "¡Miau miau!",
            "pájaro": "¡Pío pío!",
            "conejo": "¡Ñic ñic!",
            "hamster": "¡Chis chis!",
            "caballo": "¡Jiiiii!",
            "vaca": "¡Muuu!"
        }

        # Obtener el sonido de la especie, o un sonido genérico si no existe
        especie_lower = self.especie.lower()
        sonido = sonidos.get(especie_lower, "¡Hace un sonido!")

        print(f"{self.nombre} ({self.especie}): {sonido}")
        print()

