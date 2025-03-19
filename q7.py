import pandas as pd

data = {
    'customer_id': [101, 102, 101, 103, 102, 101, 103],
    'order_date': ['2024-01-01', '2024-01-02', '2024-01-05', '2024-01-10', '2024-01-12', '2024-01-15', '2024-01-20'],
    'product_name': ['A', 'B', 'A', 'C', 'A', 'B', 'C'],
    'order_quantity': [2, 1, 3, 4, 2, 5, 6]
}

order_data = pd.DataFrame(data)

order_data['order_date'] = pd.to_datetime(order_data['order_date'])

total_orders_per_customer = order_data.groupby('customer_id').size()

avg_order_quantity_per_product = order_data.groupby('product_name')['order_quantity'].mean()

earliest_order_date = order_data['order_date'].min()
latest_order_date = order_data['order_date'].max()

print("Total Orders Per Customer:\n", total_orders_per_customer)
print("\nAverage Order Quantity Per Product:\n", avg_order_quantity_per_product)
print("\nEarliest Order Date:", earliest_order_date)
print("Latest Order Date:", latest_order_date)
