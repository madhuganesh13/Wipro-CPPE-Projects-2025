# ~/dynamicpricing/analytics-engine/analytics_service.py
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Sample transaction data
data = {
    "Product": ["Product A", "Product B", "Product C", "Product D"],
    "Transactions": [150, 230, 90, 120],
    "Revenue": [3000, 4600, 1800, 2400]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plot number of transactions per product
plt.figure(figsize=(8, 5))
plt.bar(df['Product'], df['Transactions'], color='skyblue')
plt.title("Transactions per Product")
plt.xlabel("Products")
plt.ylabel("Number of Transactions")
plt.savefig("transactions_per_product.png")  # Save the chart
plt.show()

# Plot revenue per product
plt.figure(figsize=(8, 5))
plt.bar(df['Product'], df['Revenue'], color='orange')
plt.title("Revenue per Product")
plt.xlabel("Products")
plt.ylabel("Revenue ($)")
plt.savefig("revenue_per_product.png")
plt.show()
