# REFERENCIA RÁPIDA - restaurante_app Semana 11

## 🎯 En Una Página

### Para Ejecutar
```bash
# Opción 1: Con datos de ejemplo
python cargar_datos_ejemplo.py
python restaurante_app/main.py

# Opción 2: Desde cero
python restaurante_app/main.py
```

### Menú Principal (11 opciones)
```
1-5   → Productos (registrar, buscar, actualizar, eliminar, listar)
6-7   → Usuarios (registrar, listar)
8     → Categorías
9     → VENDER PRODUCTO [NUEVO]
10    → CONSULTAR VENTAS DE USUARIO [NUEVO]
11    → Salir
```

### Operación de Venta (Opción 9)
```
Solicita:   identificación usuario, código producto, cantidad
Valida:     usuario existe, producto existe, cantidad > 0, stock ≥ cantidad
Realiza:    crea Venta, disminuye stock, guarda JSON
Resultado:  éxito o error específico
```

### Consultar Ventas (Opción 10)
```
Solicita:   identificación usuario
Muestra:    todas las compras con detalles de productos
Formato:    producto, cantidad, precio, subtotal, fecha, total
```

---

## 📂 Archivos Clave

| Archivo | Propósito | Modificar |
|---------|----------|----------|
| `restaurante_app/main.py` | Menú y entrada | NO |
| `restaurante_app/modelos/venta.py` | Clase Venta | NO |
| `restaurante_app/servicios/restaurante.py` | Lógica negocio | Opcionalmente |
| `restaurante_app/datos/*.json` | Datos persistentes | NO (se actualiza automáticamente) |

---

## 🔄 Ciclo de Datos

### Al Iniciar
```
1. CargarProductos() → productos.json
2. CargarUsuarios()  → usuarios.json
3. CargarVentas()    → ventas.json
4. Mostrar menú
```

### En Una Venta
```
1. Validar usuario y producto
2. Crear objeto Venta
3. Disminuir stock de Producto
4. Guardar productos.json (stock actualizado)
5. Guardar ventas.json (nueva venta)
```

### Al Salir
```
Datos quedan en archivos JSON
Próxima ejecución recupera automáticamente
```

---

## 📋 Validaciones

### Producto
```
✓ Código único (no duplicados)
✓ Stock ≥ 0 (nunca negativo)
✓ Precio > 0
✓ Campos no vacíos
```

### Usuario
```
✓ Identificación única
✓ Campos no vacíos
```

### Venta
```
✓ Usuario existe
✓ Producto existe
✓ Cantidad > 0
✓ Stock disponible ≥ cantidad solicitada
```

---

## 🧪 Pruebas

### Ejecutar Pruebas
```bash
python test_restaurante.py
```

### Qué Prueba
- Crear productos, usuarios, ventas
- Validaciones de cada modelo
- Operaciones del servicio Restaurante
- Persistencia JSON

### Esperar
```
✓ TEST 1: PRODUCTOS CON STOCK
✓ TEST 2: USUARIOS
✓ TEST 3: VENTAS (RELACIÓN USUARIO-PRODUCTO)
✓ TEST 4: SERVICIO RESTAURANTE
✓ TEST 5: PERSISTENCIA JSON
✓ TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE
```

---

## 🐛 Solución de Errores Comunes

| Error | Causa | Solución |
|-------|-------|----------|
| `ModuleNotFoundError` | Importación mal | Verificar `__init__.py` en carpetas |
| "Producto no encontrado" | ID inválido | Usar ID registrado |
| "Stock insuficiente" | Pedir más de lo disponible | Reducir cantidad |
| "JSON inválido" | Archivo corrupto | Eliminar y recrear |
| "Permiso denegado" | Carpeta protegida | Cambiar permisos en datos/ |

---

## 📊 Estructura JSON

### Producto
```json
{
  "codigo": "P001",
  "nombre": "Hamburguesa",
  "categoria": "Comida Rápida",
  "precio": 12.50,
  "stock": 8
}
```

### Usuario
```json
{
  "identificacion": "1001",
  "nombre": "Juan García",
  "correo": "juan@example.com"
}
```

### Venta
```json
{
  "usuario_id": "1001",
  "producto_codigo": "P001",
  "cantidad": 2,
  "fecha": "2026-08-26 15:30:45"
}
```

---

## 💡 Tips

- Los datos se guardan automáticamente
- No necesitas hacer `save` manual
- Los JSON se crean en primera ejecución
- Puedes eliminar JSON para empezar desde cero
- El programa tolera JSON vacío al iniciar

---

## 🎓 Conceptos Clave

**Venta = Relación Usuario + Producto**
```
Usuario 1:M Venta
Producto 1:M Venta
```

**Persistencia = JSON como "Base de Datos"**
```
Memoria → JSON (al cerrar)
JSON → Memoria (al abrir)
```

**Validación = Guardia de Negocio**
```
Entrada → Validar → Procesar → Guardar
```

---

## 📖 Documentación

| Archivo | Leer Cuando |
|---------|------------|
| `INICIO_RÁPIDO.md` | Quieres empezar rápido |
| `INSTRUCCIONES.md` | Necesitas detalles de uso |
| `README.md` | Quieres entender todo |
| `ÍNDICE.md` | Necesitas navegar |
| `RESUMEN_ENTREGA.md` | Quieres verificar requisitos |

---

## ⚡ Comandos Esenciales

```bash
# Ver estructura
dir restaurante_app /s

# Ejecutar programa
python restaurante_app/main.py

# Ejecutar pruebas
python test_restaurante.py

# Cargar datos de ejemplo
python cargar_datos_ejemplo.py

# Verificar estructura
python verificar_estructura.py
```

---

## 🚀 Flujo Completo (Paso a Paso)

### 1. Preparar Datos
```bash
python cargar_datos_ejemplo.py
```
Carga: 5 productos + 4 usuarios + 5 ventas de ejemplo

### 2. Ejecutar Programa
```bash
python restaurante_app/main.py
```
Se muestra el menú

### 3. Probar una Venta
```
Opción: 9
Identificación usuario: 1001
Código producto: P001
Cantidad: 2
```
Resultado: Venta registrada, stock actualizado

### 4. Consultar Ventas
```
Opción: 10
Identificación usuario: 1001
```
Resultado: Todas las compras del usuario

### 5. Cerrar y Reabrir
```bash
(Presionar 11)
python restaurante_app/main.py
```
Resultado: Los datos se recuperan automáticamente

---

## 📈 Estadísticas

- **Líneas de código**: 1000+
- **Clases**: 5 (Producto, Usuario, Venta, ArchivoServicio, Restaurante)
- **Métodos**: 30+
- **Archivos**: 23
- **Pruebas**: 5
- **Documentación**: 6 archivos

---

## ✅ Antes de Entregar

- [ ] Ejecutar `python restaurante_app/main.py` sin errores
- [ ] Opción 9 (vender) funciona
- [ ] Opción 10 (consultar ventas) funciona
- [ ] Archivos JSON se actualizan
- [ ] Datos persisten al cerrar/abrir
- [ ] Repositorio GitHub es público
- [ ] README.md está actualizado

---

**¡LISTO PARA USAR!** 🎉

Lee `INICIO_RÁPIDO.md` para los 3 pasos iniciales.

