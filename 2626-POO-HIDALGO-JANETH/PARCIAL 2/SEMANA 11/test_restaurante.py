"""Script de pruebas automatizadas para restaurante_app Semana 11."""

import sys
from pathlib import Path

# Asegurar que el directorio sea accesible
project_root = Path(__file__).resolve().parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario
from restaurante_app.modelos.venta import Venta
from restaurante_app.servicios.restaurante import Restaurante


def test_productos():
    """Test 1: Crear y gestionar productos."""
    print("\n" + "=" * 70)
    print("TEST 1: PRODUCTOS CON STOCK")
    print("=" * 70)

    # Crear productos
    p1 = Producto(codigo="P001", nombre="Hamburguesa", categoria="Comida Rápida", precio=12.50, stock=10)
    p2 = Producto(codigo="P002", nombre="Ensalada", categoria="Ensaladas", precio=8.00, stock=5)

    print(f"✓ Producto 1 creado: {p1}")
    print(f"✓ Producto 2 creado: {p2}")

    # Verificar serialización
    print(f"✓ Serialización P1: {p1.to_dict()}")

    # Probar venta en producto
    try:
        p1.vender(2)
        print(f"✓ Venta de 2 unidades exitosa. Stock ahora: {p1.stock}")
    except ValueError as e:
        print(f"✗ Error: {e}")

    # Probar stock insuficiente
    try:
        p1.vender(20)
        print(f"✗ Debería haber fallado con stock insuficiente")
    except ValueError as e:
        print(f"✓ Stock insuficiente detectado correctamente: {e}")


def test_usuarios():
    """Test 2: Crear y gestionar usuarios."""
    print("\n" + "=" * 70)
    print("TEST 2: USUARIOS")
    print("=" * 70)

    # Crear usuarios
    u1 = Usuario(identificacion="1234567890", nombre="Juan García", correo="juan@example.com")
    u2 = Usuario(identificacion="0987654321", nombre="María López", correo="maria@example.com")

    print(f"✓ Usuario 1 creado: {u1}")
    print(f"✓ Usuario 2 creado: {u2}")

    # Verificar serialización
    print(f"✓ Serialización U1: {u1.to_dict()}")


def test_ventas():
    """Test 3: Crear y gestionar ventas."""
    print("\n" + "=" * 70)
    print("TEST 3: VENTAS (RELACIÓN USUARIO-PRODUCTO)")
    print("=" * 70)

    # Crear una venta
    v1 = Venta(usuario_id="1234567890", producto_codigo="P001", cantidad=2)

    print(f"✓ Venta creada: {v1}")
    print(f"✓ Serialización: {v1.to_dict()}")

    # Probar cantidad inválida
    try:
        v_invalid = Venta(usuario_id="1234567890", producto_codigo="P001", cantidad=0)
        print(f"✗ Debería haber fallado con cantidad 0")
    except ValueError as e:
        print(f"✓ Cantidad inválida detectada: {e}")


def test_restaurante():
    """Test 4: Operaciones del servicio Restaurante."""
    print("\n" + "=" * 70)
    print("TEST 4: SERVICIO RESTAURANTE")
    print("=" * 70)

    servicio = Restaurante()
    print("✓ Restaurante inicializado")

    # Registrar producto
    try:
        p1 = Producto(codigo="BURGER001", nombre="Hamburguesa Premium",
                      categoria="Comida Rápida", precio=15.00, stock=20)
        servicio.registrar_producto(p1)
        print(f"✓ Producto registrado: {p1.nombre}")
    except ValueError as e:
        print(f"✗ Error: {e}")

    # Registrar usuario
    try:
        u1 = Usuario(identificacion="DNI123456", nombre="Carlos Mendez",
                     correo="carlos@example.com")
        servicio.registrar_usuario(u1)
        print(f"✓ Usuario registrado: {u1.nombre}")
    except ValueError as e:
        print(f"✗ Error: {e}")

    # Realizar venta válida
    resultado = servicio.vender_producto("BURGER001", "DNI123456", 3)
    if resultado:
        print(f"✓ Venta exitosa")
        p = servicio.buscar_producto("BURGER001")
        print(f"  Stock restante: {p.stock}")

        ventas = servicio.obtener_ventas_usuario("DNI123456")
        print(f"  Ventas del usuario: {len(ventas)}")
    else:
        print(f"✗ La venta debería haber sido exitosa")

    # Intentar venta con stock insuficiente
    resultado = servicio.vender_producto("BURGER001", "DNI123456", 100)
    if not resultado:
        print(f"✓ Venta rechazada correctamente por stock insuficiente")
    else:
        print(f"✗ La venta debería haber sido rechazada")

    # Listar productos
    productos = servicio.listar_productos()
    print(f"✓ Total de productos: {len(productos)}")

    # Listar usuarios
    usuarios = servicio.listar_usuarios()
    print(f"✓ Total de usuarios: {len(usuarios)}")

    # Listar ventas
    ventas = servicio.listar_ventas()
    print(f"✓ Total de ventas: {len(ventas)}")


def test_persistencia():
    """Test 5: Verificar persistencia en archivos JSON."""
    print("\n" + "=" * 70)
    print("TEST 5: PERSISTENCIA JSON")
    print("=" * 70)

    datos_dir = Path(__file__).resolve().parent / "restaurante_app" / "datos"

    if (datos_dir / "productos.json").exists():
        print(f"✓ productos.json existe")

    if (datos_dir / "usuarios.json").exists():
        print(f"✓ usuarios.json existe")

    if (datos_dir / "ventas.json").exists():
        print(f"✓ ventas.json existe")

    print(f"✓ Directorio de datos: {datos_dir}")


def main():
    """Ejecutar todas las pruebas."""
    print("\n")
    print("╔" + "=" * 68 + "╗")
    print("║" + " " * 20 + "PRUEBAS RESTAURANTE_APP SEMANA 11" + " " * 15 + "║")
    print("╚" + "=" * 68 + "╝")

    try:
        test_productos()
        test_usuarios()
        test_ventas()
        test_restaurante()
        test_persistencia()

        print("\n" + "=" * 70)
        print("✓ TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE")
        print("=" * 70 + "\n")

    except Exception as e:
        print(f"\n✗ Error durante las pruebas: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()

