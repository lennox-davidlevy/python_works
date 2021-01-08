# users = ["david", "lulu", "michelle", "liane", "admin"]
# users = []
# if users:
#    for user in users:
#        if user == "admin":
#            print(f"welcome admin, your wish is our command")
#        else:
#            print(f"welcome {user}, feel free to post")
# else:
#    print("no users today")

current_users = ["JohnNy", "David", "liane", "lulu", "richard"]
current_users = [name.lower() for name in current_users]
new_users = ["billy", "david", "LIANE", "jack", "tina"]

for user in new_users:
    if user.lower() in current_users:
        print(f"username {user} has already been taken")
    else:
        print(f"nice choice, {user}, welcome")
