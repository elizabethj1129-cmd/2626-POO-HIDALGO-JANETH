"""Punto de entrada para la Semana 10: incorpora persistencia JSON de productos.

Al iniciar, los productos se cargan desde `datos/productos.json` y se reconstruyen
como objetos Producto. Tras registrar, actualizar o eliminar un producto, el
archivo se actualiza automáticamente.
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
    servicio = Restaurante()

    MENU_OPTIONS = (
        "1", "2", "3", "4", "5",
        "6", "7", "8", "9",
    )

    actions: Dict[str, Callable[[], None]] = {}

    def registrar_producto() -> None:
        try:
            codigo = input("Código del producto: ").strip()
            nombre = input("Nombre: ").strip()
            categoria = input("Categoría: ").strip()
            precio_raw = input("Precio: ").strip()
            precio = float(precio_raw)
            producto = Producto(codigo=codigo, nombre=nombre, categoria=categoria, precio=precio)
            servicio.registrar_producto(producto)
            print("Producto registrado correctamente.")
        except ValueError as e:
            print(f"Error: {e}")

    def buscar_producto() -> None:
        codigo = input("Código a buscar: ").strip()
        p = servicio.buscar_producto(codigo)
        if p:
            print("Producto encontrado:", p)
        else:
            print("Producto no encontrado.")

    def actualizar_producto() -> None:
        codigo = input("Código del producto a actualizar: ").strip()
        if servicio.buscar_producto(codigo) is None:
            print("Producto no encontrado.")
            return
        nombre = input("Nuevo nombre (enter para omitir): ").strip() or None
        categoria = input("Nueva categoría (enter para omitir): ").strip() or None
        precio_raw = input("Nuevo precio (enter para omitir): ").strip() or None
        precio = None
        try:
            if precio_raw is not None:
                precio = float(precio_raw)
        except ValueError:
            print("Precio inválido. Operación cancelada.")
            return
        ok = servicio.actualizar_producto(codigo, nombre=nombre, categoria=categoria, precio=precio)
        print("Actualizado correctamente." if ok else "No se pudo actualizar.")

    def eliminar_producto() -> None:
        codigo = input("Código del producto a eliminar: ").strip()
        ok = servicio.eliminar_producto(codigo)
        print("Producto eliminado." if ok else "Producto no encontrado.")

    def listar_productos() -> None:
        productos = servicio.listar_productos()
        if not productos:
            print("No hay productos registrados.")
            return
        print("Listado de productos:")
        for p in productos:
            print(" -", p)

    def registrar_usuario() -> None:
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
        usuarios = servicio.listar_usuarios()
        if not usuarios:
            print("No hay usuarios registrados.")
            return
        print("Listado de usuarios:")
        for u in usuarios:
            print(" -", u)

    def mostrar_categorias() -> None:
        categorias = servicio.obtener_categorias_unicas()
        if not categorias:
            print("No hay categorías para mostrar.")
            return
        print("Categorías:")
        for c in sorted(categorias):
            print(" -", c)

    def salir() -> None:
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
        "9": salir,
    })

    while True:
        print("\n========================================")
        print("        SISTEMA DE RESTAURANTE")
        print("========================================")
        print("1. Registrar producto")
        print("2. Buscar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Listar productos")
        print("----------------------------------------")
        print("6. Registrar usuario")
        print("7. Listar usuarios")
        print("----------------------------------------")
        print("8. Mostrar categorías")
        print("9. Salir")
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

