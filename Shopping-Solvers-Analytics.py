import pandas as pd

# Load the shopping data
df = pd.read_csv("online_shoppers_intention.csv")

# Show the first 5 rows
print(df.head())

# Show the number of rows and columns
print("\nDataset size:")
print(df.shape)

# Show all column names
print("\nColumn names:")
print(df.columns.tolist())

# Show how many sessions resulted in purchases
print("\nPurchase outcomes:")
print(df["Revenue"].value_counts())

# Calculate the percentage of sessions that resulted in purchases
purchase_rate = df["Revenue"].mean() * 100

print(f"\nPurchase rate: {purchase_rate:.2f}%")

# Calculate the percentage of sessions without purchases
no_purchase_rate = 100 - purchase_rate

print(f"Sessions without purchase: {no_purchase_rate:.2f}%")
