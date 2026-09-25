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

        # Logo (if exists)
        try:
            from pathlib import Path
            logo_path = Path(__file__).parent.parent / "assets" / "logo.png"
            if logo_path.exists():
                self.logo_img = tk.PhotoImage(file=str(logo_path)).subsample(4, 4) # Adjust size
                logo_label = ttk.Label(header_frame, image=self.logo_img)
                logo_label.pack(side="left", padx=5)
        except Exception as e:
            print("No se pudo cargar el logo:", e)

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

        btn_ventas = ttk.Button(
            sidebar,
            text="🛒 Ventas",
            command=self._mostrar_vista_ventas,
        )
        btn_ventas.pack(fill="x", pady=5)

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
            text="Gestión de Usuarios",
            font=("Arial", 14, "bold")
        )
        titulo.pack(pady=10)

        # Formulario
        form_frame = ttk.LabelFrame(
            self.contenedor_derecho,
            text="Datos del Usuario",
            padding="10"
        )
        form_frame.pack(fill="x", padx=5, pady=5)

        self.var_usuario_id = tk.StringVar()
        self.var_usuario_nombre = tk.StringVar()
        self.var_usuario_correo = tk.StringVar()
        self.var_usuario_pass = tk.StringVar()

        ttk.Label(form_frame, text="Identificación:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        ttk.Entry(form_frame, textvariable=self.var_usuario_id).grid(row=0, column=1, padx=5, pady=5, sticky="we")

        ttk.Label(form_frame, text="Nombre:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        ttk.Entry(form_frame, textvariable=self.var_usuario_nombre).grid(row=0, column=3, padx=5, pady=5, sticky="we")

        ttk.Label(form_frame, text="Correo:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        ttk.Entry(form_frame, textvariable=self.var_usuario_correo).grid(row=1, column=1, padx=5, pady=5, sticky="we")

        ttk.Label(form_frame, text="Contraseña:").grid(row=1, column=2, padx=5, pady=5, sticky="e")
        ttk.Entry(form_frame, textvariable=self.var_usuario_pass, show="*").grid(row=1, column=3, padx=5, pady=5, sticky="we")

        form_frame.columnconfigure(1, weight=1)
        form_frame.columnconfigure(3, weight=1)

        # Botones de acción
        action_frame = ttk.Frame(self.contenedor_derecho)
        action_frame.pack(fill="x", padx=5, pady=5)

        ttk.Button(action_frame, text="Registrar", command=self._registrar_usuario).pack(side="left", padx=5)
        ttk.Button(action_frame, text="Consultar/Cargar", command=self._cargar_usuario).pack(side="left", padx=5)
        ttk.Button(action_frame, text="Actualizar", command=self._actualizar_usuario).pack(side="left", padx=5)
        ttk.Button(action_frame, text="Eliminar", command=self._eliminar_usuario).pack(side="left", padx=5)
        ttk.Button(action_frame, text="Limpiar Formulario", command=self._limpiar_formulario_usuario).pack(side="right", padx=5)

        # Treeview para mostrar usuarios
        tree_frame = ttk.LabelFrame(self.contenedor_derecho, text="Lista de Usuarios", padding="10")
        tree_frame.pack(fill="both", expand=True, padx=5, pady=5)

        self.tree_usuarios = ttk.Treeview(
            tree_frame,
            columns=("ID", "Nombre", "Correo", "Pass"),
            show="headings"
        )
        self.tree_usuarios.heading("ID", text="Identificación")
        self.tree_usuarios.heading("Nombre", text="Nombre Completo")
        self.tree_usuarios.heading("Correo", text="Correo Electrónico")
        self.tree_usuarios.heading("Pass", text="Contraseña (Oculta)")

        self.tree_usuarios.column("ID", width=120)
        self.tree_usuarios.column("Nombre", width=250)
        self.tree_usuarios.column("Correo", width=250)
        self.tree_usuarios.column("Pass", width=100)

        self.tree_usuarios.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree_usuarios.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree_usuarios.configure(yscrollcommand=scrollbar.set)

        self._actualizar_lista_usuarios()

    def _actualizar_lista_usuarios(self) -> None:
        if hasattr(self, 'tree_usuarios'):
            for item in self.tree_usuarios.get_children():
                self.tree_usuarios.delete(item)
            for u in self.servicio.listar_usuarios():
                self.tree_usuarios.insert("", "end", values=(u.identificacion, u.nombre, u.correo, "***"))

    def _limpiar_formulario_usuario(self) -> None:
        self.var_usuario_id.set("")
        self.var_usuario_nombre.set("")
        self.var_usuario_correo.set("")
        self.var_usuario_pass.set("")

    def _registrar_usuario(self) -> None:
        identificacion = self.var_usuario_id.get().strip()
        nombre = self.var_usuario_nombre.get().strip()
        correo = self.var_usuario_correo.get().strip()
        contraseña = self.var_usuario_pass.get().strip()

        if not identificacion or not nombre or not correo or not contraseña:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        exito = self.servicio.registrar_usuario(identificacion, nombre, correo, contraseña)
        if exito:
            messagebox.showinfo("Éxito", "Usuario registrado correctamente.")
            self._actualizar_lista_usuarios()
            self._limpiar_formulario_usuario()
        else:
            messagebox.showerror("Error", "Ya existe un usuario con esa identificación.")

    def _cargar_usuario(self) -> None:
        identificacion = self.var_usuario_id.get().strip()
        if not identificacion:
            messagebox.showerror("Error", "Ingrese la identificación a consultar.")
            return

        usuario = self.servicio.buscar_usuario(identificacion)
        if usuario:
            self.var_usuario_nombre.set(usuario.nombre)
            self.var_usuario_correo.set(usuario.correo)
            self.var_usuario_pass.set("") # No cargar contraseña por seguridad
            messagebox.showinfo("Información", "Usuario cargado.")
        else:
            messagebox.showerror("Error", "No se encontró un usuario con esa identificación.")

    def _actualizar_usuario(self) -> None:
        identificacion = self.var_usuario_id.get().strip()
        nombre = self.var_usuario_nombre.get().strip()
        correo = self.var_usuario_correo.get().strip()
        contraseña = self.var_usuario_pass.get().strip()

        if not identificacion or not nombre or not correo:
            messagebox.showerror("Error", "ID, Nombre y Correo son obligatorios.")
            return

        exito = self.servicio.actualizar_usuario(identificacion, nombre, correo, contraseña)
        if exito:
            messagebox.showinfo("Éxito", "Usuario actualizado correctamente.")
            self._actualizar_lista_usuarios()
            self._limpiar_formulario_usuario()
        else:
            messagebox.showerror("Error", "No se encontró el usuario.")

    def _eliminar_usuario(self) -> None:
        identificacion = self.var_usuario_id.get().strip()
        if not identificacion:
            messagebox.showerror("Error", "Ingrese la identificación a eliminar.")
            return

        if messagebox.askyesno("Confirmar", f"¿Eliminar usuario {identificacion}?"):
            exito = self.servicio.eliminar_usuario(identificacion)
            if exito:
                messagebox.showinfo("Éxito", "Usuario eliminado.")
                self._actualizar_lista_usuarios()
                self._limpiar_formulario_usuario()
            else:
                messagebox.showerror("Error", "No se encontró el usuario.")

    def _mostrar_vista_ventas(self) -> None:
        """Mostrar la vista de gestión de ventas."""
        self._limpiar_contenedor_derecho()

        titulo = ttk.Label(
            self.contenedor_derecho,
            text="Registro de Ventas",
            font=("Arial", 14, "bold")
        )
        titulo.pack(pady=10)

        # Formulario
        form_frame = ttk.LabelFrame(
            self.contenedor_derecho,
            text="Nueva Venta",
            padding="10"
        )
        form_frame.pack(fill="x", padx=5, pady=5)

        # Variables
        self.var_venta_usuario = tk.StringVar()
        self.var_venta_producto = tk.StringVar()
        self.var_venta_cantidad = tk.IntVar(value=1)
        self.var_venta_total = tk.StringVar(value="Total: $0.00")

        # Opciones
        usuarios = [f"{u.identificacion} - {u.nombre}" for u in self.servicio.listar_usuarios()]
        self.productos_activos = [p for p in self.servicio.listar_productos() if p.stock > 0]
        productos = [f"{p.codigo} - {p.nombre} (Stock: {p.stock} | ${p.precio:.2f})" for p in self.productos_activos]

        ttk.Label(form_frame, text="Usuario:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.cb_usuarios = ttk.Combobox(form_frame, textvariable=self.var_venta_usuario, values=usuarios, state="readonly", width=40)
        self.cb_usuarios.grid(row=0, column=1, padx=5, pady=5, sticky="we")

        ttk.Label(form_frame, text="Producto:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.cb_productos = ttk.Combobox(form_frame, textvariable=self.var_venta_producto, values=productos, state="readonly", width=40)
        self.cb_productos.grid(row=1, column=1, padx=5, pady=5, sticky="we")
        self.cb_productos.bind("<<ComboboxSelected>>", self._calcular_total_venta)

        ttk.Label(form_frame, text="Cantidad:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        spinbox_cantidad = ttk.Spinbox(form_frame, from_=1, to=999, textvariable=self.var_venta_cantidad, width=10)
        spinbox_cantidad.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.var_venta_cantidad.trace_add("write", lambda *args: self._calcular_total_venta())

        lbl_total = ttk.Label(form_frame, textvariable=self.var_venta_total, font=("Arial", 12, "bold"), foreground="green")
        lbl_total.grid(row=3, column=0, columnspan=2, pady=10)

        ttk.Button(form_frame, text="Registrar Venta", command=self._registrar_venta).grid(row=4, column=0, columnspan=2, pady=10)

        # Treeview para mostrar ventas
        list_frame = ttk.LabelFrame(self.contenedor_derecho, text="Historial de Ventas", padding="10")
        list_frame.pack(fill="both", expand=True, padx=5, pady=5)

        self.tree_ventas = ttk.Treeview(
            list_frame,
            columns=("ID", "Usuario", "Producto", "Cantidad", "Total", "Fecha"),
            show="headings"
        )
        self.tree_ventas.heading("ID", text="ID Venta")
        self.tree_ventas.heading("Usuario", text="Usuario ID")
        self.tree_ventas.heading("Producto", text="Producto Código")
        self.tree_ventas.heading("Cantidad", text="Cantidad")
        self.tree_ventas.heading("Total", text="Total")
        self.tree_ventas.heading("Fecha", text="Fecha")

        self.tree_ventas.column("ID", width=80)
        self.tree_ventas.column("Usuario", width=100)
        self.tree_ventas.column("Producto", width=100)
        self.tree_ventas.column("Cantidad", width=60)
        self.tree_ventas.column("Total", width=80)
        self.tree_ventas.column("Fecha", width=130)

        self.tree_ventas.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.tree_ventas.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree_ventas.configure(yscrollcommand=scrollbar.set)

        self._actualizar_lista_ventas()

    def _calcular_total_venta(self, event=None) -> None:
        producto_seleccion = self.var_venta_producto.get()
        try:
            cantidad = self.var_venta_cantidad.get()
        except tk.TclError:
            cantidad = 0
            
        if producto_seleccion and cantidad > 0:
            producto_codigo = producto_seleccion.split(" - ")[0]
            for p in self.productos_activos:
                if p.codigo == producto_codigo:
                    total = p.precio * cantidad
                    self.var_venta_total.set(f"Total: ${total:.2f}")
                    return
        self.var_venta_total.set("Total: $0.00")

    def _actualizar_lista_ventas(self) -> None:
        """Actualizar el Treeview con la lista de ventas actual."""
        if hasattr(self, 'tree_ventas'):
            for item in self.tree_ventas.get_children():
                self.tree_ventas.delete(item)

            for v in self.servicio.listar_ventas():
                # Formatear fecha para que sea más legible
                fecha_formato = v.fecha[:19].replace('T', ' ') if 'T' in v.fecha else v.fecha
                cantidad = getattr(v, 'cantidad', 1)
                total = getattr(v, 'total', 0.0)
                self.tree_ventas.insert(
                    "",
                    "end",
                    values=(v.id_venta[:8] + "...", v.usuario_identificacion, v.producto_codigo, cantidad, f"${total:.2f}", fecha_formato)
                )

    def _registrar_venta(self) -> None:
        """Manejar el registro de una nueva venta (Callback)."""
        usuario_seleccion = self.var_venta_usuario.get()
        producto_seleccion = self.var_venta_producto.get()
        try:
            cantidad = self.var_venta_cantidad.get()
        except tk.TclError:
            cantidad = 0

        if not usuario_seleccion or not producto_seleccion or cantidad <= 0:
            messagebox.showerror("Error", "Debe seleccionar un usuario, un producto y una cantidad mayor a 0.")
            return

        usuario_id = usuario_seleccion.split(" - ")[0]
        producto_codigo = producto_seleccion.split(" - ")[0]

        exito = self.servicio.registrar_venta(usuario_id, producto_codigo, cantidad)
        if exito:
            messagebox.showinfo("Éxito", "Venta registrada correctamente.")
            self._actualizar_lista_ventas()
            self.var_venta_producto.set("")
            self.var_venta_cantidad.set(1)
            self._calcular_total_venta()
            # Actualizar opciones de productos por si se quedaron sin stock
            self.productos_activos = [p for p in self.servicio.listar_productos() if p.stock > 0]
            productos = [f"{p.codigo} - {p.nombre} (Stock: {p.stock} | ${p.precio:.2f})" for p in self.productos_activos]
            self.cb_productos['values'] = productos
        else:
            messagebox.showerror("Error", "No se pudo registrar la venta (usuario o producto no válido, o sin stock suficiente).")

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
