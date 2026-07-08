"""Punto de entrada del sistema de restaurante.

Presenta un menú interactivo para registrar, listar y buscar productos y clientes.
"""
from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente


def mostrar_menu() -> None:
    print("""
========================================
        SISTEMA DE RESTAURANTE
========================================
1. Registrar producto
2. Listar productos
3. Buscar producto
----------------------------------------
4. Registrar cliente
5. Listar clientes
6. Buscar cliente
----------------------------------------
7. Salir
""")


def solicitar_producto_interactivo() -> Producto:
    """Solicita datos por consola y devuelve un objeto Producto (lanza ValueError si inválido)."""
    nombre = input("Nombre del producto: ").strip()
    categoria = input("Categoría: ").strip()
    precio = input("Precio: ")
    disponible_input = input("¿Disponible? (s/n) [s]: ").strip().lower() or "s"
    disponible = disponible_input.startswith("s")
    producto = Producto(nombre=nombre, categoria=categoria, precio=precio, disponible=disponible)
    return producto


def solicitar_cliente_interactivo(next_id: int) -> Cliente:
    nombre = input("Nombre completo del cliente: ").strip()
    correo = input("Correo electrónico: ").strip()
    cliente = Cliente(id_cliente=next_id, nombre=nombre, correo=correo)
    return cliente


def main() -> None:
    servicio = Restaurante()

    # Datos de ejemplo para facilitar la comprensión didáctica
    try:
        servicio.registrar_producto(Producto("Café Americano", "Bebida", 2.5, True))
        servicio.registrar_producto(Producto("Ensalada César", "Entrada", 5.75, True))
        servicio.registrar_producto(Producto("Lomo Saltado", "Plato", 12.0, False))
    except Exception:
        # Ignorar errores en semilla (no deberían ocurrir)
        pass

    servicio.registrar_cliente(Cliente(id_cliente=1, nombre="María Pérez", correo="maria@example.com"))
    servicio.registrar_cliente(Cliente(id_cliente=2, nombre="Juan López", correo="juan@example.com"))

    siguiente_id_cliente = 3

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("-- Registrar producto --")
            try:
                p = solicitar_producto_interactivo()
                servicio.registrar_producto(p)
                print("Producto registrado correctamente:\n", p.mostrar_informacion())
            except Exception as e:
                print("Error al crear el producto:", e)

        elif opcion == "2":
            print("-- Lista de productos --")
            productos = servicio.listar_productos()
            if not productos:
                print("No hay productos registrados.")
            else:
                for idx, prod in enumerate(productos, start=1):
                    print(f"{idx}. {prod.mostrar_informacion()}")

        elif opcion == "3":
            print("-- Buscar producto --")
            criterio = input("Ingrese nombre o parte del nombre a buscar: ").strip()
            encontrados = servicio.buscar_producto_por_nombre(criterio)
            if not encontrados:
                print("No se encontraron productos para ese criterio.")
            else:
                for prod in encontrados:
                    print(prod.mostrar_informacion())

        elif opcion == "4":
            print("-- Registrar cliente --")
            try:
                c = solicitar_cliente_interactivo(siguiente_id_cliente)
                servicio.registrar_cliente(c)
                siguiente_id_cliente += 1
                print("Cliente registrado:", c)
            except Exception as e:
                print("Error al registrar cliente:", e)

        elif opcion == "5":
            print("-- Lista de clientes --")
            clientes = servicio.listar_clientes()
            if not clientes:
                print("No hay clientes registrados.")
            else:
                for cl in clientes:
                    print(cl)

        elif opcion == "6":
            print("-- Buscar cliente por ID --")
            entrada = input("Ingrese ID del cliente: ").strip()
            try:
                id_buscado = int(entrada)
            except ValueError:
                print("ID inválido. Debe ser un número entero.")
                continue
            cliente = servicio.buscar_cliente_por_id(id_buscado)
            if cliente is None:
                print("Cliente no encontrado.")
            else:
                print(cliente)

        elif opcion == "7":
            print("Saliendo. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()

