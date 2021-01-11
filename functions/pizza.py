def make_pizza(size, *toppings):
    print(f"\nMaking a {size}in pizza with the following toppings:")
    for idx, topping in enumerate(toppings):
        print(f"\t{idx + 1}: {topping}")


def print_something(*args):
    for item in args:
        print(item)
