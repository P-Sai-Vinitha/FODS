import matplotlib.pyplot as plt
import numpy as np
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [12000, 15000, 18000, 17000, 19000, 25000, 22000, 21000, 23000, 26000, 27000, 30000]
plt.figure(figsize=(10, 5))
plt.plot(months, sales, marker='o', linestyle='-', color='b', linewidth=2, markersize=6)
plt.title("Monthly Sales Data (Line Plot)", fontsize=14)
plt.xlabel("Months", fontsize=12)
plt.ylabel("Sales ($)", fontsize=12)
plt.grid(True)
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 5))
plt.bar(months, sales, color='skyblue', edgecolor='black')

plt.title("Monthly Sales Data (Bar Plot)", fontsize=14)
plt.xlabel("Months", fontsize=12)
plt.ylabel("Sales ($)", fontsize=12)
plt.xticks(rotation=45)

plt.show()
