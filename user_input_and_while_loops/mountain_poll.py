# responses = {}
# polling_active = True

# while polling_active:
# name = input("\nWhat is your name? ")
# response = input("Which mountain would you like to climb one day?")
# responses[name] = response
# repeat = input("Would you like to let another person respond? (yes/no) ")
# if repeat.lower() == "no":
# polling_active = False
# print("\n--- Poll Results ---")
# for name, response in responses.items():
# print(f"{name.title()} would like to climb {response.title()}")

responses = {}
polling_active = True
while polling_active:
    name = input("What is your name? ")
    response = input("Which mountain would you like to climb one day? ")
    responses[name] = response
    repeat = input("would you like to let another person answer? (yes/no) ")
    if repeat == "no":
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}")
