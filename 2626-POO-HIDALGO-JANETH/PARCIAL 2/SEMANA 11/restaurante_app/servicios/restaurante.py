from typing import List, Optional, Set
from pathlib import Path

# Imports relativos para evitar ambigüedades en diferentes entornos
from ..modelos.producto import Producto
from ..modelos.usuario import Usuario
from ..modelos.venta import Venta
from .archivo_servicio import ArchivoServicio


class Restaurante:
    """Servicio encargado de administrar productos, usuarios y ventas.

    Las operaciones de persistencia se delegan a ArchivoServicio.
    """

    def __init__(self) -> None:
        self._productos: List[Producto] = []
        self._usuarios: List[Usuario] = []
        self._ventas: List[Venta] = []

        base = Path(__file__).resolve().parents[1]
        self._datos_dir = base / "datos"
        self._productos_file = self._datos_dir / "productos.json"
        self._usuarios_file = self._datos_dir / "usuarios.json"
        self._ventas_file = self._datos_dir / "ventas.json"

        self._archivo = ArchivoServicio()
        self._load_products()
        self._load_users()
        self._load_sales()

    def _load_products(self) -> None:
        """Cargar productos desde JSON al iniciar."""
        raw = self._archivo.cargar_productos(self._productos_file)
        for item in raw:
            try:
                codigo = item["codigo"]
                nombre = item.get("nombre", "")
                categoria = item.get("categoria", "")
                precio = item.get("precio", 0.0)
                stock = item.get("stock", 0)
                p = Producto(codigo=codigo, nombre=nombre, categoria=categoria, precio=precio, stock=stock)
                if not any(x.codigo == p.codigo for x in self._productos):
                    self._productos.append(p)
            except KeyError as e:
                print(f"Registro de producto omitido: falta la clave {e}")
            except ValueError as e:
                print(f"Registro de producto omitido por valor inválido: {e}")

    def _load_users(self) -> None:
        """Cargar usuarios desde JSON al iniciar."""
        raw = self._archivo.cargar_usuarios(self._usuarios_file)
        for item in raw:
            try:
                identificacion = item["identificacion"]
                nombre = item.get("nombre", "")
                correo = item.get("correo", "")
                u = Usuario(identificacion=identificacion, nombre=nombre, correo=correo)
                if not any(x.identificacion == u.identificacion for x in self._usuarios):
                    self._usuarios.append(u)
            except KeyError as e:
                print(f"Registro de usuario omitido: falta la clave {e}")
            except ValueError as e:
                print(f"Registro de usuario omitido por valor inválido: {e}")

    def _load_sales(self) -> None:
        """Cargar ventas desde JSON al iniciar."""
        raw = self._archivo.cargar_ventas(self._ventas_file)
        for item in raw:
            try:
                usuario_id = item["usuario_id"]
                producto_codigo = item["producto_codigo"]
                cantidad = item.get("cantidad", 0)
                fecha = item.get("fecha", "")
                v = Venta(usuario_id=usuario_id, producto_codigo=producto_codigo, cantidad=cantidad)
                v.fecha = fecha  # Preservar fecha original
                if not any(x.usuario_id == v.usuario_id and x.producto_codigo == v.producto_codigo
                           and x.fecha == v.fecha for x in self._ventas):
                    self._ventas.append(v)
            except KeyError as e:
                print(f"Registro de venta omitido: falta la clave {e}")
            except ValueError as e:
                print(f"Registro de venta omitido por valor inválido: {e}")

    def _save_products(self) -> None:
        """Guardar productos en JSON."""
        data = [p.to_dict() for p in self._productos]
        self._archivo.guardar_productos(self._productos_file, data)

    def _save_users(self) -> None:
        """Guardar usuarios en JSON."""
        data = [u.to_dict() for u in self._usuarios]
        self._archivo.guardar_usuarios(self._usuarios_file, data)

    def _save_sales(self) -> None:
        """Guardar ventas en JSON."""
        data = [v.to_dict() for v in self._ventas]
        self._archivo.guardar_ventas(self._ventas_file, data)

    # ----- Productos -----
    def registrar_producto(self, producto: Producto) -> None:
        """Registrar un nuevo producto.

        Args:
            producto: objeto Producto a registrar

        Raises:
            ValueError: si el código ya existe
        """
        if any(p.codigo == producto.codigo for p in self._productos):
            raise ValueError(f"Código de producto '{producto.codigo}' ya registrado")
        self._productos.append(producto)
        self._save_products()

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        """Buscar un producto por código.

        Args:
            codigo: código del producto a buscar

        Returns:
            Objeto Producto si se encontró, None en caso contrario
        """
        codigo = str(codigo).strip()
        for p in self._productos:
            if p.codigo == codigo:
                return p
        return None

    def actualizar_producto(self, codigo: str, nombre: Optional[str] = None,
                           categoria: Optional[str] = None,
                           precio: Optional[float] = None,
                           stock: Optional[int] = None) -> bool:
        """Actualizar datos de un producto.

        Args:
            codigo: código del producto a actualizar
            nombre: nuevo nombre (opcional)
            categoria: nueva categoría (opcional)
            precio: nuevo precio (opcional)
            stock: nuevo stock (opcional)

        Returns:
            True si la actualización fue exitosa, False en caso contrario
        """
        p = self.buscar_producto(codigo)
        if p is None:
            return False
        if nombre is not None:
            p.nombre = nombre.strip()
        if categoria is not None:
            p.categoria = categoria.strip()
        if precio is not None:
            p.precio = float(precio)
        if stock is not None:
            stock = int(stock)
            if stock < 0:
                raise ValueError("El stock no puede ser negativo")
            p.stock = stock
        self._save_products()
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        """Eliminar un producto.

        Args:
            codigo: código del producto a eliminar

        Returns:
            True si la eliminación fue exitosa, False en caso contrario
        """
        p = self.buscar_producto(codigo)
        if p is None:
            return False
        self._productos.remove(p)
        self._save_products()
        return True

    def listar_productos(self) -> List[Producto]:
        """Obtener lista de todos los productos.

        Returns:
            Lista de objetos Producto
        """
        return list(self._productos)

    # ----- Usuarios -----
    def registrar_usuario(self, usuario: Usuario) -> None:
        """Registrar un nuevo usuario.

        Args:
            usuario: objeto Usuario a registrar

        Raises:
            ValueError: si la identificación ya existe
        """
        if any(u.identificacion == usuario.identificacion for u in self._usuarios):
            raise ValueError(f"Identificación '{usuario.identificacion}' ya registrada")
        self._usuarios.append(usuario)
        self._save_users()

    def buscar_usuario(self, identificacion: str) -> Optional[Usuario]:
        """Buscar un usuario por identificación.

        Args:
            identificacion: identificación del usuario a buscar

        Returns:
            Objeto Usuario si se encontró, None en caso contrario
        """
        identificacion = str(identificacion).strip()
        for u in self._usuarios:
            if u.identificacion == identificacion:
                return u
        return None

    def listar_usuarios(self) -> List[Usuario]:
        """Obtener lista de todos los usuarios.

        Returns:
            Lista de objetos Usuario
        """
        return list(self._usuarios)

    # ----- Ventas -----
    def vender_producto(self, codigo_producto: str, identificacion_usuario: str, cantidad: int) -> bool:
        """Realizar una venta de un producto a un usuario.

        Valida que el usuario y el producto existan, que la cantidad sea válida
        y que exista stock suficiente. Si todo es correcto, registra la venta,
        disminuye el stock y guarda los cambios.

        Args:
            codigo_producto: código del producto a vender
            identificacion_usuario: identificación del usuario que compra
            cantidad: cantidad a vender

        Returns:
            True si la venta fue exitosa, False en caso contrario
        """
        # Validar cantidad
        try:
            cantidad = int(cantidad)
        except (TypeError, ValueError):
            print("Error: la cantidad debe ser un número entero")
            return False

        if cantidad <= 0:
            print("Error: la cantidad debe ser mayor que cero")
            return False

        # Buscar usuario y producto
        usuario = self.buscar_usuario(identificacion_usuario)
        producto = self.buscar_producto(codigo_producto)

        if usuario is None:
            print(f"Error: usuario con identificación '{identificacion_usuario}' no encontrado")
            return False

        if producto is None:
            print(f"Error: producto con código '{codigo_producto}' no encontrado")
            return False

        # Validar stock
        if producto.stock < cantidad:
            print(f"Error: stock insuficiente. Disponible: {producto.stock}, Solicitado: {cantidad}")
            return False

        # Crear y registrar venta
        try:
            venta = Venta(usuario_id=usuario.identificacion, producto_codigo=producto.codigo, cantidad=cantidad)
            self._ventas.append(venta)

            # Disminuir stock
            producto.stock -= cantidad

            # Guardar cambios
            self._save_sales()
            self._save_products()

            print(f"Venta registrada exitosamente: {venta}")
            return True
        except ValueError as e:
            print(f"Error al registrar la venta: {e}")
            return False

    def obtener_ventas_usuario(self, identificacion_usuario: str) -> List[Venta]:
        """Obtener todas las ventas realizadas por un usuario.

        Args:
            identificacion_usuario: identificación del usuario

        Returns:
            Lista de objetos Venta asociados al usuario
        """
        identificacion_usuario = str(identificacion_usuario).strip()
        ventas_usuario: List[Venta] = []
        for venta in self._ventas:
            if venta.usuario_id == identificacion_usuario:
                ventas_usuario.append(venta)
        return ventas_usuario

    def listar_ventas(self) -> List[Venta]:
        """Obtener lista de todas las ventas.

        Returns:
            Lista de objetos Venta
        """
        return list(self._ventas)

    # ----- Auxiliares -----
    def obtener_categorias_unicas(self) -> Set[str]:
        """Obtener conjunto de categorías únicas de productos.

        Returns:
            Conjunto de categorías
        """
        return set(p.categoria for p in self._productos)

