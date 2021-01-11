# arbitrary keyword arguments
# build_profile expects a first and last name,
# and the it allows the user to pass in as many
# name-value pairs as they want
# the double asterisks cause python to create an empty
# dictionary called user_info and pack whatever
# name-value pairs it recieves into this dictionary
def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


user_profile = build_profile(
    "albert",
    "einstein",
    location="princeton",
    field="physics",
    hair="crazy",
    mind="huge",
)
lulu_profile = build_profile(
    "lulu",
    "levy",
    location="box",
    field="poop studies",
    hair="black",
    mind="tiny",
    smell="bad",
    disposition="grumpy",
)
my_profile = build_profile("david", "levy")
print(user_profile)
print(lulu_profile)
print(my_profile)
