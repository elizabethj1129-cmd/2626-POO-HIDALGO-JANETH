#!/usr/bin/env python3
"""Script de entrada para la aplicación Restaurante App.

Este archivo ejecuta la aplicación correctamente desde la carpeta raíz.
"""

import sys
from pathlib import Path

# Agregar la carpeta actual al path para que se puedan importar módulos
current_dir = Path(__file__).parent
if str(current_dir) not in sys.path:
    sys.path.insert(0, str(current_dir))

# Importar y ejecutar la aplicación
if __name__ == "__main__":
    from restaurante_app.main import main
    main()

