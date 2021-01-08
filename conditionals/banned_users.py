banned_users = ["andrew", "melissa", "david"]
users = ["marie", "andrew", "melissa", "liane", "david", "lulu"]
banned_users = [name.lower() for name in banned_users]
super_users = ["john", "darryl", "michael", "melissa"]
# if user.lower() not in banned_users:
#    print(f"{user.title()},you can post a response if you wish")
for user in users:
    if user.lower() not in banned_users:
        print(f"{user.title()}, you may post, welcome")
    elif user.lower() in super_users:
        print(f"{user.title()}, youre banned, but super")
    else:
        print(f"{user.title()}, youre banned.")
