# Restaurante App - Semana 16

## Propósito de la Semana 16
El propósito de la Semana 16 es evolucionar la aplicación para incorporar una gestión de usuarios basada en eventos, ampliando la aplicación construida en semanas anteriores. Se implementa una interfaz de administración de usuarios utilizando el componente `Treeview`, aplicando eventos de teclado y de selección.

## Evolución del Proyecto
Se parte de la versión de la Semana 15, conservando la arquitectura modular (datos, modelos, servicios, ui).
Se incorporó el atributo `rol` al modelo `Usuario` y se limitó el acceso a la sección "Usuarios" exclusivamente para cuentas con rol "Administrador".

## Gestión de Usuarios y Roles
- Se añadió un sistema básico de roles (`Administrador`, `Empleado`, `Cliente`).
- Un Administrador puede registrar, consultar, actualizar y eliminar a otros usuarios.
- La eliminación está protegida para que el administrador actual no pueda eliminar su propia cuenta accidentalmente.

## Eventos Implementados (`bind()`, `command=` y callbacks)
La interacción del usuario se captura mediante distintos eventos:
- **`<<TreeviewSelect>>`**: Asociado mediante `bind()` a la tabla de usuarios. Al hacer clic en un registro, el callback correspondiente busca el ID en el servicio y carga la información en el formulario, evitando exponer contraseñas.
- **`<Return>` (Enter)**: Asociado mediante `bind()` a los campos del formulario. Ejecuta el registro de un nuevo usuario como atajo de teclado, reutilizando la lógica del botón Registrar.
- **`<Escape>`**: Asociado mediante `bind()` a los campos del formulario. Limpia los datos ingresados y cancela la selección de la tabla.
- **`<<ComboboxSelected>>`**: Asociado al menú desplegable de "Rol". Dispara un callback que responde al cambio seleccionado por el usuario.
- **`command=`**: Se mantiene el uso de `command=` para asociar los botones principales (Registrar, Actualizar, Eliminar) a sus respectivos callbacks.

Esta separación demuestra la diferencia entre `command=` (para botones simples) y `bind()` (para eventos de ratón o teclado específicos de un widget).

## Persistencia
Todas las operaciones (crear, actualizar, eliminar) son gestionadas por la clase `RestauranteServicio`, que se encarga de las reglas de negocio y de la persistencia directa en el archivo `datos/usuarios.json`. La interfaz no lee ni modifica los archivos JSON directamente.

## Ejecución
Para ejecutar el proyecto, sitúese en el directorio del proyecto y ejecute:
```bash
python main.py
```
Ingrese con credenciales válidas (ejemplo: Administrador `12345` / `1234`).
