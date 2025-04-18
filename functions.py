from re import split, sub, match
from regex import sub as sub2


def processRawMessages(chat: str) -> dict[str, list[str]]:
    output: dict[str, list[str]] = {}
    # Split based on new line
    segments = split(r"\n", chat)
    author = ""
    for segment in segments:
        re_match = match(r"\d+/\d+/\d+, \d+:\d+ - ([^:]+): (.*)", segment)
        if re_match:
            # It's a match, get rid of date and time, keep name + message
            author = re_match.group(1)
            if author not in output:
                output[author] = []
            output[author].append(re_match.group(2))
        else:
            # Not a match, check if it's an action or continuation of sentence
            re_match2 = match(r"\d+/\d+/\d+, \d+:\d+ - ", segment)
            if re_match2:
                # It's an action, ignore
                pass
            else:
                segmentList = output.get(author)
                if segmentList:
                    segmentList[-1] += segment
                else:
                    print("ERROR functions.py line 24")
                    print(segment)
    return output


def processMessageList(messages: list[str]) -> list[str]:
    output: list[str] = []
    for message in messages:
        # Remove http(s) links
        message = sub(r"https?://(?:www\.)?\S+", "", message)
        # Remove emojis and symbols
        message = sub2(r"[\p{Emoji}?!:,.]+", "", message)
        # If it's not added media, add to output
        if message != "<Media omitted>":
            output += message.lower().split()
    return output
