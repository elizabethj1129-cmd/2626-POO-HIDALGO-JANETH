# Punto de entrada principal del sistema de gestión de restaurante
# Demuestra la creación de objetos, su gestión y la visualización de información

# Importaciones de las clases necesarias
from modelos import Producto, Cliente
from servicios import Restaurante


def main():
    """
    Función principal que ejecuta el sistema de gestión de restaurante.
    Crea objetos de ejemplo, los agrega al servicio y muestra los resultados.
    """

    # ==================== CREAR INSTANCIA DEL RESTAURANTE ====================
    restaurante_principal = Restaurante(
        nombre="La Casa del Buen Sabor",
        direccion="Calle Principal 123, Centro"
    )

    print("\n" + "="*60)
    print("SISTEMA DE GESTIÓN DE RESTAURANTE")
    print("="*60)


    # ==================== CREAR PRODUCTOS ====================
    print("\n[1] Agregando productos al inventario...\n")

    # Crear instancias de productos con diferentes características
    producto_entrata_fritos = Producto(
        nombre="Tabla de Fritos Variados",
        precio=12.50,
        cantidad=30,
        descripcion="Tabla mixta con papas, aros de cebolla y camarones fritos",
        disponible=True
    )

    producto_hamburguesa = Producto(
        nombre="Hamburguesa Deluxe",
        precio=9.99,
        cantidad=45,
        descripcion="Carne de res 200g con queso, lechuga, tomate y salsa especial",
        disponible=True
    )

    producto_bebida_gaseosa = Producto(
        nombre="Bebida Gaseosa (500ml)",
        precio=2.50,
        cantidad=100,
        descripcion="Refrescante bebida gaseosa en botella de 500ml",
        disponible=True
    )

    producto_postre_helado = Producto(
        nombre="Helado de Chocolate",
        precio=4.75,
        cantidad=60,
        descripcion="Delicioso helado de chocolate belga",
        disponible=True
    )

    # Agregar productos al restaurante
    restaurante_principal.agregar_producto(producto_entrata_fritos)
    restaurante_principal.agregar_producto(producto_hamburguesa)
    restaurante_principal.agregar_producto(producto_bebida_gaseosa)
    restaurante_principal.agregar_producto(producto_postre_helado)


    # ==================== CREAR CLIENTES ====================
    print("\n[2] Registrando clientes en el sistema...\n")

    # Crear instancias de clientes con información descriptiva
    cliente_juan = Cliente(
        nombre="Juan Pérez García",
        email="juan.perez@email.com",
        telefono="+34 612 345 678",
        cliente_frecuente=False
    )

    cliente_maria = Cliente(
        nombre="María López Rodr��guez",
        email="maria.lopez@email.com",
        telefono="+34 623 456 789",
        cliente_frecuente=True
    )

    cliente_carlos = Cliente(
        nombre="Carlos Martínez Fernández",
        email="carlos.martinez@email.com",
        telefono="+34 634 567 890",
        cliente_frecuente=False
    )

    # Agregar clientes al restaurante
    restaurante_principal.agregar_cliente(cliente_juan)
    restaurante_principal.agregar_cliente(cliente_maria)
    restaurante_principal.agregar_cliente(cliente_carlos)


    # ==================== MOSTRAR INVENTARIO DE PRODUCTOS ====================
    restaurante_principal.listar_productos()


    # ==================== MOSTRAR CLIENTES REGISTRADOS ====================
    restaurante_principal.listar_clientes()


    # ==================== PROCESAR VENTAS ====================
    print("\n[3] Procesando algunas transacciones de venta...\n")

    # Simular ventas de productos a clientes
    restaurante_principal.procesar_venta(cliente_juan, producto_hamburguesa, 2)
    restaurante_principal.procesar_venta(cliente_juan, producto_bebida_gaseosa, 2)
    restaurante_principal.procesar_venta(cliente_maria, producto_entrata_fritos, 1)
    restaurante_principal.procesar_venta(cliente_maria, producto_postre_helado, 3)
    restaurante_principal.procesar_venta(cliente_carlos, producto_hamburguesa, 1)


    # ==================== MOSTRAR INFORMACIÓN ACTUALIZADA ====================
    print("\n[4] Información actualizada después de las ventas:\n")

    # Listar productos con cantidades actualizadas
    restaurante_principal.listar_productos()

    # Listar clientes con pedidos registrados
    restaurante_principal.listar_clientes()

    # Mostrar resumen final
    restaurante_principal.obtener_resumen()

    print("\n✓ Programa finalizado correctamente.\n")


# Punto de entrada del programa
if __name__ == "__main__":
    main()

