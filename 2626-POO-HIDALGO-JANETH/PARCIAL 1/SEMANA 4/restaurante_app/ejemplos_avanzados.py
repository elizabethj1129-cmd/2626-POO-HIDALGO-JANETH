"""
Ejemplos avanzados de uso del sistema de restaurante.
Este archivo demuestra formas adicionales de utilizar el sistema.
"""

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def ejemplo_basico():
    """Ejemplo 1: Uso básico del sistema"""
    print("\n" + "="*60)
    print("EJEMPLO 1: USO BÁSICO")
    print("="*60)

    # Crear un restaurante
    rest = Restaurante("Mi Restaurante", "Calle Principal 123")

    # Crear productos
    pizza = Producto("Pizza Margherita", "Queso y tomate", 10.50, "Plato")
    rest.agregar_producto(pizza)

    # Crear cliente
    cli = Cliente("Ana", "ana@email.com", "555-1234")
    rest.agregar_cliente(cli)

    # Procesar pedido
    rest.procesarPedido(cli.numero_cliente, "Pizza Margherita")


def ejemplo_productos_por_categoria():
    """Ejemplo 2: Filtrar productos por categoría"""
    print("\n" + "="*60)
    print("EJEMPLO 2: FILTRAR PRODUCTOS POR CATEGORÍA")
    print("="*60)

    rest = Restaurante("Restaurante Gourmet", "Zona Centro")

    # Agregar productos
    productos = [
        Producto("Hamburguesa", "Con carne", 12.99, "Plato"),
        Producto("Ensalada", "Fresca", 8.50, "Entrada"),
        Producto("Agua", "Mineral", 2.00, "Bebida"),
        Producto("Jugo", "De naranja", 4.00, "Bebida"),
        Producto("Tiramisú", "Postre italiano", 7.50, "Postre"),
    ]

    for prod in productos:
        rest.agregar_producto(prod)

    # Buscar productos por categoría
    print("\n--- BEBIDAS ---")
    bebidas = [p for p in rest.listar_productos() if p.categoria == "Bebida"]
    for bebida in bebidas:
        print(f"  - {bebida.nombre}: ${bebida.precio}")
    
    print("\n--- PLATOS ---")
    platos = [p for p in rest.listar_productos() if p.categoria == "Plato"]
    for plato in platos:
        print(f"  - {plato.nombre}: ${plato.precio}")


def ejemplo_cambiar_disponibilidad():
    """Ejemplo 3: Cambiar disponibilidad de productos"""
    print("\n" + "="*60)
    print("EJEMPLO 3: GESTIONAR DISPONIBILIDAD")
    print("="*60)

    rest = Restaurante("Ristorante Italia", "Downtown")

    # Crear productos
    salmón = Producto("Salmón a la Mantequilla", "Premium", 25.00, "Plato")
    pato = Producto("Pato Pekinés", "Especialidad", 22.00, "Plato")

    rest.agregar_producto(salmón)
    rest.agregar_producto(pato)

    print("\n--- ESTADO INICIAL ---")
    print(f"Salmón: {salmón.obtener_estado()}")
    print(f"Pato: {pato.obtener_estado()}")

    # Cambiar disponibilidad
    salmón.cambiar_disponibilidad(False)
    pato.cambiar_disponibilidad(False)

    print("\n--- DESPUÉS DE AGOTAR STOCK ---")
    print(f"Salmón: {salmón.obtener_estado()}")
    print(f"Pato: {pato.obtener_estado()}")

    print("\n--- PRODUCTOS DISPONIBLES ---")
    disponibles = rest.listar_productos(solo_disponibles=True)
    print(f"Total: {len(disponibles)} productos")


def ejemplo_multiples_pedidos():
    """Ejemplo 4: Cliente realizando múltiples pedidos"""
    print("\n" + "="*60)
    print("EJEMPLO 4: MÚLTIPLES PEDIDOS POR CLIENTE")
    print("="*60)

    rest = Restaurante("Fast Food Express", "Avenida Central")

    # Crear productos
    hamburguesa = Producto("Hamburguesa", "Simple", 8.00, "Plato")
    papas = Producto("Papas Fritas", "Grandes", 4.50, "Acompañamiento")
    bebida = Producto("Bebida", "Soda", 2.50, "Bebida")

    rest.agregar_producto(hamburguesa)
    rest.agregar_producto(papas)
    rest.agregar_producto(bebida)

    # Crear cliente
    cliente = Cliente("Carlos", "carlos@email.com", "555-9999")
    rest.agregar_cliente(cliente)

    print(f"\nCliente: {cliente.nombre}")
    print(f"Número: #{cliente.numero_cliente}")

    # Realizar múltiples pedidos
    print("\n--- PEDIDOS REALIZADOS ---")
    rest.procesarPedido(cliente.numero_cliente, "Hamburguesa")
    rest.procesarPedido(cliente.numero_cliente, "Papas Fritas")
    rest.procesarPedido(cliente.numero_cliente, "Bebida")
    rest.procesarPedido(cliente.numero_cliente, "Hamburguesa")

    # Mostrar información del cliente
    print(f"\n{cliente}")


