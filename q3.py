import numpy as np

house_data = np.loadtxt("C:\\Users\\P Sai vinitha\\OneDrive\\Desktop\\FODS\\q3.csv", delimiter=',', skiprows=1)

houses_with_more_than_4_bedrooms = house_data[house_data[:, 0] > 4]

average_price = np.mean(houses_with_more_than_4_bedrooms[:, 2])

print(f"Average sale price of houses with more than 4 bedrooms: {average_price:.2f}")
