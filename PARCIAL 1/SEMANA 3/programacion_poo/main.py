"""
Programa Principal - Programación Orientada a Objetos
Este programa demuestra el uso de clases, objetos, atributos y métodos.
"""

from mascota import Mascota


def main():
    """
    Función principal que crea instancias de la clase Mascota
    y ejecuta sus métodos.
    """
    
    print("=" * 50)
    print("PROGRAMA DE PROGRAMACIÓN ORIENTADA A OBJETOS")
    print("=" * 50)
    print()
    
    # Crear el primer objeto de la clase Mascota (Perro)
    mascota1 = Mascota("Max", "Perro", 5)
    print("--- Mascota 1 ---")
    mascota1.mostrar_informacion()
    mascota1.hacer_sonido()
    
    # Crear el segundo objeto de la clase Mascota (Gato)
    mascota2 = Mascota("Whiskers", "Gato", 3)
    print("--- Mascota 2 ---")
    mascota2.mostrar_informacion()
    mascota2.hacer_sonido()
    
    # Crear un tercer objeto adicional (Pájaro)
    mascota3 = Mascota("Tweety", "Pájaro", 2)
    print("--- Mascota 3 ---")
    mascota3.mostrar_informacion()
    mascota3.hacer_sonido()
    
    print("=" * 50)
    print("Fin del programa")
    print("=" * 50)


if __name__ == "__main__":
    main()

