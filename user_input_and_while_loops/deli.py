orders = {}
orders_active = True
while orders_active:
    name = input("what is the name for the order? ")
    current_order = input("what would you like to order? ")
    orders[name] = current_order
    repeat = input("Would some one else like to order anything (yes/no)? ")
    if repeat == "no":
        orders_active = False
print("\n--- Your Order ---")
for name, order in orders.items():
    print(f"{name.title()} has ordered {order}")
