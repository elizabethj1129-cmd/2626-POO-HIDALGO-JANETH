from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Usuario:
    """Representa un usuario registrado en el sistema.

    Atributos:
        identificacion: identificador único (string o número)
        nombre: nombre completo
        correo: correo electrónico
        contraseña: contraseña para acceso al sistema
    """

    identificacion: str
    nombre: str
    correo: str
    contraseña: str = ""
    rol: str = "Cliente"

    def __post_init__(self) -> None:
        self.identificacion = str(self.identificacion).strip()
        self.nombre = str(self.nombre).strip()
        self.correo = str(self.correo).strip()
        self.contraseña = str(self.contraseña).strip()
        self.rol = str(self.rol).strip()

    def to_dict(self) -> dict:
        """Convertir el usuario a un diccionario serializable a JSON."""
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo,
            "contraseña": self.contraseña,
            "rol": self.rol,
        }

    def __str__(self) -> str:
        return f"{self.identificacion} - {self.nombre} <{self.correo}> ({self.rol})"

