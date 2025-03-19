import pandas as pd
import matplotlib.pyplot as plt
import re
import nltk
from collections import Counter
from nltk.corpus import stopwords

nltk.download('stopwords')

df = pd.read_csv("C:\\Users\\P Sai vinitha\\OneDrive\\Desktop\\FODS\\data.csv")

stop_words = set(stopwords.words('english'))
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return words

df['processed'] = df['feedback'].astype(str).apply(preprocess_text)
all_words = [word for words in df['processed'] for word in words]
word_freq = Counter(all_words)

N = int(input("Enter the number of top frequent words to display: "))
top_words = word_freq.most_common(N)

print("Top", N, "words:", top_words)
words, counts = zip(*top_words)
plt.figure(figsize=(10, 5))
plt.bar(words, counts, color='blue')
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Top N Frequent Words in Customer Feedback")
plt.xticks(rotation=45)
plt.show()

