import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

data = {
    "Age": [23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 54, 56, 57, 58, 58, 60, 61],
    "Body_Fat": [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2, 34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]
}

df = pd.DataFrame(data)

print("Mean:\n", df.mean(), "\nMedian:\n", df.median(), "\nStandard Deviation:\n", df.std())

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.boxplot(y=df["Age"], color="skyblue")
plt.title("Boxplot of Age")
plt.subplot(1, 2, 2)
sns.boxplot(y=df["Body_Fat"], color="lightcoral")
plt.title("Boxplot of Body Fat (%)")
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(x=df["Age"], y=df["Body_Fat"], color="green")
plt.xlabel("Age")
plt.ylabel("Body Fat (%)")
plt.title("Scatter Plot of Age vs. Body Fat")
plt.show()

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
stats.probplot(df["Age"], dist="norm", plot=plt)
plt.title("Q-Q Plot for Age")

plt.subplot(1, 2, 2)
stats.probplot(df["Body_Fat"], dist="norm", plot=plt)
plt.title("Q-Q Plot for Body Fat (%)")

plt.show()
