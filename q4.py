import numpy as np

sales_data = np.array([25000, 32000, 40000, 50000]) 

total_sales = np.sum(sales_data)

percentage_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100

print("Total Sales for the Year: $", total_sales)
print("Percentage Increase from Q1 to Q4: {:.2f}%".format(percentage_increase))
