import pandas as pd

df = pd.read_csv("C:\\Users\\P Sai vinitha\\OneDrive\\Desktop\\FODS\\q20.csv")

def segment_spending(spending):
    if spending > 1000:
        return "High Spender"
    elif spending >= 500:
        return "Medium Spender"
    else:
        return "Low Spender"

df["Spending Segment"] = df["Total Spending"].apply(segment_spending)

avg_age_per_segment = df.groupby("Spending Segment")["Age"].mean()

print("Customer Segmentation with Average Age:")
print(avg_age_per_segment)
print("\nSegmented Customer Data:")
print(df.head())
