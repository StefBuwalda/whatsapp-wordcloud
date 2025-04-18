from re import split, sub, match
from wordcloud import WordCloud  # type: ignore
from os import makedirs


def cleanupMessages(messages: list[str]) -> list[str]:
    # Remove "", \n, and symbols like , and .
    temp = [sub(r"([.,?!*()])", "", message) for message in messages]
    temp = [sub(r"\n", " ", message) for message in temp]
    temp = [sub(r"[^\x00-\x7F]", "", message) for message in temp]
    temp = [msg for msg in temp if msg != ""]
    return temp


# Open and read the chats from the '/data/_chat.txt' file exported by Whatsapp
try:
    file = open("data/_chat.txt", encoding="utf8")
    chat = file.read()
    file.close()
except FileNotFoundError:
    print("Sorry, the file /data/_chat.txt does not exist.")
    exit()

messages = cleanupMessages(
    split(r"\d{1,2}/\d{1,2}/\d{2}, \d{1,2}:\d{2}", chat)
)

messages = [s[3:] for s in messages if match(r" - [^ ]+?: ", s)]


author_words: dict[str, list[str]] = {}

for message in messages:
    message = sub(":", "", message)
    author, words = split(r" ", message, maxsplit=1)
    words = [word for word in words.split() if word and word != " "]
    for word in words:
        if author not in author_words:
            author_words[author] = []
        author_words[author].append(word.lower())

word_count_dicts: dict[str, int] = {}

wordcloud = WordCloud(
    width=800,
    height=400,
    background_color="black",  # or 'black', or any HTML color
    colormap="viridis",  # matplotlib colormap ('plasma', 'cool', 'inferno')
    # font_path="path/to/font.ttf",  # Use a custom font
    max_words=100,  # Max number of words to include
    min_font_size=10,
    max_font_size=100,
    prefer_horizontal=0.9,  # Between 0 (all vertical) and 1 (all horizontal)
    scale=2,  # Higher = better resolution
    contour_color="steelblue",  # Outline color (when using contour_width)
    contour_width=1,  # For consistent layout between runs
)

makedirs("output", exist_ok=True)

for author in author_words.keys():
    words = author_words.get(author)
    if words:
        for word in words:
            word_count_dicts[word] = word_count_dicts.get(word, 0) + 1
    test = wordcloud.generate_from_frequencies(  # type: ignore
        word_count_dicts
    )
    test.to_file("output/" + author + ".png")  # type: ignore
