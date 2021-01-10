movie_goers = []
prompt = "welcome to City Movies! Please tell me how many of you there are? "
number_of_guests = input(prompt)
number_of_guests = int(number_of_guests)
i = 1
while number_of_guests > 0:
    age_of_guest = input(f"how old is guest {i}? ")
    age_of_guest = int(age_of_guest)
    if age_of_guest < 3:
        price_of_ticket = 0
    elif age_of_guest < 12:
        price_of_ticket = 10
    else:
        price_of_ticket = 15
    movie_goers.append(price_of_ticket)
    number_of_guests -= 1
    i += 1

total_price = sum(movie_goers)
print(f"That will be ${total_price}. Please enjoy the show!")
