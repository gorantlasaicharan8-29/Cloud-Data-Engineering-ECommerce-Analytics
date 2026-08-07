import pandas as pd
import matplotlib.pyplot as plt

orders = pd.read_csv("exports/orders.csv")

revenue = (
    orders.groupby("order_status")["total_amount"]
    .sum()
)

plt.figure(figsize=(8,8))

revenue.plot(kind="pie", autopct="%1.1f%%")

plt.title("Revenue Distribution")

plt.ylabel("")

plt.savefig("visualization/sales_summary.png")

plt.show()