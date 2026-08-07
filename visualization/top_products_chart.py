import pandas as pd
import matplotlib.pyplot as plt

orders = pd.read_csv("exports/orders.csv")

top_products = (
    orders.groupby("product_id")
    .size()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,6))

top_products.plot(kind="bar")

plt.title("Top 10 Selling Products")
plt.xlabel("Product ID")
plt.ylabel("Orders")

plt.tight_layout()

plt.savefig("visualization/top_products.png")

plt.show()