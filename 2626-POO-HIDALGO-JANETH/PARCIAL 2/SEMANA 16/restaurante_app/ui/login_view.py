import tkinter as tk
from tkinter import ttk, messagebox
from typing import Callable
from ..servicios.restaurante_servicio import RestauranteServicio


class LoginView:
    """Vista de login para la autenticación de usuarios.

    Permite ingresar identificación y contraseña,
    y valida las credenciales mediante el servicio del restaurante.
    """

    def __init__(
        self,
        parent: tk.Tk,
        servicio: RestauranteServicio,
        on_login_success: Callable[[str], None],
    ):
        """Inicializar la vista de login.

        Args:
            parent: ventana principal de Tkinter
            servicio: instancia de RestauranteServicio
            on_login_success: callback a ejecutar cuando el login es exitoso
        """
        self.parent = parent
        self.servicio = servicio
        self.on_login_success = on_login_success

        self.frame = None
        self.entry_usuario = None
        self.entry_contraseña = None
        self.label_error = None

    def crear_interfaz(self) -> None:
        """Crear la interfaz gráfica de login."""
        # Limpiar frame anterior si existe
        if self.frame:
            self.frame.destroy()

        # Crear frame principal
        self.frame = ttk.Frame(self.parent, padding="20")
        self.frame.pack(expand=True, fill="both")

        # Título
        titulo = ttk.Label(
            self.frame,
            text="RESTAURANTE APP",
            font=("Arial", 24, "bold"),
        )
        titulo.pack(pady=20)

        # Subtítulo
        subtitulo = ttk.Label(
            self.frame,
            text="Ingrese sus credenciales",
            font=("Arial", 12),
        )
        subtitulo.pack(pady=10)

        # Frame para el formulario
        form_frame = ttk.Frame(self.frame)
        form_frame.pack(pady=20)

        # Etiqueta y entrada de usuario
        ttk.Label(form_frame, text="Identificacion:", font=("Arial", 10)).grid(
            row=0, column=0, sticky="e", padx=5, pady=10
        )
        self.entry_usuario = ttk.Entry(form_frame, width=25, font=("Arial", 10))
        self.entry_usuario.grid(row=0, column=1, padx=5, pady=10)
        self.entry_usuario.focus()

        # Etiqueta y entrada de contraseña
        ttk.Label(form_frame, text="Contrasena:", font=("Arial", 10)).grid(
            row=1, column=0, sticky="e", padx=5, pady=10
        )
        self.entry_contraseña = ttk.Entry(
            form_frame, width=25, font=("Arial", 10), show="*"
        )
        self.entry_contraseña.grid(row=1, column=1, padx=5, pady=10)

        # Bind Enter para login
        self.entry_contraseña.bind("<Return>", lambda e: self._intentar_login())

        # Label de error
        self.label_error = ttk.Label(
            self.frame, text="", foreground="red", font=("Arial", 10)
        )
        self.label_error.pack(pady=10)

        # Botón de login
        btn_login = ttk.Button(
            self.frame, text="Ingresar", command=self._intentar_login
        )
        btn_login.pack(pady=20)

    def _intentar_login(self) -> None:
        """Intentar login con las credenciales ingresadas."""
        usuario = self.entry_usuario.get().strip()
        contraseña = self.entry_contraseña.get()

        # Validar campos vacíos
        if not usuario or not contraseña:
            self.label_error.config(text="Por favor complete todos los campos")
            return

        # Validar credenciales
        if self.servicio.validar_acceso(usuario, contraseña):
            self.label_error.config(text="")
            self.entry_usuario.delete(0, tk.END)
            self.entry_contraseña.delete(0, tk.END)
            self.on_login_success(usuario)
        else:
            self.label_error.config(text="Credenciales invalidas")
            self.entry_contraseña.delete(0, tk.END)
            self.entry_usuario.select_range(0, tk.END)
            self.entry_usuario.focus()

