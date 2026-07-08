"""Módulo modelos.cliente
Contiene la clase Cliente implementada con @dataclass
"""
from dataclasses import dataclass


@dataclass
class Cliente:
    """Representa un cliente del restaurante.

    Atributos:
        id_cliente (int): identificador único del cliente
        nombre (str): nombre completo
        correo (str): correo electrónico
    """
    id_cliente: int
    nombre: str
    correo: str

    def __str__(self) -> str:
        return f"ID: {self.id_cliente} | Nombre: {self.nombre} | Correo: {self.correo}"

