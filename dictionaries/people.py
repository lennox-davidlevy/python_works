import random


def create_person(first, last, age, location):
    return {"first": first, "last": last, "age": age, "location": location}


david = create_person("david", "levy", 36, "queens")
liane = create_person("liane", "levy", 32, "queens")
lulu = create_person("lulu", "levy", 8, "queens")
johnny = create_person("johnny", "jones", 55, "brooklyn")
jackie = create_person("jackie", "robinson", 130, "brooklyn")
michael = create_person("michael", "jackson", "dead", "neverland ranch")
list_of_people = [david, liane, lulu, jackie, johnny, michael]

for person in list_of_people:
    first = person["first"]
    last = person["last"]
    location = person["location"]
    full_name = f"{first.title()} {last.title()}"
    message = f"{ full_name } is from {location.title()}"
    # print(message)


def create_pet(name, age, breed):
    return {"name": name, "age": age, "breed": breed}


lulu = create_pet("lulu", 8, "bunny")
satchmo = create_pet("satchmo", 10, "dog")
sebby = create_pet("sebby", 10, "cat")
list_of_pets = [lulu, satchmo, sebby]

for pet in list_of_pets:
    name = pet["name"].title()
    age = pet["age"]
    breed = pet["breed"].title()
    message = f"{name} is a {age} year old {breed}"
    # print(message)


david_favorite_places = ["home", "forrest", "with wife"]
liane_favorite_places = ["home", "israel", "with husband"]
lulu_favorite_places = ["hiding"]

for person in list_of_people:
    if person["first"] == "david":
        person["favorite_places"] = david_favorite_places
    elif person["first"] == "liane":
        person["favorite_places"] = liane_favorite_places
    elif person["first"] == "lulu":
        person["favorite_places"] = lulu_favorite_places
    else:
        person["favorite_places"] = []
print(list_of_people)

for person in list_of_people:
    full_name = f"{person['first'].title()} {person['last'].title()}"
    location = person["location"].title()
    print(f"{full_name} is from {location} and ")
    if len(person["favorite_places"]) > 1:
        print("his/her favorite places are:")
        for place in person["favorite_places"]:
            print(f"\t {place.title()}")
    elif len(person["favorite_places"]) == 0:
        print("she/he has no favorite place")
    else:
        print(f"her/his favorite place is {person['favorite_places'][0].title()}")


def create_random_number_list(n):
    random_list = []
    if n == 0:
        random_list.append(random.randint(1, 100))
    else:
        for i in range(0, n):
            r = random.randint(1, 100)
            random_list.append(r)
    return random_list


for idx, person in enumerate(list_of_people):
    person["favorite_numbers"] = create_random_number_list(idx)

print(f"new for loop starts now")

for person in list_of_people:
    if person["favorite_numbers"]:
        full_name = f"{person['first'].title()} {person['last'].title()}"
        location = person["location"].title()
        print(f"{full_name} is from {location},")
        if len(person["favorite_numbers"]) == 1:
            print(f"and his/her favorite number is {person['favorite_numbers'][0]}")
        else:
            print(f"his/her favorite numbers are:")
            for number in person["favorite_numbers"]:
                print(f"\t{number}")


# for person in list_of_people:
#    print(f"list_of_people: {list_of_people}")
#    full_name = f"{person['first'].title()} {person['last'].title()}"
#    location = person["location"].title()
#    if len(person["favorite_numbers"]) == 1:
#        print(
#            f"{full_name} from {location} loves the number {person[favorite_numbers][0]}"
#        )
#    else:
#        print(f"{full_name} from {location} loves these numbers:")
#        for number in person["favorite_numbers"]:
#            print(f"\t{number}")
