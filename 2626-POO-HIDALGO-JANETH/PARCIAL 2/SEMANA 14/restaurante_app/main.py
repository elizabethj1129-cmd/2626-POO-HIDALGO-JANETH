"""Punto de entrada de la aplicación de restaurante con interfaz gráfica.

Este módulo crea la ventana principal de Tkinter, prepara los servicios
e inicializa el flujo de login.
"""

import sys
from pathlib import Path

# ============================================================================
# CONFIGURACIÓN DEL SISTEMA DE PATHS - CRÍTICA PARA LOS IMPORTS
# ============================================================================
# Este código se ejecuta SIEMPRE cuando se carga el módulo, sin importar cómo
# se invoque (python -m, python archivo.py, import, etc.)

_current_file = Path(__file__).resolve()
_current_dir = _current_file.parent      # restaurante_app/
_parent_dir = _current_dir.parent        # SEMANA 13/

# Paso 1: Limpiar sys.path de directorios problemáticos
_to_remove = [str(_current_dir)]
for _path in _to_remove:
    while _path in sys.path:
        sys.path.remove(_path)

# Paso 2: Asegurar que el directorio padre esté al inicio del path
if str(_parent_dir) not in sys.path:
    sys.path.insert(0, str(_parent_dir))

# Paso 3: Verificar configuración
_imports_ok = str(_parent_dir) in sys.path and str(_current_dir) not in sys.path

# ============================================================================
# IMPORTS DESPUÉS DE CONFIGURAR EL PATH
# ============================================================================

import tkinter as tk
from tkinter import ttk

# Importar con configuración del path ya establecida
try:
    # Intentar imports relativos (cuando se importa como módulo desde run.py)
    from .servicios.restaurante_servicio import RestauranteServicio
    from .ui.login_view import LoginView
    from .ui.main_view import MainView
except ImportError:
    # Fallback: usar imports absolutos (debería funcionar con path configurado)
    from restaurante_app.servicios.restaurante_servicio import RestauranteServicio
    from restaurante_app.ui.login_view import LoginView
    from restaurante_app.ui.main_view import MainView


class RestauranteApp:
    """Aplicación principal del restaurante con interfaz gráfica.

    Gestiona la ventana principal, los servicios y el flujo entre vistas.
    """

    def __init__(self, root: tk.Tk):
        """Inicializar la aplicación.

        Args:
            root: ventana principal de Tkinter
        """
        self.root = root
        self.root.title("Restaurante App - Semana 13")
        self.root.geometry("600x500")
        self.root.resizable(True, True)

        # Crear instancia del servicio
        datos_dir = Path(__file__).parent / "datos"
        self.servicio = RestauranteServicio(datos_dir=datos_dir)

        # Vistas
        self.login_view = LoginView(
            self.root, self.servicio, self._en_login_exitoso
        )
        self.main_view = None

        # Mostrar login inicial
        self._mostrar_login()

    def _mostrar_login(self) -> None:
        """Mostrar la vista de login."""
        self.login_view.crear_interfaz()

    def _en_login_exitoso(self, usuario_identificacion: str) -> None:
        """Manejador para cuando el login es exitoso.

        Args:
            usuario_identificacion: identificación del usuario autenticado
        """
        if self.login_view.frame:
            self.login_view.frame.destroy()

        self.main_view = MainView(
            self.root,
            self.servicio,
            usuario_identificacion,
            self._en_logout,
        )
        self.main_view.crear_interfaz()

    def _en_logout(self) -> None:
        """Manejador para cuando el usuario cierra sesión."""
        if self.main_view and self.main_view.frame:
            self.main_view.frame.destroy()
        self._mostrar_login()

    def ejecutar(self) -> None:
        """Iniciar el bucle principal de la aplicación."""
        self.root.mainloop()


def main() -> None:
    """Función principal."""
    root = tk.Tk()
    app = RestauranteApp(root)
    app.ejecutar()


if __name__ == "__main__":
    main()

