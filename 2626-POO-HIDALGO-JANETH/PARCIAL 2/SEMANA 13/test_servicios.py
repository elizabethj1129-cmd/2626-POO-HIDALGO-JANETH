"""Script de prueba para verificar que los servicios funcionan correctamente.

Este script ejecuta las operaciones básicas sin necesidad de la interfaz gráfica.
"""

import sys
from pathlib import Path

# Asegurar que restaurante_app esté en el path
sys.path.insert(0, str(Path.cwd()))

from restaurante_app.servicios.restaurante_servicio import RestauranteServicio


def main():
    """Ejecutar pruebas básicas."""
    print("=" * 70)
    print("PRUEBAS DEL SERVICIO DE RESTAURANTE")
    print("=" * 70)

    # Inicializar servicio
    servicio = RestauranteServicio()

    # Prueba 1: Listar productos
    print("\n1. PRODUCTOS CARGADOS:")
    print("-" * 70)
    productos = servicio.listar_productos()
    if productos:
        for p in productos:
            print(f"  {p}")
    else:
        print("  No hay productos cargados")

    # Prueba 2: Listar usuarios
    print("\n2. USUARIOS CARGADOS:")
    print("-" * 70)
    usuarios = servicio.listar_usuarios()
    if usuarios:
        for u in usuarios:
            print(f"  {u}")
    else:
        print("  No hay usuarios cargados")

    # Prueba 3: Validar acceso
    print("\n3. PRUEBAS DE ACCESO:")
    print("-" * 70)
    test_cases = [
        ("12345", "1234", True),
        ("12345", "wrongpass", False),
        ("nonexistent", "1234", False),
        ("67890", "5678", True),
    ]

    for identificacion, contraseña, expected in test_cases:
        result = servicio.validar_acceso(identificacion, contraseña)
        status = "✓" if result == expected else "✗"
        print(f"  {status} Acceso({identificacion}, {contraseña}): {result}")

    # Prueba 4: Buscar producto
    print("\n4. BÚSQUEDA DE PRODUCTOS:")
    print("-" * 70)
    producto = servicio.buscar_producto("P001")
    if producto:
        print(f"  ✓ Producto P001 encontrado: {producto.nombre}")
    else:
        print("  ✗ Producto P001 no encontrado")

    # Prueba 5: Buscar usuario
    print("\n5. BÚSQUEDA DE USUARIOS:")
    print("-" * 70)
    usuario = servicio.buscar_usuario("12345")
    if usuario:
        print(f"  ✓ Usuario 12345 encontrado: {usuario.nombre}")
    else:
        print("  ✗ Usuario 12345 no encontrado")

    print("\n" + "=" * 70)
    print("PRUEBAS COMPLETADAS")
    print("=" * 70)


if __name__ == "__main__":
    main()