def ejemplo_estadisticas_completas():
    """Ejemplo 5: Ver estadísticas del restaurante"""
    print("\n" + "="*60)
    print("EJEMPLO 5: ESTADÍSTICAS Y REPORTES")
    print("="*60)

    rest = Restaurante("Restaurant Estadísticas", "Local")

    # Agregar productos
    for i in range(1, 6):
        prod = Producto(f"Plato {i}", f"Descripción {i}", 10 + i, "Plato")
        rest.agregar_producto(prod)

    # Agregar clientes y pedidos
    for i in range(1, 4):
        cli = Cliente(f"Cliente {i}", f"cliente{i}@email.com", f"555-000{i}")
        rest.agregar_cliente(cli)

        # Cada cliente hace varios pedidos
        for j in range(1, i + 2):
            rest.procesarPedido(cli.numero_cliente, f"Plato {j}")

    # Mostrar estadísticas
    print(f"\n{rest}")

    stats = rest.obtener_estadisticas()
    print(f"\n--- DETALLES ---")
    print(f"Productos totales: {stats['total_productos']}")
    print(f"Productos disponibles: {stats['productos_disponibles']}")
    print(f"Clientes registrados: {stats['total_clientes']}")
    print(f"Pedidos procesados: {stats['total_pedidos']}")

    # Calcular estadísticas adicionales
    if stats['total_pedidos'] > 0:
        promedio = stats['total_pedidos'] / stats['total_clientes']
        print(f"Promedio de pedidos por cliente: {promedio:.2f}")


def ejemplo_busquedas():
    """Ejemplo 6: Operaciones de búsqueda"""
    print("\n" + "="*60)
    print("EJEMPLO 6: BÚSQUEDAS EN EL SISTEMA")
    print("="*60)

    rest = Restaurante("Restaurant búsqueda", "Local")

    # Agregar productos
    productos_lista = [
        Producto("Tacos al Pastor", "Tres tacos", 9.99, "Plato"),
        Producto("Enchiladas", "Seis piezas", 11.99, "Plato"),
        Producto("Cerveza", "Local", 5.50, "Bebida"),
        Producto("Café", "Espresso", 3.00, "Bebida"),
    ]

    for p in productos_lista:
        rest.agregar_producto(p)

    # Agregar clientes
    clientes_lista = [
        Cliente("Roberto", "roberto@email.com", "555-0001"),
        Cliente("Gabriela", "gabriela@email.com", "555-0002"),
    ]

    for c in clientes_lista:
        rest.agregar_cliente(c)

    # Buscar producto
    print("\n--- BÚSQUEDA DE PRODUCTOS ---")
    prod = rest.buscar_producto_por_nombre("Tacos al Pastor")
    if prod:
        print(f"Encontrado: {prod.nombre} (${prod.precio})")

    prod_no_existe = rest.buscar_producto_por_nombre("Pizza")
    print(f"Buscando 'Pizza': {prod_no_existe}")

    # Buscar cliente
    print("\n--- BÚSQUEDA DE CLIENTES ---")
    cli = rest.buscar_cliente_por_numero(1000)
    if cli:
        print(f"Encontrado: {cli.nombre} (#{cli.numero_cliente})")

    cli_no_existe = rest.buscar_cliente_por_numero(9999)
    print(f"Buscando cliente #9999: {cli_no_existe}")


def ejemplo_listado_completo():
    """Ejemplo 7: Listar todos los datos organizados"""
    print("\n" + "="*60)
    print("EJEMPLO 7: LISTADO COMPLETO DEL SISTEMA")
    print("="*60)

    rest = Restaurante("Restaurant Completo", "Ubicación")

    # Agregar datos
    prods = [
        Producto("Filete", "Carne roja", 20.00, "Plato"),
        Producto("Pollo", "A la parrilla", 15.00, "Plato"),
    ]

    for p in prods:
        rest.agregar_producto(p)

    for i in range(3):
        c = Cliente(f"Persona {i+1}", f"p{i+1}@email.com", f"555-{i:04d}")
        rest.agregar_cliente(c)
        rest.procesarPedido(c.numero_cliente, "Filete")

    # Mostrar información
    print("\n--- INVENTARIO DE PRODUCTOS ---")
    for idx, p in enumerate(rest.listar_productos(), 1):
        print(f"\n{idx}. {p}")

    print("\n--- BASE DE DATOS DE CLIENTES ---")
    for c in rest.listar_clientes():
        print(f"\n{c}")

    print(f"\n--- INFORMACIÓN DEL RESTAURANTE ---")
    print(f"{rest}")


# ============================================================================
# EJECUTAR EJEMPLOS
# ============================================================================
if __name__ == "__main__":
    # Ejecutar todos los ejemplos
    ejemplo_basico()
    ejemplo_productos_por_categoria()
    ejemplo_cambiar_disponibilidad()
    ejemplo_multiples_pedidos()
    ejemplo_estadisticas_completas()
    ejemplo_busquedas()
    ejemplo_listado_completo()

    print("\n" + "="*60)
    print("FIN DE LOS EJEMPLOS AVANZADOS")
    print("="*60)


