def greet_users(names):
    for name in names:
        print(f"hello {name.title()}")


users = ["david", "liane", "lulu"]
greet_users(users)
