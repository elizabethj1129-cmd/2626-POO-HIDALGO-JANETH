"""Script para verificar la estructura del proyecto."""

import sys
from pathlib import Path

def verificar_estructura():
    """Verificar que la estructura del proyecto es correcta."""
    print("=" * 70)
    print("VERIFICACIÓN DE ESTRUCTURA DEL PROYECTO")
    print("=" * 70)

    proyecto_dir = Path.cwd()
    restaurante_app = proyecto_dir / "restaurante_app"

    archivos_requeridos = {
        "Raíz": [
            "restaurante_app/main.py",
            "restaurante_app/__init__.py",
            "README.md",
        ],
        "Modelos": [
            "restaurante_app/modelos/__init__.py",
            "restaurante_app/modelos/producto.py",
            "restaurante_app/modelos/usuario.py",
        ],
        "Servicios": [
            "restaurante_app/servicios/__init__.py",
            "restaurante_app/servicios/archivo_servicio.py",
            "restaurante_app/servicios/restaurante_servicio.py",
        ],
        "UI": [
            "restaurante_app/ui/__init__.py",
            "restaurante_app/ui/login_view.py",
            "restaurante_app/ui/main_view.py",
        ],
        "Datos": [
            "restaurante_app/datos/productos.json",
            "restaurante_app/datos/usuarios.json",
        ],
    }

    all_ok = True
    for seccion, archivos in archivos_requeridos.items():
        print(f"\n{seccion}:")
        print("-" * 70)
        for archivo in archivos:
            ruta = proyecto_dir / archivo
            exists = ruta.exists()
            status = "✓" if exists else "✗"
            print(f"  {status} {archivo}")
            if not exists:
                all_ok = False

    print("\n" + "=" * 70)
    if all_ok:
        print("✓ ESTRUCTURA VERIFICADA: Todos los archivos están en su lugar")
    else:
        print("✗ ESTRUCTURA INCOMPLETA: Algunos archivos faltan")
    print("=" * 70)

    return all_ok


if __name__ == "__main__":
    ok = verificar_estructura()
    sys.exit(0 if ok else 1)

