import string
from collections import Counter

with open("C:\\Users\\P Sai vinitha\\OneDrive\\Desktop\\FODS\\sample_text.txt", "r") as file:
    text = file.read()

text = text.lower().translate(str.maketrans("", "", string.punctuation))

words = text.split()

word_count = Counter(words)

for word, freq in word_count.items():
    print(f"{word}: {freq}")
