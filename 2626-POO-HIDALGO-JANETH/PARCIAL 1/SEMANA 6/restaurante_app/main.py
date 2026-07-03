from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante

def main():
    print("Iniciando el Sistema del Restaurante...\n")

    # 1. Crear la instancia del servicio Restaurante
    mi_restaurante = Restaurante("El Buen Sabor")

    # 2. Crear objetos de tipo Platillo
    platillo1 = Platillo(nombre="Enchiladas Suizas", precio=12.50, calorias=850)
    platillo2 = Platillo(nombre="Ensalada César", precio=8.00, calorias=350, disponibilidad=False)

    # 3. Crear objetos de tipo Bebida
    bebida1 = Bebida(nombre="Limonada Natural", precio=3.50, volumen_ml=400)
    bebida2 = Bebida(nombre="Café Americano", precio=2.00, volumen_ml=250)

    # 4. Demostrar la Encapsulación:
    # Se utiliza el método cambiar_precio() para modificar el atributo protegido de forma segura.
    print("--- Demostrando Encapsulación ---")
    print(f"Precio original de {bebida1.nombre}: ${bebida1.obtener_precio():.2f}")
    bebida1.cambiar_precio(4.00)
    print(f"Nuevo precio de {bebida1.nombre}: ${bebida1.obtener_precio():.2f}")
    
    # Intentar asignar un precio inválido (negativo)
    print("\nIntentando asignar un precio inválido a Café Americano...")
    bebida2.cambiar_precio(-1.50)

    # 5. Agregar los objetos al servicio Restaurante
    mi_restaurante.agregar_producto(platillo1)
    mi_restaurante.agregar_producto(platillo2)
    mi_restaurante.agregar_producto(bebida1)
    mi_restaurante.agregar_producto(bebida2)

    # 6. Mostrar el menú (Demuestra el Polimorfismo)
    # Al llamar a mostrar_menu(), el servicio recorre todos los productos.
    # Cada producto (Platillo o Bebida) responde de forma diferente al método mostrar_informacion().
    mi_restaurante.mostrar_menu()

if __name__ == "__main__":
    main()
