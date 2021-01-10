prompt = "Hello, say a word and if its a curse word, ill leave"
prompt += "\n(Type 'quit' if you want to stop anyway) "
word_said = input(prompt)
active = True
while active:
    if word_said.lower() == "fuck" or word_said.lower() == "shit":
        active = False
        print(f"oh my gosh you said {word_said.upper()}! GOODBYE!")
    elif word_said.lower() == "quit":
        print("fine, goodbye, who cares not me")
        break
    else:
        prompt = f"nope, {word_said} is not a curse, so here i am. tell me another "
        word_said = input(prompt)
