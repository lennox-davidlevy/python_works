unconfirmed_users = ["alice", "debbie", "tina"]
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
print("\f The following users have been verified today:")
for user in confirmed_users:
    print(f"\t{user.title()}")
