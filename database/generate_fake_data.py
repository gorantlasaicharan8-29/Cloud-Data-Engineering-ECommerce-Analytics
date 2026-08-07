from faker import Faker
import random
from insert_data import insert_product

fake = Faker("en_IN")

products = [
    ("Laptop", "Electronics", "HP"),
    ("Smartphone", "Electronics", "Samsung"),
    ("Mouse", "Accessories", "Logitech"),
    ("Keyboard", "Accessories", "Dell"),
    ("Monitor", "Electronics", "LG"),
    ("Headphones", "Accessories", "Sony"),
    ("Printer", "Electronics", "Canon"),
    ("Smart Watch", "Electronics", "Apple"),
    ("Tablet", "Electronics", "Lenovo"),
    ("Camera", "Electronics", "Nikon")
]

TOTAL_PRODUCTS = 500

print("🚀 Generating Products...\n")

for i in range(1, TOTAL_PRODUCTS + 1):

    product_name, category, brand = random.choice(products)

    price = random.randint(500, 100000)

    stock = random.randint(10, 500)

    insert_product(
        product_name,
        category,
        brand,
        price,
        stock
    )

    print(f"✅ Product {i} inserted")

print("\n🎉 500 Products Inserted Successfully!")