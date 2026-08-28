# Sistema de Restaurante (Aplicación SOLID)

**Autor:** (Janeth Hidalgo)
**Asignatura:** Programación Orientada a Objetos - Semana 8

## Descripción del Sistema
Este es un sistema básico de consola para la gestión de productos, bebidas y clientes en un restaurante. El objetivo de este proyecto es demostrar la correcta aplicación de los principios SOLID en Python.

## Estructura del Proyecto
El proyecto sigue una arquitectura modular:

* `modelos/`: Contiene las clases de dominio.
  * `producto.py`: Clase base `Producto`.
  * `bebida.py`: Clase `Bebida` que hereda de `Producto`.
  * `cliente.py`: Clase `Cliente`.
* `servicios/`: Contiene la lógica del negocio.
  * `restaurante.py`: Administra las listas de productos y clientes.
* `main.py`: Punto de entrada, contiene el menú interactivo.

## Principios SOLID Aplicados

1. **Responsabilidad Única (SRP):** Cada clase tiene un único propósito. `Producto`, `Bebida` y `Cliente` solo almacenan información y saben cómo mostrarla. `Restaurante` solo administra colecciones y validaciones. `main.py` solo se encarga de la entrada/salida y del flujo del usuario.
2. **Abierto/Cerrado (OCP):** El sistema puede ser extendido agregando nuevos tipos de productos (como `Bebida`) sin modificar el código de la clase `Restaurante` encargada de registrarlos y listarlos.
3. **Sustitución de Liskov (LSP):** Un objeto de la clase derivada `Bebida` puede sustituir a un objeto de la clase base `Producto` en cualquier parte del sistema (ej: al agregarlo a la lista de productos y al invocar `mostrar_informacion()`) sin alterar el funcionamiento esperado.

## Relación entre Producto y Bebida
Se ha utilizado herencia (`Bebida` hereda de `Producto`) ya que una bebida *es un* producto dentro del restaurante. Comparten atributos como código, nombre, categoría y precio, pero la bebida añade atributos específicos como tamaño y tipo de envase.

## Instrucciones de Ejecución
Para ejecutar el sistema, abre una terminal en la raíz del proyecto y ejecuta:

```bash
python main.py
```
