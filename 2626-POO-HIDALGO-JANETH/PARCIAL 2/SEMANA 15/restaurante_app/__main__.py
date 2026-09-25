"""Punto de entrada alternativo para restaurante_app.

Este archivo actúa como __main__.py cuando se ejecuta:
  python -m restaurante_app
"""

import sys
from pathlib import Path

# Configurar sys.path CORRECTAMENTE antes de cualquier import
current_dir = Path(__file__).resolve().parent  # restaurante_app
parent_dir = current_dir.parent                # SEMANA 13

# Remover el directorio actual si está en el path
if str(current_dir) in sys.path:
    sys.path.remove(str(current_dir))

# Asegurar que el padre esté en el path
if str(parent_dir) not in sys.path:
    sys.path.insert(0, str(parent_dir))

# Ahora importar y ejecutar main
from restaurante_app.main import main

if __name__ == "__main__":
    main()

