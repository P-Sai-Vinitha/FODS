import pandas as pd  

df = pd.read_csv("C:\\Users\\P Sai vinitha\\OneDrive\\Desktop\\FODS\\q21.csv")

df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")

df.dropna(subset=["Department"], inplace=True)

df["First Name"] = df["Full Name"].str.split().str[0]

print(df.head())
