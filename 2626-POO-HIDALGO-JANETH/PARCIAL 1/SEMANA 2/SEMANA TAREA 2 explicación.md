# Explicación detallada del código de programación orientada a objetos

Este archivo explica cada parte del programa de Python que está en `SEMANA TAREA 2.py`. El objetivo es ayudarte a entender la programación orientada a objetos (POO) con un ejemplo sencillo de una `CuentaBancaria`.

---

## 1. ¿Qué es un objeto y una clase?

- Un **objeto** es una entidad que representa algo del mundo real, como una cuenta de banco, un libro o un coche.
- Una **clase** es la plantilla o el molde que define cómo se construye ese objeto.
- En POO, trabajamos con clases para crear objetos.

En el código, la clase es `CuentaBancaria`.

---

## 2. Definición de la clase

```python
class CuentaBancaria:
    """Representa una cuenta bancaria simple."""
```

- `class CuentaBancaria:` define una nueva clase llamada `CuentaBancaria`.
- La línea siguiente entre comillas triples es un **docstring**, una explicación corta de lo que hace la clase.

---

## 3. El método `__init__`

```python
    def __init__(self, titular, numero, saldo_inicial=0.0):
        self.titular = titular
        self.numero = numero
        self.saldo = float(saldo_inicial)
```

- `__init__` es el **constructor** de la clase. Se ejecuta cuando se crea un nuevo objeto.
- `self` representa el propio objeto que se está construyendo.
- `titular`, `numero` y `saldo_inicial` son los datos que necesita la cuenta.
- Dentro del constructor se crean los **atributos** del objeto:
  - `self.titular` guarda el nombre del dueño.
  - `self.numero` guarda el número de cuenta.
  - `self.saldo` guarda el dinero disponible.
- `saldo_inicial=0.0` significa que, si no se recibe ese dato, el saldo empieza en 0.

---

## 4. Método `depositar`

```python
    def depositar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a depositar debe ser mayor que 0.")
        self.saldo += cantidad
        return self.saldo
```

- Este método permite agregar dinero a la cuenta.
- `cantidad` es lo que se quiere depositar.
- Se usa una validación: si la cantidad no es mayor que 0, se lanza un error con `raise ValueError(...)`.
- `self.saldo += cantidad` suma el dinero depositado al saldo actual.
- `return self.saldo` devuelve el saldo actualizado.

---

## 5. Método `retirar`

```python
    def retirar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser mayor que 0.")
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente para realizar el retiro.")
        self.saldo -= cantidad
        return self.saldo
```

- Este método permite sacar dinero de la cuenta.
- Primero valida que la cantidad sea mayor que 0.
- Después valida que haya suficiente saldo para retirar.
- Si las condiciones son correctas, se resta el valor de `self.saldo`.
- `return self.saldo` devuelve el saldo después del retiro.

---

## 6. Método `mostrar_detalles`

```python
    def mostrar_detalles(self):
        return (
            f"Titular: {self.titular}\n"
            f"Número de cuenta: {self.numero}\n"
            f"Saldo actual: ${self.saldo:,.2f}"
        )
```

- Este método crea y devuelve una cadena con la información de la cuenta.
- Usa `f-strings` para incluir los valores de `self.titular`, `self.numero` y `self.saldo`.
- `:,.2f` formatea el saldo con dos decimales y separador de miles.

---

## 7. Función principal `main`

```python
def main():
    cuenta = CuentaBancaria(titular="Janeth Hidalgo", numero="1234567890", saldo_inicial=500.0)

    print("=== Detalles de la cuenta bancaria ===")
    print(cuenta.mostrar_detalles())

    print("\nDepositando $250.00...")
    cuenta.depositar(250.0)
    print(cuenta.mostrar_detalles())

    print("\nRetirando $100.00...")
    cuenta.retirar(100.0)
    print(cuenta.mostrar_detalles())
```

- `main()` es una función que prueba cómo funciona la clase.
- Crea un objeto `cuenta` usando la clase `CuentaBancaria`.
- Llama a los métodos `mostrar_detalles`, `depositar` y `retirar`.
- Imprime los resultados para que puedas ver qué ocurre.

---

## 8. Comprobar que se ejecuta el programa

```python
if __name__ == "__main__":
    main()
```

- Esta línea comprueba si el archivo se ejecuta directamente.
- Si el archivo se ejecuta como programa principal, llama a `main()`.
- Si el archivo se importa desde otro módulo, no ejecuta `main()` automáticamente.

---

## 9. Resumen para principiantes

- El ejemplo usa la programación orientada a objetos para modelar una cuenta bancaria.
- La clase define los datos (atributos) y las acciones (métodos).
- Crear un objeto es usar la clase como un molde.
- El objeto puede realizar operaciones seguras: depositar, retirar y mostrar su estado.

---

## 10. Sugerencia práctica

Puedes cambiar los valores dentro de `main()` para usar otros nombres, números de cuenta y cantidades.

Si quieres, también puedes crear otra clase como `Estudiante`, `Libro` o `Mascota` usando la misma idea.