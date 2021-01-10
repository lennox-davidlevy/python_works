number = input("Enter a number and I'll tell you if it's even or odd: ")
number = int(number)
if number == 0:
    print(f"zero is neither odd or even, its an idea!")
elif number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
