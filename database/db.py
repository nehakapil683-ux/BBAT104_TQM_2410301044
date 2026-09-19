import sqlite3
from pathlib import Path


# ============================================================
# PROJECT PATH
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = BASE_DIR / "database" / "restaurant.db"


# ============================================================
# DATABASE CONNECTION
# ============================================================

def get_connection():
    """
    Create and return SQLite database connection.
    Foreign keys are enabled for data integrity.
    """

    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row

    # Enable foreign key support
    connection.execute("PRAGMA foreign_keys = ON")

    return connection


# ============================================================
# DATABASE INITIALIZATION
# ============================================================

def initialize_database():
    """
    Create all required tables and indexes.
    """

    connection = get_connection()
    cursor = connection.cursor()

    # ========================================================
    # MENU ITEMS
    # ========================================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS menu_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL CHECK(price >= 0),
            available INTEGER NOT NULL DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # ========================================================
    # CUSTOMERS
    # ========================================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # ========================================================
    # ORDERS
    # ========================================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            total_amount REAL NOT NULL DEFAULT 0,
            status TEXT NOT NULL DEFAULT 'Completed',

            FOREIGN KEY (customer_id)
            REFERENCES customers(id)
            ON DELETE SET NULL
        )
    """)

    # ========================================================
    # ORDER ITEMS
    # ========================================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS order_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER NOT NULL,
            menu_item_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL CHECK(quantity > 0),
            price REAL NOT NULL CHECK(price >= 0),
            subtotal REAL NOT NULL CHECK(subtotal >= 0),

            FOREIGN KEY (order_id)
            REFERENCES orders(id)
            ON DELETE CASCADE,

            FOREIGN KEY (menu_item_id)
            REFERENCES menu_items(id)
            ON DELETE RESTRICT
        )
    """)

    # ========================================================
    # DATABASE INDEXES
    # ========================================================

    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_menu_name
        ON menu_items(name)
    """)

    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_menu_category
        ON menu_items(category)
    """)

    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_menu_available
        ON menu_items(available)
    """)

    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_customer_name
        ON customers(name)
    """)

    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_customer_phone
        ON customers(phone)
    """)

    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_orders_date
        ON orders(order_date)
    """)

    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_orders_customer
        ON orders(customer_id)
    """)

    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_order_items_order
        ON order_items(order_id)
    """)

    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_order_items_menu
        ON order_items(menu_item_id)
    """)

    connection.commit()
    connection.close()


# ============================================================
# MENU FUNCTIONS
# ============================================================

def add_menu_item(name, category, price, available=1):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO menu_items
        (name, category, price, available)
        VALUES (?, ?, ?, ?)
    """, (
        name,
        category,
        price,
        available
    ))

    connection.commit()

    item_id = cursor.lastrowid

    connection.close()

    return item_id


def get_menu_items(search_text=""):

    connection = get_connection()
    cursor = connection.cursor()

    search_text = search_text.strip()

    if search_text:

        search = f"{search_text}%"

        cursor.execute("""
            SELECT
                id,
                name,
                category,
                price,
                available,
                created_at
            FROM menu_items
            WHERE name LIKE ?
               OR category LIKE ?
            ORDER BY id DESC
        """, (
            search,
            search
        ))

    else:

        cursor.execute("""
            SELECT
                id,
                name,
                category,
                price,
                available,
                created_at
            FROM menu_items
            ORDER BY id DESC
        """)

    items = cursor.fetchall()

    connection.close()

    return items


def get_menu_item(item_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            name,
            category,
            price,
            available,
            created_at
        FROM menu_items
        WHERE id = ?
    """, (item_id,))

    item = cursor.fetchone()

    connection.close()

    return item


def update_menu_item(
    item_id,
    name,
    category,
    price,
    available=1
):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE menu_items
        SET
            name = ?,
            category = ?,
            price = ?,
            available = ?
        WHERE id = ?
    """, (
        name,
        category,
        price,
        available,
        item_id
    ))

    connection.commit()
    connection.close()


def delete_menu_item(item_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM menu_items
        WHERE id = ?
    """, (item_id,))

    connection.commit()
    connection.close()


def get_menu_count():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*) AS total
        FROM menu_items
    """)

    result = cursor.fetchone()

    connection.close()

    return result["total"]


def get_available_menu_items():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            name,
            category,
            price
        FROM menu_items
        WHERE available = 1
        ORDER BY name
    """)

    items = cursor.fetchall()

    connection.close()

    return items


# ============================================================
# CUSTOMER FUNCTIONS
# ============================================================

def add_customer(name, phone=""):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO customers
        (name, phone)
        VALUES (?, ?)
    """, (
        name,
        phone
    ))

    connection.commit()

    customer_id = cursor.lastrowid

    connection.close()

    return customer_id


