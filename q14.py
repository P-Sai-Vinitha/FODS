import pandas as pd
from collections import Counter

data = {
    "Customer_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Age": [25, 30, 22, 25, 40, 35, 30, 22, 40, 25],
    "Purchase_Amount": [200, 150, 300, 250, 400, 350, 180, 220, 500, 275]
}

df = pd.DataFrame(data)

age_counts = df["Age"].value_counts().sort_index()

print("Frequency Distribution of Customer Ages:")
print(age_counts)
