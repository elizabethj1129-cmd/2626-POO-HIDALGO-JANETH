from typing import List, Optional, Set
import json
from pathlib import Path
from dataclasses import asdict

from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario


class Restaurante:
    """Servicio encargado de administrar productos y usuarios.

    Internamente usa listas para colecciones dinámicas (productos y usuarios).
    Además persiste la información en archivos JSON dentro de la carpeta `data/`.
    """

    def __init__(self) -> None:
        self._productos: List[Producto] = []
        self._usuarios: List[Usuario] = []

        # Rutas para persistencia
        base = Path(__file__).resolve().parents[1]
        self._data_dir = base / "data"
        self._productos_file = self._data_dir / "productos.json"
        self._usuarios_file = self._data_dir / "usuarios.json"

        self._ensure_data_dir()
        self._load_from_files()

    def _ensure_data_dir(self) -> None:
        try:
            self._data_dir.mkdir(parents=True, exist_ok=True)
        except Exception:
            # En caso de fallo, continuamos sin persistencia
            pass

    def _load_from_files(self) -> None:
        # Cargar productos (se espera un diccionario {codigo: {...}})
        try:
            if self._productos_file.exists():
                with self._productos_file.open("r", encoding="utf-8") as f:
                    data = json.load(f)
                    if isinstance(data, dict):
                        for codigo, item in data.items():
                            try:
                                p = Producto(
                                    codigo=codigo,
                                    nombre=item.get("nombre", ""),
                                    categoria=item.get("categoria", ""),
                                    precio=item.get("precio", 0.0),
                                )
                                if not any(x.codigo == p.codigo for x in self._productos):
                                    self._productos.append(p)
                            except Exception:
                                continue
                    elif isinstance(data, list):
                        # Soporte retrocompatible: lista de dicts
                        for item in data:
                            try:
                                p = Producto(
                                    codigo=item.get("codigo", ""),
                                    nombre=item.get("nombre", ""),
                                    categoria=item.get("categoria", ""),
                                    precio=item.get("precio", 0.0),
                                )
                                if not any(x.codigo == p.codigo for x in self._productos):
                                    self._productos.append(p)
                            except Exception:
                                continue
        except Exception:
            # No detener la inicialización si hay errores de IO/JSON
            pass

        # Cargar usuarios (se espera un diccionario {identificacion: {...}})
        try:
            if self._usuarios_file.exists():
                with self._usuarios_file.open("r", encoding="utf-8") as f:
                    data = json.load(f)
                    if isinstance(data, dict):
                        for identificacion, item in data.items():
                            try:
                                u = Usuario(
                                    identificacion=identificacion,
                                    nombre=item.get("nombre", ""),
                                    correo=item.get("correo", ""),
                                )
                                if not any(x.identificacion == u.identificacion for x in self._usuarios):
                                    self._usuarios.append(u)
                            except Exception:
                                continue
                    elif isinstance(data, list):
                        for item in data:
                            try:
                                u = Usuario(
                                    identificacion=item.get("identificacion", ""),
                                    nombre=item.get("nombre", ""),
                                    correo=item.get("correo", ""),
                                )
                                if not any(x.identificacion == u.identificacion for x in self._usuarios):
                                    self._usuarios.append(u)
                            except Exception:
                                continue
        except Exception:
            pass

    def _save_products_file(self) -> None:
        try:
            data = {p.codigo: {"nombre": p.nombre, "categoria": p.categoria, "precio": p.precio} for p in self._productos}
            with self._productos_file.open("w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception:
            pass

    def _save_users_file(self) -> None:
        try:
            data = {u.identificacion: {"nombre": u.nombre, "correo": u.correo} for u in self._usuarios}
            with self._usuarios_file.open("w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception:
            pass

    # ----- Productos -----
    def registrar_producto(self, producto: Producto) -> None:
        if any(p.codigo == producto.codigo for p in self._productos):
            raise ValueError(f"Código de producto '{producto.codigo}' ya registrado")
        self._productos.append(producto)
        self._save_products_file()

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
        self._save_products_file()
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        p = self.buscar_producto(codigo)
        if p is None:
            return False
        self._productos.remove(p)
        self._save_products_file()
        return True

    def listar_productos(self) -> List[Producto]:
        # devolver una copia superficial para evitar manipulación externa
        return list(self._productos)

    # ----- Usuarios -----
    def registrar_usuario(self, usuario: Usuario) -> None:
        if any(u.identificacion == usuario.identificacion for u in self._usuarios):
            raise ValueError(f"Identificación '{usuario.identificacion}' ya registrada")
        self._usuarios.append(usuario)
        self._save_users_file()

    def listar_usuarios(self) -> List[Usuario]:
        return list(self._usuarios)

    # ----- Operaciones auxiliares -----
    def obtener_categorias_unicas(self) -> Set[str]:
        return set(p.categoria for p in self._productos)
