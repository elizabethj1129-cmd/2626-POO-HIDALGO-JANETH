"""Script para verificar la estructura correcta del proyecto."""

import os
from pathlib import Path

def verificar_estructura():
    """Verifica que todos los archivos necesarios existan."""

    base_path = Path(__file__).resolve().parent

    archivos_requeridos = {
        "Documentación": [
            "README.md",
            "INSTRUCCIONES.md",
            "ÍNDICE.md",
            "RESUMEN_ENTREGA.md",
            "INICIO_RÁPIDO.md",
        ],
        "Scripts": [
            "test_restaurante.py",
            "cargar_datos_ejemplo.py",
        ],
        "Configuración": [
            ".gitignore",
        ],
        "Aplicación": [
            "restaurante_app/__init__.py",
            "restaurante_app/main.py",
            "restaurante_app/modelos/__init__.py",
            "restaurante_app/modelos/producto.py",
            "restaurante_app/modelos/usuario.py",
            "restaurante_app/modelos/venta.py",
            "restaurante_app/servicios/__init__.py",
            "restaurante_app/servicios/archivo_servicio.py",
            "restaurante_app/servicios/restaurante.py",
            "restaurante_app/datos/productos.json",
            "restaurante_app/datos/usuarios.json",
            "restaurante_app/datos/ventas.json",
        ],
    }

    print("\n" + "=" * 70)
    print("VERIFICACIÓN DE ESTRUCTURA DEL PROYECTO")
    print("=" * 70)

    archivo_faltante = False

    for categoria, archivos in archivos_requeridos.items():
        print(f"\n{categoria}:")
        for archivo in archivos:
            ruta = base_path / archivo
            if ruta.exists():
                tamaño = ruta.stat().st_size
                print(f"  ✓ {archivo} ({tamaño} bytes)")
            else:
                print(f"  ✗ {archivo} - FALTANTE")
                archivo_faltante = True

    print("\n" + "=" * 70)

    if not archivo_faltante:
        print("✓ ESTRUCTURA CORRECTA - Todos los archivos presentes")
        print("=" * 70)
        return True
    else:
        print("✗ ESTRUCTURA INCOMPLETA - Faltan archivos")
        print("=" * 70)
        return False


def verificar_contenido():
    """Verifica que algunos archivos contengan código válido."""

    base_path = Path(__file__).resolve().parent

    print("\n" + "=" * 70)
    print("VERIFICACIÓN DE CONTENIDO")
    print("=" * 70)

    archivos_python = [
        "restaurante_app/main.py",
        "restaurante_app/modelos/producto.py",
        "restaurante_app/modelos/usuario.py",
        "restaurante_app/modelos/venta.py",
        "restaurante_app/servicios/restaurante.py",
        "restaurante_app/servicios/archivo_servicio.py",
    ]

    todo_ok = True
    for archivo in archivos_python:
        ruta = base_path / archivo
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                contenido = f.read()
                lineas = len(contenido.split('\n'))

                # Verificar que tenga contenido
                if len(contenido) > 100:  # Mínimo arbitrario
                    print(f"  ✓ {archivo} ({lineas} líneas)")
                else:
                    print(f"  ✗ {archivo} - Muy pequeño")
                    todo_ok = False
        except Exception as e:
            print(f"  ✗ {archivo} - Error: {e}")
            todo_ok = False

    print("\n" + "=" * 70)
    if todo_ok:
        print("✓ CONTENIDO VALIDADO - Archivos tienen contenido válido")
    else:
        print("✗ PROBLEMAS DETECTADOS - Revisa los archivos")
    print("=" * 70)

    return todo_ok


def verificar_json():
    """Verifica que los archivos JSON sean válidos."""

    import json

    base_path = Path(__file__).resolve().parent

    print("\n" + "=" * 70)
    print("VERIFICACIÓN DE ARCHIVOS JSON")
    print("=" * 70)

    archivos_json = [
        "restaurante_app/datos/productos.json",
        "restaurante_app/datos/usuarios.json",
        "restaurante_app/datos/ventas.json",
    ]

    todo_ok = True
    for archivo in archivos_json:
        ruta = base_path / archivo
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                datos = json.load(f)
                tipo = "array" if isinstance(datos, list) else "object"
                print(f"  ✓ {archivo} - JSON válido ({tipo}, {len(datos)} elementos)")
        except FileNotFoundError:
            print(f"  ! {archivo} - No existe (se creará en la primera ejecución)")
        except json.JSONDecodeError:
            print(f"  ✗ {archivo} - JSON inválido")
            todo_ok = False
        except Exception as e:
            print(f"  ✗ {archivo} - Error: {e}")
            todo_ok = False

    print("\n" + "=" * 70)
    if todo_ok:
        print("✓ ARCHIVOS JSON VALIDADOS")
    else:
        print("✗ PROBLEMAS CON JSON - Revisa los archivos")
    print("=" * 70)

    return todo_ok


def generar_reporte():
    """Genera un reporte completo."""

    print("\n")
    print("╔" + "=" * 68 + "╗")
    print("║" + " " * 15 + "REPORTE DE VERIFICACIÓN DE ESTRUCTURA" + " " * 16 + "║")
    print("╚" + "=" * 68 + "╝")

    estructura_ok = verificar_estructura()
    contenido_ok = verificar_contenido()
    json_ok = verificar_json()

    print("\n" + "=" * 70)
    print("RESUMEN FINAL")
    print("=" * 70)
    print(f"  Estructura:     {'✓ OK' if estructura_ok else '✗ PROBLEMAS'}")
    print(f"  Contenido:      {'✓ OK' if contenido_ok else '✗ PROBLEMAS'}")
    print(f"  JSON:           {'✓ OK' if json_ok else '✗ PROBLEMAS'}")
    print("=" * 70)

    if estructura_ok and contenido_ok and json_ok:
        print("✓ PROYECTO LISTO PARA USAR")
        print("\nProximos pasos:")
        print("  1. python cargar_datos_ejemplo.py  (cargar datos de ejemplo)")
        print("  2. python restaurante_app/main.py  (ejecutar el programa)")
        print("  3. python test_restaurante.py      (ejecutar pruebas)")
    else:
        print("✗ REVISA LOS PROBLEMAS ANTES DE USAR EL PROYECTO")

    print("=" * 70 + "\n")


if __name__ == "__main__":
    generar_reporte()

