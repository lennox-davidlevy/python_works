active_flag = True
print("welcome to addition, give me two numbers and ill give you the sum")
while active_flag:
    first_num = input("Enter in your first number: ")
    second_num = input("Please enter your second number: ")

    try:
        numbers_sum = int(first_num) + int(second_num)
    except ValueError:
        print("sorry, I can only add NUMBERS together!")
    else:
        print(f"The sum is: {numbers_sum}")
        repeat = input("\nWould you like the continue (y/n)? ")
        if repeat == "n":
            active_flag = False
