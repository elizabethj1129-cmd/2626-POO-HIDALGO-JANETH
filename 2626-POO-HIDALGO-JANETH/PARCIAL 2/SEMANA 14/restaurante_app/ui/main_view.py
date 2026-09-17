import tkinter as tk
from tkinter import ttk, messagebox
from typing import Callable
from ..servicios.restaurante_servicio import RestauranteServicio


class MainView:
    """Vista principal de la aplicación después del login.

    Muestra un menú con opciones para consultar y gestionar productos,
    y usuarios del restaurante.
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
        self.frame = ttk.Frame(self.parent, padding="10")
        self.frame.pack(expand=True, fill="both")

        # Encabezado con bienvenida
        header_frame = ttk.Frame(self.frame)
        header_frame.pack(fill="x", pady=(0, 10))

        titulo = ttk.Label(
            header_frame,
            text="SISTEMA DE RESTAURANTE",
            font=("Arial", 16, "bold"),
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

        # Contenedor principal que divide navegación y contenido
        main_content = ttk.Frame(self.frame)
        main_content.pack(fill="both", expand=True)

        # Barra lateral (Navegación)
        sidebar = ttk.Frame(main_content, width=150)
        sidebar.pack(side="left", fill="y", padx=(0, 10))

        btn_productos = ttk.Button(
            sidebar,
            text="📦 Productos",
            command=self._mostrar_vista_productos,
        )
        btn_productos.pack(fill="x", pady=5)

        btn_usuarios = ttk.Button(
            sidebar,
            text="👥 Usuarios",
            command=self._mostrar_vista_usuarios,
        )
        btn_usuarios.pack(fill="x", pady=5)

        btn_logout = ttk.Button(
            sidebar,
            text="🚪 Cerrar sesión",
            command=self._cerrar_sesion,
        )
        btn_logout.pack(fill="x", pady=5, side="bottom")

        # Contenedor derecho para el contenido dinámico
        self.contenedor_derecho = ttk.Frame(main_content)
        self.contenedor_derecho.pack(side="right", fill="both", expand=True)

        # Mostrar productos por defecto
        self._mostrar_vista_productos()

    def _limpiar_contenedor_derecho(self) -> None:
        """Elimina todos los widgets del contenedor derecho."""
        for widget in self.contenedor_derecho.winfo_children():
            widget.destroy()

    def _mostrar_vista_usuarios(self) -> None:
        """Mostrar la vista de gestión de usuarios."""
        self._limpiar_contenedor_derecho()

        titulo = ttk.Label(
            self.contenedor_derecho,
            text="Consulta de Usuarios",
            font=("Arial", 14, "bold")
        )
        titulo.pack(pady=10)

        # Treeview para mostrar usuarios
        tree_frame = ttk.Frame(self.contenedor_derecho)
        tree_frame.pack(fill="both", expand=True, padx=5, pady=5)

        tree = ttk.Treeview(
            tree_frame,
            columns=("ID", "Nombre", "Correo"),
            show="headings"
        )
        tree.heading("ID", text="Identificación")
        tree.heading("Nombre", text="Nombre")
        tree.heading("Correo", text="Correo")

        tree.column("ID", width=120)
        tree.column("Nombre", width=200)
        tree.column("Correo", width=200)

        tree.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side="right", fill="y")
        tree.configure(yscrollcommand=scrollbar.set)

        # Cargar datos
        for u in self.servicio.listar_usuarios():
            tree.insert("", "end", values=(u.identificacion, u.nombre, u.correo))

    def _mostrar_vista_productos(self) -> None:
        """Mostrar la vista de gestión de productos."""
        self._limpiar_contenedor_derecho()

        titulo = ttk.Label(
            self.contenedor_derecho,
            text="Gestión de Productos",
            font=("Arial", 14, "bold")
        )
        titulo.pack(pady=10)

        # Formulario
        form_frame = ttk.LabelFrame(
            self.contenedor_derecho,
            text="Datos del Producto",
            padding="10"
        )
        form_frame.pack(fill="x", padx=5, pady=5)

        # Variables de control del formulario
        self.var_codigo = tk.StringVar()
        self.var_nombre = tk.StringVar()
        self.var_categoria = tk.StringVar()
        self.var_precio = tk.StringVar()
        self.var_stock = tk.StringVar()

        # Grid para el formulario
        ttk.Label(form_frame, text="Código:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        ttk.Entry(form_frame, textvariable=self.var_codigo).grid(row=0, column=1, padx=5, pady=5, sticky="we")

        ttk.Label(form_frame, text="Nombre:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        ttk.Entry(form_frame, textvariable=self.var_nombre).grid(row=0, column=3, padx=5, pady=5, sticky="we")

        ttk.Label(form_frame, text="Categoría:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        ttk.Combobox(
            form_frame,
            textvariable=self.var_categoria,
            values=["Plato Principal", "Bebida", "Postre", "Entrada"],
            state="normal"
        ).grid(row=1, column=1, padx=5, pady=5, sticky="we")

        ttk.Label(form_frame, text="Precio:").grid(row=1, column=2, padx=5, pady=5, sticky="e")
        ttk.Entry(form_frame, textvariable=self.var_precio).grid(row=1, column=3, padx=5, pady=5, sticky="we")

        ttk.Label(form_frame, text="Stock:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        ttk.Entry(form_frame, textvariable=self.var_stock).grid(row=2, column=1, padx=5, pady=5, sticky="we")

        form_frame.columnconfigure(1, weight=1)
        form_frame.columnconfigure(3, weight=1)

        # Botones de acción
        action_frame = ttk.Frame(self.contenedor_derecho)
        action_frame.pack(fill="x", padx=5, pady=5)

        ttk.Button(action_frame, text="Registrar", command=self._registrar_producto).pack(side="left", padx=5)
        ttk.Button(action_frame, text="Consultar/Cargar", command=self._cargar_producto).pack(side="left", padx=5)
        ttk.Button(action_frame, text="Actualizar", command=self._actualizar_producto).pack(side="left", padx=5)
        ttk.Button(action_frame, text="Eliminar", command=self._eliminar_producto).pack(side="left", padx=5)
        ttk.Button(action_frame, text="Limpiar Formulario", command=self._limpiar_formulario).pack(side="right", padx=5)

        # Treeview para mostrar productos
        list_frame = ttk.LabelFrame(self.contenedor_derecho, text="Lista de Productos", padding="10")
        list_frame.pack(fill="both", expand=True, padx=5, pady=5)

        self.tree_productos = ttk.Treeview(
            list_frame,
            columns=("Codigo", "Nombre", "Categoria", "Precio", "Stock"),
            show="headings"
        )
        self.tree_productos.heading("Codigo", text="Código")
        self.tree_productos.heading("Nombre", text="Nombre")
        self.tree_productos.heading("Categoria", text="Categoría")
        self.tree_productos.heading("Precio", text="Precio")
        self.tree_productos.heading("Stock", text="Stock")

        self.tree_productos.column("Codigo", width=80)
        self.tree_productos.column("Nombre", width=150)
        self.tree_productos.column("Categoria", width=100)
        self.tree_productos.column("Precio", width=80)
        self.tree_productos.column("Stock", width=80)

        self.tree_productos.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.tree_productos.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree_productos.configure(yscrollcommand=scrollbar.set)

        self._actualizar_lista_productos()

    def _actualizar_lista_productos(self) -> None:
        """Actualizar el Treeview con la lista de productos actual."""
        for item in self.tree_productos.get_children():
            self.tree_productos.delete(item)

        productos = self.servicio.listar_productos()
        for p in productos:
            self.tree_productos.insert(
                "",
                "end",
                values=(p.codigo, p.nombre, p.categoria, f"${p.precio:.2f}", p.stock)
            )

    def _limpiar_formulario(self) -> None:
        """Limpiar los campos del formulario de productos."""
        self.var_codigo.set("")
        self.var_nombre.set("")
        self.var_categoria.set("")
        self.var_precio.set("")
        self.var_stock.set("")

    def _registrar_producto(self) -> None:
        """Manejar el registro de un nuevo producto."""
        try:
            codigo = self.var_codigo.get().strip()
            nombre = self.var_nombre.get().strip()
            categoria = self.var_categoria.get().strip()
            precio_str = self.var_precio.get().strip()
            stock_str = self.var_stock.get().strip()

            if not codigo or not nombre or not categoria or not precio_str or not stock_str:
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return

            precio = float(precio_str)
            stock = int(stock_str)

            exito = self.servicio.registrar_producto(codigo, nombre, categoria, precio, stock)
            if exito:
                messagebox.showinfo("Éxito", "Producto registrado correctamente.")
                self._actualizar_lista_productos()
                self._limpiar_formulario()
            else:
                messagebox.showerror("Error", "Ya existe un producto con ese código.")

        except ValueError:
            messagebox.showerror("Error", "Precio debe ser un número y Stock un entero.")

    def _cargar_producto(self) -> None:
        """Cargar los datos de un producto en el formulario para su consulta o edición."""
        codigo = self.var_codigo.get().strip()
        if not codigo:
            messagebox.showerror("Error", "Ingrese el código del producto a consultar.")
            return

        producto = self.servicio.buscar_producto(codigo)
        if producto:
            self.var_nombre.set(producto.nombre)
            self.var_categoria.set(producto.categoria)
            self.var_precio.set(str(producto.precio))
            self.var_stock.set(str(producto.stock))
            messagebox.showinfo("Información", "Producto cargado en el formulario.")
        else:
            messagebox.showerror("Error", "No se encontró un producto con ese código.")

    def _actualizar_producto(self) -> None:
        """Manejar la actualización de un producto existente."""
        try:
            codigo = self.var_codigo.get().strip()
            nombre = self.var_nombre.get().strip()
            categoria = self.var_categoria.get().strip()
            precio_str = self.var_precio.get().strip()
            stock_str = self.var_stock.get().strip()

            if not codigo:
                messagebox.showerror("Error", "Ingrese el código del producto a actualizar.")
                return
                
            if not nombre or not categoria or not precio_str or not stock_str:
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return

            precio = float(precio_str)
            stock = int(stock_str)

            exito = self.servicio.actualizar_producto(codigo, nombre, categoria, precio, stock)
            if exito:
                messagebox.showinfo("Éxito", "Producto actualizado correctamente.")
                self._actualizar_lista_productos()
                self._limpiar_formulario()
            else:
                messagebox.showerror("Error", "No se encontró el producto o el código no es válido.")

        except ValueError:
            messagebox.showerror("Error", "Precio debe ser un número y Stock un entero.")

    def _eliminar_producto(self) -> None:
        """Manejar la eliminación de un producto."""
        codigo = self.var_codigo.get().strip()
        if not codigo:
            messagebox.showerror("Error", "Ingrese el código del producto a eliminar.")
            return

        if messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar el producto {codigo}?"):
            exito = self.servicio.eliminar_producto(codigo)
            if exito:
                messagebox.showinfo("Éxito", "Producto eliminado correctamente.")
                self._actualizar_lista_productos()
                self._limpiar_formulario()
            else:
                messagebox.showerror("Error", "No se encontró el producto.")

    def _cerrar_sesion(self) -> None:
        """Cerrar sesión y retornar al login."""
        self.on_logout()
