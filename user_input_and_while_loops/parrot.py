# message = input("Tell me something, and i will repeat it back to you: ")
# print(message)

prompt = f"\nTell me something, and I will repeat it back to you:"
prompt += f"\nEnter 'quit' to end the program. "
message = ""
active = True
while active:
    message = input(prompt)
    if message == "quit":
        active = False
    else:
        print(message)
