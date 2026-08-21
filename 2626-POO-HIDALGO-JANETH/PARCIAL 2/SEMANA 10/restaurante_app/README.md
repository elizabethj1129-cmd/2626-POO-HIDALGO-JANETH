# restaurante_app - Semana 10

Alumno: [Tu nombre completo]

Descripción
-----------
Evolución del proyecto restaurante_app para la Semana 10. Se incorpora persistencia
para los productos mediante un archivo JSON ubicado en `datos/productos.json`.

Estructura
---------
restaurante_app/
├── datos/
│   └── productos.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md

Flujo de carga y guardado
-------------------------
- Al iniciar `main.py`, `Restaurante` utiliza `ArchivoServicio.cargar_productos`
  para leer `datos/productos.json`. Si el archivo no existe, se inicia con
  una colección vacía; si contiene JSON inválido se informa y también se
  inicia con colección vacía.
- Al registrar, actualizar o eliminar un producto, `Restaurante` llama a
  `ArchivoServicio.guardar_productos` para escribir la lista actualizada en
  `datos/productos.json`.

Excepciones controladas
-----------------------
- FileNotFoundError: si `productos.json` no existe — se inicia con colección vacía.
- json.JSONDecodeError: se informa y se inicia con colección vacía.
- PermissionError: se informa al intentar leer o escribir sin permisos.
- KeyError / ValueError: al reconstruir objetos Producto desde registros
  defectuosos, el registro se omite y se informa al usuario.

Ejecución
--------
Desde la carpeta `PARCIAL 2/SEMANA 10`, ejecutar:

```powershell
python .\restaurante_app\main.py
```

Pruebas mínimas realizadas
--------------------------
1. Ejecuté `main.py` y registré productos mediante el menú.
2. Verifiqué que `datos/productos.json` contiene los productos ingresados.
3. Cerré la aplicación y volví a ejecutar `main.py` — los productos se recuperaron.
4. Actualicé y eliminé productos y comprobé que los cambios persisten tras reiniciar.

Notas
-----
Mantener en memoria que los usuarios no se persisten en esta entrega (solo
productos). El módulo `ArchivoServicio` concentra toda la IO sobre JSON para
facilitar pruebas y mantenimiento.

