from typing import List, Optional, Set
from pathlib import Path

# Imports relativos para evitar ambigüedades en diferentes entornos
from ..modelos.producto import Producto
from ..modelos.usuario import Usuario
from .archivo_servicio import ArchivoServicio


class Restaurante:
    """Servicio encargado de administrar productos y usuarios.

    Las operaciones de persistencia se delegan a ArchivoServicio.
    """

    def __init__(self) -> None:
        self._productos: List[Producto] = []
        self._usuarios: List[Usuario] = []

        base = Path(__file__).resolve().parents[1]
        self._datos_dir = base / "datos"
        self._productos_file = self._datos_dir / "productos.json"

        self._archivo = ArchivoServicio()
        self._load_products()

    def _load_products(self) -> None:
        raw = self._archivo.cargar_productos(self._productos_file)
        for item in raw:
            try:
                codigo = item["codigo"]
                nombre = item.get("nombre", "")
                categoria = item.get("categoria", "")
                precio = item.get("precio", 0.0)
                p = Producto(codigo=codigo, nombre=nombre, categoria=categoria, precio=precio)
                if not any(x.codigo == p.codigo for x in self._productos):
                    self._productos.append(p)
            except KeyError as e:
                print(f"Registro de producto omitido: falta la clave {e}")
            except ValueError as e:
                print(f"Registro de producto omitido por valor inválido: {e}")

    def _save_products(self) -> None:
        data = [p.to_dict() for p in self._productos]
        self._archivo.guardar_productos(self._productos_file, data)

    # ----- Productos -----
    def registrar_producto(self, producto: Producto) -> None:
        if any(p.codigo == producto.codigo for p in self._productos):
            raise ValueError(f"Código de producto '{producto.codigo}' ya registrado")
        self._productos.append(producto)
        self._save_products()

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        codigo = str(codigo).strip()
        for p in self._productos:
            if p.codigo == codigo:
                return p
        return None

    def actualizar_producto(self, codigo: str, nombre: Optional[str] = None,
                             categoria: Optional[str] = None,
                             precio: Optional[float] = None) -> bool:
        p = self.buscar_producto(codigo)
        if p is None:
            return False
        if nombre is not None:
            p.nombre = nombre.strip()
        if categoria is not None:
            p.categoria = categoria.strip()
        if precio is not None:
            p.precio = float(precio)
        self._save_products()
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        p = self.buscar_producto(codigo)
        if p is None:
            return False
        self._productos.remove(p)
        self._save_products()
        return True

    def listar_productos(self) -> List[Producto]:
        return list(self._productos)

    # ----- Usuarios (no persistidos en esta entrega) -----
    def registrar_usuario(self, usuario: Usuario) -> None:
        if any(u.identificacion == usuario.identificacion for u in self._usuarios):
            raise ValueError(f"Identificación '{usuario.identificacion}' ya registrada")
        self._usuarios.append(usuario)

    def listar_usuarios(self) -> List[Usuario]:
        return list(self._usuarios)

    # ----- Auxiliares -----
    def obtener_categorias_unicas(self) -> Set[str]:
        return set(p.categoria for p in self._productos)

