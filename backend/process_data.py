from os import makedirs
from backend.functions import (
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

total_frequency = 0
total_frequency_dict: dict[str, int] = Counter()
word_frequency_dict: dict[str, dict[str, int]] = {}


for author in test:
    word_frequency_dict[author] = {}
    messageList = test.get(author)
    if messageList:
        wordList = Counter(processMessageList(messageList))
        word_frequency_dict[author] = wordList
        for count in wordList.items():
            total_frequency_dict.update({author: count[1]})
            total_frequency += count[1]
