pizza_toppings = []

prompt = "\nPlease enter some pizza toppings for your pizza!"
prompt += "\n(When you are done type 'done') "
active = True

while active:
    topping = input(prompt)
    if topping == "done":
        active = False
    elif len(topping) == 0 or topping.isspace():
        continue
    else:
        pizza_toppings.append(topping)
        print(
            f"Oooooh, {topping.title()} is delicious! {topping.title()} has been added to your pizza!"
        )

if len(pizza_toppings) == 0:
    print("Your plain pizza is coming right up!")
elif len(pizza_toppings) == 1:
    print(f"Your { pizza_toppings[0] } pizza is coming right up!")
else:
    print("Your pizza with:")
    for topping in pizza_toppings:
        print(f"\t{topping.title()}")
    print("is coming right up!")
