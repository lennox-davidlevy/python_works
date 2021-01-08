import random

age_of_people = random.sample(range(1, 80), 40)

for person in age_of_people:
    if person < 2:
        print(f"You are {person}, a baby")
    elif person >= 2 and person < 4:
        print(f"You are {person}, a toddler")
    elif person >= 4 and person < 13:
        print(f"You are {person}, a kid")
    elif person >= 13 and person < 20:
        print(f"You are {person}, a teenager")
    elif person >= 20 and person < 65:
        print(f"You are {person}, an adult")
    else:
        print(f"You are {person}, an elder")
