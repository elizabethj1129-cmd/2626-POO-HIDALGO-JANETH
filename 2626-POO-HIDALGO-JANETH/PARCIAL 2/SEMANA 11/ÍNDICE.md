# ÍNDICE DE DOCUMENTACIÓN - restaurante_app Semana 11

## 📚 Archivos de Documentación

### 1. **README.md** - Documentación Principal
Contiene:
- Descripción general del proyecto
- Estructura del proyecto
- Descripción de componentes (Producto, Usuario, Venta)
- Explicación de servicios (ArchivoServicio, Restaurante)
- Operación de venta completa
- Modelo de persistencia JSON
- Manejo de excepciones
- Validaciones implementadas
- Ejemplo de sesión completa
- Pruebas realizadas
- Mejoras respecto a Semana 10
- Conclusiones

**Léelo primero para entender el proyecto completo.**

### 2. **INSTRUCCIONES.md** - Guía de Uso
Contiene:
- Prerrequisitos y requisitos del sistema
- Estructura del proyecto
- Cómo ejecutar el programa
- Cómo ejecutar las pruebas
- Flujo de uso del programa
- Menú principal explicado
- Operaciones disponibles en detalle
- Ejemplo completo de sesión
- Validaciones y restricciones
- Manejo de errores y solución de problemas
- Notas para desarrolladores

**Consulta cuando necesites saber cómo usar el programa.**

### 3. **RESUMEN_ENTREGA.md** - Checklist de Entrega
Contiene:
- Estado del proyecto
- Checklist de todos los requisitos
- Lista de características implementadas
- Validaciones implementadas
- Casos de prueba
- Características adicionales
- Lista de archivos creados
- Próximos pasos recomendados
- Comandos útiles
- Validación final

**Verifica aquí que todo está completo antes de entregar.**

### 4. **Este Archivo - ÍNDICE.md**
Proporciona un mapa de navegación de toda la documentación.

---

## 📁 Estructura de Directorios

```
SEMANA 11/
│
├── 📄 README.md                    ← Documentación principal
├── 📄 INSTRUCCIONES.md             ← Guía de uso
├── 📄 RESUMEN_ENTREGA.md           ← Checklist de entrega
├── 📄 ÍNDICE.md                    ← Este archivo
│
├── 🐍 main.py (raíz)               ← [NO USAR - Ver restaurante_app/main.py]
│
├── 🐍 test_restaurante.py          ← Pruebas automatizadas
├── 🐍 cargar_datos_ejemplo.py      ← Carga datos de ejemplo
│
├── .gitignore                      ← Configuración para Git
│
└── 📁 restaurante_app/             ← Aplicación principal
    │
    ├── __init__.py                 ← Marca como paquete
    ├── 🐍 main.py                  ← Punto de entrada (EJECUTAR ESTE)
    │
    ├── 📁 datos/                   ← Persistencia JSON
    │   ├── productos.json
    │   ├── usuarios.json
    │   └── ventas.json
    │
    ├── 📁 modelos/                 ← Clases del dominio
    │   ├── __init__.py
    │   ├── 🐍 producto.py          ← Clase Producto
    │   ├── 🐍 usuario.py           ← Clase Usuario
    │   └── 🐍 venta.py             ← Clase Venta (NUEVA)
    │
    └── 📁 servicios/               ← Lógica de negocio
        ├── __init__.py
        ├── 🐍 archivo_servicio.py  ← Persistencia JSON
        └── 🐍 restaurante.py       ← Lógica de negocios
```

---

## 🚀 Inicio Rápido

### Opción 1: Ejecución Interactiva
```bash
# 1. Cargar datos de ejemplo
python cargar_datos_ejemplo.py

# 2. Ejecutar el programa
python restaurante_app/main.py
```

### Opción 2: Solo Pruebas
```bash
python test_restaurante.py
```

### Opción 3: Desarrollo Manual
```bash
# Ejecutar directamente sin datos previos
python restaurante_app/main.py
# Registrar manualmente productos y usuarios
# Realizar ventas
```

---

## 📖 Flujo de Lectura Recomendado

