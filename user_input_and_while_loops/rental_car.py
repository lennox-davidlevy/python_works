available_cars = ["suburu", "honda", "bently", "ford"]
prompt = "Welcome to CarEntalPrize, what kind of car can we get for you? "


def secondary_prompt(str):
    return f"I'm sorry, we don't have {str.title()}, please choose another! "


car = input(prompt)
car = car.lower()
while car not in available_cars:
    # prompt = secondary_prompt(car)
    car = input(secondary_prompt(car))
if car in available_cars:
    print(f"I'll go get you that {car.title()}")
