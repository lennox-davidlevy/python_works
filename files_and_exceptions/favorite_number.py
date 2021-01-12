import json


def store_numbers_in_json(filename, numbers):
    with open(filename, "w") as f:
        json.dump(numbers, f)


def number_writer():
    active_flag = True
    favorite_numbers = []
    print("i will save your favorite numbers in a file for you")
    name = input("\nWhat is your name? ")
    filename = f"{name}_favorite_numbers.json"
    print("press 's' to save / press 'q' to quit")
    while active_flag:
        number = input(f"Give me a favorite number ")
        if number == "q":
            print("bye")
            break
        elif number == "s":
            active_flag = False
            store_numbers_in_json(filename, favorite_numbers)
            print(f"{favorite_numbers} stored in {filename}!")
        else:
            try:
                number = int(number)
            except ValueError:
                print(f"{number} is not a number!")
            else:
                favorite_numbers.append(number)


number_writer()
