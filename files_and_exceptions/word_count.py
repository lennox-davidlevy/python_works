def word_count(filename):
    try:
        with open(filename, encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        # to fail silently, use pass
        pass
        # print(f"Sorry, the file {filename} does not exist")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filenames = [
    "alice.txt",
    "siddhartha.txt",
    "moby_dick.txt",
    "little_women.txt",
    "butts.txt",
]
for filename in filenames:
    word_count(filename)
