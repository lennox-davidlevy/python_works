users = {
    "aeinstein": {"first": "albert", "last": "einstein", "location": "princeton"},
    "mcurie": {"first": "mary", "last": "curie", "location": "paris"},
    "rfeinman": {"first": "richard", "last": "feinman", "location": "queens"},
}
for username, user_info in users.items():
    first = user_info["first"]
    last = user_info["last"]
    location = user_info["location"]
    full_name = f"{first.title()} {last.title()}"
    print(f"{full_name} is from {location.title()}")
