def is_multiple_of_ten(n):
    return n % 10 == 0


def is_a_number(n):
    return n.isnumeric()


prompt = "Please enter a number that is a multiple of ten: "

number_provided = input(prompt)

while (
    is_a_number(number_provided) is not True
    or is_multiple_of_ten(int(number_provided)) is not True
):
    if is_a_number(number_provided):
        prompt = f"{number_provided} is not a multiple of ten, please try again: "
        number_provided = input(prompt)
    else:
        prompt = f"{number_provided} is not a number, please enter a number that is a multiple of ten: "
        number_provided = input(prompt)

print(f"{number_provided} is a multiple of ten!")
