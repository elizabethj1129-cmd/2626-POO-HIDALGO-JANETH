import json
from pathlib import Path
from typing import List, Dict, Any
from json import JSONDecodeError


class ArchivoServicio:
    """Servicio responsable de la lectura y escritura de archivos JSON.

    Maneja persistencia para productos, usuarios y ventas.
    """

    @staticmethod
    def cargar_productos(path: Path) -> List[Dict[str, Any]]:
        """Cargar productos desde archivo JSON.

        Args:
            path: ruta al archivo de productos

        Returns:
            Lista de diccionarios con datos de productos
        """
        try:
            with path.open("r", encoding="utf-8") as f:
                data = json.load(f)
                # Soportar tanto lista como diccionario (retrocompatibilidad)
                if isinstance(data, dict):
                    result: List[Dict[str, Any]] = []
                    for codigo, item in data.items():
                        if isinstance(item, dict):
                            record = dict(item)
                            record.setdefault("codigo", codigo)
                            result.append(record)
                    return result
                elif isinstance(data, list):
                    return data
                else:
                    raise ValueError("Formato de archivo de productos no reconocido")
        except FileNotFoundError:
            # Primer inicio: no existe el archivo, arrancar con colección vacía
            return []
        except JSONDecodeError:
            print("Error: el archivo de productos contiene JSON inválido. Se iniciará con lista vacía.")
            return []
        except PermissionError:
            print("Error: permisos insuficientes para leer productos.json")
            return []

    @staticmethod
    def guardar_productos(path: Path, productos: List[Dict[str, Any]]) -> None:
        """Guardar productos en archivo JSON.

        Args:
            path: ruta al archivo de productos
            productos: lista de diccionarios con datos de productos
        """
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("w", encoding="utf-8") as f:
                json.dump(productos, f, ensure_ascii=False, indent=2)
        except PermissionError:
            print("Error: permisos insuficientes para escribir productos.json")
        except Exception as e:
            print("Error al guardar productos:", e)

    @staticmethod
    def cargar_usuarios(path: Path) -> List[Dict[str, Any]]:
        """Cargar usuarios desde archivo JSON.

        Args:
            path: ruta al archivo de usuarios

        Returns:
            Lista de diccionarios con datos de usuarios
        """
        try:
            with path.open("r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    return data
                else:
                    raise ValueError("Formato de archivo de usuarios no reconocido")
        except FileNotFoundError:
            # Primer inicio: no existe el archivo
            return []
        except JSONDecodeError:
            print("Error: el archivo de usuarios contiene JSON inválido. Se iniciará con lista vacía.")
            return []
        except PermissionError:
            print("Error: permisos insuficientes para leer usuarios.json")
            return []

    @staticmethod
    def guardar_usuarios(path: Path, usuarios: List[Dict[str, Any]]) -> None:
        """Guardar usuarios en archivo JSON.

        Args:
            path: ruta al archivo de usuarios
            usuarios: lista de diccionarios con datos de usuarios
        """
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("w", encoding="utf-8") as f:
                json.dump(usuarios, f, ensure_ascii=False, indent=2)
        except PermissionError:
            print("Error: permisos insuficientes para escribir usuarios.json")
        except Exception as e:
            print("Error al guardar usuarios:", e)

    @staticmethod
    def cargar_ventas(path: Path) -> List[Dict[str, Any]]:
        """Cargar ventas desde archivo JSON.

        Args:
            path: ruta al archivo de ventas

        Returns:
            Lista de diccionarios con datos de ventas
        """
        try:
            with path.open("r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    return data
                else:
                    raise ValueError("Formato de archivo de ventas no reconocido")
        except FileNotFoundError:
            # Primer inicio: no existe el archivo
            return []
        except JSONDecodeError:
            print("Error: el archivo de ventas contiene JSON inválido. Se iniciará con lista vacía.")
            return []
        except PermissionError:
            print("Error: permisos insuficientes para leer ventas.json")
            return []

    @staticmethod
    def guardar_ventas(path: Path, ventas: List[Dict[str, Any]]) -> None:
        """Guardar ventas en archivo JSON.

        Args:
            path: ruta al archivo de ventas
            ventas: lista de diccionarios con datos de ventas
        """
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("w", encoding="utf-8") as f:
                json.dump(ventas, f, ensure_ascii=False, indent=2)
        except PermissionError:
            print("Error: permisos insuficientes para escribir ventas.json")
        except Exception as e:
            print("Error al guardar ventas:", e)

