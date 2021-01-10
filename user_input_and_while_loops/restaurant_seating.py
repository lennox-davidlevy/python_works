import random

# def closest_accommodated_table(n, tables):
#    return min([v for v in tables if v >= n] or [None])


def closest_accommodated_table(n, tables):
    if not n or len(tables) == 0:
        return "NOBODY"
    closest = None
    for i in tables:
        if (i >= n) and (closest is None or i < closest):
            closest = i
    return closest


available_tables = [random.randint(1, 8) for i in range(2)]


prompt = "Welcome to FoodTown, how many guests are in your party?"
guests = input(prompt)
guests = int(guests)

if guests >= 8 or closest_accommodated_table(guests, available_tables) is None:
    print(
        f"I'm sorry, we don't have any tables to accomidate {guests} guests right now."
    )
else:
    closest = closest_accommodated_table(guests, available_tables)
    print(f"Fantastic, we have a table that can seat {closest} right over here")
