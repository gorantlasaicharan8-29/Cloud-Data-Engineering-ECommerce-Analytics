import pandas as pd
import matplotlib.pyplot as plt

# Load CSV files
customers = pd.read_csv("exports/customers.csv")
products = pd.read_csv("exports/products.csv")
orders = pd.read_csv("exports/orders.csv")

# Count order status
status = orders["order_status"].value_counts()

# Create bar chart
status.plot(kind="bar")

plt.title("Order Status Distribution")
plt.xlabel("Order Status")
plt.ylabel("Number of Orders")

# Save chart
plt.savefig("visualization/order_status.png")

# Show chart
plt.show()

print("✅ Chart created successfully!")