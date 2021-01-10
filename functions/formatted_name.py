def get_formatted_name(first_name, last_name, middle_name=""):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


# me = get_formatted_name("david", "levy")
# liane = get_formatted_name("liane", "levy", "sarah")
# print(me, liane)


def build_person(first_name, last_name, age=None):
    person = {"first_name": first_name, "last_name": last_name}
    if age:
        person["age"] = age
    return person


me = build_person("david", "levy")
liane = build_person("liane", "levy", 32)
print(me)
print(f"\n{liane}")