def get_customers(search_text=""):

    connection = get_connection()
    cursor = connection.cursor()

    search_text = search_text.strip()

    if search_text:

        search = f"{search_text}%"

        cursor.execute("""
            SELECT
                id,
                name,
                phone,
                created_at
            FROM customers
            WHERE name LIKE ?
               OR phone LIKE ?
            ORDER BY id DESC
        """, (
            search,
            search
        ))

    else:

        cursor.execute("""
            SELECT
                id,
                name,
                phone,
                created_at
            FROM customers
            ORDER BY id DESC
        """)

    customers = cursor.fetchall()

    connection.close()

    return customers


def get_customer(customer_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            name,
            phone,
            created_at
        FROM customers
        WHERE id = ?
    """, (customer_id,))

    customer = cursor.fetchone()

    connection.close()

    return customer


def get_customer_count():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*) AS total
        FROM customers
    """)

    result = cursor.fetchone()

    connection.close()

    return result["total"]


# ============================================================
# ORDER FUNCTIONS
# ============================================================

def create_order(customer_id, items):

    if not items:
        raise ValueError(
            "Order must contain at least one item."
        )

    connection = get_connection()
    cursor = connection.cursor()

    try:

        total_amount = 0

        # ----------------------------------------------------
        # Calculate total
        # ----------------------------------------------------

        for item in items:

            quantity = int(item["quantity"])
            price = float(item["price"])

            if quantity <= 0:
                raise ValueError(
                    "Quantity must be greater than zero."
                )

            if price < 0:
                raise ValueError(
                    "Price cannot be negative."
                )

            total_amount += quantity * price

        # ----------------------------------------------------
        # Create order
        # ----------------------------------------------------

        cursor.execute("""
            INSERT INTO orders
            (
                customer_id,
                total_amount,
                status
            )
            VALUES (?, ?, ?)
        """, (
            customer_id,
            total_amount,
            "Completed"
        ))

        order_id = cursor.lastrowid

        # ----------------------------------------------------
        # Add order items
        # ----------------------------------------------------

        for item in items:

            menu_item_id = int(item["menu_item_id"])
            quantity = int(item["quantity"])
            price = float(item["price"])

            subtotal = quantity * price

            cursor.execute("""
                INSERT INTO order_items
                (
                    order_id,
                    menu_item_id,
                    quantity,
                    price,
                    subtotal
                )
                VALUES (?, ?, ?, ?, ?)
            """, (
                order_id,
                menu_item_id,
                quantity,
                price,
                subtotal
            ))

        connection.commit()

        return order_id

    except Exception:

        connection.rollback()
        raise

    finally:

        connection.close()


def get_orders():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            o.id,
            o.order_date,
            o.total_amount,
            o.status,
            COALESCE(
                c.name,
                'Walk-in Customer'
            ) AS customer_name,
            c.phone
        FROM orders o
        LEFT JOIN customers c
            ON o.customer_id = c.id
        ORDER BY o.id DESC
    """)

    orders = cursor.fetchall()

    connection.close()

    return orders


def get_order(order_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            o.id,
            o.order_date,
            o.total_amount,
            o.status,
            COALESCE(
                c.name,
                'Walk-in Customer'
            ) AS customer_name,
            c.phone
        FROM orders o
        LEFT JOIN customers c
            ON o.customer_id = c.id
        WHERE o.id = ?
    """, (order_id,))

    order = cursor.fetchone()

    connection.close()

    return order


def get_order_items(order_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            oi.id,
            oi.order_id,
            oi.menu_item_id,
            m.name AS item_name,
            m.category,
            oi.quantity,
            oi.price,
            oi.subtotal
        FROM order_items oi
        INNER JOIN menu_items m
            ON oi.menu_item_id = m.id
        WHERE oi.order_id = ?
        ORDER BY oi.id
    """, (order_id,))

    items = cursor.fetchall()

    connection.close()

    return items


def get_order_count():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*) AS total
        FROM orders
    """)

    result = cursor.fetchone()

    connection.close()

    return result["total"]


def get_total_sales():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            COALESCE(
                SUM(total_amount),
                0
            ) AS total
        FROM orders
        WHERE status = 'Completed'
    """)

    result = cursor.fetchone()

    connection.close()

    return float(result["total"])


def get_today_sales():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            COALESCE(
                SUM(total_amount),
                0
            ) AS total
        FROM orders
        WHERE status = 'Completed'
          AND DATE(order_date) =
              DATE('now', 'localtime')
    """)

    result = cursor.fetchone()

    connection.close()

    return float(result["total"])


