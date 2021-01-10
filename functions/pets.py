animal_list = []


def describe_pet(pet_name, animal_type):
    animal = {"name": pet_name, "animal_type": animal_type}
    return animal


active_flag = True
while active_flag:
    name = input("input name of animal ")
    breed = input("input type of animal ")
    animal = describe_pet(name, breed)
    animal_list.append(animal)
    repeat = input("add another (yes/no)? ")
    if repeat == "no":
        active_flag = False

print("\n--- animal list ---")
for animal in animal_list:
    print(f"{animal}")


# explicitly telling which parameter each argument should breed
# matched with ignores argument/parameter position
# both function calls below work
# def describe_pet(animal_type, pet_name):
#    print(f"{animal_type} {pet_name}")
#
# describe_pet(animal_type="rabbit",pet_name="lulu")
# describe_pet(pet_name="lulu",animal_type="rabbit")

# default value in python
# def describe_pet(animal_type, pet_name="lulu"):
# print(f"{animal_type} {pet_name}")


# non-default argument follows default will throw error
# def describe_pet(pet_name="lulu", animal_type):
# print(f"{animal_type} {pet_name}")
# describe_pet("bunny")
