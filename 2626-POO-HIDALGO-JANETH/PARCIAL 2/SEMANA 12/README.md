# Restaurante App - Semana 12

Este repositorio contiene la evolución de la aplicación `restaurante_app` de la Semana 11, incorporando mejoras internas en el uso de colecciones para optimizar las búsquedas, consultas y validaciones, sin perder las funcionalidades previas ni la persistencia de datos (JSON).

## Mejoras Implementadas

Se han modificado las estructuras de datos dentro de la capa de servicio (`restaurante.py`) para evitar recorrer listas completas repetitivamente:

1.  **Búsqueda de Productos (`_indice_productos`)**:
    *   **Colección:** Diccionario (`dict`).
    *   **Clave:** `codigo` del producto.
    *   **Valor:** Objeto `Producto`.
    *   **Beneficio:** Permite buscar productos por su código en tiempo constante $O(1)$ en métodos como `buscar_producto`, `vender_producto`, `actualizar_producto` y `eliminar_producto`, evitando el recorrido lineal por la lista `_productos`.

2.  **Búsqueda de Usuarios (`_indice_usuarios`)**:
    *   **Colección:** Diccionario (`dict`).
    *   **Clave:** `identificacion` del usuario.
    *   **Valor:** Objeto `Usuario`.
    *   **Beneficio:** Permite validar la existencia de usuarios y buscarlos por identificación instantáneamente al registrar usuarios o ventas, evitando iteraciones innecesarias sobre `_usuarios`.

3.  **Consulta de Ventas por Usuario (`_ventas_por_usuario`)**:
    *   **Colección:** Diccionario (`dict`).
    *   **Clave:** `identificacion` del usuario (`usuario_id`).
    *   **Valor:** Lista (`list`) de objetos `Venta` relacionados a ese usuario.
    *   **Beneficio:** Mejora el rendimiento del método `obtener_ventas_usuario(identificacion)`. En lugar de iterar por toda la colección global de `_ventas`, se recupera directamente la lista de ventas del cliente requerido.

4.  **Uso de Set (`obtener_categorias_unicas`)**:
    *   **Colección:** Conjunto (`set`).
    *   **Beneficio:** Continúa su uso para la validación de unicidad de categorías, devolviendo rápidamente un listado de categorías únicas.

*Nota:* Las colecciones principales en forma de lista (`_productos`, `_usuarios`, `_ventas`) se mantuvieron intactas y sincronizadas, ya que son indispensables para listar todos los objetos iterativamente y facilitar la persistencia JSON. Las nuevas estructuras auxiliares en memoria (índices) se reconstruyen automáticamente al iniciar la aplicación (`_load_products`, `_load_users`, `_load_sales`) en el constructor del servicio.

## Forma de Ejecución

Para ejecutar la aplicación:

1.  Abra una terminal en este directorio (donde se encuentra `main.py`).
2.  Ejecute el comando:
    ```bash
    python main.py
    ```
3.  El sistema presentará el menú interactivo para gestionar la tienda.

## Pruebas Realizadas

1.  **Carga de datos JSON**: Al abrir el programa, los índices de diccionario se reconstruyen correctamente partiendo de los archivos en `datos/`.
2.  **Búsqueda de Productos y Usuarios**: Comprobada la validación de códigos repetidos al registrar, y la obtención inmediata de registros al realizar una venta.
3.  **Consulta de Ventas**: Verificada la obtención del historial de compras de un usuario específico de manera directa.
4.  **Actualización y sincronización**: Al realizar una venta, el índice global, los índices auxiliares (`_ventas_por_usuario`) y la persistencia JSON, junto con el stock del producto modificado, mantienen consistencia y sincronización total. Al eliminar un producto, este es removido tanto de la lista principal como de su índice.
