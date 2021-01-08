# requested_topping = "mushrooms"
# if requested_topping != "anchovies":
#    print("Hold the anchovies")
#
# if requested_topping != "anchovies" and requested_topping != "raisins":
#    print("thank god")
#
# print((requested_topping == "mushrooms") and (requested_topping != "anchovies"))

# requested_toppings = ["mushrooms", "onions", "pineapple"]
# print("mushrooms" in requested_toppings)
# print("pepperoni" in requested_toppings)
#
# requested_toppings = [1]
# if requested_toppings:
#    print("request toppings exist")
# else:
#    print("requested_toppings does not exist")
available_toppings = ["cheese", "pineapple", "anchovies", "mushrooms"]
requested_toppings = ["cheese", "mushrooms", "ziti", "salad"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"adding {requested_topping} because we have it")
    else:
        print(f"I'm sorry, we do not have {requested_topping} right now")
