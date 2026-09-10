import tkinter as tk
from tkinter import ttk, messagebox
from typing import Callable
from ..servicios.restaurante_servicio import RestauranteServicio


class MainView:
    """Vista principal de la aplicación después del login.

    Muestra un menú con opciones para consultar productos,
    usuarios y otras funcionalidades del restaurante.
    """

    def __init__(
        self,
        parent: tk.Tk,
        servicio: RestauranteServicio,
        usuario_identificacion: str,
        on_logout: Callable[[], None],
    ):
        """Inicializar la vista principal.

        Args:
            parent: ventana principal de Tkinter
            servicio: instancia de RestauranteServicio
            usuario_identificacion: identificación del usuario autenticado
            on_logout: callback a ejecutar cuando se cierra sesión
        """
        self.parent = parent
        self.servicio = servicio
        self.usuario_identificacion = usuario_identificacion
        self.on_logout = on_logout

        self.frame = None
        self.usuario_obj = self.servicio.buscar_usuario(usuario_identificacion)

    def crear_interfaz(self) -> None:
        """Crear la interfaz gráfica principal."""
        # Limpiar frame anterior si existe
        if self.frame:
            self.frame.destroy()

        # Crear frame principal
        self.frame = ttk.Frame(self.parent, padding="20")
        self.frame.pack(expand=True, fill="both")

        # Encabezado con bienvenida
        header_frame = ttk.Frame(self.frame)
        header_frame.pack(fill="x", pady=10)

        titulo = ttk.Label(
            header_frame,
            text="SISTEMA DE RESTAURANTE",
            font=("Arial", 20, "bold"),
        )
        titulo.pack(side="left")

        # Label con información del usuario
        usuario_nombre = (
            f"Usuario: {self.usuario_obj.nombre}" if self.usuario_obj else ""
        )
        info_usuario = ttk.Label(
            header_frame,
            text=usuario_nombre,
            font=("Arial", 10),
            foreground="gray",
        )
        info_usuario.pack(side="right")

        # Separador
        separator = ttk.Separator(self.frame, orient="horizontal")
        separator.pack(fill="x", pady=10)

        # Botones principales
        botones_frame = ttk.Frame(self.frame)
        botones_frame.pack(fill="both", expand=True, pady=20)

        # Botón Productos
        btn_productos = ttk.Button(
            botones_frame,
            text="📦 Productos",
            command=self._mostrar_productos,
        )
        btn_productos.pack(pady=10, padx=10, fill="x")

        # Botón Usuarios
        btn_usuarios = ttk.Button(
            botones_frame,
            text="👥 Usuarios",
            command=self._mostrar_usuarios,
        )
        btn_usuarios.pack(pady=10, padx=10, fill="x")

        # Botón Ventas (pendiente)
        btn_ventas = ttk.Button(
            botones_frame,
            text="💳 Ventas (Pendiente)",
            command=self._mostrar_pendiente,
            state="disabled",
        )
        btn_ventas.pack(pady=10, padx=10, fill="x")

        # Botón Cerrar sesión
        btn_logout = ttk.Button(
            botones_frame,
            text="🚪 Cerrar sesión",
            command=self._cerrar_sesion,
        )
        btn_logout.pack(pady=10, padx=10, fill="x")

        # Área de información
        self.info_frame = ttk.LabelFrame(
            self.frame, text="Información", padding="10"
        )
        self.info_frame.pack(fill="both", expand=True, pady=10)

        # Canvas y scrollbar para información
        canvas = tk.Canvas(self.info_frame)
        scrollbar = ttk.Scrollbar(self.info_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        self.info_text = tk.Text(
            scrollable_frame,
            height=15,
            width=60,
            state="disabled",
            font=("Arial", 9),
        )
        self.info_text.pack()

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def _mostrar_productos(self) -> None:
        """Mostrar lista de productos en el área de información."""
        self.info_frame.config(text="Información - Productos")
        productos = self.servicio.listar_productos()

        self.info_text.config(state="normal")
        self.info_text.delete(1.0, tk.END)

        if not productos:
            self.info_text.insert(tk.END, "No hay productos registrados.")
        else:
            self.info_text.insert(tk.END, "LISTA DE PRODUCTOS\n")
            self.info_text.insert(tk.END, "=" * 60 + "\n\n")

            for p in productos:
                self.info_text.insert(
                    tk.END, f"Código: {p.codigo}\n"
                )
                self.info_text.insert(
                    tk.END, f"Nombre: {p.nombre}\n"
                )
                self.info_text.insert(
                    tk.END, f"Categoría: {p.categoria}\n"
                )
                self.info_text.insert(
                    tk.END, f"Precio: ${p.precio:.2f}\n"
                )
                self.info_text.insert(
                    tk.END, f"Stock: {p.stock}\n"
                )
                self.info_text.insert(tk.END, "-" * 60 + "\n\n")

        self.info_text.config(state="disabled")

    def _mostrar_usuarios(self) -> None:
        """Mostrar lista de usuarios en el área de información."""
        self.info_frame.config(text="Información - Usuarios")
        usuarios = self.servicio.listar_usuarios()

        self.info_text.config(state="normal")
        self.info_text.delete(1.0, tk.END)

        if not usuarios:
            self.info_text.insert(tk.END, "No hay usuarios registrados.")
        else:
            self.info_text.insert(tk.END, "LISTA DE USUARIOS\n")
            self.info_text.insert(tk.END, "=" * 60 + "\n\n")

            for u in usuarios:
                self.info_text.insert(
                    tk.END, f"Identificación: {u.identificacion}\n"
                )
                self.info_text.insert(
                    tk.END, f"Nombre: {u.nombre}\n"
                )
                self.info_text.insert(
                    tk.END, f"Correo: {u.correo}\n"
                )
                self.info_text.insert(tk.END, "-" * 60 + "\n\n")

        self.info_text.config(state="disabled")

    def _mostrar_pendiente(self) -> None:
        """Mostrar mensaje de funcionalidad pendiente."""
        messagebox.showinfo(
            "Funcionalidad Pendiente",
            "La gestión de ventas será implementada en próximas semanas.",
        )

    def _cerrar_sesion(self) -> None:
        """Cerrar sesión y retornar al login."""
        self.on_logout()

