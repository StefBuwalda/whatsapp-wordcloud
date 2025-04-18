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
total_frequency_dict: dict[str, int] = {}
word_frequency_dict: dict[str, dict[str, int]] = {}


for author in test:
    word_frequency_dict[author] = {}
    messageList = test[author]
    if messageList:
        wordFreqList = Counter(processMessageList(messageList))
        word_frequency_dict[author] = wordFreqList
        total_frequency_dict[author] = sum(wordFreqList.values())
total_frequency = sum(total_frequency_dict.values())
