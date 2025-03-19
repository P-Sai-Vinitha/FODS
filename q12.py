import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperatures = [5, 7, 12, 18, 22, 25, 27, 26, 21, 15, 10, 6]  
rainfall = [78, 56, 68, 72, 85, 92, 110, 105, 90, 80, 65, 70]  

plt.figure(figsize=(10, 5))
plt.plot(months, temperatures, marker='o', linestyle='-', color='r', label='Temperature (°C)')
plt.xlabel('Months')
plt.ylabel('Temperature (°C)')
plt.title('Monthly Temperature Variation')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))
plt.scatter(months, rainfall, color='b', label='Rainfall (mm)')
plt.xlabel('Months')
plt.ylabel('Rainfall (mm)')
plt.title('Monthly Rainfall Distribution')
plt.legend()
plt.grid(True)
plt.show()
