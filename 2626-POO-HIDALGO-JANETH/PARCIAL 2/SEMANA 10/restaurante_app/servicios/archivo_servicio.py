import json
from pathlib import Path
from typing import List, Dict, Any
from json import JSONDecodeError


class ArchivoServicio:
    """Servicio responsable de la lectura y escritura del archivo de productos en JSON.

    Métodos estáticos expuestos para facilitar su uso desde el servicio Restaurante.
    """

    @staticmethod
    def cargar_productos(path: Path) -> List[Dict[str, Any]]:
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
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("w", encoding="utf-8") as f:
                json.dump(productos, f, ensure_ascii=False, indent=2)
        except PermissionError:
            print("Error: permisos insuficientes para escribir productos.json")
        except Exception as e:
            # No usar captura genérica para ocultar errores: aquí informamos
            print("Error al guardar productos:", e)

