"""Script para cargar datos de ejemplo en restaurante_app."""

import sys
from pathlib import Path

# Asegurar que el directorio sea accesible
project_root = Path(__file__).resolve().parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario
from restaurante_app.servicios.restaurante import Restaurante


def cargar_datos_ejemplo():
    """Cargar datos de ejemplo en el sistema."""
    print("\n" + "=" * 70)
    print("CARGANDO DATOS DE EJEMPLO")
    print("=" * 70)

    servicio = Restaurante()

    # Crear productos de ejemplo
    productos_ejemplo = [
        ("P001", "Hamburguesa", "Comida Rápida", 12.50, 15),
        ("P002", "Pizza Margherita", "Pizzas", 18.00, 10),
        ("P003", "Ensalada César", "Ensaladas", 9.50, 20),
        ("P004", "Refesco Pequeño", "Bebidas", 2.50, 50),
        ("P005", "Helado de Vainilla", "Postres", 5.00, 30),
    ]

    print("\nRegistrando productos...")
    for codigo, nombre, categoria, precio, stock in productos_ejemplo:
        try:
            if servicio.buscar_producto(codigo) is None:
                p = Producto(codigo=codigo, nombre=nombre, categoria=categoria,
                            precio=precio, stock=stock)
                servicio.registrar_producto(p)
                print(f"  ✓ {nombre} (${precio:.2f}, Stock: {stock})")
            else:
                print(f"  - {nombre} ya existe")
        except Exception as e:
            print(f"  ✗ Error al registrar {nombre}: {e}")

    # Crear usuarios de ejemplo
    usuarios_ejemplo = [
        ("1001", "Juan García", "juan.garcia@email.com"),
        ("1002", "María López", "maria.lopez@email.com"),
        ("1003", "Carlos Mendez", "carlos.mendez@email.com"),
        ("1004", "Ana Rodríguez", "ana.rodriguez@email.com"),
    ]

    print("\nRegistrando usuarios...")
    for identificacion, nombre, correo in usuarios_ejemplo:
        try:
            if servicio.buscar_usuario(identificacion) is None:
                u = Usuario(identificacion=identificacion, nombre=nombre, correo=correo)
                servicio.registrar_usuario(u)
                print(f"  ✓ {nombre} ({identificacion})")
            else:
                print(f"  - {nombre} ya existe")
        except Exception as e:
            print(f"  ✗ Error al registrar {nombre}: {e}")

    # Realizar algunas ventas de ejemplo
    ventas_ejemplo = [
        ("P001", "1001", 2),  # Juan compra 2 hamburguesas
        ("P002", "1001", 1),  # Juan compra 1 pizza
        ("P003", "1002", 3),  # María compra 3 ensaladas
        ("P004", "1002", 5),  # María compra 5 refrescos
        ("P005", "1003", 2),  # Carlos compra 2 helados
    ]

    print("\nRegistrando ventas de ejemplo...")
    for codigo_producto, identificacion_usuario, cantidad in ventas_ejemplo:
        try:
            resultado = servicio.vender_producto(codigo_producto, identificacion_usuario, cantidad)
            if resultado:
                producto = servicio.buscar_producto(codigo_producto)
                usuario = servicio.buscar_usuario(identificacion_usuario)
                print(f"  ✓ {usuario.nombre} compró {cantidad}x {producto.nombre}")
            else:
                print(f"  ✗ No se pudo completar la venta")
        except Exception as e:
            print(f"  ✗ Error: {e}")

    print("\n" + "=" * 70)
    print("DATOS DE EJEMPLO CARGADOS EXITOSAMENTE")
    print("=" * 70)

    # Mostrar resumen
    print("\nRESUMEN:")
    print(f"  • Productos registrados: {len(servicio.listar_productos())}")
    print(f"  • Usuarios registrados: {len(servicio.listar_usuarios())}")
    print(f"  • Ventas realizadas: {len(servicio.listar_ventas())}")

    print("\nPuedes ejecutar 'python restaurante_app/main.py' para interactuar con los datos.")


if __name__ == "__main__":
    cargar_datos_ejemplo()

