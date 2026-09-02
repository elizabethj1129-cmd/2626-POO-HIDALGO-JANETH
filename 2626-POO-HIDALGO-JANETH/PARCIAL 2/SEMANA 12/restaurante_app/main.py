"""Punto de entrada para la Semana 11: incorpora ventas, persistencia de usuarios y ventas.

Al iniciar, productos, usuarios y ventas se cargan desde sus archivos JSON.
Tras registrar, actualizar o eliminar, se persisten automáticamente.
"""

from typing import Callable, Dict
import sys
from pathlib import Path

# Asegurar que el directorio padre de `restaurante_app` esté en sys.path
project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario
from restaurante_app.servicios.restaurante import Restaurante


def main() -> None:
    """Función principal del sistema de restaurante."""
    servicio = Restaurante()

    MENU_OPTIONS = (
        "1", "2", "3", "4", "5",
        "6", "7", "8", "9", "10", "11",
    )

    actions: Dict[str, Callable[[], None]] = {}

    def registrar_producto() -> None:
        """Registrar un nuevo producto."""
        try:
            codigo = input("Código del producto: ").strip()
            nombre = input("Nombre: ").strip()
            categoria = input("Categoría: ").strip()
            precio_raw = input("Precio: ").strip()
            precio = float(precio_raw)
            stock_raw = input("Stock disponible: ").strip()
            stock = int(stock_raw)
            producto = Producto(codigo=codigo, nombre=nombre, categoria=categoria, precio=precio, stock=stock)
            servicio.registrar_producto(producto)
            print("Producto registrado correctamente.")
        except ValueError as e:
            print(f"Error: {e}")

    def buscar_producto() -> None:
        """Buscar un producto por código."""
        codigo = input("Código a buscar: ").strip()
        p = servicio.buscar_producto(codigo)
        if p:
            print("Producto encontrado:", p)
        else:
            print("Producto no encontrado.")

    def actualizar_producto() -> None:
        """Actualizar datos de un producto."""
        codigo = input("Código del producto a actualizar: ").strip()
        if servicio.buscar_producto(codigo) is None:
            print("Producto no encontrado.")
            return
        nombre = input("Nuevo nombre (enter para omitir): ").strip() or None
        categoria = input("Nueva categoría (enter para omitir): ").strip() or None
        precio_raw = input("Nuevo precio (enter para omitir): ").strip() or None
        stock_raw = input("Nuevo stock (enter para omitir): ").strip() or None
        precio = None
        stock = None
        try:
            if precio_raw is not None:
                precio = float(precio_raw)
            if stock_raw is not None:
                stock = int(stock_raw)
        except ValueError:
            print("Valor inválido. Operación cancelada.")
            return
        ok = servicio.actualizar_producto(codigo, nombre=nombre, categoria=categoria, precio=precio, stock=stock)
        print("Actualizado correctamente." if ok else "No se pudo actualizar.")

    def eliminar_producto() -> None:
        """Eliminar un producto."""
        codigo = input("Código del producto a eliminar: ").strip()
        ok = servicio.eliminar_producto(codigo)
        print("Producto eliminado." if ok else "Producto no encontrado.")

    def listar_productos() -> None:
        """Listar todos los productos."""
        productos = servicio.listar_productos()
        if not productos:
            print("No hay productos registrados.")
            return
        print("Listado de productos:")
        for p in productos:
            print(" -", p)

    def registrar_usuario() -> None:
        """Registrar un nuevo usuario."""
        try:
            identificacion = input("Identificación: ").strip()
            nombre = input("Nombre: ").strip()
            correo = input("Correo: ").strip()
            usuario = Usuario(identificacion=identificacion, nombre=nombre, correo=correo)
            servicio.registrar_usuario(usuario)
            print("Usuario registrado correctamente.")
        except ValueError as e:
            print(f"Error: {e}")

    def listar_usuarios() -> None:
        """Listar todos los usuarios."""
        usuarios = servicio.listar_usuarios()
        if not usuarios:
            print("No hay usuarios registrados.")
            return
        print("Listado de usuarios:")
        for u in usuarios:
            print(" -", u)

    def mostrar_categorias() -> None:
        """Mostrar todas las categorías únicas."""
        categorias = servicio.obtener_categorias_unicas()
        if not categorias:
            print("No hay categorías para mostrar.")
            return
        print("Categorías:")
        for c in sorted(categorias):
            print(" -", c)

    def vender_producto() -> None:
        """Realizar una venta de producto a un usuario."""
        print("\n--- Realizar una venta ---")
        identificacion_usuario = input("Identificación del usuario: ").strip()
        codigo_producto = input("Código del producto: ").strip()
        cantidad_raw = input("Cantidad a vender: ").strip()

        try:
            cantidad = int(cantidad_raw)
        except ValueError:
            print("Error: la cantidad debe ser un número entero.")
            return

        # Usar el servicio para registrar la venta
        servicio.vender_producto(codigo_producto, identificacion_usuario, cantidad)

    def consultar_ventas_usuario() -> None:
        """Consultar todas las ventas realizadas por un usuario."""
        print("\n--- Consultar ventas de un usuario ---")
        identificacion_usuario = input("Identificación del usuario: ").strip()

        usuario = servicio.buscar_usuario(identificacion_usuario)
        if usuario is None:
            print(f"Error: usuario con identificación '{identificacion_usuario}' no encontrado.")
            return

        ventas = servicio.obtener_ventas_usuario(identificacion_usuario)
        if not ventas:
            print(f"El usuario {usuario.nombre} no tiene ventas registradas.")
            return

        print(f"\nVentas del usuario: {usuario.nombre} ({usuario.identificacion})")
        print("=" * 70)
        total_cantidad = 0
        for venta in ventas:
            producto = servicio.buscar_producto(venta.producto_codigo)
            if producto:
                print(f"  Producto: {producto.nombre} ({venta.producto_codigo})")
                print(f"  Cantidad: {venta.cantidad}")
                print(f"  Precio unitario: ${producto.precio:.2f}")
                print(f"  Subtotal: ${producto.precio * venta.cantidad:.2f}")
                print(f"  Fecha: {venta.fecha}")
                print("-" * 70)
                total_cantidad += venta.cantidad

        print(f"Total de artículos vendidos: {total_cantidad}")

    def salir() -> None:
        """Salir del programa."""
        print("Saliendo...")
        raise SystemExit

    actions.update({
        "1": registrar_producto,
        "2": buscar_producto,
        "3": actualizar_producto,
        "4": eliminar_producto,
        "5": listar_productos,
        "6": registrar_usuario,
        "7": listar_usuarios,
        "8": mostrar_categorias,
        "9": vender_producto,
        "10": consultar_ventas_usuario,
        "11": salir,
    })

    while True:
        print("\n" + "=" * 70)
        print("        SISTEMA DE RESTAURANTE - SEMANA 11")
        print("=" * 70)
        print("PRODUCTOS:")
        print("  1. Registrar producto")
        print("  2. Buscar producto")
        print("  3. Actualizar producto")
        print("  4. Eliminar producto")
        print("  5. Listar productos")
        print("-" * 70)
        print("USUARIOS:")
        print("  6. Registrar usuario")
        print("  7. Listar usuarios")
        print("-" * 70)
        print("CONSULTAS:")
        print("  8. Mostrar categorías")
        print("-" * 70)
        print("VENTAS:")
        print("  9. Vender producto")
        print("  10. Consultar ventas de un usuario")
        print("-" * 70)
        print("  11. Salir")
        print("=" * 70)
        opcion = input("Seleccione una opción: ").strip()
        if opcion not in MENU_OPTIONS:
            print("Opción inválida. Intente de nuevo.")
            continue
        try:
            actions[opcion]()
        except SystemExit:
            break
        except Exception as e:
            print("Ocurrió un error al procesar la opción:", e)


if __name__ == "__main__":
    main()

