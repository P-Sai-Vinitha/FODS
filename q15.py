import pandas as pd

data = {
    "Post_ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Likes": [100, 200, 150, 100, 250, 300, 150, 100, 200, 250]
}

df = pd.DataFrame(data)

likes_counts = df["Likes"].value_counts().sort_index()

print("Frequency Distribution of Likes:")
print(likes_counts)
