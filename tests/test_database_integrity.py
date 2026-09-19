import os
import sys
import sqlite3

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from database.db import get_connection


def test_database_connection():
    connection = get_connection()

    assert isinstance(connection, sqlite3.Connection)

    connection.close()

    print("Database connection verified.")


def test_required_tables():
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
        """
    )

    tables = {row[0] for row in cursor.fetchall()}

    connection.close()

    required_tables = {
        "menu_items",
        "customers",
        "orders",
        "order_items",
    }

    missing_tables = required_tables - tables

    assert not missing_tables, (
        f"Missing database tables: {missing_tables}"
    )

    print("Required database tables verified.")


def test_required_indexes():
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT name
        FROM sqlite_master
        WHERE type = 'index'
        """
    )

    indexes = {row[0] for row in cursor.fetchall()}

    connection.close()

    required_indexes = {
        "idx_menu_name",
        "idx_menu_category",
        "idx_customer_name",
        "idx_customer_phone",
        "idx_orders_date",
        "idx_orders_customer",
    }

    missing_indexes = required_indexes - indexes

    assert not missing_indexes, (
        f"Missing database indexes: {missing_indexes}"
    )

    print("Required database indexes verified.")


if __name__ == "__main__":
    print("Database Integrity Verification")
    print("=" * 40)

    test_database_connection()
    test_required_tables()
    test_required_indexes()

    print("\nRESULT: PASS")