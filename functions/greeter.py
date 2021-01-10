def get_formatted_name(first_name, last_name, middle_name=""):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


active_flag = True

name_list = []
while active_flag:
    first_name = input("\nPlease tell me your first name: ")
    middle_name = input("\nPlease tell me your middle name: ")
    last_name = input("\nPlease tell me your last name: ")
    full_name = get_formatted_name(first_name, last_name, middle_name)
    print(full_name)
    name_list.append(full_name)
    repeat = input("\nAdd another name (yes/no)? ")
    if repeat == "no" or repeat == "n":
        active_flag = False
print("\nThese are the names in the name_list:")
for name in name_list:
    print(f"{name}")
