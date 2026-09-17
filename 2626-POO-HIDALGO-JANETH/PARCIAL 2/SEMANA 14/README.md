# Proyecto Restaurante App - Semana 14

## Propósito
El propósito de esta semana es aplicar los conceptos de componentes y contenedores en Tkinter/ttk para mejorar significativamente la interfaz gráfica (GUI) de la aplicación del restaurante. Además, se implementa el flujo completo (CRUD) para la gestión de productos, utilizando la arquitectura modular N-Capas existente.

## Estructura del Proyecto
```
restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── main.py
```

## Mejoras en la Interfaz
- Se reemplazó la vista básica con un diseño organizado usando contenedores `ttk.Frame` y `ttk.LabelFrame`.
- Se implementó una barra lateral de navegación para cambiar entre las secciones de "Productos" y "Usuarios".
- Se agregó un formulario completo para el registro, carga, actualización y eliminación de productos utilizando componentes como `ttk.Entry` y `ttk.Combobox`.
- Se incorporó un componente `ttk.Treeview` para visualizar la información de los productos y usuarios en formato tabular de manera clara.

## Operaciones sobre Productos (CRUD)
Se implementaron las siguientes operaciones que interactúan a través de los componentes de la GUI (mediante `command=`) delegando la lógica a `RestauranteServicio`:
- **Registrar:** Crea un nuevo producto validando los campos y comprobando que el código no exista.
- **Consultar/Cargar:** Busca un producto por su código y carga sus datos en el formulario para revisión o edición.
- **Actualizar:** Modifica la información (nombre, categoría, precio y stock) de un producto existente.
- **Eliminar:** Elimina un producto del sistema previa confirmación.

## Persistencia
Se mantiene la persistencia basada en archivos JSON (`productos.json` y `usuarios.json`). `RestauranteServicio` se encarga de guardar los cambios luego de cualquier modificación en la lista de productos.

## Pasos para ejecutar
1. Asegúrese de tener instalado Python 3.7 o superior.
2. Abra una terminal en la carpeta principal del proyecto (donde se encuentra `main.py` o el directorio `restaurante_app`).
3. Ejecute el siguiente comando:
   ```bash
   python restaurante_app/main.py
   ```
   (O simplemente `python main.py` si se encuentra dentro del directorio `restaurante_app`).
4. Ingrese con las credenciales por defecto (ej. admin / admin123).
