import pandas as pd
import matplotlib.pyplot as plt

orders = pd.read_csv("exports/orders.csv")

top_customers = (
    orders.groupby("customer_id")
    .size()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,6))

top_customers.plot(kind="bar")

plt.title("Top 10 Customers")

plt.tight_layout()

plt.savefig("visualization/top_customers.png")

plt.show()