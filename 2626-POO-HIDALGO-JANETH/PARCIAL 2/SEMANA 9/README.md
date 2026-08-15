# Restaurante App - Semana 9

Estudiante: [Tu nombre aquí]

Descripción
-----------
Proyecto modular que administra productos y usuarios de un restaurante. En esta semana se integran estructuras de datos: lista, tupla, diccionario y conjunto, aplicadas con una finalidad concreta dentro del sistema.

Estructura del proyecto
-----------------------
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py

Responsabilidad de los componentes
---------------------------------
- `modelos/producto.py`: clase `Producto` (codigo, nombre, categoria, precio).
- `modelos/usuario.py`: clase `Usuario` (identificacion, nombre, correo).
- `servicios/restaurante.py`: clase `Restaurante` que administra las colecciones (listas) y ofrece métodos para CRUD.
- `main.py`: interfaz por consola, muestra menú y solicita datos al usuario.

Uso de estructuras de datos
--------------------------
- Lista (`list`): las colecciones dinámicas de productos y usuarios se almacenan como listas en la clase `Restaurante`.
- Tupla (`tuple`): las opciones del menú (`MENU_OPTIONS`) se definen como una tupla, ya que son valores estables durante la ejecución.
- Diccionario (`dict`): en `main.py` se usa un diccionario `actions` para mapear la opción seleccionada a la función correspondiente (relación clave → valor).
- Conjunto (`set`): el servicio provee `obtener_categorias_unicas()` que devuelve un `set` con las categorías sin duplicados.

Ejecución
---------
Desde la carpeta `SEMANA 9` ejecutar:

```powershell
python -m restaurante_app.main
```

O bien desde dentro de `restaurante_app`:

```powershell
python main.py
```

Persistencia de datos
---------------------
Los productos y usuarios se almacenan de forma persistente en la carpeta `restaurante_app/data/` como archivos JSON:

- `productos.json`: lista de diccionarios que representan cada `Producto`.
- `usuarios.json`: lista de diccionarios que representan cada `Usuario`.
 - `productos.json`: diccionario cuya clave es el `codigo` del producto y el valor un diccionario con sus campos (nombre, categoria, precio).
 - `usuarios.json`: diccionario cuya clave es la `identificacion` del usuario y el valor un diccionario con sus campos (nombre, correo).

El servicio `Restaurante` carga estos archivos al iniciar y guarda los cambios automáticamente tras operaciones de registro, actualización o eliminación.

Notas finales
------------
Se han aplicado validaciones básicas para evitar códigos de productos e identificaciones de usuarios duplicadas. La administración de las colecciones se realiza exclusivamente desde la clase `Restaurante`; `main.py` solo invoca sus métodos.

