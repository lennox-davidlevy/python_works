height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print(f"\nYou're tall enough to ride")
else:
    print(f"\nYou are too short. Seriously {height} inches is TINY!")
