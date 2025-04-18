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

frequency_dictionary: dict[str, dict[str, int]] = {}

for author in test.keys():
    frequency_dictionary[author] = {}
    messageList = test.get(author)
    if messageList:
        frequency_dictionary[author] = Counter(processMessageList(messageList))
