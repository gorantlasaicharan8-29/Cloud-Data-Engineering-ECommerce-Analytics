from db_connection import get_connection


# -----------------------------
# Insert Customer
# -----------------------------
def insert_customer(first_name, last_name, email, phone, city, country):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO customers
    (first_name, last_name, email, phone, city, country)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = (
        first_name,
        last_name,
        email,
        phone,
        city,
        country
    )

    cursor.execute(query, values)
    conn.commit()

    print("✅ Customer inserted successfully!")

    cursor.close()
    conn.close()


# -----------------------------
# Insert Product
# -----------------------------
def insert_product(product_name, category, brand, price, stock):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO products
    (product_name, category, brand, price, stock)
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        product_name,
        category,
        brand,
        price,
        stock
    )

   # -----------------------------
# Insert Order
# -----------------------------
def insert_order(customer_id, product_id, quantity, total_amount, order_status):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO orders
    (customer_id, product_id, quantity, total_amount, order_status)
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        customer_id,
        product_id,
        quantity,
        total_amount,
        order_status
    )

    cursor.execute(query, values)

    conn.commit()

    cursor.close()
    conn.close()