# Instrucciones de Ejecución - Restaurante App Semana 13

## Verificación Previa

Antes de ejecutar la aplicación, verifica que la estructura está completa:

```powershell
cd C:\Users\Herobook\UEA\2626-POO-HIDALGO-JANETH\PARCIAL 2\SEMANA 13
python verificar_estructura.py
```

Deberías ver:
```
✓ ESTRUCTURA VERIFICADA: Todos los archivos están en su lugar
```

## Prueba de Servicios

Para verificar que los servicios funcionan sin necesidad de la interfaz gráfica:

```powershell
python test_servicios.py
```

Deberías ver:
- Los 6 productos cargados correctamente
- Los 3 usuarios cargados correctamente
- Todas las pruebas de acceso con ✓

## Ejecución de la Aplicación Gráfica

**La forma más simple y recomendada:**

```powershell
cd C:\Users\Herobook\UEA\2626-POO-HIDALGO-JANETH\PARCIAL 2\SEMANA 13
python run.py
```

**Alternativas:**

- **En Windows (doble click)**: Abre `ejecutar.bat`
- **Con PowerShell**: Ejecuta `ejecutar.ps1`
- **Con módulo Python**: `python -m restaurante_app.main`

**La aplicación abrirá una ventana con la interfaz de login.**

## Credenciales de Prueba

Usa cualquiera de estas para hacer login:

| Usuario | Contraseña |
|---------|-----------|
| 12345   | 1234      |
| 67890   | 5678      |
| 11111   | 9999      |

## Flujo de Uso

1. **Inicia la aplicación** → LoginView
2. **Ingresa usuario y contraseña** → se valida contra usuarios.json
3. **Login exitoso** → MainView
4. **Opciones disponibles**:
   - Productos: muestra lista desde productos.json
   - Usuarios: muestra lista desde usuarios.json
   - Ventas: mensaje de pendiente (deshabilitado)
   - Cerrar sesión: regresa a LoginView

## Solución de Problemas

### "ModuleNotFoundError: No module named 'restaurante_app'"
- Asegúrate de estar en la carpeta SEMANA 13
- Verifica que restaurante_app/ sea un subdirectorio

### La interfaz gráfica no aparece
- Verifica que Tkinter esté instalado:
  ```powershell
  python -c "import tkinter; print('Tkinter OK')"
  ```
- En Windows, Tkinter generalmente viene incluido con Python

### El login falla incluso con credenciales válidas
- Ejecuta `test_servicios.py` para verificar que los datos se cargan correctamente
- Revisa que usuarios.json no esté corrupto

## Próximos Pasos

Esta es la base estructural para la Semana 13. En futuras semanas se agregarán:
- Funcionalidad de Ventas
- Operaciones CRUD gráficas
- Más entidades del restaurante
- Mejor diseño visual
- Persistencia de cambios

---

**Última actualización**: Semana 13

