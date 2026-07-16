import sys
from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def mostrar_menu():
    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("----------------------------------------")
    print("4. Listar productos")
    print("5. Listar clientes")
    print("----------------------------------------")
    print("6. Salir")
    print("========================================")

def opcion_registrar_producto(servicio: Restaurante):
    print("\n-- Registrar Producto --")
    codigo = input("Ingrese código: ")
    nombre = input("Ingrese nombre: ")
    categoria = input("Ingrese categoría: ")
    try:
        precio = float(input("Ingrese precio: "))
        producto = Producto(codigo, nombre, categoria, precio)
        servicio.registrar_producto(producto)
    except ValueError:
        print("Error: El precio debe ser un número válido.")

def opcion_registrar_bebida(servicio: Restaurante):
    print("\n-- Registrar Bebida --")
    codigo = input("Ingrese código: ")
    nombre = input("Ingrese nombre: ")
    categoria = input("Ingrese categoría: ")
    try:
        precio = float(input("Ingrese precio: "))
        tamano = input("Ingrese tamaño (ej. 500ml): ")
        tipo_envase = input("Ingrese tipo de envase (ej. Botella de vidrio): ")
        bebida = Bebida(codigo, nombre, categoria, precio, tamano, tipo_envase)
        servicio.registrar_producto(bebida)
    except ValueError:
        print("Error: El precio debe ser un número válido.")

def opcion_registrar_cliente(servicio: Restaurante):
    print("\n-- Registrar Cliente --")
    identificacion = input("Ingrese identificación: ")
    nombre = input("Ingrese nombre: ")
    correo = input("Ingrese correo: ")
    cliente = Cliente(identificacion, nombre, correo)
    servicio.registrar_cliente(cliente)

def cargar_datos_ejemplo(servicio: Restaurante):
    servicio.registrar_producto(Producto("P001", "Hamburguesa Clásica", "Plato Fuerte", 5.50))
    servicio.registrar_producto(Bebida("B001", "Coca Cola", "Bebida Fría", 1.50, "500ml", "Botella Plástica"))
    servicio.registrar_producto(Bebida("B002", "Café Americano", "Bebida Caliente", 2.00, "250ml", "Taza de cerámica"))
    
    servicio.registrar_cliente(Cliente("1700000000", "Juan Pérez", "juan.perez@email.com"))
    servicio.registrar_cliente(Cliente("1700000001", "María López", "maria.lopez@email.com"))

def main():
    servicio = Restaurante()
    print("Iniciando sistema...")
    print("Cargando datos de ejemplo (Didáctica de principios SOLID)...")
    cargar_datos_ejemplo(servicio)
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            opcion_registrar_producto(servicio)
        elif opcion == "2":
            opcion_registrar_bebida(servicio)
        elif opcion == "3":
            opcion_registrar_cliente(servicio)
        elif opcion == "4":
            servicio.listar_productos()
        elif opcion == "5":
            servicio.listar_clientes()
        elif opcion == "6":
            print("Saliendo del sistema...")
            sys.exit(0)
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == '__main__':
    main()
