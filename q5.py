import numpy as np

fuel_efficiency = np.array([22, 25, 30, 35, 40]) 

avg_efficiency = np.mean(fuel_efficiency)

mpg_model_1 = fuel_efficiency[0]  
mpg_model_2 = fuel_efficiency[-1]

percentage_improvement = ((mpg_model_2 - mpg_model_1) / mpg_model_1) * 100

print("Average Fuel Efficiency: {:.2f} MPG".format(avg_efficiency))
print("Percentage Improvement from Model 1 to Model 2: {:.2f}%".format(percentage_improvement))
