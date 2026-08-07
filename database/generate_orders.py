import random
from insert_data import insert_order

TOTAL_ORDERS = 20000

print("🚀 Generating Orders...\n")

order_status = [
    "Pending",
    "Processing",
    "Shipped",
    "Delivered",
    "Cancelled"
]

for i in range(1, TOTAL_ORDERS + 1):

    customer_id = random.randint(1, 1001)

    product_id = random.randint(1, 500)

    quantity = random.randint(1, 5)

    price = random.randint(500, 100000)

    total_amount = quantity * price

    status = random.choice(order_status)

    insert_order(
        customer_id,
        product_id,
        quantity,
        total_amount,
        status
    )

    if i % 100 == 0:
        print(f"✅ {i} Orders Inserted")

print("\n🎉 20,000 Orders Inserted Successfully!")