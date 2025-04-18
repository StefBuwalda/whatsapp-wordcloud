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
combined = Counter()
for author in data:
    combined.update(data[author])

top_words = [word for word, _ in combined.most_common(TOP_N)]

# Create DataFrame with only top words
df = pd.DataFrame(data).fillna(0).astype(int)
df = df.loc[df.index.intersection(top_words)]

# Plot heatmap
import seaborn as sns

plt.figure(figsize=(8, 5))
sns.heatmap(
    df, annot=True, fmt="d", cmap="YlGnBu", cbar_kws={"format": "%.0f"}
)
plt.title(f"Top {TOP_N} Word Frequencies")
plt.xlabel("Author")
plt.ylabel("Word")
plt.tight_layout()
plt.show()
