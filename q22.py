import pandas as pd  
import matplotlib.pyplot as plt  

df = pd.read_csv("C:\\Users\\P Sai vinitha\\OneDrive\\Desktop\\FODS\\q22.csv")

df["Date"] = pd.to_datetime(df["Date"])

df["Year-Month"] = df["Date"].dt.to_period("M")
monthly_avg_temp = df.groupby("Year-Month")["Temperature (Celsius)"].mean().reset_index()


print(monthly_avg_temp)

plt.figure(figsize=(10, 5))
plt.plot(monthly_avg_temp["Year-Month"].astype(str), monthly_avg_temp["Temperature (Celsius)"], marker="o", linestyle="-", color="b")
plt.xlabel("Month-Year")
plt.ylabel("Average Temperature (°C)")
plt.title("Monthly Average Temperature Trend")
plt.xticks(rotation=45)
plt.grid()
plt.show()
