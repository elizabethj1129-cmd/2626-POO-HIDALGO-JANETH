# Restaurante App - Semana 15

Este proyecto es una aplicación de gestión para un restaurante con interfaz gráfica construida en Tkinter, la cual ha sido evolucionada para incluir el registro de **Ventas**.

## Fundamentos de Eventos (Semana 15)
Se ha implementado el fundamento principal de manejo de eventos, demostrando el flujo de acción en la interfaz hacia la lógica de negocio y persistencia:
`Acción del usuario` → `Botón (command=)` → `Callback` → `Servicio (Lógica + Persistencia)` → `Actualización Visual`

### Características Implementadas:
- **Gestión de Ventas:** Nueva sección en la interfaz para relacionar a un usuario con un producto mediante una venta.
- **Modelo Venta:** Creación de un modelo de datos `Venta` en `modelos/venta.py`.
- **Persistencia en JSON:** Se almacena el historial de ventas en `datos/ventas.json`.
- **Delegación:** La UI recolecta los datos de los ComboBox de usuarios y productos, y el callback (`_registrar_venta`) solicita al `RestauranteServicio` que valide, reduzca el stock, guarde y retorne el resultado.
- **Logotipo:** Inclusión de un logotipo para la aplicación usando la carpeta `assets/logo.png`.
- **Continuidad:** Se preservan el inicio de sesión y la gestión de productos/usuarios desarrollados en semanas anteriores.

## Ejecución
Para ejecutar la aplicación, dirígete a la carpeta `restaurante_app` (o el directorio raíz que la contiene) y ejecuta:
```bash
python main.py
```
