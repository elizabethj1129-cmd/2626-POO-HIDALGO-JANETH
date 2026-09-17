from pathlib import Path
from typing import List, Dict, Any, Optional
from ..modelos.producto import Producto
from ..modelos.usuario import Usuario
from .archivo_servicio import ArchivoServicio


class RestauranteServicio:
    """Servicio principal que gestiona productos y usuarios del restaurante.

    Responsabilidades:
        - Cargar datos desde archivos JSON a través de ArchivoServicio
        - Convertir datos JSON en objetos Producto y Usuario
        - Validar acceso de usuarios
        - Proporcionar operaciones para consultar productos y usuarios
    """

    def __init__(self, datos_dir: Path = None):
        """Inicializar el servicio del restaurante.

        Args:
            datos_dir: directorio donde se almacenan los archivos JSON
        """
        if datos_dir is None:
            datos_dir = Path(__file__).parent.parent / "datos"

        self.datos_dir = Path(datos_dir)
        self.archivo_servicio = ArchivoServicio()
        self.productos: List[Producto] = []
        self.usuarios: List[Usuario] = []

        # Cargar datos al inicializar
        self._cargar_datos()

    def _cargar_datos(self) -> None:
        """Cargar productos y usuarios desde archivos JSON."""
        # Cargar productos
        productos_data = self.archivo_servicio.cargar_productos(
            self.datos_dir / "productos.json"
        )
        self.productos = [
            Producto(**p) for p in productos_data if self._validar_producto(p)
        ]

        # Cargar usuarios
        usuarios_data = self.archivo_servicio.cargar_usuarios(
            self.datos_dir / "usuarios.json"
        )
        self.usuarios = [
            Usuario(**u) for u in usuarios_data if self._validar_usuario(u)
        ]

    @staticmethod
    def _validar_producto(p: Dict[str, Any]) -> bool:
        """Validar que un diccionario de producto tenga los campos necesarios."""
        required = {"codigo", "nombre", "categoria", "precio"}
        return required.issubset(set(p.keys()))

    @staticmethod
    def _validar_usuario(u: Dict[str, Any]) -> bool:
        """Validar que un diccionario de usuario tenga los campos necesarios."""
        required = {"identificacion", "nombre", "correo"}
        return required.issubset(set(u.keys()))

    def validar_acceso(self, identificacion: str, contraseña: str) -> bool:
        """Validar las credenciales de un usuario.

        Args:
            identificacion: identificación del usuario
            contraseña: contraseña del usuario

        Returns:
            True si las credenciales son válidas, False en caso contrario
        """
        usuario = self.buscar_usuario(identificacion)
        if usuario is None:
            return False
        return usuario.contraseña == contraseña

    def buscar_usuario(self, identificacion: str) -> Optional[Usuario]:
        """Buscar un usuario por identificación.

        Args:
            identificacion: identificación del usuario

        Returns:
            El usuario encontrado o None
        """
        for usuario in self.usuarios:
            if usuario.identificacion == identificacion:
                return usuario
        return None

    def listar_usuarios(self) -> List[Usuario]:
        """Obtener la lista de todos los usuarios.

        Returns:
            Lista de usuarios registrados
        """
        return self.usuarios.copy()

    def listar_productos(self) -> List[Producto]:
        """Obtener la lista de todos los productos.

        Returns:
            Lista de productos registrados
        """
        return self.productos.copy()

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        """Buscar un producto por código.

        Args:
            codigo: código del producto

        Returns:
            El producto encontrado o None
        """
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None

    def obtener_cantidad_producto(self, codigo: str) -> int:
        """Obtener la cantidad disponible de un producto.

        Args:
            codigo: código del producto

        Returns:
            Cantidad disponible o 0 si no existe
        """
        producto = self.buscar_producto(codigo)
        return producto.stock if producto else 0

    def _guardar_productos(self) -> None:
        """Guardar la lista actual de productos en el archivo JSON."""
        productos_data = [p.to_dict() for p in self.productos]
        self.archivo_servicio.guardar_productos(
            self.datos_dir / "productos.json", productos_data
        )

    def registrar_producto(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int = 0) -> bool:
        """Registra un nuevo producto si el código no existe."""
        if self.buscar_producto(codigo) is not None:
            return False
        
        nuevo_producto = Producto(codigo=codigo, nombre=nombre, categoria=categoria, precio=precio, stock=stock)
        self.productos.append(nuevo_producto)
        self._guardar_productos()
        return True

    def actualizar_producto(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int) -> bool:
        """Actualiza un producto existente."""
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False
        
        producto.nombre = str(nombre).strip()
        producto.categoria = str(categoria).strip()
        producto.precio = float(precio)
        producto.stock = int(stock)
        
        self._guardar_productos()
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        """Elimina un producto por su código."""
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False
        
        self.productos.remove(producto)
        self._guardar_productos()
        return True

