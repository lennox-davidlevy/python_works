def get_formatted_name(first, last, middle=""):
    if len(middle) > 0:
        full_name = f"{last}, {first} {middle}"
    else:
        full_name = f"{last}, {first}"
    return full_name.title()
