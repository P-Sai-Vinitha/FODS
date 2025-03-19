import pandas as pd
import string
from collections import Counter

data = {
    "Review_ID": [1, 2, 3, 4, 5],
    "Review_Text": [
        "Great product! Really loved it.",
        "The product quality is amazing and worth the price.",
        "Not satisfied with the product. It broke within a week.",
        "Amazing quality! Highly recommend this product.",
        "The product is decent but could be better."
    ]
}
df = pd.DataFrame(data)

all_reviews = " ".join(df["Review_Text"]).lower()

all_reviews = all_reviews.translate(str.maketrans("", "", string.punctuation))

words = all_reviews.split()

word_count = Counter(words)

print("Frequency Distribution of Words in Customer Reviews:")
for word, freq in word_count.items():
    print(f"{word}: {freq}")
