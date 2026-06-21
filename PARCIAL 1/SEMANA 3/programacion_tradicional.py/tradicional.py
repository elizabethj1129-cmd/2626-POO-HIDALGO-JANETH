# Programación Tradicional - Sistema de Registro de Mascotas
# Sin uso de clases ni objetos

# Lista global para almacenar las mascotas
mascotas = []


def registrar_mascota():
    """
    Función para registrar una nueva mascota.
    Solicita datos por teclado y los almacena.
    """
    print("\n" + "=" * 50)
    print("REGISTRO DE NUEVA MASCOTA")
    print("=" * 50)

    # Solicitar datos por teclado
    nombre = input("Ingrese el nombre de la mascota: ").strip()
    tipo = input("Ingrese el tipo de mascota (perro, gato, pajaro, etc.): ").strip()
    raza = input("Ingrese la raza: ").strip()
    edad = input("Ingrese la edad (en años): ").strip()
    peso = input("Ingrese el peso (en kg): ").strip()
    color = input("Ingrese el color: ").strip()
    dueno = input("Ingrese el nombre del dueño: ").strip()

    # Crear un diccionario con la información de la mascota
    mascota = {
        "nombre": nombre,
        "tipo": tipo,
        "raza": raza,
        "edad": edad,
        "peso": peso,
        "color": color,
        "dueno": dueno
    }

    # Agregar la mascota a la lista
    mascotas.append(mascota)
    print("\n✓ ¡Mascota registrada exitosamente!")


def mostrar_mascotas():
    """
    Función para mostrar toda la información de las mascotas registradas
    de forma organizada.
    """
    if len(mascotas) == 0:
        print("\n⚠ No hay mascotas registradas aún.")
        return

    print("\n" + "=" * 70)
    print("INFORMACIÓN DE MASCOTAS REGISTRADAS")
    print("=" * 70)

    for indice, mascota in enumerate(mascotas, 1):
        print(f"\n🐾 MASCOTA #{indice}")
        print("-" * 70)
        print(f"  Nombre:        {mascota['nombre']}")
        print(f"  Tipo:          {mascota['tipo']}")
        print(f"  Raza:          {mascota['raza']}")
        print(f"  Edad:          {mascota['edad']} años")
        print(f"  Peso:          {mascota['peso']} kg")
        print(f"  Color:         {mascota['color']}")
        print(f"  Dueño:         {mascota['dueno']}")
        print("-" * 70)


def buscar_mascota():
    """
    Función para buscar una mascota por nombre.
    """
    if len(mascotas) == 0:
        print("\n⚠ No hay mascotas registradas aún.")
        return

    nombre_buscar = input("\nIngrese el nombre de la mascota a buscar: ").strip()

    encontrada = False
    for mascota in mascotas:
        if mascota['nombre'].lower() == nombre_buscar.lower():
            print("\n✓ ¡Mascota encontrada!")
            print("\n" + "=" * 50)
            print(f"  Nombre:        {mascota['nombre']}")
            print(f"  Tipo:          {mascota['tipo']}")
            print(f"  Raza:          {mascota['raza']}")
            print(f"  Edad:          {mascota['edad']} años")
            print(f"  Peso:          {mascota['peso']} kg")
            print(f"  Color:         {mascota['color']}")
            print(f"  Dueño:         {mascota['dueno']}")
            print("=" * 50)
            encontrada = True
            break

    if not encontrada:
        print(f"\n✗ No se encontró ninguna mascota con el nombre '{nombre_buscar}'")


def eliminar_mascota():
    """
    Función para eliminar una mascota del registro.
    """
    if len(mascotas) == 0:
        print("\n⚠ No hay mascotas registradas aún.")
        return

    nombre_eliminar = input("\nIngrese el nombre de la mascota a eliminar: ").strip()

    for indice, mascota in enumerate(mascotas):
        if mascota['nombre'].lower() == nombre_eliminar.lower():
            mascotas.pop(indice)
            print(f"\n✓ ¡La mascota '{nombre_eliminar}' ha sido eliminada!")
            return

    print(f"\n✗ No se encontró ninguna mascota con el nombre '{nombre_eliminar}'")


def contar_mascotas():
    """
    Función para mostrar el número total de mascotas registradas.
    """
    total = len(mascotas)
    print(f"\nTotal de mascotas registradas: {total}")


def menu_principal():
    """
    Función que muestra el menú principal y gestiona las opciones.
    """
    while True:
        print("\n" + "=" * 50)
        print("SISTEMA DE REGISTRO DE MASCOTAS")
        print("=" * 50)
        print("1. Registrar una nueva mascota")
        print("2. Mostrar todas las mascotas")
        print("3. Buscar una mascota")
        print("4. Eliminar una mascota")
        print("5. Contar mascotas")
        print("6. Salir")
        print("=" * 50)

        opcion = input("Seleccione una opción (1-6): ").strip()

        if opcion == "1":
            registrar_mascota()
        elif opcion == "2":
            mostrar_mascotas()
        elif opcion == "3":
            buscar_mascota()
        elif opcion == "4":
            eliminar_mascota()
        elif opcion == "5":
            contar_mascotas()
        elif opcion == "6":
            print("\n¡Gracias por usar el sistema! Hasta luego.\n")
            break
        else:
            print("\n✗ Opción no válida. Por favor, seleccione una opción entre 1 y 6.")


# Programa principal
if __name__ == "__main__":
    print("\n" + "🐾" * 20)
    print("BIENVENIDO AL SISTEMA DE REGISTRO DE MASCOTAS")
    print("🐾" * 20)
    menu_principal()
