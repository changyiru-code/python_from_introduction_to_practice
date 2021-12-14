def show_messages(texts):
    for text in texts:
        print(text)


def send_messages(texts_messages, sent_messages):
    while texts_messages:
        texts_message = texts_messages.pop()
        sent_messages.append(texts_message)


texts_messages = ["I love python.", "Python is very interesting.", "If you study, you will love it."]
sent_messages = []
show_messages(texts_messages)
send_messages(texts_messages[:], sent_messages)

print(texts_messages)
print(sent_messages)
