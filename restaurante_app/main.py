"""
Punto de entrada del sistema de gestión de restaurante.

Este archivo demuestra el funcionamiento del sistema creando objetos
de las clases Producto, Cliente y Restaurante, mostrando cómo se
comunican entre sí mediante importaciones.
"""

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def main():
    """Función principal que ejecuta la demostración del sistema."""

    print("=" * 60)
    print("SISTEMA DE GESTIÓN DE RESTAURANTE")
    print("=" * 60)
    print()

    # ============================================================
    # PASO 1: Crear el restaurante
    # ============================================================
    restaurante = Restaurante("El Sabor Gourmet", "Centro Comercial Downtown")
    print(f"Restaurante creado: {restaurante.nombre} en {restaurante.ubicacion}")
    print()

    # ============================================================
    # PASO 2: Crear y agregar productos al catálogo
    # ============================================================
    print("--- AGREGANDO PRODUCTOS ---")

    producto1 = Producto(
        nombre="Hamburguesa Clásica",
        descripcion="Carne molida con lechuga, tomate y queso",
        precio=12.99,
        categoria="Plato"
    )
    restaurante.agregar_producto(producto1)

    producto2 = Producto(
        nombre="Salmón a la Mantequilla",
        descripcion="Filete de salmón fresco preparado en mantequilla",
        precio=18.50,
        categoria="Plato"
    )
    restaurante.agregar_producto(producto2)

    producto3 = Producto(
        nombre="Ensalada César",
        descripcion="Lechuga romana con croutons y aderezo Caesar",
        precio=8.99,
        categoria="Entrada"
    )
    restaurante.agregar_producto(producto3)

    producto4 = Producto(
        nombre="Jugo Natural de Naranja",
        descripcion="Jugo recién exprimido",
        precio=4.50,
        categoria="Bebida"
    )
    restaurante.agregar_producto(producto4)

    producto5 = Producto(
        nombre="Gaseosa Cola",
        descripcion="Bebida gaseosa de cola fría",
        precio=3.00,
        categoria="Bebida"
    )
    restaurante.agregar_producto(producto5)

    producto6 = Producto(
        nombre="Postre de Chocolate",
        descripcion="Brownie de chocolate con helado de vainilla",
        precio=6.99,
        categoria="Postre"
    )
    restaurante.agregar_producto(producto6)

    print()

    # ============================================================
    # PASO 3: Registrar clientes en el sistema
    # ============================================================
    print("--- REGISTRANDO CLIENTES ---")

    cliente1 = Cliente("Juan Pérez", "juan@email.com", "555-0101")
    restaurante.agregar_cliente(cliente1)

    cliente2 = Cliente("María García", "maria@email.com", "555-0102")
    restaurante.agregar_cliente(cliente2)

    cliente3 = Cliente("Carlos López", "carlos@email.com", "555-0103")
    restaurante.agregar_cliente(cliente3)

    print()

    # ============================================================
    # PASO 4: Mostrar catálogo de productos disponibles
    # ============================================================
    print("--- CATÁLOGO DE PRODUCTOS DISPONIBLES ---")
    productos_disponibles = restaurante.listar_productos(solo_disponibles=True)
    for idx, producto in enumerate(productos_disponibles, 1):
        print(f"\n{idx}. {producto}")

    print()

    # ============================================================
    # PASO 5: Procesar pedidos
    # ============================================================
    print("--- PROCESANDO PEDIDOS ---")

    restaurante.procesarPedido(cliente1.numero_cliente, "Hamburguesa Clásica")
    restaurante.procesarPedido(cliente1.numero_cliente, "Jugo Natural de Naranja")

    restaurante.procesarPedido(cliente2.numero_cliente, "Salmón a la Mantequilla")
    restaurante.procesarPedido(cliente2.numero_cliente, "Gaseosa Cola")
    restaurante.procesarPedido(cliente2.numero_cliente, "Postre de Chocolate")

    restaurante.procesarPedido(cliente3.numero_cliente, "Ensalada César")
    restaurante.procesarPedido(cliente3.numero_cliente, "Gaseosa Cola")

    # Intentar un pedido que fallará (producto inexistente)
    restaurante.procesarPedido(cliente1.numero_cliente, "Pizza")

    print()

    # ============================================================
    # PASO 6: Cambiar disponibilidad de un producto
    # ============================================================
    # Cambiar disponibilidad
    salmón = restaurante.buscar_producto_por_nombre("Salmón a la Mantequilla")
    if salmón:
        salmón.cambiar_disponibilidad(False)
        print(f"[OK] '{salmón.nombre}' marcado como no disponible.")

    print()

    # ============================================================
    # PASO 7: Listar todos los clientes y sus datos
    # ============================================================
    print("--- REGISTRO DE CLIENTES ---")
    clientes = restaurante.listar_clientes()
    for cliente in clientes:
        print(f"\n{cliente}")

    print()

    # ============================================================
    # PASO 8: Mostrar información del restaurante y estadísticas
    # ============================================================
    print("--- INFORMACIÓN Y ESTADÍSTICAS DEL RESTAURANTE ---")
    print(f"\n{restaurante}")

    print()
    print("=" * 60)
    print("FIN DE LA DEMOSTRACIÓN DEL SISTEMA")
    print("=" * 60)


if __name__ == "__main__":
    main()


