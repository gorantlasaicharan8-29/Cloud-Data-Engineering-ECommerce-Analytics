"""
Runs SQL analytics queries against the Neon PostgreSQL database
and prints results to the console.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'database'))

from db_connection import get_connection

queries = {
    "Total Customers":     "SELECT COUNT(*) FROM customers;",
    "Total Products":      "SELECT COUNT(*) FROM products;",
    "Total Orders":        "SELECT COUNT(*) FROM orders;",
    "Total Revenue":       "SELECT SUM(total_amount) FROM orders;",
    "Avg Order Value":     "SELECT ROUND(AVG(total_amount), 2) FROM orders;",
    "Highest Order":       "SELECT MAX(total_amount) FROM orders;",
    "Lowest Order":        "SELECT MIN(total_amount) FROM orders;",
    "Order Status Count":  """
        SELECT order_status, COUNT(*) AS total
        FROM orders GROUP BY order_status ORDER BY total DESC;
    """,
    "Top 10 Customers":    """
        SELECT customer_id, COUNT(*) AS total_orders
        FROM orders GROUP BY customer_id ORDER BY total_orders DESC LIMIT 10;
    """,
    "Top 10 Products":     """
        SELECT product_id, COUNT(*) AS total_sales
        FROM orders GROUP BY product_id ORDER BY total_sales DESC LIMIT 10;
    """,
}

conn = get_connection()
cursor = conn.cursor()

for label, query in queries.items():
    print(f"\n{'='*40}")
    print(f"📊 {label}")
    print('='*40)
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)

cursor.close()
conn.close()
print("\n✅ Analytics Complete!")
