from config import wordcloud  # type: ignore
from os import makedirs
from functions import (
    processRawMessages,
    processMessageList,
)
from collections import Counter


# Open and read the chats from the '/data/_chat.txt' file exported by Whatsapp
try:
    file = open("data/_chat.txt", encoding="utf8")
    chat = file.read()
    file.close()
except FileNotFoundError:
    print("Sorry, the file /data/_chat.txt does not exist.")
    exit()

makedirs("output", exist_ok=True)

test = processRawMessages(chat)

for author in test.keys():
    messageList = test.get(author)
    if messageList:
        wordList = processMessageList(messageList)
        freq_dict = Counter(wordList)
        image = wordcloud.generate_from_frequencies(freq_dict)  # type: ignore
        image.to_file(f"output/{author}.png")  # type: ignore
