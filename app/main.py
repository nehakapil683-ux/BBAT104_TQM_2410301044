import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

import customtkinter as ctk

from database.db import (
    initialize_database,
    insert_sample_menu_data,

    add_menu_item,
    get_menu_items,
    get_menu_item,
    update_menu_item,
    delete_menu_item,

    add_customer,
    get_customers,
    get_customer_count,

    create_order,
    get_orders,
    get_order,
    get_order_items,

    get_dashboard_data,

    get_sales_report,
    get_sales_report_count,

    get_database_indexes,
    get_search_query_plan,
)


# ============================================================
# APPLICATION SETTINGS
# ============================================================

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


# ============================================================
# MAIN APPLICATION
# ============================================================

class RestaurantBillingApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Restaurant Billing System - Q05")
        self.geometry("1450x900")
        self.minsize(1150, 750)

        # ----------------------------------------------------
        # ORDER CART
        # ----------------------------------------------------

        self.current_order_items = []

        # ----------------------------------------------------
        # DASHBOARD CACHE
        # ----------------------------------------------------

        self.dashboard_cache = None
        self.dashboard_cache_time = None

        # ----------------------------------------------------
        # DATABASE
        # ----------------------------------------------------

        initialize_database()
        insert_sample_menu_data()

        # ----------------------------------------------------
        # WINDOW CONFIGURATION
        # ----------------------------------------------------

        self.configure(fg_color="#F5F7FA")

        self.create_header()
        self.create_navigation()
        self.create_content_area()

        self.show_dashboard()

    # ========================================================
    # HEADER
    # ========================================================

    def create_header(self):

        header = ctk.CTkFrame(
            self,
            height=110,
            corner_radius=0,
            fg_color="#172033"
        )

        header.pack(
            fill="x",
            side="top"
        )

        header.pack_propagate(False)

        title = ctk.CTkLabel(
            header,
            text="Restaurant Billing System",
            font=ctk.CTkFont(
                family="Arial",
                size=30,
                weight="bold"
            ),
            text_color="white"
        )

        title.pack(
            pady=(18, 2)
        )

        subtitle = ctk.CTkLabel(
            header,
            text="Q05 • Reduce Response Time",
            font=ctk.CTkFont(
                family="Arial",
                size=15
            ),
            text_color="#D8DEE9"
        )

        subtitle.pack()

    # ========================================================
    # NAVIGATION
    # ========================================================

    def create_navigation(self):

        navigation = ctk.CTkFrame(
            self,
            height=65,
            corner_radius=0,
            fg_color="#101827"
        )

        navigation.pack(
            fill="x",
            side="top"
        )

        navigation.pack_propagate(False)

        buttons = [
            ("Dashboard", self.show_dashboard),
            ("Menu", self.show_menu),
            ("Customers", self.show_customers),
            ("New Order", self.show_new_order),
            ("Order History", self.show_order_history),
            ("Reports", self.show_reports),
            ("Q05 Performance", self.show_performance),
        ]

        for text, command in buttons:

            button = ctk.CTkButton(
                navigation,
                text=text,
                command=command,
                width=145,
                height=40,
                corner_radius=6,
                font=ctk.CTkFont(
                    size=14,
                    weight="bold"
                ),
                fg_color="#25344D",
                hover_color="#355173",
                text_color="white"
            )

            button.pack(
                side="left",
                padx=7,
                pady=12
            )

    # ========================================================
    # CONTENT AREA
    # ========================================================

    def create_content_area(self):

        self.content = ctk.CTkScrollableFrame(
            self,
            corner_radius=0,
            fg_color="#F5F7FA",
            scrollbar_button_color="#94A3B8",
            scrollbar_button_hover_color="#64748B"
        )

        self.content.pack(
            fill="both",
            expand=True
        )
    # ========================================================
    # CLEAR CONTENT
    # ========================================================

    def clear_content(self):

        for widget in self.content.winfo_children():
            widget.destroy()

    # ========================================================
    # PAGE TITLE
    # ========================================================

    def create_page_title(
        self,
        title,
        subtitle=""
    ):

        title_label = ctk.CTkLabel(
            self.content,
            text=title,
            font=ctk.CTkFont(
                family="Arial",
                size=27,
                weight="bold"
            ),
            text_color="#172033"
        )

        title_label.pack(
            anchor="w",
            padx=35,
            pady=(28, 2)
        )

        if subtitle:

            subtitle_label = ctk.CTkLabel(
                self.content,
                text=subtitle,
                font=ctk.CTkFont(
                    family="Arial",
                    size=14
                ),
                text_color="#64748B"
            )

            subtitle_label.pack(
                anchor="w",
                padx=35,
                pady=(0, 18)
            )

    # ========================================================
    # DASHBOARD
    # ========================================================

    def show_dashboard(self):

        self.clear_content()

        self.create_page_title(
            "Dashboard",
            "Quick overview of restaurant billing operations"
        )

       # ----------------------------------------------------
       # CACHE CHECK
       # ----------------------------------------------------

        if self.dashboard_cache is None:
            self.dashboard_cache = get_dashboard_data()
            self.dashboard_cache_time = datetime.now().strftime(
                "%H:%M:%S"
            )

        data = self.dashboard_cache

        # ----------------------------------------------------
        # STATISTICS GRID
        # ----------------------------------------------------

        stats_frame = ctk.CTkFrame(
            self.content,
            fg_color="transparent"
        )

        stats_frame.pack(
            fill="x",
            padx=35,
            pady=5
        )

        for column in range(3):
            stats_frame.grid_columnconfigure(
                column,
                weight=1
            )

        self.create_stat_card(
            stats_frame,
            "Menu Items",
            str(data["menu_count"]),
            0,
            0
        )

        self.create_stat_card(
            stats_frame,
            "Customers",
            str(data["customer_count"]),
            0,
            1
        )

        self.create_stat_card(
            stats_frame,
            "Total Orders",
            str(data["order_count"]),
            0,
            2
        )

        self.create_stat_card(
            stats_frame,
            "Total Sales",
            f"₹{data['total_sales']:,.2f}",
            1,
            0
        )

        self.create_stat_card(
            stats_frame,
            "Today's Orders",
            str(data["today_orders"]),
            1,
            1
        )

        self.create_stat_card(
            stats_frame,
            "Today's Sales",
            f"₹{data['today_sales']:,.2f}",
            1,
            2
        )

        # ----------------------------------------------------
        # CACHE INFORMATION
        # ----------------------------------------------------

        cache_frame = ctk.CTkFrame(
            self.content,
            height=65,
            fg_color="#E7EBF1",
            corner_radius=8
        )

        cache_frame.pack(
            fill="x",
            padx=35,
            pady=(30, 10)
        )

        cache_frame.pack_propagate(False)

        cache_time = self.dashboard_cache_time or "-"

        cache_label = ctk.CTkLabel(
            cache_frame,
            text=(
                "Dashboard data loaded from cache"
                f" • Last refresh: {cache_time}"
            ),
            font=ctk.CTkFont(
                size=14
            ),
            text_color="#334155"
        )

        cache_label.pack(
            side="left",
            padx=20
        )

        refresh_button = ctk.CTkButton(
            cache_frame,
            text="Refresh Dashboard",
            width=150,
            height=38,
            command=self.refresh_dashboard_cache
        )

        refresh_button.pack(
            side="right",
            padx=15,
            pady=13
        )

    # ========================================================
    # STAT CARD
    # ========================================================
    
    def create_stat_card(
        self,
        parent,
        label,
        value,
        row,
        column
    ):
        card = ctk.CTkFrame(
            parent,
            height=120,
            corner_radius=8,
            fg_color="white",
            border_width=1,
            border_color="#CBD5E1"
        )

        card.grid(
            row=row,
            column=column,
            sticky="nsew",
            padx=8,
            pady=8
        )

        card.grid_propagate(False)

        label_widget = ctk.CTkLabel(
            card,
            text=label,
            font=ctk.CTkFont(
                size=14,
                weight="bold"
            ),
            text_color="#64748B"
        )

        label_widget.pack(
            pady=(18, 2)
        )

        value_widget = ctk.CTkLabel(
            card,
            text=value,
            font=ctk.CTkFont(
                size=24,
                weight="bold"
            ),
            text_color="#172033"
        )

        value_widget.pack(
            pady=(2, 12)
        )

    # ========================================================
    # DASHBOARD CACHE
    # ========================================================

    def refresh_dashboard_cache(self):

        self.dashboard_cache = get_dashboard_data()

        self.dashboard_cache_time = datetime.now().strftime(
            "%H:%M:%S"
        )

        self.show_dashboard()

    # ========================================================
    # MENU PAGE
    # ========================================================

    def show_menu(self):

        self.clear_content()

        self.create_page_title(
            "Menu Management",
            "Add, update, delete and quickly search menu items"
        )

        # ----------------------------------------------------
        # FORM
        # ----------------------------------------------------

        form = ctk.CTkFrame(
            self.content,
            fg_color="white",
            corner_radius=8,
            border_width=1,
            border_color="#CBD5E1"
        )

        form.pack(
            fill="x",
            padx=35,
            pady=5
        )

        form.grid_columnconfigure(1, weight=1)
        form.grid_columnconfigure(3, weight=1)

        ctk.CTkLabel(
            form,
            text="Item Name",
            font=ctk.CTkFont(
                size=14,
                weight="bold"
            ),
            text_color="#334155"
        ).grid(
            row=0,
            column=0,
            padx=15,
            pady=(18, 8),
            sticky="w"
        )

        self.menu_name_entry = ctk.CTkEntry(
            form,
            height=38,
            placeholder_text="Enter item name"
        )

        self.menu_name_entry.grid(
            row=0,
            column=1,
            padx=10,
            pady=(18, 8),
            sticky="ew"
        )

        ctk.CTkLabel(
            form,
            text="Category",
            font=ctk.CTkFont(
                size=14,
                weight="bold"
            ),
            text_color="#334155"
        ).grid(
            row=0,
            column=2,
            padx=15,
            pady=(18, 8),
            sticky="w"
        )

        self.menu_category_entry = ctk.CTkEntry(
            form,
            height=38,
            placeholder_text="e.g. Pizza"
        )

        self.menu_category_entry.grid(
            row=0,
            column=3,
            padx=10,
            pady=(18, 8),
            sticky="ew"
        )

        ctk.CTkLabel(
            form,
            text="Price",
            font=ctk.CTkFont(
                size=14,
                weight="bold"
            ),
            text_color="#334155"
        ).grid(
            row=1,
            column=0,
            padx=15,
            pady=8,
            sticky="w"
        )

        self.menu_price_entry = ctk.CTkEntry(
            form,
            height=38,
            placeholder_text="Enter price"
        )

        self.menu_price_entry.grid(
            row=1,
            column=1,
            padx=10,
            pady=8,
            sticky="ew"
        )

        ctk.CTkLabel(
            form,
            text="Availability",
            font=ctk.CTkFont(
                size=14,
                weight="bold"
            ),
            text_color="#334155"
        ).grid(
            row=1,
            column=2,
            padx=15,
            pady=8,
            sticky="w"
        )

        self.menu_available = ctk.CTkComboBox(
            form,
            values=["Available", "Not Available"],
            height=38
        )

        self.menu_available.set("Available")

        self.menu_available.grid(
            row=1,
            column=3,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # ----------------------------------------------------
        # BUTTONS
        # ----------------------------------------------------

        button_frame = ctk.CTkFrame(
            form,
            fg_color="transparent"
        )

        button_frame.grid(
            row=2,
            column=0,
            columnspan=4,
            pady=(10, 18)
        )

        ctk.CTkButton(
            button_frame,
            text="Add Item",
            width=120,
            command=self.add_menu
        ).pack(
            side="left",
            padx=5
        )

        ctk.CTkButton(
            button_frame,
            text="Update",
            width=120,
            command=self.update_menu
        ).pack(
            side="left",
            padx=5
        )

        ctk.CTkButton(
            button_frame,
            text="Delete",
            width=120,
            fg_color="#DC2626",
            hover_color="#B91C1C",
            command=self.delete_menu
        ).pack(
            side="left",
            padx=5
        )

        ctk.CTkButton(
            button_frame,
            text="Clear",
            width=120,
            fg_color="#64748B",
            hover_color="#475569",
            command=self.clear_menu_form
        ).pack(
            side="left",
            padx=5
        )

        # ----------------------------------------------------
        # FAST SEARCH
        # ----------------------------------------------------

        search_frame = ctk.CTkFrame(
            self.content,
            fg_color="transparent"
        )

        search_frame.pack(
            fill="x",
            padx=35,
            pady=(18, 8)
        )

        ctk.CTkLabel(
            search_frame,
            text="Fast Search:",
            font=ctk.CTkFont(
                size=14,
                weight="bold"
            ),
            text_color="#334155"
        ).pack(
            side="left",
            padx=(0, 10)
        )

        self.menu_search = ctk.CTkEntry(
            search_frame,
            height=38,
            placeholder_text="Search by item name or category..."
        )

        self.menu_search.pack(
            side="left",
            fill="x",
            expand=True
        )

        self.menu_search.bind(
            "<KeyRelease>",
            self.search_menu
        )

        # ----------------------------------------------------
        # TABLE
        # ----------------------------------------------------

        table_frame = ctk.CTkFrame(
            self.content,
            fg_color="white",
            corner_radius=8
        )

        table_frame.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=(5, 25)
        )

        columns = (
            "id",
            "name",
            "category",
            "price",
            "available"
        )

        self.menu_tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=12
        )

        headings = {
            "id": "ID",
            "name": "Item Name",
            "category": "Category",
            "price": "Price",
            "available": "Availability"
        }

        widths = {
            "id": 70,
            "name": 300,
            "category": 220,
            "price": 150,
            "available": 180
        }

        for column in columns:

            self.menu_tree.heading(
                column,
                text=headings[column]
            )

            self.menu_tree.column(
                column,
                width=widths[column],
                anchor="center"
            )

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.menu_tree.yview
        )

        self.menu_tree.configure(
            yscrollcommand=scrollbar.set
        )

        self.menu_tree.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(10, 0),
            pady=10
        )

        scrollbar.pack(
            side="right",
            fill="y",
            padx=(0, 10),
            pady=10
        )

        self.menu_tree.bind(
            "<<TreeviewSelect>>",
            self.select_menu
        )

        self.load_menu_table()

    # ========================================================
    # LOAD MENU TABLE
    # ========================================================

    def load_menu_table(self, search=""):

        if not hasattr(self, "menu_tree"):
            return

        for item in self.menu_tree.get_children():
            self.menu_tree.delete(item)

        rows = get_menu_items(search)

        for row in rows:

            availability = (
                "Available"
                if row["available"]
                else "Not Available"
            )

            self.menu_tree.insert(
                "",
                "end",
                values=(
                    row["id"],
                    row["name"],
                    row["category"],
                    f"₹{row['price']:,.2f}",
                    availability
                )
            )

    # ========================================================
    # MENU SEARCH
    # ========================================================

    def search_menu(self, event=None):

        search_text = self.menu_search.get()

        self.load_menu_table(search_text)

    # ========================================================
    # SELECT MENU
    # ========================================================

    def select_menu(self, event=None):

        selected = self.menu_tree.selection()

        if not selected:
            return

        values = self.menu_tree.item(
            selected[0],
            "values"
        )

        self.menu_name_entry.delete(0, "end")
        self.menu_name_entry.insert(
            0,
            values[1]
        )

        self.menu_category_entry.delete(0, "end")
        self.menu_category_entry.insert(
            0,
            values[2]
        )

        self.menu_price_entry.delete(0, "end")
        self.menu_price_entry.insert(
            0,
            values[3].replace("₹", "").replace(",", "")
        )

        self.menu_available.set(
            values[4]
        )

        self.selected_menu_id = int(
            values[0]
        )

    # ========================================================
    # ADD MENU
    # ========================================================

    def add_menu(self):

        name = self.menu_name_entry.get().strip()
        category = self.menu_category_entry.get().strip()
        price_text = self.menu_price_entry.get().strip()

        if not name:
            messagebox.showwarning(
                "Validation",
                "Please enter item name."
            )
            return

        if not category:
            messagebox.showwarning(
                "Validation",
                "Please enter category."
            )
            return

        try:
            price = float(price_text)

            if price < 0:
                raise ValueError

        except ValueError:

            messagebox.showwarning(
                "Validation",
                "Please enter a valid price."
            )
            return

        available = (
            1
            if self.menu_available.get() == "Available"
            else 0
        )

        try:

            add_menu_item(
                name,
                category,
                price,
                available
            )

            messagebox.showinfo(
                "Success",
                "Menu item added successfully."
            )

            self.clear_menu_form()
            self.load_menu_table()

            self.dashboard_cache = None

        except Exception as error:

            messagebox.showerror(
                "Database Error",
                str(error)
            )

    # ========================================================
    # UPDATE MENU
    # ========================================================

    def update_menu(self):

        if not hasattr(self, "selected_menu_id"):

            messagebox.showwarning(
                "Selection Required",
                "Please select a menu item first."
            )

            return

        name = self.menu_name_entry.get().strip()
        category = self.menu_category_entry.get().strip()
        price_text = self.menu_price_entry.get().strip()

        if not name or not category:

            messagebox.showwarning(
                "Validation",
                "Name and category are required."
            )

            return

        try:
            price = float(price_text)

            if price < 0:
                raise ValueError

        except ValueError:

            messagebox.showwarning(
                "Validation",
                "Please enter a valid price."
            )

            return

        available = (
            1
            if self.menu_available.get() == "Available"
            else 0
        )

        try:

            update_menu_item(
                self.selected_menu_id,
                name,
                category,
                price,
                available
            )

            messagebox.showinfo(
                "Success",
                "Menu item updated successfully."
            )

            self.clear_menu_form()
            self.load_menu_table()

        except Exception as error:

            messagebox.showerror(
                "Database Error",
                str(error)
            )

    # ========================================================
    # DELETE MENU
    # ========================================================

    def delete_menu(self):

        if not hasattr(self, "selected_menu_id"):

            messagebox.showwarning(
                "Selection Required",
                "Please select a menu item first."
            )

            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this menu item?"
        )

        if not confirm:
            return

        try:

            delete_menu_item(
                self.selected_menu_id
            )

            messagebox.showinfo(
                "Success",
                "Menu item deleted successfully."
            )

            self.clear_menu_form()
            self.load_menu_table()

            self.dashboard_cache = None

        except Exception as error:

            messagebox.showerror(
                "Delete Error",
                str(error)
            )

    # ========================================================
    # CLEAR MENU FORM
    # ========================================================

    def clear_menu_form(self):

        self.menu_name_entry.delete(0, "end")
        self.menu_category_entry.delete(0, "end")
        self.menu_price_entry.delete(0, "end")
        self.menu_available.set("Available")

        if hasattr(self, "selected_menu_id"):
            del self.selected_menu_id

    # ========================================================
    # CUSTOMERS
    # ========================================================

    def show_customers(self):

        self.clear_content()

        self.create_page_title(
            "Customers",
            "Manage customer information"
        )

        form = ctk.CTkFrame(
            self.content,
            fg_color="white",
            corner_radius=8,
            border_width=1,
            border_color="#CBD5E1"
        )

        form.pack(
            fill="x",
            padx=35,
            pady=5
        )

        ctk.CTkLabel(
            form,
            text="Customer Name",
            font=ctk.CTkFont(
                size=14,
                weight="bold"
            ),
            text_color="#334155"
        ).pack(
            side="left",
            padx=(20, 8),
            pady=20
        )

        self.customer_name = ctk.CTkEntry(
            form,
            width=280,
            height=38,
            placeholder_text="Enter customer name"
        )

        self.customer_name.pack(
            side="left",
            padx=8
        )

        ctk.CTkLabel(
            form,
            text="Phone",
            font=ctk.CTkFont(
                size=14,
                weight="bold"
            ),
            text_color="#334155"
        ).pack(
            side="left",
            padx=(20, 8)
        )

        self.customer_phone = ctk.CTkEntry(
            form,
            width=220,
            height=38,
            placeholder_text="Enter phone number"
        )

        self.customer_phone.pack(
            side="left",
            padx=8
        )

        ctk.CTkButton(
            form,
            text="Add Customer",
            width=140,
            height=38,
            command=self.add_customer_action
        ).pack(
            side="left",
            padx=15
        )

        # ----------------------------------------------------
        # SEARCH
        # ----------------------------------------------------

        search_frame = ctk.CTkFrame(
            self.content,
            fg_color="transparent"
        )

        search_frame.pack(
            fill="x",
            padx=35,
            pady=(20, 8)
        )

        ctk.CTkLabel(
            search_frame,
            text="Search:",
            font=ctk.CTkFont(
                size=14,
                weight="bold"
            )
        ).pack(
            side="left",
            padx=(0, 10)
        )

        self.customer_search = ctk.CTkEntry(
            search_frame,
            height=38,
            placeholder_text="Search customer..."
        )

        self.customer_search.pack(
            fill="x",
            expand=True
        )

        self.customer_search.bind(
            "<KeyRelease>",
            lambda event: self.load_customers(
                self.customer_search.get()
            )
        )

        # ----------------------------------------------------
        # CUSTOMER TABLE
        # ----------------------------------------------------

        table = ctk.CTkFrame(
            self.content,
            fg_color="white",
            corner_radius=8
        )

        table.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=(5, 25)
        )

        columns = (
            "id",
            "name",
            "phone",
            "created"
        )

        self.customer_tree = ttk.Treeview(
            table,
            columns=columns,
            show="headings"
        )

        headings = {
            "id": "ID",
            "name": "Customer Name",
            "phone": "Phone",
            "created": "Created At"
        }

        for column in columns:

            self.customer_tree.heading(
                column,
                text=headings[column]
            )

            self.customer_tree.column(
                column,
                width=250,
                anchor="center"
            )

        self.customer_tree.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.load_customers()

    # ========================================================
    # ADD CUSTOMER
    # ========================================================

    def add_customer_action(self):

        name = self.customer_name.get().strip()
        phone = self.customer_phone.get().strip()

        if not name:

            messagebox.showwarning(
                "Validation",
                "Customer name is required."
            )

            return

        try:

            add_customer(
                name,
                phone
            )

            messagebox.showinfo(
                "Success",
                "Customer added successfully."
            )

            self.customer_name.delete(0, "end")
            self.customer_phone.delete(0, "end")

            self.load_customers()

            self.dashboard_cache = None

        except Exception as error:

            messagebox.showerror(
                "Database Error",
                str(error)
            )

    # ========================================================
    # LOAD CUSTOMERS
    # ========================================================

    def load_customers(self, search=""):

        for item in self.customer_tree.get_children():
            self.customer_tree.delete(item)

        customers = get_customers(search)

        for customer in customers:

            self.customer_tree.insert(
                "",
                "end",
                values=(
                    customer["id"],
                    customer["name"],
                    customer["phone"] or "",
                    customer["created_at"]
                )
            )

    # ========================================================
    # NEW ORDER
    # ========================================================

    def show_new_order(self):

        self.clear_content()

        self.current_order_items = []

        self.create_page_title(
            "New Order",
            "Select customer and add menu items to create a bill"
        )

        # ----------------------------------------------------
        # CUSTOMER SECTION
        # ----------------------------------------------------

        customer_frame = ctk.CTkFrame(
            self.content,
            fg_color="white",
            corner_radius=8,
            border_width=1,
            border_color="#CBD5E1"
        )

        customer_frame.pack(
            fill="x",
            padx=35,
            pady=5
        )

        ctk.CTkLabel(
            customer_frame,
            text="Customer",
            font=ctk.CTkFont(
                size=14,
                weight="bold"
            ),
            text_color="#334155"
        ).pack(
            side="left",
            padx=(20, 10),
            pady=18
        )

        customers = get_customers()

        self.order_customer_map = {
            "Walk-in Customer": None
        }

        customer_values = [
            "Walk-in Customer"
        ]

        for customer in customers:

            display = (
                f"{customer['name']} "
                f"({customer['phone'] or 'No phone'})"
            )

            customer_values.append(display)

            self.order_customer_map[
                display
            ] = customer["id"]

        self.order_customer = ctk.CTkComboBox(
            customer_frame,
            values=customer_values,
            width=350,
            height=38
        )

        self.order_customer.set(
            "Walk-in Customer"
        )

        self.order_customer.pack(
            side="left",
            padx=10
        )

        # ----------------------------------------------------
        # ITEM SECTION
        # ----------------------------------------------------

        item_frame = ctk.CTkFrame(
            self.content,
            fg_color="white",
            corner_radius=8,
            border_width=1,
            border_color="#CBD5E1"
        )

        item_frame.pack(
            fill="x",
            padx=35,
            pady=(18, 5)
        )

        ctk.CTkLabel(
            item_frame,
            text="Menu Item",
            font=ctk.CTkFont(
                size=14,
                weight="bold"
            ),
            text_color="#334155"
        ).pack(
            side="left",
            padx=(20, 10),
            pady=18
        )

        menu_items = get_available_menu_items_safe()

        self.order_menu_map = {}

        menu_values = []

        for item in menu_items:

            display = (
                f"{item['name']} "
                f"• ₹{item['price']:,.2f}"
            )

            menu_values.append(display)

            self.order_menu_map[
                display
            ] = item

        self.order_menu = ctk.CTkComboBox(
            item_frame,
            values=menu_values or ["No menu items"],
            width=360,
            height=38
        )

        if menu_values:
            self.order_menu.set(menu_values[0])

        item_frame.pack_propagate(False)

        self.order_menu.pack(
            side="left",
            padx=10
        )

        ctk.CTkLabel(
            item_frame,
            text="Quantity",
            font=ctk.CTkFont(
                size=14,
                weight="bold"
            ),
            text_color="#334155"
        ).pack(
            side="left",
            padx=(20, 8)
        )

        self.order_quantity = ctk.CTkEntry(
            item_frame,
            width=100,
            height=38
        )

        self.order_quantity.insert(
            0,
            "1"
        )

        self.order_quantity.pack(
            side="left",
            padx=8
        )

        ctk.CTkButton(
            item_frame,
            text="Add to Order",
            width=140,
            height=38,
            command=self.add_order_item
        ).pack(
            side="left",
            padx=15
        )

        # ----------------------------------------------------
        # ORDER TABLE
        # ----------------------------------------------------

        table_frame = ctk.CTkFrame(
            self.content,
            fg_color="white",
            corner_radius=8
        )

        table_frame.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=(18, 10)
        )

        columns = (
            "item",
            "quantity",
            "price",
            "subtotal"
        )

        self.order_tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        headings = {
            "item": "Item",
            "quantity": "Quantity",
            "price": "Price",
            "subtotal": "Subtotal"
        }

        for column in columns:

            self.order_tree.heading(
                column,
                text=headings[column]
            )

            self.order_tree.column(
                column,
                width=250,
                anchor="center"
            )

        self.order_tree.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        # ----------------------------------------------------
        # TOTAL / BILL
        # ----------------------------------------------------

        bottom = ctk.CTkFrame(
            self.content,
            fg_color="transparent"
        )

        bottom.pack(
            fill="x",
            padx=35,
            pady=(5, 25)
        )

        self.order_total_label = ctk.CTkLabel(
            bottom,
            text="Total: ₹0.00",
            font=ctk.CTkFont(
                size=22,
                weight="bold"
            ),
            text_color="#172033"
        )

        self.order_total_label.pack(
            side="left"
        )

        ctk.CTkButton(
            bottom,
            text="Generate Bill",
            width=180,
            height=45,
            font=ctk.CTkFont(
                size=15,
                weight="bold"
            ),
            command=self.generate_bill
        ).pack(
            side="right"
        )

        ctk.CTkButton(
            bottom,
            text="Remove Selected",
            width=160,
            height=45,
            fg_color="#DC2626",
            hover_color="#B91C1C",
            command=self.remove_order_item
        ).pack(
            side="right",
            padx=10
        )

    # ========================================================
    # ADD ORDER ITEM
    # ========================================================

    def add_order_item(self):

        selected = self.order_menu.get()

        if selected not in self.order_menu_map:

            messagebox.showwarning(
                "Menu",
                "Please select a valid menu item."
            )

            return

        try:

            quantity = int(
                self.order_quantity.get()
            )

            if quantity <= 0:
                raise ValueError

        except ValueError:

            messagebox.showwarning(
                "Validation",
                "Quantity must be a positive number."
            )

            return

        menu_item = self.order_menu_map[selected]

        subtotal = (
            quantity *
            float(menu_item["price"])
        )

        self.current_order_items.append({
            "menu_item_id": menu_item["id"],
            "name": menu_item["name"],
            "quantity": quantity,
            "price": float(menu_item["price"]),
            "subtotal": subtotal
        })

        self.refresh_order_table()

        self.order_quantity.delete(
            0,
            "end"
        )

        self.order_quantity.insert(
            0,
            "1"
        )

    # ========================================================
    # REFRESH ORDER TABLE
    # ========================================================

    def refresh_order_table(self):

        for item in self.order_tree.get_children():
            self.order_tree.delete(item)

        total = 0

        for item in self.current_order_items:

            total += item["subtotal"]

            self.order_tree.insert(
                "",
                "end",
                values=(
                    item["name"],
                    item["quantity"],
                    f"₹{item['price']:,.2f}",
                    f"₹{item['subtotal']:,.2f}"
                )
            )

        self.order_total_label.configure(
            text=f"Total: ₹{total:,.2f}"
        )

    # ========================================================
    # REMOVE ORDER ITEM
    # ========================================================

    def remove_order_item(self):

        selected = self.order_tree.selection()

        if not selected:
            messagebox.showwarning(
                "Selection",
                "Please select an item to remove."
            )
            return

        index = self.order_tree.index(
            selected[0]
        )

        del self.current_order_items[index]

        self.refresh_order_table()

    # ========================================================
    # GENERATE BILL
    # ========================================================

    def generate_bill(self):

        if not self.current_order_items:

            messagebox.showwarning(
                "Order",
                "Please add at least one item."
            )

            return

        customer_display = (
            self.order_customer.get()
        )

        customer_id = self.order_customer_map.get(
            customer_display
        )

        database_items = []

        for item in self.current_order_items:

            database_items.append({
                "menu_item_id": item["menu_item_id"],
                "quantity": item["quantity"],
                "price": item["price"]
            })

        try:

            order_id = create_order(
                customer_id,
                database_items
            )

            order = get_order(order_id)

            items = get_order_items(order_id)

            bill = (
                "====================================\n"
                "       RESTAURANT BILL\n"
                "====================================\n"
                f"Order ID : {order['id']}\n"
                f"Customer : {order['customer_name']}\n"
                f"Date     : {order['order_date']}\n"
                "------------------------------------\n"
            )

            for item in items:

                bill += (
                    f"{item['item_name']}\n"
                    f"  {item['quantity']} x "
                    f"₹{item['price']:,.2f}"
                    f" = ₹{item['subtotal']:,.2f}\n"
                )

            bill += (
                "------------------------------------\n"
                f"TOTAL: ₹{order['total_amount']:,.2f}\n"
                "===================================="
            )

            messagebox.showinfo(
                "Bill Generated",
                bill
            )

            self.dashboard_cache = None

            self.show_new_order()

        except Exception as error:

            messagebox.showerror(
                "Order Error",
                str(error)
            )

    # ========================================================
    # ORDER HISTORY
    # ========================================================

    def show_order_history(self):

        self.clear_content()

        self.create_page_title(
            "Order History",
            "View all completed restaurant orders"
        )

        table_frame = ctk.CTkFrame(
            self.content,
            fg_color="white",
            corner_radius=8
        )

        table_frame.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=(5, 25)
        )

        columns = (
            "id",
            "date",
            "customer",
            "amount",
            "status"
        )

        self.order_history_tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        headings = {
            "id": "Order ID",
            "date": "Date",
            "customer": "Customer",
            "amount": "Total Amount",
            "status": "Status"
        }

        for column in columns:

            self.order_history_tree.heading(
                column,
                text=headings[column]
            )

            self.order_history_tree.column(
                column,
                width=220,
                anchor="center"
            )

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.order_history_tree.yview
        )

        self.order_history_tree.configure(
            yscrollcommand=scrollbar.set
        )

        self.order_history_tree.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(10, 0),
            pady=10
        )

        scrollbar.pack(
            side="right",
            fill="y",
            padx=(0, 10),
            pady=10
        )

        orders = get_orders()

        for order in orders:

            self.order_history_tree.insert(
                "",
                "end",
                values=(
                    order["id"],
                    order["order_date"],
                    order["customer_name"],
                    f"₹{order['total_amount']:,.2f}",
                    order["status"]
                )
            )

    # ========================================================
    # REPORTS
    # ========================================================

    def show_reports(self):

        self.clear_content()

        self.create_page_title(
            "Sales Reports",
            "Paginated reports for faster navigation and lower UI load"
        )

        self.report_page = 0
        self.report_page_size = 10

        # ----------------------------------------------------
        # REPORT INFO
        # ----------------------------------------------------

        info_frame = ctk.CTkFrame(
            self.content,
            fg_color="#E7EBF1",
            corner_radius=8
        )

        info_frame.pack(
            fill="x",
            padx=35,
            pady=5
        )

        self.report_info = ctk.CTkLabel(
            info_frame,
            text="",
            font=ctk.CTkFont(
                size=14,
                weight="bold"
            ),
            text_color="#334155"
        )

        self.report_info.pack(
            side="left",
            padx=20,
            pady=14
        )

        # ----------------------------------------------------
        # REPORT TABLE
        # ----------------------------------------------------

        table_frame = ctk.CTkFrame(
            self.content,
            fg_color="white",
            corner_radius=8
        )

        table_frame.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=15
        )

        columns = (
            "id",
            "date",
            "customer",
            "amount",
            "status"
        )

        self.report_tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        headings = {
            "id": "Order ID",
            "date": "Date",
            "customer": "Customer",
            "amount": "Amount",
            "status": "Status"
        }

        for column in columns:

            self.report_tree.heading(
                column,
                text=headings[column]
            )

            self.report_tree.column(
                column,
                width=220,
                anchor="center"
            )

        self.report_tree.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        # ----------------------------------------------------
        # PAGINATION
        # ----------------------------------------------------

        pagination = ctk.CTkFrame(
            self.content,
            fg_color="transparent"
        )

        pagination.pack(
            fill="x",
            padx=35,
            pady=(0, 25)
        )

        ctk.CTkButton(
            pagination,
            text="← Previous",
            width=140,
            command=self.previous_report_page
        ).pack(
            side="left"
        )

        ctk.CTkButton(
            pagination,
            text="Next →",
            width=140,
            command=self.next_report_page
        ).pack(
            side="right"
        )

        self.load_report_page()

    # ========================================================
    # LOAD REPORT PAGE
    # ========================================================

    def load_report_page(self):

        for item in self.report_tree.get_children():
            self.report_tree.delete(item)

        total = get_sales_report_count()

        offset = (
            self.report_page *
            self.report_page_size
        )

        rows = get_sales_report(
            self.report_page_size,
            offset
        )

        for row in rows:

            self.report_tree.insert(
                "",
                "end",
                values=(
                    row["id"],
                    row["order_date"],
                    row["customer_name"],
                    f"₹{row['total_amount']:,.2f}",
                    row["status"]
                )
            )

        if total == 0:

            page_text = "No records available"

        else:

            start = offset + 1
            end = min(
                offset + self.report_page_size,
                total
            )

            page_text = (
                f"Showing {start}-{end} "
                f"of {total} records"
            )

        self.report_info.configure(
            text=(
                f"Page {self.report_page + 1}"
                f" • {page_text}"
            )
        )

    # ========================================================
    # NEXT REPORT PAGE
    # ========================================================

    def next_report_page(self):

        total = get_sales_report_count()

        max_page = max(
            0,
            (total - 1) //
            self.report_page_size
        )

        if self.report_page < max_page:

            self.report_page += 1
            self.load_report_page()

    # ========================================================
    # PREVIOUS REPORT PAGE
    # ========================================================

    def previous_report_page(self):

        if self.report_page > 0:

            self.report_page -= 1
            self.load_report_page()

    # ========================================================
    # Q05 PERFORMANCE
    # ========================================================

    def show_performance(self):

        self.clear_content()

        self.create_page_title(
            "Q05 Performance",
            "Reduce Response Time — optimization and database verification"
        )

        # ----------------------------------------------------
        # FEATURES
        # ----------------------------------------------------

        features = [
            (
                "Fast Search",
                "Prefix-based search updates results while typing."
            ),
            (
                "Quick Navigation",
                "Navigation buttons switch between modules directly."
            ),
            (
                "Cached Dashboard",
                "Dashboard statistics are stored in memory until refreshed."
            ),
            (
                "DB Indexing",
                "Indexes are created on frequently searched and joined columns."
            ),
            (
                "Paginated Reports",
                "Reports load limited records using LIMIT and OFFSET."
            ),
        ]

        for title, description in features:

            frame = ctk.CTkFrame(
                self.content,
                fg_color="white",
                corner_radius=8,
                border_width=1,
                border_color="#CBD5E1"
            )

            frame.pack(
                fill="x",
                padx=35,
                pady=7
            )

            ctk.CTkLabel(
                frame,
                text=title,
                font=ctk.CTkFont(
                    size=16,
                    weight="bold"
                ),
                text_color="#172033"
            ).pack(
                anchor="w",
                padx=18,
                pady=(12, 2)
            )

            ctk.CTkLabel(
                frame,
                text=description,
                font=ctk.CTkFont(
                    size=13
                ),
                text_color="#64748B"
            ).pack(
                anchor="w",
                padx=18,
                pady=(0, 12)
            )

        # ----------------------------------------------------
        # INDEXES
        # ----------------------------------------------------

        index_frame = ctk.CTkFrame(
            self.content,
            fg_color="#E7EBF1",
            corner_radius=8
        )

        index_frame.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=(15, 25)
        )

        ctk.CTkLabel(
            index_frame,
            text="Database Index Verification",
            font=ctk.CTkFont(
                size=18,
                weight="bold"
            ),
            text_color="#172033"
        ).pack(
            anchor="w",
            padx=18,
            pady=(15, 8)
        )

        indexes = get_database_indexes()

        index_text = ""

        for index in indexes:

            index_text += (
                f"✓ {index['name']} "
                f"→ {index['tbl_name']}\n"
            )

        if not index_text:
            index_text = "No custom indexes found."

        textbox = ctk.CTkTextbox(
            index_frame,
            height=120,
            font=ctk.CTkFont(
                size=13
            )
        )

        textbox.pack(
            fill="both",
            expand=True,
            padx=18,
            pady=(0, 10)
        )

        textbox.insert(
            "1.0",
            index_text
        )

        textbox.configure(
            state="disabled"
        )

        # ----------------------------------------------------
        # QUERY PLAN
        # ----------------------------------------------------

        plan = get_search_query_plan()

        plan_text = "\n".join(
            str(row["detail"])
            for row in plan
        )

        ctk.CTkLabel(
            index_frame,
            text="SQLite Search Query Plan:",
            font=ctk.CTkFont(
                size=14,
                weight="bold"
            ),
            text_color="#334155"
        ).pack(
            anchor="w",
            padx=18,
            pady=(5, 3)
        )

        plan_label = ctk.CTkLabel(
            index_frame,
            text=plan_text,
            font=ctk.CTkFont(
                size=12
            ),
            text_color="#475569",
            justify="left"
        )

        plan_label.pack(
            anchor="w",
            padx=18,
            pady=(0, 15)
        )


# ============================================================
# SAFE MENU FUNCTION
# ============================================================

def get_available_menu_items_safe():

    try:

        from database.db import get_available_menu_items

        return get_available_menu_items()

    except Exception:

        return []


# ============================================================
# APPLICATION START
# ============================================================

if __name__ == "__main__":

    app = RestaurantBillingApp()

    app.mainloop()