def get_today_order_count():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*) AS total
        FROM orders
        WHERE DATE(order_date) =
              DATE('now', 'localtime')
    """)

    result = cursor.fetchone()

    connection.close()

    return result["total"]


# ============================================================
# DASHBOARD
# ============================================================

def get_dashboard_data():
    """
    Fetch all dashboard statistics
    using one optimized database call.

    Supports:
    Q05 - Cached Dashboard
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT

            (
                SELECT COUNT(*)
                FROM menu_items
            ) AS menu_count,

            (
                SELECT COUNT(*)
                FROM customers
            ) AS customer_count,

            (
                SELECT COUNT(*)
                FROM orders
            ) AS order_count,

            (
                SELECT COALESCE(
                    SUM(total_amount),
                    0
                )
                FROM orders
                WHERE status = 'Completed'
            ) AS total_sales,

            (
                SELECT COUNT(*)
                FROM orders
                WHERE DATE(order_date) =
                      DATE('now', 'localtime')
            ) AS today_orders,

            (
                SELECT COALESCE(
                    SUM(total_amount),
                    0
                )
                FROM orders
                WHERE status = 'Completed'
                  AND DATE(order_date) =
                      DATE('now', 'localtime')
            ) AS today_sales
    """)

    result = cursor.fetchone()

    connection.close()

    return {
        "menu_count": result["menu_count"],
        "customer_count": result["customer_count"],
        "order_count": result["order_count"],
        "total_sales": float(
            result["total_sales"]
        ),
        "today_orders": result["today_orders"],
        "today_sales": float(
            result["today_sales"]
        )
    }


# ============================================================
# REPORTS
# ============================================================

def get_sales_report(limit=10, offset=0):
    """
    Return paginated sales records.

    Supports:
    Q05 - Paginated Reports
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            o.id,
            o.order_date,
            COALESCE(
                c.name,
                'Walk-in Customer'
            ) AS customer_name,
            o.total_amount,
            o.status
        FROM orders o
        LEFT JOIN customers c
            ON o.customer_id = c.id
        ORDER BY o.id DESC
        LIMIT ? OFFSET ?
    """, (
        int(limit),
        int(offset)
    ))

    rows = cursor.fetchall()

    connection.close()

    return rows


def get_sales_report_count():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*) AS total
        FROM orders
    """)

    result = cursor.fetchone()

    connection.close()

    return result["total"]


# ============================================================
# DATABASE INDEX VERIFICATION
# ============================================================

def get_database_indexes():
    """
    Return database indexes for
    Q05 DB Indexing demonstration.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            name,
            tbl_name
        FROM sqlite_master
        WHERE type = 'index'
          AND name NOT LIKE 'sqlite_%'
        ORDER BY name
    """)

    indexes = cursor.fetchall()

    connection.close()

    return indexes


def get_search_query_plan():
    """
    Return SQLite query plan for indexed
    prefix menu search.
    """

    connection = get_connection()
    cursor = connection.cursor()

    # SQLite can use a B-tree index for prefix LIKE
    # when LIKE optimization is enabled.
    cursor.execute("PRAGMA case_sensitive_like = ON")

    cursor.execute("""
        EXPLAIN QUERY PLAN
        SELECT
            id,
            name,
            category,
            price
        FROM menu_items
        WHERE name LIKE ?
    """, (
        "Pizza%",
    ))

    plan = cursor.fetchall()

    connection.close()

    return plan


# ============================================================
# SAMPLE DATA
# ============================================================

def insert_sample_menu_data():
    """
    Insert sample menu items only when
    menu table is empty.
    """

    if get_menu_count() > 0:
        return

    sample_items = [
        (
            "Margherita Pizza",
            "Pizza",
            249,
            1
        ),
        (
            "Veg Burger",
            "Burger",
            149,
            1
        ),
        (
            "French Fries",
            "Snacks",
            99,
            1
        ),
        (
            "White Sauce Pasta",
            "Pasta",
            199,
            1
        ),
        (
            "Masala Dosa",
            "South Indian",
            129,
            1
        ),
        (
            "Paneer Tikka",
            "Starter",
            229,
            1
        ),
        (
            "Cold Coffee",
            "Beverage",
            119,
            1
        ),
        (
            "Fresh Lime Soda",
            "Beverage",
            89,
            1
        )
    ]

    connection = get_connection()
    cursor = connection.cursor()

    cursor.executemany("""
        INSERT INTO menu_items
        (
            name,
            category,
            price,
            available
        )
        VALUES (?, ?, ?, ?)
    """, sample_items)

    connection.commit()
    connection.close()


# ============================================================
# MAIN DATABASE SETUP
# ============================================================

if __name__ == "__main__":

    initialize_database()

    print()
    print("======================================")
    print("Restaurant Billing Database")
    print("======================================")
    print("Database initialized successfully.")
    print(f"Database location: {DB_PATH}")
    print("Tables and indexes are ready.")
    print()