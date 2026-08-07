import pandas as pd
import matplotlib.pyplot as plt

orders = pd.read_csv("exports/orders.csv")

revenue = (
    orders.groupby("order_status")["total_amount"]
    .sum()
)

plt.figure(figsize=(8,6))

revenue.plot(kind="bar")

plt.title("Revenue by Order Status")

plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig("visualization/revenue_status.png")

plt.show()