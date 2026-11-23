"""Database insert helpers for the e-commerce pipeline."""

from database.db_connection import get_connection


def _insert(query, values):
    """Execute one parameterized insert and always close the connection."""
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cursor:
                cursor.execute(query, values)
    finally:
        conn.close()


def insert_customer(first_name, last_name, email, phone, city, country):
    query = """
        INSERT INTO customers
            (first_name, last_name, email, phone, city, country)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    _insert(query, (first_name, last_name, email, phone, city, country))


def insert_product(product_name, category, brand, price, stock):
    query = """
        INSERT INTO products
            (product_name, category, brand, price, stock)
        VALUES (%s, %s, %s, %s, %s)
    """
    _insert(query, (product_name, category, brand, price, stock))


def insert_order(customer_id, product_id, quantity, total_amount, order_status):
    query = """
        INSERT INTO orders
            (customer_id, product_id, quantity, total_amount, order_status)
        VALUES (%s, %s, %s, %s, %s)
    """
    _insert(
        query,
        (customer_id, product_id, quantity, total_amount, order_status),
    )
