def read_words_from_txt(filename):
    try:
        with open(filename, encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"{filename} does not exist")
    else:
        print(f"From: {filename}")
        words = contents.split()
        for idx, word in enumerate(words):
            print(f"Name {idx+1}: {word}")


filenames = ["cats.txt", "dogs.txt", "bunnies.txt"]
for filename in filenames:
    read_words_from_txt(filename)
