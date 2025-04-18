from backend.process_data import (
    total_frequency_dict as freq_dict,
    total_frequency as total,
)

for author in freq_dict:
    fraction = round(freq_dict[author] / total * 100, 1)
    print(
        f"{author + ":":<30}",
        f"{str(freq_dict.get(author))+"/"+str(total):>15}",
        f"({fraction:>4}%)",
    )
