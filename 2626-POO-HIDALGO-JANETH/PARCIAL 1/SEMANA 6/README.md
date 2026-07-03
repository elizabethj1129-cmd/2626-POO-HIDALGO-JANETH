# Restaurante App - Programación Orientada a Objetos (Semana 6)

**Estudiante:** Janeth Hidalgo  
**Asignatura:** Programación Orientada a Objetos

## Descripción del Proyecto
Este sistema simula la administración de los productos de un restaurante, aplicando los principios fundamentales de la Programación Orientada a Objetos en Python. En lugar de utilizar el ejemplo de la biblioteca desarrollado por el docente, este proyecto adapta la estructura para manejar el menú de un restaurante.

## Estructura del Proyecto
El proyecto sigue una arquitectura modular y organizada:
- `restaurante_app/modelos/`: Contiene las clases que representan las entidades (Producto, Platillo, Bebida).
- `restaurante_app/servicios/`: Contiene la clase `Restaurante` encargada de administrar la lista de productos.
- `restaurante_app/main.py`: Es el punto de arranque que inicializa los objetos y ejecuta el programa.

## Principios de POO Aplicados

1. **Herencia:** Se creó una clase padre `Producto` que contiene los atributos y métodos generales. Las clases hijas `Platillo` y `Bebida` heredan de ella, reutilizando el constructor mediante `super().__init__()` y agregando atributos propios como `calorias` y `volumen_ml`.
2. **Encapsulación:** El atributo precio en la clase `Producto` ha sido encapsulado (`__precio`) para protegerlo de modificaciones directas desde fuera de la clase. Se implementaron los métodos `obtener_precio()` y `cambiar_precio()` para controlarlo de manera segura e impedir que tome valores negativos o cero.
3. **Polimorfismo:** En la clase `Restaurante`, el método `mostrar_menu()` recorre una lista heterogénea de productos. Al invocar el método `mostrar_informacion()`, Python determina en tiempo de ejecución si debe ejecutar la versión sobrescrita de `Platillo` o de `Bebida`, permitiendo comportamientos específicos para cada objeto utilizando la misma llamada.

## Reflexión
Aplicar los principios de POO en proyectos modulares de Python permite estructurar el código de forma mantenible y escalable. La herencia facilita la reutilización del código, la encapsulación protege la integridad de los datos evitando estados inconsistentes, y el polimorfismo otorga flexibilidad, ya que permite tratar diferentes tipos de objetos a través de una interfaz común.
