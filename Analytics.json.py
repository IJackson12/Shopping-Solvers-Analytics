import json
import os
import pandas as pd

df = pd.read_csv("online_shoppers_intention.csv")
# Calculate the analytics
total_sessions = len(df)
purchase_sessions = int(df["Revenue"].sum())
no_purchase_sessions = total_sessions - purchase_sessions

analytics = {
    "totalSessions": total_sessions,
    "purchaseSessions": purchase_sessions,
    "sessionsWithoutPurchase": no_purchase_sessions,
    "purchaseRate": round(purchase_sessions / total_sessions * 100, 2),
    "noPurchaseRate": round(no_purchase_sessions / total_sessions * 100, 2)
}

# Create a folder for the website data
os.makedirs("data", exist_ok=True)

# Save the analytics as JSON
with open("data/analytics.json", "w") as file:
    json.dump(analytics, file, indent=4)

print("\nAnalytics saved to data/analytics.json")
