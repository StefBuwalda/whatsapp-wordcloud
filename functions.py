from re import split, sub, match


def processRawMessages(chat: str):
    temp = split(r"\d{1,2}/\d{1,2}/\d{2}, \d{1,2}:\d{2}", chat)

    temp = [sub(r"([.,?!*()])", "", message) for message in temp]
    temp = [sub(r"\n", " ", message) for message in temp]
    temp = [sub(r"[^\x00-\x7F]", "", message) for message in temp]
    temp = [msg for msg in temp if msg != ""]

    return [s[3:] for s in temp if match(r" - [^ ]+?: ", s)]
