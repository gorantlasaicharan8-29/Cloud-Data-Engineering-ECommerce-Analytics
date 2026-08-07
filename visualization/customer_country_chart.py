import pandas as pd
import matplotlib.pyplot as plt

customers = pd.read_csv("exports/customers.csv")

country = customers["country"].value_counts().head(10)

plt.figure(figsize=(10,6))

country.plot(kind="bar")

plt.title("Top Countries")

plt.tight_layout()

plt.savefig("visualization/customer_country.png")

plt.show()