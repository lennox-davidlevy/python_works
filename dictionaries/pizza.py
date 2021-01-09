pizza = {"crust": "thick", "toppings": ["mushrooms", "extra cheese"]}
print(f"You ordered a {pizza['crust']}-pizza with the following toppings:")
for idx, topping in enumerate(pizza["toppings"]):
    print(f"\t {idx + 1}: " + topping)
