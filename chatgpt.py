import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from backend.process_data import word_frequency_dict
from collections import Counter

# Example dictionary
data = word_frequency_dict

# Choose how many top words to show
TOP_N = 5

# Collect top words globally or per author
combined = Counter()  # type: ignore
for author in data:
    combined.update(data[author])  # type: ignore

top_words = [word for word, _ in combined.most_common(TOP_N)]  # type: ignore

# Create DataFrame with only top words
df = pd.DataFrame(data).fillna(0).astype(int)  # type: ignore
df = df.loc[df.index.intersection(top_words)]  # type: ignore


plt.figure(figsize=(8, 5))  # type: ignore
sns.heatmap(  # type: ignore
    df, annot=True, fmt="d", cmap="YlGnBu", cbar_kws={"format": "%.0f"}
)
plt.title(f"Top {TOP_N} Word Frequencies")  # type: ignore
plt.xlabel("Author")  # type: ignore
plt.ylabel("Word")  # type: ignore
plt.tight_layout()
plt.show()  # type: ignore
