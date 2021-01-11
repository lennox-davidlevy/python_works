messages_list = ["hello", "how are you", "show me your feet"]


def send_messages(messages_list, sent_messages):
    while messages_list:
        current_message = messages_list.pop()
        sent_messages.append(current_message)
    return sent_messages


sent_messages = send_messages(messages_list[:], [])
for message in sent_messages:
    print(f"message sent: {message}")
print(f"org mesages: {messages_list}\nsent messages: {sent_messages}")
