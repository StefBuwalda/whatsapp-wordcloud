from backend.process_data import (
    total_frequency_dict as freq_dict,
    total_frequency as total,
)
import matplotlib.pyplot as plt

for author in freq_dict:
    fraction = round(freq_dict[author] / total * 100, 1)
    print(
        f"{author + ":":<30}",
        f"{str(freq_dict.get(author))+"/"+str(total):>15}",
        f"({fraction:>4}%)",
    )

# ChatGPT generated
# Prepare labels and sizes
labels = list(freq_dict.keys())
sizes = [v / total * 100 for v in freq_dict.values()]  # percentages

# Plot
plt.figure(figsize=(8, 8))  # type: ignore
plt.pie(sizes, labels=labels, autopct="%.1f%%", startangle=90)  # type: ignore
plt.title("Word Frequency Distribution by Author")  # type: ignore
plt.axis("equal")  # type: ignore # Equal aspect ratio for a perfect circle
plt.tight_layout()
plt.show()  # type: ignore
