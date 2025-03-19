import pandas as pd

df = pd.read_csv("C:\\Users\\P Sai vinitha\\OneDrive\\Desktop\\FODS\\q19.csv")

df["Total Sales"] = df["Quantity Sold"] * df["Unit Price"]

product_sales = df.groupby("Product")["Total Sales"].sum().reset_index()

product_sales["Profit"] = product_sales["Total Sales"] * 0.2

top_products = product_sales.sort_values(by="Profit", ascending=False).head(5)

print("Top 5 Most Profitable Products:")
print(top_products)
