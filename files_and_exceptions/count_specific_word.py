def count_word(filename, word):
    try:
        with open(filename, encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"sorry, {filename} not found")
    else:
        word_count = contents.lower().count(word.lower())
        print(f"The '{word}' count in {filename} is {word_count}")


filenames = [
    "alice.txt",
    "siddhartha.txt",
    "moby_dick.txt",
    "little_women.txt",
    "butts.txt",
]
for filename in filenames:
    count_word(filename, "forgive")
