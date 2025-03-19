import pandas as pd

data = {
    'product_name': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'C', 'B', 'A'],
    'order_quantity': [10, 5, 8, 15, 7, 6, 20, 12, 9, 25],
    'order_date': pd.date_range(start='2024-01-01', periods=10, freq='D')
}

sales_data = pd.DataFrame(data)

last_month_sales = sales_data[sales_data['order_date'] >= '2024-01-01']

top_products = last_month_sales.groupby('product_name')['order_quantity'].sum()

top_5_products = top_products.sort_values(ascending=False).head(5)

print("Top 5 Best-Selling Products:\n", top_5_products)
