import pandas as pd  

orders_df = pd.read_csv("C:\\Users\\P Sai vinitha\\OneDrive\\Desktop\\FODS\\1q23.csv")

customers_df = pd.read_csv("C:\\Users\\P Sai vinitha\\OneDrive\Desktop\\FODS\\2q23.csv")

merged_df = pd.merge(orders_df, customers_df, on="Customer ID", how="inner")

merged_df["Order Date"] = pd.to_datetime(merged_df["Order Date"])

merged_df.sort_values(by=["Customer ID", "Order Date"], inplace=True)

merged_df["Time Between Orders"] = merged_df.groupby("Customer ID")["Order Date"].diff()

average_time_between_orders = merged_df["Time Between Orders"].mean()

print(merged_df)
print(f"\nAverage time between consecutive orders: {average_time_between_orders}")
