import pandas as pd

products = [
    {"id": 1, "name": "Notebook", "price": 25, "quantity": 20},
    {"id": 2, "name": "Keyboard", "price": 150, "quantity": 5},
    {"id": 3, "name": "Mouse", "price": 80, "quantity": 10},
    {"id": 4, "name": "Monitor", "price": 250, "quantity": 3},
    {"id": 5, "name": "USB drive", "price": 120, "quantity": 8},
]

products_df = pd.DataFrame(products)

# Save the data to a CSV file
products_df.to_csv("products.csv", index=False)

# Read the CSV file
products_df = pd.read_csv("products.csv")

# Add a column for each product's total value
products_df["total"] = products_df["price"] * products_df["quantity"]

print("All products:")
print(products_df)

print("\nProducts with price > 100:")
print(products_df[products_df["price"] > 100])

# Calculate the total inventory value
inventory_value = products_df["total"].sum()
print(f"\nTotal inventory value: {inventory_value}")