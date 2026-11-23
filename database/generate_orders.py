"""Generate synthetic order records."""

import random

from database.insert_data import insert_order

TOTAL_ORDERS = 20000
TOTAL_CUSTOMERS = 1000
TOTAL_PRODUCTS = 500

ORDER_STATUSES = ["Pending", "Processing", "Shipped", "Delivered", "Cancelled"]


def main():
    print(f"Generating {TOTAL_ORDERS} orders...")
    for index in range(1, TOTAL_ORDERS + 1):
        customer_id = random.randint(1, TOTAL_CUSTOMERS)
        product_id = random.randint(1, TOTAL_PRODUCTS)
        quantity = random.randint(1, 5)
        unit_price = random.randint(500, 100000)
        total_amount = quantity * unit_price
        status = random.choice(ORDER_STATUSES)

        insert_order(customer_id, product_id, quantity, total_amount, status)

        if index % 100 == 0:
            print(f"Inserted {index}/{TOTAL_ORDERS} orders")
    print("Order generation completed.")


if __name__ == "__main__":
    main()
