import numpy as np

sales_data = np.array([
    [150, 200, 250],
    [180, 220, 260],
    [170, 210, 240]
])

average_price = np.mean(sales_data)
print(f"Average price of all products sold: {average_price:.2f}")