### Para Estudiantes
1. **INSTRUCCIONES.md** - Aprende cómo usar el programa
2. **restaurante_app/main.py** - Ve cómo se estructura el menú
3. **restaurante_app/servicios/restaurante.py** - Entiende la lógica de negocio
4. **restaurante_app/modelos/** - Revisa las clases
5. **README.md** - Profundiza en detalles técnicos

### Para Profesores
1. **README.md** - Visión completa del proyecto
2. **RESUMEN_ENTREGA.md** - Verifica requisitos cumplidos
3. **restaurante_app/servicios/restaurante.py** - Valida lógica
4. **test_restaurante.py** - Ejecuta pruebas
5. **restaurante_app/datos/** - Verifica persistencia

### Para Revisión de Código
1. **restaurante_app/modelos/venta.py** - Nueva clase clave
2. **restaurante_app/servicios/restaurante.py** - Operación vender_producto()
3. **restaurante_app/servicios/archivo_servicio.py** - Persistencia mejorada
4. **restaurante_app/main.py** - Opciones 9 y 10 nuevas

---

## 🔍 Búsqueda de Información Específica

### Entender la Operación de Venta
- **README.md** → Sección "Operación de Venta: Flujo Completo"
- **restaurante_app/servicios/restaurante.py** → Método `vender_producto()`

### Aprender sobre Persistencia
- **README.md** → Sección "Persistencia de Datos"
- **restaurante_app/servicios/archivo_servicio.py** → Todos los métodos

### Ver Validaciones
- **README.md** → Sección "Validaciones Implementadas"
- **restaurante_app/modelos/producto.py** → Método `__post_init__()` y `vender()`

### Entender Manejo de Errores
- **README.md** → Sección "Manejo de Excepciones Requerido"
- **restaurante_app/servicios/archivo_servicio.py** → Try/except blocks

### Ejecutar y Probar
- **INSTRUCCIONES.md** → Sección "Ejecución del Programa"
- **test_restaurante.py** → Ejecuta tests
- **cargar_datos_ejemplo.py** → Carga datos iniciales

---

## 📋 Checklist de Verificación

Antes de entregar, verifica:

- [ ] Todos los archivos están presentes en SEMANA 11/
- [ ] restaurante_app/main.py ejecuta sin errores
- [ ] test_restaurante.py ejecuta correctamente
- [ ] cargar_datos_ejemplo.py genera archivos JSON
- [ ] Se pueden realizar ventas con validaciones
- [ ] Se pueden consultar ventas por usuario
- [ ] Los datos persisten después de cerrar y reabrir
- [ ] README.md está completo y actualizado
- [ ] INSTRUCCIONES.md proporciona guía clara
- [ ] Código tiene type hints y nombres descriptivos
- [ ] No hay archivos __pycache__ en el repositorio

---

## 🔗 Enlaces Rápidos a Archivos Clave

| Concepto | Archivo | Función |
|----------|---------|---------|
| Punto de entrada | restaurante_app/main.py | Menú interactivo |
| Clase Producto | restaurante_app/modelos/producto.py | Con stock |
| Clase Usuario | restaurante_app/modelos/usuario.py | Con to_dict() |
| Clase Venta | restaurante_app/modelos/venta.py | NUEVA |
| Servicios | restaurante_app/servicios/restaurante.py | Lógica de negocio |
| Persistencia | restaurante_app/servicios/archivo_servicio.py | JSON I/O |
| Datos | restaurante_app/datos/ | Archivos JSON |
| Pruebas | test_restaurante.py | Validación automática |
| Datos ejemplo | cargar_datos_ejemplo.py | Carga inicial |

---

## ❓ Preguntas Frecuentes

### ¿Por dónde empiezo?
→ Lee **INSTRUCCIONES.md** y ejecuta `python restaurante_app/main.py`

### ¿Cómo cargo datos de ejemplo?
→ Ejecuta `python cargar_datos_ejemplo.py`

### ¿Cómo sé si todo funciona?
→ Ejecuta `python test_restaurante.py`

### ¿Dónde se guardan los datos?
→ En `restaurante_app/datos/` (productos.json, usuarios.json, ventas.json)

### ¿Qué cambió respecto a Semana 10?
→ Lee **README.md** → Sección "Mejoras Respecto a Semana 10"

### ¿Cómo agrego mis propias pruebas?
→ Ver ejemplo en `test_restaurante.py`

### ¿Puedo agregar más funcionalidades?
→ Sí, respeta la arquitectura. Lee el código en `servicios/restaurante.py`

---

## 📊 Estadísticas del Proyecto

- **Archivos Python**: 9
- **Archivos de Datos**: 3 (JSON)
- **Archivos de Documentación**: 4
- **Líneas de Código**: ~1000+
- **Métodos Implementados**: 30+
- **Clases Definidas**: 4 (Producto, Usuario, Venta, ArchivoServicio, Restaurante)
- **Casos de Prueba**: 5+

---

## 🎯 Objetivos de Aprendizaje Alcanzados

✓ Usar colecciones para almacenar objetos del dominio  
✓ Persistir datos usando JSON  
✓ Relacionar objetos mediante clases (Venta)  
✓ Validar operaciones de negocio  
✓ Manejar excepciones específicas  
✓ Separar responsabilidades (modelos, servicios, presentación)  
✓ Implementar un CRUD completo  
✓ Trabajar con archivos en Python  
✓ Documentar código profesionalmente  

---

## 📞 Soporte

### Errores Comunes

1. **"ModuleNotFoundError: No module named 'restaurante_app'"**
   → Verifica estar en la carpeta correcta
   → Verifica que existan los archivos `__init__.py`

2. **"FileNotFoundError: [Errno 2] No such file or directory"**
   → Los archivos JSON se crearán automáticamente
   → Si persiste, verifica permisos de la carpeta

3. **"ValueError: stock inválido"**
   → Solo números enteros positivos permitidos
   → Lee INSTRUCCIONES.md → Validaciones

---

## 📝 Notas Finales

Este proyecto constituye una **evolución significativa** del sistema de restaurante_app. Los conceptos clave implementados son:

1. **Colecciones como Relaciones**: Ventas conectan Usuarios y Productos
2. **Persistencia Completa**: 3 archivos JSON diferentes
3. **Validación Integral**: Cada operación valida antes de ejecutar
4. **Arquitectura Limpia**: Separación clara entre capas
5. **Documentación Profesional**: Código autodocumentado + guías

El código está **listo para producción educativa** y puede servir como base para futuras mejoras.

---

**Versión**: 1.0  
**Fecha**: 26 de agosto de 2026  
**Estado**: Completo y Verificado ✓  
**Destinatario**: Semana 11 - Programación Orientada a Objetos

