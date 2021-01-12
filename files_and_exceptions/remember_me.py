import json


def get_stored_username():
    filename = "username.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def store_username():
    filename = "username.json"
    username = input("what is your name? ")
    with open(filename, "w") as f:
        json.dump(username, f)
    return username


def greet_user():
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}")
    else:
        username = store_username()
        print(f"we'll remember you {username}")


greet_user()
